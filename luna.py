import re
import os
import asyncio
from asyncio import gather, get_event_loop, sleep

from aiohttp import ClientSession
from pyrogram import Client, filters, idle, compose
from Python_ARQ import ARQ
from pyrogram import enums

is_config = os.path.exists("config.py")

if is_config:
    from config import *
else:
    from sample_config import *
#bot_token=bot_token,
luna = Client(
    ":memory:",
    bot_token=bot_token,
    api_id=api_id2,
    api_hash=api_hash2,
    session_string=session_string,
)

bot = [
    Client(
    ":memory2:",
    bot_token=bot_token,
    api_id=api_id2,
    api_hash=api_hash2,
),
    Client(
    ":memory3:",
    bot_token=bot_token2,
    api_id=api_id2,
    api_hash=api_hash2,
)
]

bot_id = int(bot_token.split(":")[0])
arq = None


async def lunaQuery(query: str, user_id: int):
    query = (
        query
        if LANGUAGE == "en"
        else (await arq.translate(query, "en")).result.translatedText
    )
    resp = (await arq.luna(query, user_id)).result
    return (
        resp
        if LANGUAGE == "en"
        else (
            await arq.translate(resp, LANGUAGE)
        ).result.translatedText
    )

async def type_and_send(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await luna.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    await message.reply_text(response)
    await luna.send_chat_action(chat_id, enums.ChatAction.CANCEL)

@luna.on_message(filters.reply)
async def type_and_send0(_, message):
    #print(message)
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    me = message.reply_to_message.from_user.is_self if message.reply_to_message.from_user else 0
    if me == True :
        if message.text : #6434323473:
            await type_and_send(message)
        else :
            await sleep(2)
            print(message)
            await message.reply_animation("CgACAgUAAx0CbEe_8wACwBZmbA2kzc9rzPRvnfGCM0gZibErBQACGg4AAub0cVYJdq2Iu8nLwB4E")
    else:
        return

    
@luna.on_message(filters.regex("@muoimuoimusic") & filters.group & filters.text)
async def type_and_send1(_, message):
    await type_and_send(message)

@luna.on_message(filters.regex("@muoimuoimusicbot") & filters.group & filters.text)
async def type_and_send3(_, message):
    await type_and_send(message)

stk = (filters.regex("stk") | filters.regex("Stk") | filters.regex("STK"))
@luna.on_message(filters.private & filters.text & stk)
async def type_and_send4(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    await luna.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response = "190002525457 HOANG TRONG THUONG  NCB"
    await sleep(2)
    await message.reply_text(response)
    await luna.send_chat_action(chat_id, enums.ChatAction.CANCEL)


@bot.on_message((filters.regex("stk") | filters.regex("Stk") | filters.regex("STK")) & filters.text & filters.group)
async def type_and_send4(_, message):
    chat_id = message.chat.id
    msg = message.id
    user_id = message.from_user.id if message.from_user else 0
    #query = message.text.strip()
    await luna.send_chat_action(chat_id, enums.ChatAction.TYPING)
    await sleep(2)
    response = "190002525457 HOANG TRONG THUONG  NCB"
    #await message.reply_text(response)
    await luna.send_message(chat_id, response, reply_to_message_id=msg)
    await luna.send_chat_action(chat_id, enums.ChatAction.CANCEL)


@luna.on_message(filters.regex("còi ơi") | filters.regex("Còi ơi") & filters.group & filters.text)
async def type_and_send5(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    #query = message.text.strip()
    await luna.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response = "@COIAHYCOC có người kiếm."
    await message.reply_text(response)
    await luna.send_chat_action(chat_id, enums.ChatAction.CANCEL)
        
get = filters.command("get")
@luna.on_message(get)
#@luna.on_edited_message(get)
async def get(_, message):
    file_id = message.reply_to_message.animation.file_id
    print(file_id)
    await message.reply_text(f"file_id")

repo = filters.command("repo")
@luna.on_message(repo)
@luna.on_edited_message(repo)
async def repo(_, message):
    await message.reply_text(
        "[GitHub](https://github.com/)"
        + " | [Group](t.me/muoimuoimusicbot)",
        disable_web_page_preview=True,
    )

help = filters.command("help")
@luna.on_message(help)
@luna.on_edited_message(help)
async def start(_, message):
    await luna.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    await sleep(2)
    await message.reply_text("/repo - Get Repo Link")


help = filters.command("help")
@luna.on_message(help & ~filters.private
    & filters.text, group=69,)
@luna.on_edited_message(help & ~filters.private
    & filters.text, group=69,)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user:
            return
        from_user_id = message.reply_to_message.from_user.id
        if from_user_id != bot_id:
            return
    else:
        match = re.search(
            "[.|\n]{0,}luna[.|\n]{0,}",
            message.text.strip(),
            flags=re.IGNORECASE,
        )
        if not match:
            return
    await type_and_send(message)


@luna.on_message(filters.private & ~filters.command("help"))
@luna.on_edited_message(filters.private & ~filters.command("help"))
async def chatpm(_, message):
    if not message.text:
        return
    await type_and_send(message)


async def main():
    global arq
    session = ClientSession()
    arq = ARQ(ARQ_API_BASE_URL, ARQ_API_KEY, session)

    await luna.start()
    await compose(bot).start()
    print(
        """
-----------------
| Luna Khởi động! |
-----------------
"""
    )
    await idle()


#loop = get_event_loop()
#loop.run_until_complete(main())
asyncio.get_event_loop().run_until_complete(main())
