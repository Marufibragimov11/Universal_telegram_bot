import pytz
from aiogram import types
from loader import dp, bot, db
from states.all_states import MoneyState, Comment
from aiogram.dispatcher import FSMContext

from keyboards.inline.main_btn import menu_btn, months_menu, detailed_btn
from datetime import datetime

all_months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
month_lst = []


# For Income
@dp.callback_query_handler(text="income")
async def incomes(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id,
                           text="🤑Qancha pul tushdi?")
    await MoneyState.Income.set()


@dp.message_handler(state=MoneyState.Income)
async def answer_fullname(message: types.Message, state: FSMContext):
    money_in = message.text
    await state.update_data(
        {"profit": money_in}
    )

    await message.answer("💬Kommentariya yozing!")
    await Comment.comment_in.set()


@dp.message_handler(state=Comment.comment_in)
async def get_comment(message: types.Message, state: FSMContext):
    comment_in = message.text
    await state.update_data(
        {"comment": comment_in}
    )

    # get data
    data = await state.get_data()
    user_id = message.from_user.id
    income_sum = data.get('profit')
    income_comment = data.get('comment')

    # get time and date
    format_data = "%d/%B/%y %H:%M:%S"
    current_data = datetime.now(pytz.timezone('Asia/Tashkent'))
    in_time = current_data.strftime(format_data)

    await message.answer("Ma'lumotlar bazaga yuklandi. Raxmat! ✅\n"
                         "Quidagi bo'limlardan birini tanlang 👇🏻", reply_markup=menu_btn)
    await state.finish()

    db.add_income(user_id=user_id, sum=income_sum, comment=income_comment, data=in_time, state="income")


# For Outcome
@dp.callback_query_handler(text="outcome")
async def outcomes(call: types.CallbackQuery):
    await call.message.delete()
    await bot.send_message(chat_id=call.from_user.id,
                           text="💸Qancha pul sarfladingiz?")
    await MoneyState.Outcome.set()


@dp.message_handler(state=MoneyState.Outcome)
async def get_outcome(message: types.Message, state: FSMContext):
    money_out = message.text
    await state.update_data(
        {"bills": money_out}
    )

    await message.answer("💬Kommentariya yozing!")
    await Comment.comment_out.set()


@dp.message_handler(state=Comment.comment_out)
async def get_comment(message: types.Message, state: FSMContext):
    comment_out = message.text
    await state.update_data(
        {"comment": comment_out}
    )
    # get data
    data = await state.get_data()
    user_id = message.from_user.id
    outcome_sum = data.get('bills')
    outcome_comment = data.get('comment')

    # get time and date
    format_data = "%d/%B/%y %H:%M:%S"
    current_data = datetime.now(pytz.timezone('Asia/Tashkent'))
    out_time = current_data.strftime(format_data)

    await message.answer("Ma'lumotlar bazaga yuklandi. Raxmat!✅ \n"
                         "Quidagi bo'limlardan birini tanlang 👇🏻", reply_markup=menu_btn)
    await state.finish()

    db.add_income(user_id=user_id, sum=outcome_sum, comment=outcome_comment, data=out_time, state="outcome")


# For statistics
@dp.callback_query_handler(text="statistics")
async def statistics(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("📊Qaysi oyni statistikasi kerak?", reply_markup=months_menu)


@dp.callback_query_handler(text=all_months)
async def send_data(call: types.CallbackQuery):
    total_in = db.get_income_data(user_id=call.from_user.id, month=call.data)
    total_out = db.get_outcome_data(user_id=call.from_user.id, month=call.data)
    if len(total_in) == 0 and len(total_out) == 0:
        await call.message.delete()
        await bot.send_message(chat_id=call.from_user.id,
                               text="‼️Bu oy uchun xech qanday ma'lumot yo'q! \n"
                                    "Quidagi bo'limlardan birini tanlang 👇🏻",
                               reply_markup=menu_btn)
    else:
        await call.message.delete()
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"🟢Bu oydagi foydangiz: <b>💲{sum(total_in)}</b> \n"
                                    f"\n"
                                    f"🔴Bu oydagi xarajatlaringiz: <b>➖{sum(total_out)}</b> \n"
                                    f"\n"
                                    f"⚪️Qolishi kerak bo'lgan summa: <b>{sum(total_in) - sum(total_out)}</b>",
                               reply_markup=detailed_btn)
        month_lst.append(call.data)


@dp.callback_query_handler(text="all_details")
async def all_statistics(call: types.CallbackQuery):
    await call.message.delete()

    in_data = db.get_more_indata(call.from_user.id, month_lst[0])
    out_data = db.get_more_outdata(call.from_user.id, month_lst[0])

    await bot.send_message(chat_id=call.from_user.id,
                           text="‼️Bu oyda kelib tushgan summa 👇🏻")
    for i in in_data:
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"💵Kelib tushgan summa: <b>${i[0]}</b>\n"
                                    f"❓Nma uchun: <b>{i[1]}</b> \n"
                                    f"⏳Vaqti: {i[2]}")

    await bot.send_message(chat_id=call.from_user.id,
                           text="‼️Umumiy qilingan xarajatlar 👇🏻")
    for i in out_data:
        await bot.send_message(chat_id=call.from_user.id,
                               text=f"💵Xarajatlar: <b>-{i[0]}</b>\n"
                                    f"❓Nma uchun sarflangan: <b>{i[1]}</b> \n"
                                    f"⏳Vaqti: {i[2]}")

    await bot.send_message(chat_id=call.from_user.id,
                           text="Quidagi bo'limlardan birini tanlang 👇🏻", reply_markup=menu_btn)
    month_lst.clear()


@dp.callback_query_handler(text="menu")
async def main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Quidagi bo'limlardan birini tanlang 👇🏻", reply_markup=menu_btn)
