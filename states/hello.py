import requests
from fpdf import FPDF
from telebot import types

from states.base import BaseState, MESSAGES

data_for_cv: dict = {}

data_for_cv_lang: dict = {}

data_for_cv_soft: dict = {}

data_for_cv_hard: dict = {}

data_for_cv_exp: dict = {}

data_number_soft: dict = {}

data_number_hard: dict = {}

data_number_exp: dict = {}


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
            if message.data == 'next state: SoftSkills':
                return SoftSkills
            if message.data == 'next state: Collaboration':
                return Collaboration
            if message.data == 'next state: TimeManagement':
                return TimeManagement
            if message.data == 'next state: Feedback':
                return Feedback
            if message.data == 'next state: Analysis':
                return Analysis
            if message.data == 'next state: HardSkills':
                return HardSkills
            if message.data == 'next state: Python':
                return Python
            if message.data == 'next state: Django':
                return Django
            if message.data == 'next state: OOP':
                return OOP
            if message.data == 'next state: DataStructures':
                return DataStructures
            if message.data == 'next state: Experience':
                return Experience
            if message.data == 'next state: AddNewJob':
                return AddNewJob
            if message.data == 'next state: AddCompanyName':
                return AddCompanyName
            if message.data == 'next state: AddCompanyExp':
                return AddCompanyExp
            if message.data == 'next state: AddYourPosition':
                return AddYourPosition
            if message.data == 'next state: AddAboutYou':
                return AddAboutYou
            if message.data == 'next state: CreatePDF':
                return CreatePDF
        return self.__class__

    def return_step(self):
        return self.__class__

    def for_save_skill(self, data_dictionary: dict, number_dictionary: dict):
        try:
            if data_dictionary[self.chat_id]:
                data_dictionary[self.chat_id][self.name] = self.text_for_dict
                number_dictionary[self.chat_id].append(1)
        except KeyError:
            data_dictionary[self.chat_id] = {}
            data_dictionary[self.chat_id][self.name] = self.text_for_dict
            number_dictionary[self.chat_id].append(1)

    def for_remove_skill(self, data_dictionary: dict, number_dictionary: dict):
        del data_dictionary[self.chat_id][self.name]
        if len(number_dictionary[self.chat_id]) == 1:
            del number_dictionary[self.chat_id]
            del data_dictionary[self.chat_id]
        else:
            number_dictionary[self.chat_id].pop()

    def for_display_skill(self, number_dictionary: dict):
        number_dictionary[self.chat_id] = []
        self.bot.delete_message(self.chat_id, MESSAGES[self.chat_id], timeout=0)
        message_from_bot = self.bot.send_message(
            self.chat_id,
            self.text,
            reply_markup=self.get_keyboard(),
            parse_mode='HTML'
        )
        MESSAGES[self.chat_id] = message_from_bot.id


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
    name = ""

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

    def save_skill(self, message: types.CallbackQuery):
        try:
            if data_for_cv_lang[self.chat_id]:
                self.for_save_skill_lang(message)
        except KeyError:
            data_for_cv_lang[self.chat_id] = {}
            self.for_save_skill_lang(message)

    def for_save_skill_lang(self, message):
        if message.data == 'next state: Elementary':
            data_for_cv_lang[self.chat_id][self.name] = 'Elementary (A1)'
        elif message.data == 'next state: PreIntermediate':
            data_for_cv_lang[self.chat_id][self.name] = 'Pre-Intermediate (A2)'
        elif message.data == 'next state: Intermediate':
            data_for_cv_lang[self.chat_id][self.name] = 'Intermediate (B1)'
        elif message.data == 'next state: UpperIntermediate':
            data_for_cv_lang[self.chat_id][self.name] = 'Upper-Intermediate (B2)'
        elif message.data == 'next state: Advanced':
            data_for_cv_lang[self.chat_id][self.name] = 'Advanced (C1)'
        elif message.data == 'next state: Proficiency':
            data_for_cv_lang[self.chat_id][self.name] = 'Proficiency (C2)'
        elif message.data == 'next state: Native':
            data_for_cv_lang[self.chat_id][self.name] = 'Native'


class SoftSkill(BaseStateData):
    name = ""
    text_for_dict: str = ""

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        try:
            if data_for_cv_soft[self.chat_id][self.name]:
                keyboard.add(types.InlineKeyboardButton(text='Remove', callback_data='next state: RemoveSkill'))
        except KeyError:
            keyboard.add(types.InlineKeyboardButton(text='Add', callback_data='next state: AddSoftSkill'))
        return keyboard

    def save_skill(self, message):
        if message.data == 'next state: AddSoftSkill':
            self.for_save_skill(data_for_cv_soft, data_number_soft)
        if message.data == 'next state: RemoveSkill':
            self.for_remove_skill(data_for_cv_soft, data_number_soft)


class HardSkill(BaseStateData):
    name = ""
    text_for_dict: str = ""

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        try:
            if data_for_cv_hard[self.chat_id][self.name]:
                keyboard.add(types.InlineKeyboardButton(text='Remove', callback_data='next state: RemoveSkill'))
        except KeyError:
            keyboard.add(types.InlineKeyboardButton(text='Add', callback_data='next state: AddHardSkill'))
        return keyboard

    def save_skill(self, message):
        if message.data == 'next state: AddHardSkill':
            self.for_save_skill(data_for_cv_hard, data_number_hard)
        if message.data == 'next state: RemoveSkill':
            self.for_remove_skill(data_for_cv_hard, data_number_hard)


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
        keyboard.add(types.InlineKeyboardButton(text='1st template', callback_data='next state: FirstTemplate'))
        keyboard.add(types.InlineKeyboardButton(text='2nd template', callback_data='next state: SecondTemplate'))
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
    text = '<b>Next step</b> \n\nEnter your LinkedIn url \n\nRequirements: ...'

    def save_text(self, message):
        text_by_user = message.text
        try:
            response = requests.get(text_by_user)
            if response.status_code == 200:
                data_for_cv[self.chat_id]['LinkedInUrl'] = text_by_user
        except Exception:
            data_for_cv[self.chat_id]['LinkedInUrl'] = 'non-response'

    def return_step(self):
        return AddLinkedInStep


class AddLinkedInStep(CreateStep):
    text = '<b>LinkedIn url received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddLinkedIn'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddYourPosition'))
        return keyboard


class AddYourPosition(BaseStateData):
    text = '<b>Next step</b> \n\nEnter your position for CV'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['YourPosition'] = text_by_user

    def return_step(self):
        return AddYourPositionStep


class AddYourPositionStep(CreateStep):
    text = '<b>Your position received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddYourPosition'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddAboutYou'))
        return keyboard


class AddAboutYou(BaseStateData):
    text = '<b>Next step</b> \n\nEnter "About You": \n\nRequirements: ...'

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv[self.chat_id]['AboutYou'] = text_by_user

    def return_step(self):
        return AddAboutYouStep


class AddAboutYouStep(CreateStep):
    text = '<b>"About you" received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddAboutYou'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: LanguageSkills'))
        return keyboard


class LanguageSkills(BaseStateData):
    text = '<b>Language skills</b> \n\nClick on the language you speak'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        try:
            if data_for_cv_lang[self.chat_id]['English']:
                keyboard.add(types.InlineKeyboardButton(text=f'English: {data_for_cv_lang[self.chat_id]["English"]}',
                                                        callback_data='next state: English'))
        except KeyError:
            keyboard.add(types.InlineKeyboardButton(text='English', callback_data='next state: English'))
        try:
            if data_for_cv_lang[self.chat_id]['Ukrainian']:
                keyboard.add(types.InlineKeyboardButton(
                    text=f'Ukrainian: {data_for_cv_lang[self.chat_id]["Ukrainian"]}',
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
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: SoftSkills'))
        return keyboard


class Ukrainian(Language):
    text = '<b>Ukrainian</b> \n\nWhat is your skill level?'
    name = 'Ukrainian'

    def return_step(self):
        return UkrainianStep


class UkrainianStep(CreateStep):
    text = '<b>Ukrainian level added</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: Ukrainian'))
        keyboard.add(types.InlineKeyboardButton(text='Languages', callback_data='next state: LanguageSkills'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: SoftSkills'))
        return keyboard


class SoftSkills(BaseStateData):
    text = "<b>Soft Skills</b> \n\nChoose 3 skills that are right for you!"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        if len(data_number_soft[self.chat_id]) == 3:
            keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: HardSkills'))
        else:
            try:
                if data_for_cv_soft[self.chat_id]['Collaboration']:
                    keyboard.add(types.InlineKeyboardButton(text='Collaboration: Selected',
                                                            callback_data='next state: Collaboration'))
            except KeyError:
                keyboard.add(
                    types.InlineKeyboardButton(text='Collaboration', callback_data='next state: Collaboration'))
            try:
                if data_for_cv_soft[self.chat_id]['TimeManagement']:
                    keyboard.add(types.InlineKeyboardButton(text='Time management: Selected',
                                                            callback_data='next state: TimeManagement'))
            except KeyError:
                keyboard.add(
                    types.InlineKeyboardButton(text='Time management', callback_data='next state: TimeManagement'))
            try:
                if data_for_cv_soft[self.chat_id]['Feedback']:
                    keyboard.add(types.InlineKeyboardButton(text='Feedback: Selected',
                                                            callback_data='next state: Feedback'))
            except KeyError:
                keyboard.add(types.InlineKeyboardButton(text='Feedback', callback_data='next state: Feedback'))
            try:
                if data_for_cv_soft[self.chat_id]['Analysis']:
                    keyboard.add(types.InlineKeyboardButton(text='Analysis: Selected',
                                                            callback_data='next state: Analysis'))
            except KeyError:
                keyboard.add(types.InlineKeyboardButton(text='Analysis', callback_data='next state: Analysis'))
        return keyboard

    def display(self):
        try:
            if data_number_soft[self.chat_id]:
                if len(data_number_soft[self.chat_id]) == 3:
                    self.text = "<b>Soft Skills</b> \n\nYou have chosen the available number of Soft skills."
                self.bot.delete_message(self.chat_id, MESSAGES[self.chat_id], timeout=0)
                message_from_bot = self.bot.send_message(
                    self.chat_id,
                    self.text,
                    reply_markup=self.get_keyboard(),
                    parse_mode='HTML'
                )
                MESSAGES[self.chat_id] = message_from_bot.id
        except KeyError:
            self.for_display_skill(data_number_soft)


class Collaboration(SoftSkill):
    text = "<b>Collaboration</b> \n\nWhat will you choose?"
    name = "Collaboration"
    text_for_dict = "Collaboration - text"

    def return_step(self):
        return SoftSkills


class TimeManagement(SoftSkill):
    text = "<b>Time Management</b> \n\nWhat will you choose?"
    name = "TimeManagement"
    text_for_dict = "Time Management - text"

    def return_step(self):
        return SoftSkills


class Feedback(SoftSkill):
    text = "<b>Feedback</b> \n\nWhat will you choose?"
    name = "Feedback"
    text_for_dict = "Feedback - text"

    def return_step(self):
        return SoftSkills


class Analysis(SoftSkill):
    text = "<b>Analysis</b> \n\nWhat will you choose?"
    name = "Analysis"
    text_for_dict = "Analysis - text"

    def return_step(self):
        return SoftSkills


class HardSkills(BaseStateData):
    text = "<b>Hard Skills</b> \n\nChoose 3 skills that are right for you!"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        if len(data_number_hard[self.chat_id]) == 3:
            keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: Experience'))
        else:
            try:
                if data_for_cv_hard[self.chat_id]['Python']:
                    keyboard.add(types.InlineKeyboardButton(text='Python: Selected',
                                                            callback_data='next state: Python'))
            except KeyError:
                keyboard.add(
                    types.InlineKeyboardButton(text='Python', callback_data='next state: Python'))
            try:
                if data_for_cv_hard[self.chat_id]['Django']:
                    keyboard.add(types.InlineKeyboardButton(text='Django: Selected',
                                                            callback_data='next state: Django'))
            except KeyError:
                keyboard.add(
                    types.InlineKeyboardButton(text='Django', callback_data='next state: Django'))
            try:
                if data_for_cv_hard[self.chat_id]['OOP']:
                    keyboard.add(types.InlineKeyboardButton(text='OOP: Selected',
                                                            callback_data='next state: OOP'))
            except KeyError:
                keyboard.add(types.InlineKeyboardButton(text='OOP', callback_data='next state: OOP'))
            try:
                if data_for_cv_hard[self.chat_id]['DataStructures']:
                    keyboard.add(types.InlineKeyboardButton(text='Data Structures: Selected',
                                                            callback_data='next state: DataStructures'))
            except KeyError:
                keyboard.add(types.InlineKeyboardButton(text='Data Structures',
                                                        callback_data='next state: DataStructures'))
        return keyboard

    def display(self):
        try:
            if data_number_hard[self.chat_id]:
                if len(data_number_hard[self.chat_id]) == 3:
                    self.text = "<b>Hard Skills</b> \n\nYou have chosen the available number of Hard skills."
                self.bot.delete_message(self.chat_id, MESSAGES[self.chat_id], timeout=0)
                message_from_bot = self.bot.send_message(
                    self.chat_id,
                    self.text,
                    reply_markup=self.get_keyboard(),
                    parse_mode='HTML'
                )
                MESSAGES[self.chat_id] = message_from_bot.id
        except KeyError:
            self.for_display_skill(data_number_hard)


class Python(HardSkill):
    text = "<b>Python</b> \n\nWhat will you choose?"
    name = "Python"
    text_for_dict = "Python - text"

    def return_step(self):
        return HardSkills


class Django(HardSkill):
    text = "<b>Django</b> \n\nWhat will you choose?"
    name = "Django"
    text_for_dict = "Django - text"

    def return_step(self):
        return HardSkills


class OOP(HardSkill):
    text = "<b>OOP</b> \n\nWhat will you choose?"
    name = "OOP"
    text_for_dict = "OOP - text"

    def return_step(self):
        return HardSkills


class DataStructures(HardSkill):
    text = "<b>DataStructures</b> \n\nWhat will you choose?"
    name = "DataStructures"
    text_for_dict = "DataStructures - text"

    def return_step(self):
        return HardSkills


class Experience(BaseStateData):
    text = "<b>Experience</b> \n\nAdd relevant work experience (maximum three jobs)."

    def get_keyboard(self):
        print()
        print(data_for_cv)
        print(data_for_cv_lang)
        print(data_for_cv_soft)
        print(data_for_cv_hard)
        print(data_for_cv_exp)
        print()
        keyboard = types.InlineKeyboardMarkup()
        if len(data_number_exp[self.chat_id]) == 3:
            keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: CreatePDF'))
        else:
            keyboard.add(types.InlineKeyboardButton(
                text=f'Add job (You added: {len(data_number_exp[self.chat_id])})',
                callback_data='next state: AddNewJob'))
            keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: CreatePDF'))
        return keyboard

    def display(self):
        try:
            if data_number_exp[self.chat_id]:
                if len(data_number_exp[self.chat_id]) == 3:
                    self.text = "<b>Experience</b> \n\nYou have chosen the available number of jobs."
                self.bot.delete_message(self.chat_id, MESSAGES[self.chat_id], timeout=0)
                message_from_bot = self.bot.send_message(
                    self.chat_id,
                    self.text,
                    reply_markup=self.get_keyboard(),
                    parse_mode='HTML'
                )
                MESSAGES[self.chat_id] = message_from_bot.id
        except KeyError:
            self.for_display_skill(data_number_exp)


class AddNewJob(BaseStateData):
    text = "<b>Add relevant job</b> \n\nAdd your position in the company"

    def save_text(self, message):
        text_by_user = message.text
        data_number_exp[self.chat_id].append(1)
        try:
            if data_for_cv_exp[self.chat_id]:
                data_for_cv_exp[self.chat_id].append(text_by_user)
        except KeyError:
            data_for_cv_exp[self.chat_id] = [text_by_user]

    def return_step(self):
        return AddNewJobStep


class AddNewJobStep(CreateStep):
    text = '<b>Your position received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddNewJob'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddCompanyName'))
        return keyboard


class AddCompanyName(BaseStateData):
    text = "<b>Add company name</b> \n\nAdd company name for this position"

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv_exp[self.chat_id].append(text_by_user)

    def return_step(self):
        return AddCompanyNameStep


class AddCompanyNameStep(CreateStep):
    text = '<b>Your company name received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddCompanyName'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: AddCompanyExp'))
        return keyboard


class AddCompanyExp(BaseStateData):
    text = "<b>Add experience</b> \n\nAdd your experience on this job"

    def save_text(self, message):
        text_by_user = message.text
        data_for_cv_exp[self.chat_id].append(text_by_user)

    def return_step(self):
        return AddCompanyExpStep


class AddCompanyExpStep(CreateStep):
    text = '<b>Your experience received</b> \n\nWhere next?'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Try again', callback_data='next state: AddCompanyName'))
        keyboard.add(types.InlineKeyboardButton(text='Next step', callback_data='next state: Experience'))
        return keyboard


class CreatePDF(BaseState):
    text = "<b>CREATE CV PDF FILE</b>"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Create PDF', callback_data='next state: CreatePDF'))
        return keyboard

    def display(self):
        self.bot.send_message(
            self.chat_id, self.text, reply_markup=self.get_keyboard(),
            parse_mode='HTML')

    def create_file(self, message: types.CallbackQuery):
        if message.data == 'next state: CreatePDF':
            pdf = PDF(self.chat_id)
            # pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
            # pdf.add_font('DejaVu', 'B', 'DejaVuSansCondensed.ttf', uni=True)
            pdf.set_title("P PP PP PP PP")
            pdf.create_cv_template()
            pdf.output(
                f"{data_for_cv[self.chat_id]['YourPosition']}_{data_for_cv[self.chat_id]['name']}{data_for_cv[self.chat_id]['surname']}.pdf")
            self.send_file()

    def send_file(self):
        self.bot.send_document(
            self.chat_id,
            open(
                f"{data_for_cv[self.chat_id]['YourPosition']}_{data_for_cv[self.chat_id]['name']}{data_for_cv[self.chat_id]['surname']}.pdf",
                'rb')
        )


class PDF(FPDF):
    x_pos = 0
    y_pos = 0

    def __init__(self, chat_id):
        super().__init__()
        self.chat_id = chat_id

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "B", 8)
        self.cell(0, 10, "CVLite", align="C")

    def chapter_title(self):
        self.set_font("DejaVu", "", 16)
        # Setting background color
        width = self.get_string_width(self.title) + 150
        self.set_y(20)
        self.set_x(50)
        # self.set_draw_color(0, 80, 180)
        self.set_fill_color(241, 234, 226)
        # Printing chapter name:
        self.cell(
            width,
            12,
            "",
            align="C",
            fill=True,
        )

    def add_name(self):
        self.set_font("DejaVu", style='', size=24)
        self.set_y(24)
        self.set_x(125)
        self.cell(
            w=0,
            h=6,
            txt=f"{data_for_cv[self.chat_id]['name'].upper()}",
            align="l",
            fill=False,
        )
        self.set_y(34)
        self.set_x(125)
        self.set_font("DejaVu", style='', size=24)
        self.cell(
            w=0,
            h=6,
            txt=f"{data_for_cv[self.chat_id]['surname'].upper()}",
            align="l",
            fill=False,
        )
        self.set_font("DejaVu", size=12)

    def add_cv_position(self):
        self.set_font("DejaVu", style='', size=14)
        self.set_y(49)
        self.set_x(125)
        self.cell(
            w=0,
            h=6,
            txt=f"{data_for_cv[self.chat_id]['YourPosition'].upper()}",
            align="l",
            fill=False,
        )

    def add_about_you(self):
        self.set_font("DejaVu", style='', size=12)
        self.set_y(60)
        self.set_x(89)
        self.multi_cell(
            w=110,
            h=10,
            txt=f"{data_for_cv[self.chat_id]['AboutYou']}",
            align="l",
        )

    def add_hard_skills(self):
        self.set_font("DejaVu", style='', size=14)
        self.set_y(117)
        self.set_x(125)
        self.cell(
            w=0,
            h=6,
            txt="HARD SKILLS",
            align="l",
            fill=False,
        )

    def add_hard_skill(self):
        self.set_font("DejaVu", style='', size=12)
        self.set_y(127)
        self.set_x(89)
        self.multi_cell(
            w=110,
            h=10,
            txt=f"{data_for_cv_hard[self.chat_id]['Python']}",
            align="l",
        )

    def add_experience(self):
        self.set_font("DejaVu", style='', size=14)
        self.set_y(205)
        self.set_x(125)
        self.cell(
            w=0,
            h=6,
            txt="EXPERIENCE",
            align="l",
            fill=False,
        )

    def add_experience_sample(self):
        self.set_font("DejaVu", style='', size=12)
        self.set_y(215)
        self.set_x(89)
        self.multi_cell(
            w=110,
            h=10,
            txt=f"{data_for_cv_exp[self.chat_id]}",
            align="l",
        )

    def add_number(self):
        self.set_font("DejaVu", style='B', size=12)
        self.set_y(85)
        self.set_x(10)
        self.cell(
            w=0,
            h=6,
            txt="Phone:",
            align="l",
            fill=False,
        )
        self.set_y(85)
        self.set_x(26)
        self.set_font("DejaVu", style='', size=12)
        self.cell(
            w=0,
            h=6,
            txt=f"{data_for_cv[self.chat_id]['number']}",
            align="l",
            fill=False,
        )
        self.set_font("helvetica", size=12)

    def add_email(self):
        self.set_font("DejaVu", style='B', size=12)
        self.set_y(95)
        self.set_x(10)
        self.cell(
            w=0,
            h=6,
            txt="Email:",
            align="l",
            fill=False,
        )
        self.set_y(95)
        self.set_x(26)
        self.set_font("DejaVu", style='', size=12)
        self.cell(
            w=0,
            h=6,
            txt=f"{data_for_cv[self.chat_id]['email']}",
            align="l",
            fill=False,
        )
        self.set_font("DejaVu", size=12)

    def add_liked_in_url(self):
        self.set_font("DejaVu", size=12)
        self.set_y(105)
        self.set_x(10)
        self.cell(
            w=18,
            h=6,
            txt="LinkedIn",
            align="l",
            fill=False,
            link=f"{data_for_cv[self.chat_id]['LinkedInUrl']}",
            border=1
        )

    def add_language_skills(self):
        self.set_font("DejaVu", style='', size=14)
        self.set_y(120)
        self.set_x(10)
        self.cell(
            w=0,
            h=6,
            txt="LANGUAGE SKILLS",
            align="l",
            fill=False,
        )

    def add_languages(self):
        # self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font("DejaVu", style='B', size=12)
        self.set_y(135)
        self.set_x(10)
        self.cell(
            w=0,
            h=6,
            txt="English:",
            align="l",
            fill=False,
        )
        self.set_y(135)
        self.set_x(30)
        self.set_font("DejaVu", style='', size=12)
        self.cell(
            w=0,
            h=6,
            txt=f"{data_for_cv_lang[self.chat_id]['English']}",
            align="l",
            fill=False,
        )
        self.set_font("DejaVu", size=12)

    def add_soft_skills(self):
        # self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font("DejaVu", style='', size=14)
        self.set_y(160)
        self.set_x(10)
        self.cell(
            w=0,
            h=6,
            txt="SOFT SKILLS",
            align="l",
            fill=False,
        )

    def add_soft_skill(self):
        # self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.set_font("DejaVu", style='', size=12)
        self.set_y(175)
        self.set_x(10)
        self.multi_cell(
            w=70,
            h=10,
            txt=f"{data_for_cv_soft[self.chat_id]['Collaboration']}",
            align="l",
        )

    def create_cv_template(self):
        self.add_font('DejaVu', 'B', 'DejaVuSansCondensed.ttf', uni=True)
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        self.add_page()
        self.chapter_title()
        self.add_name()
        self.add_cv_position()
        self.add_about_you()
        self.add_hard_skills()
        self.add_hard_skill()
        self.add_experience()
        self.add_experience_sample()
        self.add_number()
        self.add_email()
        self.add_liked_in_url()
        self.add_language_skills()
        self.add_languages()
        self.add_soft_skills()
        self.add_soft_skill()
        self.image('new_avatar_170.png', 10, 10)
