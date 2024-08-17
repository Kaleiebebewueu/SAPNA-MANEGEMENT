import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from MukeshRobot import pbot


@pbot.on_message(filters.command("telegraph"))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ"
        )
    try:
        text = await message.reply("❍ ᴘʀᴏᴄᴇssɪɴɢ...")

        async def progress(current, total):
            await text.edit_text(f"❍ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ... {current * 100 / total:.1f}%")

        try:
            location = f"cache"
            local_path = await message.reply_to_message.download(
                location, progress=progress
            )
            await text.edit_text("❍ ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
            upload_path = upload_file(local_path)
            await text.edit_text(
                f"❖ | [ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ](https://telegra.ph{upload_path[0]}) | ❖",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ •",
                                url=f"https://telegra.ph{upload_path[0]}",
                            )
                        ]
                    ]
                ),
            )
            os.remove(local_path)
        except Exception as e:
            await text.edit_text(f"❍ |ғɪʟᴇ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ \n\n<i>ʀᴇᴀsᴏɴ: {e}</i>")
            os.remove(local_path)
            return
    except Exception:
        pass
__help__ = """
 ❍ ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ


 ❍ /telegraph ➛ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ
 ❍ /tgt ➛ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴛᴇxᴛ
 ❍ /tgt [ᴄᴜsᴛᴏᴍ ɴᴀᴍᴇ] ➛ ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴛᴇxᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ɴᴀᴍᴇ.
"""

__mod_name__ = "ɢʀᴀᴘʜ"
