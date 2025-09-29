from fastapi import FastAPI

from faststream.rabbit.fastapi import RabbitRouter
from pydantic import BaseModel

from settings import RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS

# rabbit
router = RabbitRouter(url=f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@rabbitmq/")

@router.post("/order")
async def make_order(name: str):
    await router.broker.publish(
        f'New order {name}',
        queue="orders",
    )
    return {'order': name}
###########

app = FastAPI()

app.include_router(router)


# class CreateOrder(BaseModel):
#     name: str
#     price: int
#
# @app.post("/order")
# async def create_order(order: CreateOrder):
#     return {"message": f"Order created {order.name}, price: {order.price}"}