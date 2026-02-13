import httpx
import pytest
from unittest.mock import AsyncMock

from icecream import ic

from src.app.core.appsettings import appsettings
from src.app.services.data_capturer import process_url


#create mock data for data_capturer, so that testing woulnd need to use real API every time
#this is self-evident: for logic testing real httpx client is not necessary

def get_client(single_connection: bool):
    if single_connection:
        limits = httpx.Limits(max_connections=1)
        client = httpx.AsyncClient(limits=limits, headers={"User-Agent": appsettings.HEADERS})
        return client
    else:
        limits = httpx.Limits(max_connections=1000)
        client = httpx.AsyncClient(limits=limits, headers={"User-Agent": appsettings.HEADERS})
        return client

@pytest.mark.asyncio
async def test_api_capture_shape():
    data = await process_url(get_client(True),"https://stackoverflow.com/questions", appsettings.PAGESPEED_API_KEY)
    ic(data)
    #assert "url" in data[0]
    #assert "perf_score" in data[0]

