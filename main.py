import os

import telebot

from email_validator import validate_email, EmailNotValidError

from dotenv import load_dotenv

from states.base import BaseState

from states.bot_states import Hello, FirstTemplate, SecondTemplate, CreateCV, AddName, AddSurname, AddMobNumber, \
    AddEmail, AddLinkedIn, AddYourPosition, AddAboutYou, English, Ukrainian, Collaboration, Feedback, TimeManagement, \
    Analysis, Python, OOP, DataStructures, Django, AddNewJob1, AddCompanyName1, AddCompanyExp1, AddNewJob2, \
    AddCompanyName2, AddCompanyExp2, AddNewJob3, AddCompanyName3, AddCompanyExp3, CreatePDF, FinishIteration

load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_SECRET'))

clients: dict = {}

current_template: dict = {}

symbols_tuple = (
    '-', '@', '.', '+', '!', '&',
    '?', '(', ')', ':', '/', '\\',
    '*', '%', '$', ' ', '=', '_',
    ',', '#', ';', '*'
)

text_direct_tuple: tuple = (
    AddName,
    AddSurname,
    AddEmail,
    AddMobNumber,
    AddLinkedIn,
    AddYourPosition,
    AddAboutYou,
    AddNewJob1,
    AddCompanyName1,
    AddCompanyExp1,
    AddNewJob2,
    AddCompanyName2,
    AddCompanyExp2,
    AddNewJob3,
    AddCompanyName3,
    AddCompanyExp3
)

query_direct_tuple: tuple = (
    English,
    Ukrainian,
    Collaboration,
    Feedback,
    TimeManagement,
    Analysis,
    Python,
    OOP,
    DataStructures,
    Django,
    CreatePDF
)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    greetings = Hello(bot, message.chat.id)
    greetings.display()
    clients[message.chat.id] = Hello


@bot.callback_query_handler(func=lambda message: clients[message.from_user.id] not in query_direct_tuple)
def process_call_back(message):
    chat_id = message.from_user.id
    new_state_class = get_state(chat_id).process_call_back(message)
    get_template(new_state_class, chat_id)
    clients[chat_id] = new_state_class
    display(chat_id)


@bot.callback_query_handler(func=lambda message: clients[message.from_user.id] in query_direct_tuple)
def special_call_back(message):
    chat_id = message.from_user.id
    if clients[message.from_user.id] == CreatePDF:
        state = CreatePDF(bot, chat_id)
        state.create_file(message)
        new_state_class = FinishIteration
        clients[chat_id] = new_state_class
        display(chat_id)
    else:
        chat_id = message.from_user.id
        query_processing(clients[chat_id], message, chat_id)


@bot.message_handler(func=lambda message: clients[message.chat.id] not in text_direct_tuple)
def echo_all(message: telebot.types.Message):
    chat_id = message.chat.id
    new_state_class = get_state(chat_id).process_text_message(message)
    clients[chat_id] = new_state_class
    display(chat_id)


@bot.message_handler(func=lambda message: clients[message.chat.id] in text_direct_tuple)
def text_form(message: telebot.types.Message):
    chat_id = message.chat.id
    choice_text_processing(chat_id, message)


@bot.message_handler(content_types=['photo'])
def photo(message):
    chat_id = message.from_user.id
    state_variable = clients[chat_id]
    save_jpg(state_variable, message, chat_id)


@bot.message_handler(content_types=['document', 'video', 'audio', 'voice', 'file', 'sticker', 'animation'])
def photo(message):
    chat_id = message.from_user.id
    bot.send_message(
        chat_id,
        "<b>Sorry, I don't work with this format now</b>",
        parse_mode='HTML'
    )
    display(chat_id)


def display(chat_id):
    state = get_state(chat_id)
    state.display()


def get_state(chat_id) -> BaseState:
    current_state = clients.get(chat_id, Hello)
    instance_of_class = current_state(bot, chat_id)
    return instance_of_class


def get_template(state: 'BaseState', chat_id):
    if state in [FirstTemplate, SecondTemplate]:
        current_template[chat_id] = state


def save_jpg(state, message, chat_id):
    if state == CreateCV:
        new_state_variable = CreateCV(bot, chat_id)
        new_state_variable.save_jpg(message)
        returned_step(new_state_variable, chat_id)
    else:
        bot.send_message(chat_id, "<b>Now it's useless.</b>", parse_mode='HTML')

    display(chat_id)


def choice_text_processing(chat_id, message):
    if clients[chat_id] in [AddName, AddSurname, AddYourPosition]:
        if message_check_for_file(message):
            text_processing(clients[chat_id], message, chat_id)
        else:
            bot.send_message(
                chat_id,
                "<b>Don't use smiles or special characters when filling these fields (name, surname, position).</b>",
                parse_mode='HTML'
            )
            display(chat_id)
    elif clients[chat_id] == AddEmail:
        if validate_email_func(message):
            text_processing(clients[chat_id], message, chat_id)
        else:
            bot.send_message(
                chat_id,
                "<b>Incorrect email. \n\nPlease try again enter correct</b>",
                parse_mode='HTML'
            )
            display(chat_id)
    elif message_check(message):
        text_processing(clients[chat_id], message, chat_id)
    else:
        bot.send_message(
            chat_id,
            "<b>Don't use smiles or special characters (except for dashes, plus, at, dot) when filling out fields.</b>",
            parse_mode='HTML'
        )
        display(chat_id)


def text_processing(state, message, chat_id):
    new_state_variable = state(bot, chat_id)
    new_state_variable.save_text(message)
    returned_step(new_state_variable, chat_id)
    display(chat_id)


def query_processing(state, message, chat_id):
    new_state_variable = state(bot, chat_id)
    new_state_variable.save_skill(message)
    returned_step(new_state_variable, chat_id)
    display(chat_id)


def returned_step(state, chat_id):
    returned_state_step = state.return_step()
    clients[chat_id] = returned_state_step


def message_check(message):
    message_text = message.text
    for i in range(len(message_text)):
        if message_text[i].isalpha() or message_text[i].isdigit() or message_text[i] in symbols_tuple:
            continue
        else:
            return False
    return True


def message_check_for_file(message):
    message_text = message.text
    for i in range(len(message_text)):
        if message_text[i].isalpha() or message_text[i].isdigit() or message_text[i] == ' ':
            continue
        else:
            return False
    return True


def validate_email_func(message):
    email_from_user = message.text
    try:
        email = validate_email(email_from_user).email
        print(email)
        return True
    except EmailNotValidError:
        return False


if __name__ == '__main__':
    bot.infinity_polling()
