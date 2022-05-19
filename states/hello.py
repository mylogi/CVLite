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
            if message.data == 'next state: AddSurname':
                return AddSurname
            if message.data == 'next state: AddMail':
                return AddMail
            if message.data == 'next state: AddMobNumber':
                return AddMobNumber
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
    text = "<b>CVLite</b> \n\nWhere next?"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='CV Templates', callback_data='next state: AvailableCVTemplates'))
        keyboard.add(types.InlineKeyboardButton(text='CV Tips', callback_data='next state: CVTips'))
        return keyboard


class AvailableCVTemplates(BaseStateData):
    text = "<b>CV Templates</b> \n\nWhich one will you choose?"

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
    text = "<b>Create CV</b> \n\nDrop photo here \n\nRequirements: ..."
    text_2 = "<b>Photo received</b> \n\nWhere next?"

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


class AddName(CreateStep):
    text = '<b>Next step</b> \n\nEnter your name'
    text_2 = '<b>Name received</b> \n\nWhere next?'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['name'] = text_by_user.capitalize()

    def get_keyboard_new(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddName'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddSurname'))
        return keyboard


class AddSurname(CreateStep):
    text = '<b>Next step</b> \n\nEnter your surname'
    text_2 = '<b>Surname received</b> \n\nWhere next?'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['surname'] = text_by_user.capitalize()

    def get_keyboard_new(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddSurname'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddMail'))
        return keyboard


class AddMail(CreateStep):
    text = '<b>Next step</b> \n\nEnter your mail'
    text_2 = '<b>Mail received</b> \n\nWhere next?'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['mail'] = text_by_user

    def get_keyboard_new(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddSurname'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddMobNumber'))
        return keyboard


class AddMobNumber(CreateStep):
    text = '<b>Next step</b> \n\nEnter your mobile number'
    text_2 = '<b>Number received</b> \n\nWhere next?'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['number'] = text_by_user
        print(data_for_cv)

    def get_keyboard_new(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddSurname'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddLinkedIn'))
        return keyboard


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
