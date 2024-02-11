# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import asyncio, time,requests
from pyrogram.types import InlineKeyboardMarkup
from .. import Mukesh
from pyrogram.enums import ChatAction,ParseMode
from config import *
from ..modules.buttons import *




#blackbox
@Mukesh.on_message(filters.command(["blackbox"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def blackbox_chat(bot, message):
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/blackbox how r u?`")
    else:
        a = message.text.split(' ', 1)[1]
    try:
        #  CREDITS
        # TELEGRAM : @Mr_Sukkun
        #  GITHUB : NOOB-MUKESH
                
        response = requests.get(f'https://mukesh-api.vercel.app/blackbox?query={a}') 
        if response.status_code==200:
            x=response,json()["results"]
               
    except requests.exceptions.RequestException as e:

        response = requests.get(f'https://mukesh-api.vercel.app/chatgpt?query={a}') 
        if response.status_code==200:
            x=response.json()["results"]
    except requests.exceptions.RequestException as e:
        response = requests.get(f'https://mukesh-api.vercel.app/bard?query={a}') 
        if response.status_code==200:
            x=response.json()["results"]
    finally:
        await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{Mukesh.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True,disable_web_page_preview=True)  
        

