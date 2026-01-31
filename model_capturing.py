import asyncio, time
import httpx
import aiosqlite
import sqlalchemy as sa
import pandas



#see what structure and how much labels it has
#premake data model and migrate to db with py ef
#check if i could turn captured data in csv with pands
#taught the model and prepare datasets for it with labels(tight answers) and both test and validation
DB = "picsum_metrics.db"
URLS = []

async def fetch_once(client: httpx.AsyncClient, url: str):
    t0 = time.perf_counter()
    try:
        r = await client.get(url, follow_redirects=True, timeout=10)
        latency_ms = (time.perf_counter() - t0 * 1000)
        size = len(r.content)
        return (int(time.time()), url, r.status_code, latency_ms, size, None)
    except Exception as e:
    latency_ms = time.perf_counter() - t0 * 1000
    return(int(time.time()), url, None, latency_ms, str(e))

async def loop(period_sec = 5, concurency= 3):
    limit = httpx.Limits(max_connections=concurency, max_keepalive_connections=concurency)
    await with httpx.AsyncClient(limits=limit, headers={"User Agent": "Metrics Collector"}) as client:
        while True:
            tasks  = [fetch_once(client, u) for u in URLS]
            rows = await asyncio.gather(*tasks)
            #where to store them

