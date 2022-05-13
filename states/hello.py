from telebot import types

from states.base import BaseState


class Hello(BaseState):
    text = "Welcome to CVLite!"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Sale', callback_data='nextstate: ActionState'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data and message.data == 'nextstate: ActionState':
            return ActionState
        return Hello


class ActionState(BaseState):
    text = 'Sale example: 1 - New Year, 2 - More minutes, 3 - Soon return'

    def process_text_message(self, message: types.Message) -> 'BaseState':
        if message.text in ('1', '2', '3'):
            return ActionAppliedState
        self.send_warning('Press 1, 2 or 3!')
        return ActionState


class ActionAppliedState(BaseState):
    text = 'Sorry mistake with proccesing'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Home', callback_data='nextstate:Hello'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data and message.data == 'nextstate:Hello':
            return Hello
        return ActionAppliedState
