"""
    This module doesn't have processing logic
It exists only to capture data via API
"""
import json
import time

import httpx

from src.appsetting.appsettings import appsettings

"""Health check function"""
async def fetch_once(client: httpx.AsyncClient, url: str):
    t0 = time.perf_counter()
    status_code = None
    raw_json_string = None

    try:
        r = await client.get(url, follow_redirects=True, timeout=10)
        # If this is 4xx or 5xx, it jumps to 'except'
        r.raise_for_status()

        latency_ms = (time.perf_counter() - t0) * 1000
        return {
            "url": url,
            "response_code": r.status_code,
            "latency_ms": latency_ms,
            "content_length": len(r.content),
            "is_up": 1,
            "error": None,
        }
    except Exception as e:
        latency_ms = (time.perf_counter() - t0) * 1000
        current_status = None
        content_length = 0
        is_up = 0

        # Check if we actually got a response object back
        response_obj = getattr(e, "response", None)

        if response_obj is not None:
            current_status = response_obj.status_code
            # A site is "Up" if it responds with success or a redirect
            is_up = 1 if 200 <= current_status < 400 else 0
            content_length = len(response_obj.content)
            raw_json_string = response_obj.text

        return {
            "url": url,
            "response_code": current_status,
            "latency_ms": latency_ms,
            "content_length": content_length,
            "is_up": is_up,
            "error": str(e),
        }

"""Metrics capturing function"""
async def fetch_pagespeed_metrics(client: httpx.AsyncClient, target_url: str, api_key: str):
    # CRITICAL: Use the API endpoint, not the web URL
    base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": target_url,
        "key": api_key,
        "strategy": "mobile",
        "category": "performance"
    }
    status_code = None
    raw_json_string = None
    try:
        response = await client.get(base_url, params=params, timeout=30.0)
        response.raise_for_status()
        status_code = response.status_code
        data = response.json()  # Fixed: json is a method (), not a property

        lighthouse = data.get("lighthouseResult", {})

        audits = lighthouse.get("audits", {})

        raw_json_string = json.dumps(lighthouse)
        return {
            "url": params.get("url"),
            "strategy": params.get("strategy"),
            "response_code": response.status_code,
            "perf_score": lighthouse.get("categories", {}).get("performance", {}).get("score"),
            "lcp_ms": audits.get("largest-contentful-paint", {}).get("numericValue"),
            "cls": audits.get("cumulative-layout-shift", {}).get("numericValue"),
            "fcp_ms": audits.get("first-contentful-paint", {}).get("numericValue"),
            "speed_index_ms": audits.get("speed-index", {}).get("numericValue"),
            "error": None,
        }
    except Exception as e:
        return {
            "url": params.get("url"),
            "strategy": params.get("strategy"),
            "response_code": status_code,
            "perf_score": None,
            "lcp_ms": None,
            "cls": None,
            "fcp_ms": None,
            "speed_index_ms": None,
            "error": str(e),
        }

"""Capture full data for one url"""
async def process_url(client, url, api_key):
    health = await fetch_once(client, url)
    metrics = await fetch_pagespeed_metrics(client, url, api_key)
    print(f"Health check: {health},\n"
          f"Metrics captured: {metrics}")
    return health, metrics

async def loop(urls, api_key):
    limits = httpx.Limits(max_connections=5)
    # The client lives here for the entire duration of the program
    async with httpx.AsyncClient(limits=limits, headers={"User-Agent": appsettings.HEADERS}) as client:
            for u in urls:
                health = await fetch_once(client, u)
                metrics = await fetch_pagespeed_metrics(client, u, api_key)
                print(f"Health check: {health},\n"
                      f"Metrics captured: {metrics}")
            return health, metrics              #returning tuple by default

#no API for this
#async def getlimit(client: httpx.AsyncClient, #api_key: str):
#generator





