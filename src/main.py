from fastapi import FastAPI
from src.app.api.routers.metrics import router
from src.app.api.app import lifespan


def get_app():
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)
    return app

def _register_routes(app):
    from src.app.api.routers.metrics import router
    
    app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    app = get_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
