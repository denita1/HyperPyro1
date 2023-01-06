from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from rams import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from rams.helpers.misc import create_botlog, git, heroku

MSG_ON = """
🔥 **RamPyro-Bot Menyala** 🔥
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
🤖 **Userbot Version -** `{}`
⌨️ **Ketik** `{}rama` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ramsupportt")
            await bot.join_chat("k0kb4c0de")
            await bot.join_chat("userbotch")
            await bot.join_chat("GeezSupport")
            await bot.join_chat("mutualan_temanrandom")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("rams").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("dragons").warning(a)
    LOGGER("rams").info(f"RamPyro-Bot v{BOT_VER} [🔥 UDAH AKTIF NGENTOT! 🔥]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("rams").info("Starting RamPyro-Bot")
    install()
    heroku()
    LOOP.run_until_complete(main())
