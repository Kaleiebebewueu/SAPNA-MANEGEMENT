import requests
from telegram import ParseMode
from telegram.ext import CommandHandler

# Imports dispatcher = updater.dispatcher from __init__.py (*MUST EDIT* CHANGE MODULE NAME TO THE FOLDER NAME OF MODULES IN YOUR BOT)
from MukeshRobot import dispatcher

# Main code, Credit to https://github.com/itspro-dev for making the API. 
def ann(update, context):
    try:
        msg = update.effective_message
        # API (DON'T EDIT)
        url = f'https://api.animeepisode.org/waifu/animenews.php'
        result = requests.get(url).json()
        img = result['Post_image']
        # Message (EDIT THIS PART AS HTML *IF YOU WANT*)
        text = f'''
<b>❍ ᴛɪᴛʟᴇ ➛</b> <code>{result['Post_title']}</code>
        
<b>❍ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➛</b> <code>{result['Description']}</code>

<b>❍ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ➛</b> <code>{result['Post_url']}</code>
'''
        msg.reply_photo(photo=img, caption=text, parse_mode=ParseMode.HTML)

    except Exception as e:
        text = f'<b>Error</b>: <code>' + e + '</code>'
        msg.reply_text(text, parse_mode=ParseMode.HTML)

# Code Handler (YOU CAN CHANGE 'ann' TO ANY 'cmd' FOR THIS TO BE WORKED AS '/cmd' *IF YOU WANT*.)
ANN_HANDLER = CommandHandler('ann', ann, run_async=True)
dispatcher.add_handler(ANN_HANDLER)

#  Buttons for /help .
__mod_name__ = "ᴀɴɪᴍᴇ-ɴ"  # *IF YOU WANT* EDIT NAME OF BUTTON IN '/help'

# *IF YOU WANT* EDIT MESSAGE FOR HELP OF THIS MODULE.
__help__ = '''
❍ `/ann` ➛ ɢɪᴠᴇs ʟᴀᴛᴇsᴛ ᴀɴɪᴍᴇ ɴᴇᴡs.
❍ `/subscribe` ➛ sᴜsᴄʀɪʙᴇs ᴛᴏ ᴀɴɪᴍᴇ ɴᴇᴡs ɴᴇᴛᴡᴏʀᴋ ғᴇᴇᴅs.
❍ `/unsubscribe` ➛ sᴜsᴄʀɪʙᴇs ᴛᴏ ᴀɴɪᴍᴇ ɴᴇᴡs ɴᴇᴛᴡᴏʀᴋ ғᴇᴇᴅs.
'''

# DON'T EDIT
__handlers__ = [ANN_HANDLER]
