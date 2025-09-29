import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


from faststream.rabbit import RabbitBroker

from settings import RABBITMQ_DEFAULT_PASS, RABBITMQ_DEFAULT_USER, TG_TOKEN, CHAT_ID

# Bot token can be obtained via https://t.me/BotFather
TOKEN = TG_TOKEN


dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

broker = RabbitBroker(url=f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@localhost:5672/")


@broker.subscriber("orders")
async def handle_orders(data: str):
    # send data to user
    await bot.send_message(chat_id=CHAT_ID, text=data)


# simple example
@dp.message()
async def handle_msg(msg:Message):
    await msg.answer(f'Ваш чат id: {msg.chat.id}')

async def main() -> None:
    async with broker:
        await broker.start()
        logging.info("RabbitMQ Bot started.")
        await dp.start_polling(bot)

    logging.info("All done...")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())