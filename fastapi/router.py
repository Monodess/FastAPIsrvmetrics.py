import fastapi
'''
"Use case" vs "Normal function"
some_route = fastapi.APIRouter()
@some_route.api_route("/"...)
    return SomeDbDataGetter()

@some_route.api_route("/"..., input?)
    ...
    input validation
    ...
    errors handler
    ...
    return SomeDbDataGetter()

'''
''' Use cases: 
1) GET metrics from pgs 
2) POST: url: str, time schedule(how long to monitor): int, save to db: bool 
'''
metrics = fastapi.APIRouter()

@metrics.api_route("/metrics", methods=["POST", "GET"])
def MetricsApi ():
