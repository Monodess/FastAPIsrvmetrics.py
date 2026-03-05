from fastapi.openapi.docs import get_swagger_ui_html

from src.app.api.app import get_app
from src.app.api.routers.any import ANYTHING
from src.app.api.routers.metrics import router

app = get_app()

"""Root handler"""
@app.get("/")
def read_root():
    return {"Hello": "This is main metrics page"}

app.include_router(router)
app.include_router(ANYTHING)

