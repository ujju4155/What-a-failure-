# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Commands for BOT Users
├ /start - Start Bot
├ /about - About this Bot
├ /help - Help this Bot Command
├ /batch - To Batch Files
└ /uptime - To view bot status

ᴍʏ ꜱᴇɴꜱᴇɪ 💕 </b><a href='https://t.me/aye_ujjwal'>@aye_ujjwal</a>
"""

    close = [
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ:

ᴛʜɪꜱ ɪꜱ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ @aye_ujjwal.

 • ᴍʏ ɴᴀᴍᴇ ❣️: @{}
 • ᴍᴀɪɴ: <a href='https://t.me/Otaku_Vision_M'>ᴏᴛᴀᴋᴜ ᴠɪꜱɪᴏɴ</a>
 • ᴄᴏɴᴛᴀᴄᴛ ꜰᴏʀ ʀᴇᴘᴏ: <a href='https://t.me/aye_ujjwal'>@ᴀʏᴇ_ᴜᴊᴊᴡᴀʟ </a>

ᴍʏ ꜱᴇɴꜱᴇɪ 💕 </b><a href='https://t.me/aye_ujjwal'>@aye_ujjwal</a>
"""
