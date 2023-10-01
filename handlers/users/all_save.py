from aiogram import types
import logging
from loader import dp, bot, db
from utils.insta_saver import save_insta
from utils.youtube_saver import download_yt
from aiogram.dispatcher import FSMContext
from keyboards.inline.main_btn import menu_btn
from states.all_states import SocialMedia


# Save from instagram
@dp.callback_query_handler(text="insta_save")
async def insta_save(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id,
                           text="Iltimos Link yuboring!")
    await SocialMedia.insta_state.set()


@dp.message_handler(state=SocialMedia.insta_state, content_types=types.ContentTypes.TEXT)
async def send_video(message: types.Message, state: FSMContext):
    url = message.text
    if 'https://www.instagram.com/' in url:
        await message.answer('🔍')
        r_url = save_insta(url)
        if r_url:
            await message.reply_video(video=r_url, caption="Tayyor✅")
            await message.answer("Quidagi bo'limlardan birini tanlang 👇🏻", reply_markup=menu_btn)
            await state.finish()
        else:
            await message.answer("Siz yuborgan link bo'yicha xech nma yuklab bo'lmadi!!!\n"
                                 "Iltimos boshqa link yuboring!")
    else:
        await message.answer("Iltimos link yuboring!")


# Save from YouTube
@dp.callback_query_handler(text="yt_save")
async def youtube_save(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Iltimos YouTube dan link yuboring!")
    await SocialMedia.yt_state.set()


@dp.message_handler(state=SocialMedia.yt_state)
async def send_video_yt(message: types.Message, state: FSMContext):
    url = message.text
    if 'https://youtu.be/' in url:
        await message.answer('🔍')
        name = download_yt(url)
        try:
            with open(name, 'rb') as video:
                await bot.send_video(chat_id=message.from_user.id, video=video)
                await message.answer("Quidagi bo'limlardan birini tanlang 👇🏻", reply_markup=menu_btn)
                await state.finish()
        except Exception as e:
            logging.error(str(e))
            await message.answer("Xatolik yuz berdi. Bu link orqali video yuklab bolmadi! \n"
                                 "Iltimos boshqa link yuboring")
    else:
        await message.answer("Iltimos link yuboring!")
