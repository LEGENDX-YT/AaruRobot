import random
from pyrogram import __version__ as pyrover
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from AaruRobot import OWNER_USERNAME, SUPPORT_CHAT, dispatcher
from AaruRobot.events import register
from AaruRobot import telethn as tbot


PHOTO = [
    "https://te.legra.ph/file/fdf0fe6a94d55dc2f137f.jpg",
    "https://te.legra.ph/file/fdf0fe6a94d55dc2f137f.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ  ✘ ʀᴏʙᴏᴛ​**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [⏤͟͟͞͞x𝐃🥀| 𓆩 𝐂𝐎𝐃𝐄𝐑 𓆪 |∘𖣘︎⃞⃟🔥°](https://t.me/NOMRExd)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/AVADHUTMNGR_bot?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/NOMRExd"),
        ]
    ]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)
  
  ##AARU ALIVE MOD
