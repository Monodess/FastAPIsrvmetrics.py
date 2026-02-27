import httpx

from src.appsetting.appsettings import appsettings


def create_http_client():
    limits = httpx.Limits(max_connections=5)

    client = httpx.AsyncClient(limits=limits,
                                   headers={
                                       "User-Agent": appsettings.HEADERS,  # Your Chrome 120 string
                                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                       "Accept-Language": "en-US,en;q=0.5",
                                       "Accept-Encoding": "gzip, deflate, br",
                                       "DNT": "1",  # Do Not Track
                                       "Connection": "keep-alive",
                                       "Upgrade-Insecure-Requests": "1"
                                   },
                                   follow_redirects=True,
                                   http2=True)
    return client