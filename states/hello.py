from telebot import types

from states.base import BaseState


class Hello(BaseState):
    text = "<b>Welcome to CVLite!</b>"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='CV Templates', callback_data='next state: AvailableCVTemplates'))
        keyboard.add(types.InlineKeyboardButton(text='CV Tips', callback_data='next state: CVTips'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data:
            if message.data == 'next state: AvailableCVTemplates':
                return AvailableCVTemplates
            if message.data == 'next state: CVTips':
                return CVTipsMenu
        return Hello


class AvailableCVTemplates(BaseState):
    text = "<b>CV Templates</b> \n\n Which one will you choose?"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='1 template', callback_data='next state: FirstTemplate'))
        keyboard.add(types.InlineKeyboardButton(text='2 template', callback_data='next state: SecondTemplate'))
        keyboard.add(types.InlineKeyboardButton(text='Back', callback_data='next state: Hello'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data:
            if message.data == 'next state: FirstTemplate':
                return FirstTemplate
            if message.data == 'next state: SecondTemplate':
                return SecondTemplate
            if message.data == 'next state: Hello':
                return Hello
            return AvailableCVTemplates


class FirstTemplate(BaseState):
    text = "<b>First template</b>"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Create CV', callback_data='next state: CreateCV'))
        keyboard.add(types.InlineKeyboardButton(text='CV Templates', callback_data='next state: AvailableCVTemplates'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data:
            if message.data == 'next state: CreateCV':
                return CreateCV
            if message.data == 'next state: AvailableCVTemplates':
                return AvailableCVTemplates
            return FirstTemplate


class SecondTemplate(BaseState):
    text = "<b>Second template</b>"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Create CV', callback_data='next state: CreateCV'))
        keyboard.add(types.InlineKeyboardButton(text='CV Templates', callback_data='next state: AvailableCVTemplates'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data:
            if message.data == 'next state: CreateCV':
                return CreateCV
            if message.data == 'next state: AvailableCVTemplates':
                return AvailableCVTemplates
            return SecondTemplate


class CVTipsMenu(BaseState):
    text = '<b>\t CV Tips</b> \n\n What is needed for CV? Read on!'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text='Next tip', callback_data='next state: NextTip'),
            types.InlineKeyboardButton(text='Previous tip', callback_data='next state: PreviousTip')
        )
        keyboard.add(types.InlineKeyboardButton(text='CV Templates', callback_data='next state: AvailableCVTemplates'))
        keyboard.add(types.InlineKeyboardButton(text='Back', callback_data='next state: Hello'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data:
            if message.data == 'next state: NextTip':
                pass
            if message.data == 'next state: PreviousTip':
                pass
            if message.data == 'next state: AvailableCVTemplates':
                return AvailableCVTemplates
            if message.data == 'next state: Hello':
                return Hello
        return self

    def send_tip(self, number):
        self.bot.send_message(
            self.chat_id, self.image_name_dictionary[number], parse_mode='HTML')
        self.bot.send_message(
            self.chat_id, self.tips_dictionary[number], parse_mode='HTML')


class CreateCV(BaseState):
    text = "<b>Create CV</b>\n\n Follow the instructions to create a CV.\n\n Good luck!"


class ActionState(BaseState):
    text = 'Sale example: 1 - New Year, 2 - More minutes, 3 - Soon return'

    def process_text_message(self, message: types.Message) -> 'BaseState':
        if message.text in ('1', '2', '3'):
            return ActionAppliedState
        self.send_warning('Press 1, 2 or 3!')
        return ActionState


class ActionAppliedState(BaseState):
    text = 'Sorry mistake with processing'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Home', callback_data='next state: Hello'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data and message.data == 'next state: Hello':
            return Hello
        return ActionAppliedState
