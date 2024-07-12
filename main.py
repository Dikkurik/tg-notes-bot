# -*- coding: utf-8 -*-
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.methods import ForwardMessages
from aiogram.types import Message, MessageOriginChannel, Chat

from note_editor import Note
from config import config

# Bot token can be obtained via https://t.me/BotFather
# TOKEN = getenv()
TOKEN = config.TOKEN

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

# bot methods

@dp.message(Command(prefix="/",commands="help"))
async def get_files(message: Message):
    """
    This command return help message 
    """
    help_msg = """This is bot for CRUD operations with notes on PC through telegram,
created for fun.
/nget - get all notes in folder
/nread [filename] - read note
/nedit [filename] - edit note"""

    await message.answer(text=f"{help_msg}")

@dp.message(Command(prefix="/",commands="nget"))
async def get_files(message: Message):
    """
    This command return list of existed files 
    """
    note = Note()
    n_list = note.getNotes()
    await message.answer(text=f"Existed files:\n{n_list}")

@dp.message(Command(prefix="/",commands="nread"))
async def read_note(message: Message):
    """
    This command return list of existed files 
    """
    note = Note()
    n_text = note.readNote(message.text.split(' ')[1])
    await message.answer(text=f"{n_text}")

@dp.message(Command(prefix="/",commands="nedit"))
async def edit_note(message: Message):
    """
    This command return list of existed files 
    """
    note = Note()
    n_text = note.readNote(message.text.split(' ')[1])
    print(n_text)
    await message.answer(text=f"{n_text}")

# channel methods

@dp.channel_post(Command(prefix="/",commands="help"))
async def get_files(message: Message):
    """
    This command return help message 
    """
    help_msg = """This is bot for CRUD operations with notes on PC through telegram,
created for fun.
/nget - get all notes in folder
/nread [filename] - read note
/nedit [filename] - edit note"""

    await message.answer(text=f"{help_msg}")

@dp.channel_post(Command(prefix="/",commands="nget"))
async def get_files(message: Message):
    """
    This command return list of existed files 
    """
    note = Note()
    n_list = note.getNotes()
    await message.answer(text=f"Existed files:\n{n_list}")

@dp.channel_post(Command(prefix="/",commands="nread"))
async def read_note(message: Message):
    """
    This command return list of existed files 
    """
    note = Note()
    n_text = note.readNote(message.text.split(' ')[1])
    await message.answer(text=f"{n_text}")    

@dp.channel_post(Command(prefix="/",commands="nedit"))
async def edit_note(message: Message):
    """
    This command return list of existed files 
    """
    note = Note()
    n_text = note.editNote(message.text.split(" ")[1], message.text.split("  ")[1])
    print(n_text)
    await message.answer(text=f"{n_text}")

@dp.channel_post(Command(prefix="/",commands="clear"))
async def read_note(message: Message):
    """
    This command clear chanel  
    """
    message.delete
    await message.answer()

@dp.channel_post(Command(prefix="/",commands="check"))
async def read_note(message: Chat, post: Message):
    id = message.id
    await post.answer(id)

@dp.channel_post()
async def create_note(message: Message):
    try:
        note = Note()
        note.createNote(message.text)
        note.saveToFile()
        print("saved to yourfile")
        await message.delete()
    except:
        print("Something went wrong")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())