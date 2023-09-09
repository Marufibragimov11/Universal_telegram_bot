from aiogram.dispatcher.filters.state import StatesGroup, State


class MoneyState(StatesGroup):
    Income = State()
    Outcome = State()


class Comment(StatesGroup):
    comment_in = State()
    comment_out = State()


class SocialMedia(StatesGroup):
    insta_state = State()
    yt_state = State()