from pyrogram import Client, filters
from pyrogram.types import *

from LegendGirl.Config import *

from .. import sudos
from ..core.clients import *

wish = False


@Client.on_message(
    filters.user(sudos) & filters.command(["gm" "gdmrng"], prefixes=HANDLER)
)
async def gdmrngcmd(Legend: Client, e: Message):
    try:
        text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
    except IndexError:
        return await e.reply_text(usage)
    wishgdmrng = "╭━━━┳━━━┳━━━┳━━━╮\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\n╰━━━┻━━━┻━━━┻━━━╯.\n\n╱╱╱╱╱╱╱╱╱╱╭╮\n╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯"
    flag = text[0]
    counts = int(text[1])
    if flag == "-u":
        global wish
        wish = True
        if e.reply_to_message:
            lmao = e.reply_to_message
            while wish == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(
                            e.chat.id, f"{lmao.from_user.mention}\n\n{wishgdmrng}"
                        )
        else:
            while wish == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, wishgdmrng)
    else:
        if e.reply_to_message:
            lmao = e.reply_to_message
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(
                            e.chat.id, f"{lmao.from_user.mention}\n\n{wishgdmrng}"
                        )
        else:
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, wishgdmrng)
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"#Started Good Morning Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["stopwish"], prefixes=HANDLER)
)
async def stopwish(_, e: Message):
    global wish
    wish = False
    await e.reply_text("Stopped Unlimited Wish gdmrng")