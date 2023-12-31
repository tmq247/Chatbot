import re
import os
from asyncio import gather, get_event_loop, sleep

from aiohttp import ClientSession
from pyrogram import Client, filters, idle
from Python_ARQ import ARQ
from pyrogram import enums

is_config = os.path.exists("config.py")

if is_config:
    from config import *
else:
    from sample_config import *

luna = Client(
    ":memory:",
    bot_token=bot_token,
    api_id=api_id2,
    api_hash=api_hash2,
    session_string=session_string,
)

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
    await message._client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, enums.ChatAction.CANCEL)
    
    
@luna.on_message(filters.regex("@muoimuoimusic") & filters.group)
async def type_and_send2(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, enums.ChatAction.CANCEL)

@luna.on_message(filters.regex("@muoimuoibot") & filters.group)
async def type_and_send3(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    query = message.text.strip()
    await message._client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response, _ = await gather(lunaQuery(query, user_id), sleep(2))
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, enums.ChatAction.CANCEL)
#group = "-1001712715936"
@luna.on_message(filters.command("x") & filters.group)
async def type_and_send6(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    message.text and message.text.upper()[1] in ['T'] and message.text[3:].isdigit()
    bet_amount = int(message.text[3:])
    #query = message.text.strip()
    await message._client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response = f"/t {bet_amount}"
    await sleep(2)
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, enums.ChatAction.CANCEL)

@luna.on_message(filters.command("t") & filters.group)
async def type_and_send6(_, message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    message.text and message.text.upper()[1] in ['T'] and message.text[3:].isdigit()
    bet_amount = int(message.text[3:])
    #query = message.text.strip()
    await message._client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response = f"/x {bet_amount}"
    await sleep(2)
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, enums.ChatAction.CANCEL)


async def type_and_send4(message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else 0
    await message._client.send_chat_action(chat_id, enums.ChatAction.TYPING)
    response = "đừng như thế,hãy nói chuyện với tôi bằng văn bản"
    await message.reply_text(response)
    await message._client.send_chat_action(chat_id, enums.ChatAction.CANCEL)
        




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
    print(
        """
-----------------
| Luna Khởi động! |
-----------------
"""
    )
    await idle()


loop = get_event_loop()
loop.run_until_complete(main())
