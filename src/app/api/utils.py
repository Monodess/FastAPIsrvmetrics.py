from starlette.requests import Request


def get_client (request: Request):
    return request.app.state.http_client

"""This function parses query params with operators 
                or single value"""
def parse_filters(raw_filters: dict | None ):
    processed_filters = {}
    # 1: Iterate through a query string
    for key, val in raw_filters.items():
        # 2: Find "operator & digit" pairs
        if "," in val:
            # Split the op and the digit
            op, clean_val = val.split(",", 1)
            # Try parse digit into int
            if clean_val.isdigit():
                clean_val = int(clean_val)
            # Add it as a tuple
            processed_filters[key] = (op, clean_val)
        else:
            processed_filters[key] = int(val) if val.isdigit() else val
    if processed_filters : return processed_filters
    else: return None
