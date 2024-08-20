from pyrogram import Client, filters
from MukeshRobot import pbot as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/SAPNA_X_ROBOT?startgroup=true"),
    ],
]

@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ [˹ sʌᴘηʌ ꭙ ʀσʙσᴛ ˼ ♪](https://t.me/SAPNA_X_ROBOT)", reply_markup=InlineKeyboardMarkup(EVAA),)
    except IndexError:
        # User didn't provide a location
        message.reply_text("⬤ ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟᴏᴄᴀᴛɪᴏɴ ♥︎ Use ➥ /weather NEW YORK")



__help__ = """

 ⬤ /weather <ᴄɪᴛʏ>* ➥* ᴀᴅᴠᴀɴᴄᴇᴅ ᴡᴇᴀᴛʜᴇʀ ᴍᴏᴅᴜʟᴇ, ᴜsᴀɢᴇ sᴀᴍᴇ ᴀs /ᴡᴇᴀᴛʜᴇʀ
 ⬤ /weather  ᴍᴏᴏɴ* ➥* ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ᴏғ ᴍᴏᴏɴ
 ⬤ /calendar <year> ➥ sʜᴏᴡ ᴄᴀʟᴇɴᴅᴀʀ, ᴇx - 1984, 2004, 2024
 ⬤ /day ➥ sʜᴏᴡ ᴅᴀʏ, [● ᴇx ➣ 16/06/2003]
"""

__mod_name__ = "x-ᴡᴇᴀᴛʜᴇʀ"
