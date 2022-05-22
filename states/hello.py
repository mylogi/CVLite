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
            if message.data == 'next state: AddEmail':
                return AddEmail
            if message.data == 'next state: AddMobNumber':
                return AddMobNumber
            if message.data == 'next state: AddLinkedIn':
                return AddLinkedIn
            if message.data == 'next state: LanguageSkills':
                return LanguageSkills
            if message.data == 'next state: English':
                return English
            if message.data == 'next state: Ukrainian':
                return Ukrainian
        return self.__class__

    def return_step(self):
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

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: CreateCV'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddName'))
        return keyboard


class Language(BaseStateData):
    name = ''

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text='Elementary (A1)', callback_data='next state: Elementary'),
            types.InlineKeyboardButton(text='Pre-Intermediate (A2)', callback_data='next state: PreIntermediate')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='Intermediate (B1)', callback_data='next state: Intermediate'),
            types.InlineKeyboardButton(text='Upper-Intermediate (B2)', callback_data='next state: UpperIntermediate')
        )
        keyboard.add(
            types.InlineKeyboardButton(text='Advanced (C1)', callback_data='next state: Advanced'),
            types.InlineKeyboardButton(text='Proficiency (C2)', callback_data='next state: Proficiency')
        )
        keyboard.add(types.InlineKeyboardButton(text='Native', callback_data='next state: Native'))
        return keyboard

    def save_lang_level(self, message: types.CallbackQuery):
        if message.data == 'next state: Elementary':
            data_for_cv[self.chat_id][self.name] = 'Elementary (A1)'
        elif message.data == 'next state: PreIntermediate':
            data_for_cv[self.chat_id][self.name] = 'Pre-Intermediate (A2)'
        elif message.data == 'next state: Intermediate':
            data_for_cv[self.chat_id][self.name] = 'Intermediate (B1)'
        elif message.data == 'next state: UpperIntermediate':
            data_for_cv[self.chat_id][self.name] = 'Upper-Intermediate (B2)'
        elif message.data == 'next state: Advanced':
            data_for_cv[self.chat_id][self.name] = 'Advanced (C1)'
        elif message.data == 'next state: Proficiency':
            data_for_cv[self.chat_id][self.name] = 'Proficiency (C2)'
        elif message.data == 'next state: Native':
            data_for_cv[self.chat_id][self.name] = 'Native'


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


class CreateCV(BaseStateData):
    text = "<b>Create CV</b> \n\nDrop photo here \n\nRequirements: ..."

    def save_jpg(self, message):
        file_id = message.photo[-1].file_id
        data_for_cv[self.chat_id] = {'photo': file_id}
        file_info = self.bot.get_file(file_id)
        downloaded_file = self.bot.download_file(file_info.file_path)
        with open('image.jpg', 'wb') as new_file:
            new_file.write(downloaded_file)

    def return_step(self):
        return CreateCVStep


class CreateCVStep(CreateStep):
    text = "<b>Photo received</b> \n\nWhere next?"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: CreateCV'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddName'))
        return keyboard


class AddName(BaseStateData):
    text = '<b>Next step</b> \n\nEnter your name'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['name'] = text_by_user.capitalize()

    def return_step(self):
        return AddNameStep


class AddNameStep(CreateStep):
    text = '<b>Name received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddName'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddSurname'))
        return keyboard


class AddSurname(BaseStateData):
    text = '<b>Next step</b> \n\nEnter your surname'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['surname'] = text_by_user.capitalize()

    def return_step(self):
        return AddSurnameStep


class AddSurnameStep(CreateStep):
    text = '<b>Surname received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddSurname'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddEmail'))
        return keyboard


class AddEmail(BaseStateData):
    text = '<b>Next step</b> \n\nEnter your email'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['email'] = text_by_user

    def return_step(self):
        return AddEmailStep


class AddEmailStep(CreateStep):
    text = '<b>Email received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddSurname'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddMobNumber'))
        return keyboard


class AddMobNumber(BaseStateData):
    text = '<b>Next step</b> \n\nEnter your mobile number'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['number'] = text_by_user

    def return_step(self):
        return AddMobNumberStep


class AddMobNumberStep(CreateStep):
    text = '<b>Number received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddMobNumber'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddLinkedIn'))
        return keyboard


class AddLinkedIn(BaseStateData):
    text = '<b>Next step</b> \n\nEnter your LinkedIn url'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['LinkedInUrl'] = text_by_user

    def return_step(self):
        return AddLinkedInStep


class AddLinkedInStep(CreateStep):
    text = '<b>LinkedIn url received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddLinkedIn'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: LanguageSkills'))
        return keyboard


class LanguageSkills(BaseStateData):
    text = '<b>Language skills</b> \n\nClick on the language you speak'

    def get_keyboard(self):
        print(data_for_cv)
        keyboard = types.InlineKeyboardMarkup()
        try:
            if data_for_cv[self.chat_id]['English']:
                keyboard.add(types.InlineKeyboardButton(text=f'English: {data_for_cv[self.chat_id]["English"]}',
                                                        callback_data='next state: English'))
        except KeyError:
            keyboard.add(types.InlineKeyboardButton(text='English', callback_data='next state: English'))
        try:
            if data_for_cv[self.chat_id]['Ukrainian']:
                keyboard.add(types.InlineKeyboardButton(text=f'Ukrainian: {data_for_cv[self.chat_id]["Ukrainian"]}',
                                                        callback_data='next state: Ukrainian'))
        except KeyError:
            keyboard.add(types.InlineKeyboardButton(text='Ukrainian', callback_data='next state: Ukrainian'))
        return keyboard


class English(Language):
    text = '<b>English</b> \n\nWhat is your skill level?'
    name = 'English'

    def return_step(self):
        return EnglishStep


class EnglishStep(CreateStep):
    text = '<b>English level added</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: English'))
        keyboard.add(types.InlineKeyboardButton(text='Languages', callback_data='next state: LanguageSkills'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: LanguageSkills'))
        return keyboard


class Ukrainian(Language):
    text = '<b>Ukrainian</b> \n\nWhat is your skill level?'
    name = 'Ukrainian'

    def return_step(self):
        return UkrainianStep


class UkrainianStep(CreateStep):
    text = '<b>English level added</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: Ukrainian'))
        keyboard.add(types.InlineKeyboardButton(text='Languages', callback_data='next state: LanguageSkills'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: LanguageSkills'))
        return keyboard
