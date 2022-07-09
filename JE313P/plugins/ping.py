import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/5f3090a61ad28947d3913.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@x_bo_dy_alkbir"
)

CAPTION = f"**سرعة البنج:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/boodywe")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
