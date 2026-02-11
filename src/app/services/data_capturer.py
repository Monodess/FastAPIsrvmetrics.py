import asyncio, time
import httpx
from icecream import ic
from rich import print as rprint
from src.app.core.appsettings import appsettings

#see what structure and how much labels it has
#premake data model and migrate to db with py ef
#check if i could turn captured data in csv with pands
#taught the model and prepare datasets for it with labels(tight answers) and both test and validation

URLS = ["https://docs.python.org/uk/3.13/library/__main__.html"]

#metrics capturing functin
async def fetch_pagespeed_metrics(client: httpx.AsyncClient, target_url: str, api_key: str):
    # CRITICAL: Use the API endpoint, not the web URL
    base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": target_url,
        "key": api_key,
        "strategy": "mobile",
        "category": "performance"
    }

    try:
        #httpx obj has headers prop 
        response = await client.get(base_url, params=params, timeout=30.0)  # PageSpeed is slow
        ic(response)
        #get quota left
        ic(dict(response.headers)) #[dict]- every header
        if response.status_code == 200:
            data = response.json()  # Fixed: json is a method (), not a property

            lighthouse = data.get("lighthouseResult", {})
            audits = lighthouse.get("audits", {})
            json1 = response.content
            ic(json1)
            return {
                "overall_score": lighthouse.get("categories", {}).get("performance", {}).get("score"),
                "lcp": audits.get("largest-contentful-paint", {}).get("numericValue"),
                "cls": audits.get("cumulative-layout-shift", {}).get("numericValue"),
                "fcp": audits.get("first-contentful-paint", {}).get("numericValue"),
                "speed_index": audits.get("speed-index", {}).get("numericValue")
            }
    except Exception as e:
        print(f"PageSpeed Error for {target_url}: {e}")
    return None

#health check function
async def fetch_once(client: httpx.AsyncClient, url: str):
    t0 = time.perf_counter()
    try:
        r = await client.get(url, follow_redirects=True, timeout=10)
        # Fixed the math: (End - Start) * 1000
        latency_ms = (time.perf_counter() - t0) * 1000
        return {
            "time": int(time.time()),
            "url": url,
            "status_code": r.status_code,
            "latency_ms": latency_ms,
            "length": len(r.content),
            }
    except Exception as e:
        latency_ms = (time.perf_counter() - t0) * 1000
        return {int(time.time()), url, None, latency_ms, 0, str(e)}



async def loop(urls, api_key):
    limits = httpx.Limits(max_connections=5)
    # The client lives here for the entire duration of the program
    async with httpx.AsyncClient(limits=limits, headers={"User-Agent": "MetricsCollector/1.0"}) as client:
        while True:
            for u in urls:
                health = await fetch_once(client, u)
                metrics = await fetch_pagespeed_metrics(client, u, api_key)
                print(f"Health check: {health},\n"
                      f"Metrics captured: {metrics}")
            return health, metrics              #returning tuple

#no API for this
#async def getlimit(client: httpx.AsyncClient, #api_key: str):
    
async def time_loop(attempts: int):
    for i in range (1, attempts):
        yield await (loop(URLS, appsettings.PAGESPEED_API_KEY))


data =  asyncio.run(loop(URLS, appsettings.PAGESPEED_API_KEY))     #only once making main coroutine
if __name__ == '__main__':
    rprint(data)
    ic(data)




