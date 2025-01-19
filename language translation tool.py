import nest_asyncio
nest_asyncio.apply()
import asyncio
from googletrans import Translator
async def translate_text():
    async with Translator() as translator:
        result = await translator.translate('good morning', dest='te')
        print(f"Translated text: {result.text}")
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(translate_text())
loop.close()
