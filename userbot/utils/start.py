from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/bd7cae1518e65f940ac11.jpg",
                caption="✨ **Yansen Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 7.0@master\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @trashme2 ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/YansenSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
