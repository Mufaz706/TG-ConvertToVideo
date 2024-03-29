class Translation(object):


#This will be appeared when anyone use start command

      START = """Hello {0}

I am a converter clone of [Convert Ns Bot](https://telegram.dog/convert_Ns_bot) by {1}

I can convert file to video or video to file with custom thumbnail support.
"""

else:
            first_name = update.effective_user.first_name
            update.effective_message.reply_text(
                PM_START_TEXT.format(escape_markdown(first_name), escape_markdown(bot.first_name), OWNER_ID),

                parse_mode=ParseMode.MARKDOWN, reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton(text="👨‍💼 Master", url="t.me/MRK_YT"),  InlineKeyboardButton(text="Help 🤔", url="https://t.me/{}?start=help".format(bot.username))],
                     [InlineKeyboardButton(text="🖥️ Tutorial Video🖥️", url="https://youtu.be/wKL90i3cjPw")],
                     [InlineKeyboardButton(text="👥 Any Doubt", url="t.me/Mo_Tech_Group"), InlineKeyboardButton(text="MT Updates🤖", url="t.me/Mo_Tech_YT")],
                     [InlineKeyboardButton(text="🎬 YT Channel", url="https://youtube.com/channel/UCmGBpXoM-OEm-FacOccVKgQ"), InlineKeyboardButton(text="Repo ⛓️", url="https://github.com/MRK-YT/MT-Rose-Bot-Model")],
                     [InlineKeyboardButton(text="➕ Add me to your group ➕", url="t.me/{}?startgroup=true".format(bot.username)) ]]))
    else:

#This will be appeared when anyone use help command

      HELP = """**Hey you need help 🤔 ?**

1. Send me the telegram file or video which you wanted to convert.

2. Send me the thumbnail(photo) optional.

3. Reply to video /converttofile for converting into file.

4. Reply to file /converttovideo for converting into video.

**SUPPORT GROUP:** [NS Bot Supporters](https://telegram.dog/Ns_Bot_supporters)
"""


#Please don't change this about command 🙏

      ABOUT = """
**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**👨‍💻 Developer:** [Anonymous](https://t.me/Ns_AnoNymouS)

**📮 Channel:** [NS BOT UPDATES](https://t.me/Ns_bot_updates)

**👥 Group:** [NS BOT SUPPOTERS](https://t.me/Ns_Bot_supporters)

**💻 Source Code:**[Press Me](https://github.com/Ns-AnoNymouS/TG-CONVERT-BOT)

"""

##############################################################################################################################
##############################################################################################################################


#DON'T CHANGE THE NUMBERS IN THE FLOWER BRACKETS AND THE ORDER OF PERCENTAGE, DONE, TOTAL, SPEED, ETA ONLY CHANGE THE THEME 

      PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
       
      DOWNLOAD_PROGRESS = "▪️"
      UPLOAD_PROGRESS = "▫️"

##############################################################################################################################
##############################################################################################################################

      DOWNLOAD_START = "Trying to Download 📥"
      DOWNLOAD_COMPLETE = "✅ Media Downloaded successfully\nPreparing for upload"
      UPLOAD_START = "Trying to Upload 📤"
      UPLOAD_COMPLETE = "THANKS FOR USING ME"
      SAVED_CUSTOM_THUMB_NAIL = "✅ Saved Thumbnail Successfully. This will be deleted in 24hrs"
      BANNED_TEXT = "YOU ARE BANNED. SO YOUR ARE NOT ABLE TO USE ME 🐒"
      REPLY_TEXT = "👩‍✈️ Reply to the media which you need to convert"
      DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail Deleted Successfully ✅"
