import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from NoinoiRobot.events import register as MEMEK
from NoinoiRobot import telethn as tbot

PHOTO = "https://telegra.ph/file/eb89fecd86d300697f0f0.jpg"

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  LUNA = "**HELLO I AM *{}* ๐ต!** \n\n"
  LUNA += "โจ **I'M WORKING PROPERLY** \n\n"
  LUNA += "โจ **MY MASTER : [Owner Bot](https://T.ME/ribajosmani)** \n\n"
  LUNA += f"โจ **Telethon Version : {tlhver}** \n\n"
  LUNA += f"โจ **PYROGRAM VERSION : {pyrover}** \n\n"
  LUNA += "**THANS FOR ADDING ME HEAR โค๏ธ**"
  BUTTON = [[Button.url("สแดสแด", "https://t.me/Mss_Rosan_Bot?start=help"), Button.url("sแดแดแดแดสแด", "https://t.me/osmanigroupbot")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)

@MEMEK(pattern=("/cmd"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "โ **๐๐๐๐ฅ ๐ง๐๐ ๐ฆ๐ข๐ ๐ ๐๐ข๐ ๐ ๐๐ก๐ ๐๐ข๐ฅ ยป๐ ๐จ๐ฆ๐๐ & ๐ฉ๐๐๐๐ข & ๐๐ซ๐ง๐๐ฅ๐ก๐๐ ๐๐๐๐ง๐จ๐ฅ๐๐ฆ ๐**"
  buttons = [
    [
        InlineKeyboardButton(text="๐๐ข๐ ๐ ๐๐ก๐๐ฆ ๐", callback_data="luna_"),
    ],
            ]
  await tbot.send_file(event.chat_id, PHOTO, caption=LUNA,  buttons=BUTTON)
