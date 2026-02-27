from starlette.requests import Request


def get_client (request: Request):
    return request.app.state.http_client
