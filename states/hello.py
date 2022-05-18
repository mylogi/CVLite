from telebot import types

from states.base import BaseState

data_for_cv: dict = {}


class BaseStateData(BaseState):

    def process_call_back(self, message: types.CallbackQuery):
        if message.data:
            if message.data == 'next state: Hello':
                return Hello
            if message.data == 'next state: CVLite':
                return CVLite
            if message.data == 'next state: AvailableCVTemplates':
                return AvailableCVTemplates
            if message.data == 'next state: CVTips':
                return FirstTip
            if message.data == 'next state: CreateCV':
                return CreateCV
            if message.data == 'next state: FirstTemplate':
                return FirstTemplate
            if message.data == 'next state: SecondTemplate':
                return SecondTemplate
            if message.data == 'next state: AddName':
                return AddName
        return self.__class__


class Template(BaseStateData):

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Create CV', callback_data='next state: CreateCV'))
        keyboard.add(types.InlineKeyboardButton(text='CV Templates', callback_data='next state: AvailableCVTemplates'))
        return keyboard


class Tip(BaseState):

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text='Next tip', callback_data='next state: NextTip'),
            types.InlineKeyboardButton(text='Previous tip', callback_data='next state: PreviousTip')
        )
        keyboard.add(types.InlineKeyboardButton(text='CVLite', callback_data='next state: CVLite'))
        return keyboard


class CreateStep(BaseStateData):
    text_2 = ""

    def get_keyboard_new(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: CreateCV'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddName'))
        return keyboard

    def display_new(self):
        self.bot.send_message(self.chat_id, self.text_2, reply_markup=self.get_keyboard_new(), parse_mode='HTML')


class Hello(BaseStateData):
    text = "<b>Welcome to CVLite!</b>"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='CV Templates', callback_data='next state: AvailableCVTemplates'))
        keyboard.add(types.InlineKeyboardButton(text='CV Tips', callback_data='next state: CVTips'))
        return keyboard


class CVLite(BaseStateData):
    text = "<b>CVLite</b>\n\n Where next?"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='CV Templates', callback_data='next state: AvailableCVTemplates'))
        keyboard.add(types.InlineKeyboardButton(text='CV Tips', callback_data='next state: CVTips'))
        return keyboard


class AvailableCVTemplates(BaseStateData):
    text = "<b>CV Templates</b> \n\n Which one will you choose?"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='1 template', callback_data='next state: FirstTemplate'))
        keyboard.add(types.InlineKeyboardButton(text='2 template', callback_data='next state: SecondTemplate'))
        keyboard.add(types.InlineKeyboardButton(text='CVLite', callback_data='next state: CVLite'))
        return keyboard


class FirstTemplate(Template):
    text = "<b>First template</b>"


class SecondTemplate(Template):
    text = "<b>Second template</b>"


class FirstTip(Tip):
    text = "First tip"

    def process_call_back(self, message: types.CallbackQuery):
        if message.data:
            if message.data == 'next state: NextTip':
                return SecondTip
            if message.data == 'next state: PreviousTip':
                return ThirdTip
            if message.data == 'next state: CVLite':
                return CVLite
        return FirstTip


class SecondTip(Tip):
    text = "Second tip"

    def process_call_back(self, message: types.CallbackQuery):
        if message.data:
            if message.data == 'next state: NextTip':
                return ThirdTip
            if message.data == 'next state: PreviousTip':
                return FirstTip
            if message.data == 'next state: CVLite':
                return CVLite
        return SecondTip


class ThirdTip(Tip):
    text = "Third tip"

    def process_call_back(self, message: types.CallbackQuery):
        if message.data:
            if message.data == 'next state: NextTip':
                return FirstTip
            if message.data == 'next state: PreviousTip':
                return SecondTip
            if message.data == 'next state: CVLite':
                return CVLite
        return ThirdTip


class CreateCV(CreateStep):
    text = "<b>Create CV</b>\n\n Drop photo here\n\n Requirements: ..."
    text_2 = "<b>Photo received</b>\n\n Where next?"

    def save_jpg(self, message):
        file_id = message.photo[-1].file_id
        data_for_cv[self.chat_id] = {'photo': file_id}
        file_info = self.bot.get_file(file_id)
        downloaded_file = self.bot.download_file(file_info.file_path)
        with open('image.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)

    def get_keyboard_new(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: CreateCV'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddName'))
        return keyboard


class AddName(BaseStateData):
    text = '<b>Next step</b>\n\n Enter your name'


# class OptimizePhoto(BaseStateData):
#     text = "Photo optimization options"
#
#     def get_keyboard(self):
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(types.InlineKeyboardButton(text='Auto optimize', callback_data='next state: AutoOptimize'))
#         keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: TryAgain'))
#         return keyboard
#
#     def process_call_back(self, message: types.CallbackQuery):
#         if message.data:
#             if message.data == 'next state: AutoOptimize':
#                 return True
#             if message.data == 'next state: TryAgain':
#                 return CreateCV
#         return OptimizePhoto


class ActionState(BaseState):
    text = 'Sale example: 1 - New Year, 2 - More minutes, 3 - Soon return'

    def process_text_message(self, message: types.Message):
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

    def process_call_back(self, message: types.CallbackQuery):
        if message.data and message.data == 'next state: Hello':
            return Hello
        return ActionAppliedState
