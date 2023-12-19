import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import translate

translator_to_uz = translate.Translator(to_lang='uz')

TOKEN = getenv("TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Xush kelibsiz!")


@dp.message()
async def translate_handler(message: types.Message) -> None:
    response = translator_to_uz.translate(message.text)
    await message.answer(response)


async def main() -> None:
    bot = Bot("TOKEN", parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
