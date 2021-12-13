from fastapi import FastAPI

from api.app.injector import get_user_controller


def create_app() -> FastAPI:
    app = FastAPI(openapi_url=f"/openapi.json", docs_url=f"/docs", redoc_url=f"/redoc",)
    setup_injector()
    setup_router(app)
    return app


def setup_injector():
    get_user_controller()


def setup_router(app: FastAPI):
    from api.app.router import router

    app.include_router(router, prefix="/api/v1")

    @app.get("/")
    async def index():
        return {"status": "successful"}

    @app.get("/status")
    async def status():
        return {"status": "successful"}


app = create_app()
