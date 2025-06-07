class script(object):
    START_TXT = """<b>Hᴇʏ {}, </b>\n\n<i>Send me a file or add me as an admin to any channel to instantly generate file links.

Add me to your channel to instantly generate links for any downloadable media. Once received, I will automatically attach appropriate buttons to the post containing the URL.</i>\n\n<blockquote><a href="https://t.me/{}?startchannel&admin=post_messages+edit_messages+delete_messages">➜ 𝖠𝖽𝖽 𝖳𝗈 𝖢𝗁𝖺𝗇𝗇𝖾𝗅</a></blockquote>"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.6 [ Sᴛᴀʙʟᴇ ]</code></b>"""

    HELP_TXT = """<b>ʏᴏᴜ ᴅᴏɴ'ᴛ ɴᴇᴇᴅ ᴍᴀɴʏ ᴄᴏᴍᴍᴇɴᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 

ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ғɪʟᴇs ᴀɴᴅ I ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs

ᴀʟsᴏ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ — ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ 💥

ғᴏʀ ᴍᴏʀᴇ, ᴜꜱᴇ /help ᴏʀ /about</b>

<u><i>ʀᴇᴘᴏʀᴛ ʙᴜɢs ᴛᴏ <a href='https://t.me/AV_OWNER_BOT'>ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></i></u>"""

    LOG_TEXT = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""

    ABOUT_TXT = """<b>╔═══❰ {} ❱══════❍
║╭━━━━━━━━━━━━━━━━━━➣
║┣⪼ 🤖 ᴍʏ ɴᴀᴍᴇ : {}
║┣⪼ 👦 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/marvaldoom'>ᴄʜᴀᴛ ᴏᴡɴᴇʀ</a>
║┣⪼ ❣️ ᴜᴘᴅᴀᴛᴇ : <a href="https://t.me/marvaldoom">ʙᴏᴛᴢ</a>
║┣⪼ ⏲️ ᴜᴘᴛɪᴍᴇ : {}
║┣⪼ 📡 ʜᴏsᴛᴇᴅ ᴏɴ : ᴋᴏʏᴇʙ 
║┣⪼ 🗣️ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 
║┣⪼ 📚 ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ
║┣⪼ 🗒️ ᴠᴇʀsɪᴏɴ : v{} [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ </b>"""

    AUTH_TXT = """<b>Dᴇᴀʀ {}!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>"""

    CAPTION_TXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

<b>📧 ꜰɪʟᴇ ɴᴀᴍᴇ :- </b> <i><a href="{0}">{1}</a></i>

<b>📦 ꜰɪʟᴇ sɪᴢᴇ :- </b> <i>{2}</i>

<b><u><i>Tap To Copy Link 👇</i></u></b>

<b>🖥 Stream  : </b> <code>{3}</code>

<b>📥 Download : </b> <code>{4}</code>

<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE </b>"""

    CAPTION2_TXT = """
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>

<b>📧 ꜰɪʟᴇ ɴᴀᴍᴇ :- </b> <i><a href="{0}">{1}</a></i>

<b>📦 ꜰɪʟᴇ sɪᴢᴇ :- </b> <i>{2}</i>

<b><u><i>Tap To Copy Link 👇</i></u></b>

<b>📥 Download : </b> <code>{3}</code>

<b>🚸 Nᴏᴛᴇ : LINK WON'T EXPIRE TILL I DELETE </b>"""
