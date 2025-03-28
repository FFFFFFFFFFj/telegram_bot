from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

start_router = Router(name=__name__)

@start_router.message(CommandStart())
async def cmd_start(message: Message):
	await message.answer('Starting message on call /start using the CommandStart() filter')
	
@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
	await message.answer('Starting message on call /start_2 using the CommandStart() filter')

@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
	await message.answer('Starting message on call /start_3 using the F.text  filter')
