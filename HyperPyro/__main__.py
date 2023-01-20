import time
import importlib
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from HyperPyro import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from HyperPyro.helpers.misc import create_botlog, git, heroku
from HyperPyro.modules import ALL_MODULES

MSG_ON = """
🔥 **HyperPyro-Bot Activated** 🔥
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
🤖 **Userbot Version -** `{}`
⌨️ **Ketik** `{}ling` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""
MSG_BOT = (f"**Hyper Robot Assistant**\nis alive...")


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"HyperPyro.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("HyperSupportQ")
            await bot.join_chat("storyQi")
            await bot.join_chat("ProjectHyper")
            await bot.join_chat("drasticmeasureson")
            await bot.join_chat("zonkeyamanahdansyariah")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("HyperPyro").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("master").warning(a)
    LOGGER("HyperPyro").info(f"Hyper-Bot v{BOT_VER} [🔥 UDAH AKTIF BLOK! 🔥]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("HyperPyro").info("Starting Hyper-Bot")
    install()
    heroku()
    LOOP.run_until_complete(main())
