from pytgcalls import idle
from config import call_py
from music.التشغيل import arq
async def main():
    await call_py.start()
    print("""    ------------------
   | تم تشغيل سورس سمسون ميوزك بنجاح ✅ ! |
    ------------------"""    )
    await idle()
    await arq.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
