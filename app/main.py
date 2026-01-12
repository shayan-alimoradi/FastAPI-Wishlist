from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from users.api.v1 import router as users_router
from users.authentication import router as authentication_router
from products.api.v1 import router as products_router
from comments.api.v1 import router as comments_router
from carts.api.v1 import router as carts_router
from orders.api.v1 import router as orders_router


app = FastAPI(version="1.0.2")
app.include_router(users_router)
app.include_router(authentication_router)
app.include_router(products_router)
app.include_router(comments_router)
app.include_router(carts_router)
app.include_router(orders_router)


@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}
