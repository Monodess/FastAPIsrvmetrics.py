import pytest
from icecream import ic

from tests.app.services.test_capturer import get_client, get_url


@pytest.mark.asyncio
async def test_debug_headers() :
    client = get_client(True)
    response = await client.get(get_url())
    ic(response.request.headers)
    ic(response.text)