import os

import telebot

from dotenv import load_dotenv

from states.base import BaseState
from states.hello import Hello, FirstTemplate, SecondTemplate, CreateCV, AddName, AddSurname, AddMobNumber, AddEmail

load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_SECRET'))
clients: dict = {}
current_template: dict = {}
direct_list: list = [AddName, AddSurname, AddEmail, AddMobNumber]


# data_for_cv: dict = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    greetings = Hello(bot, message.chat.id)
    greetings.display()
    clients[message.chat.id] = Hello
    # print(message.chat.id)
    # print(clients[message.chat.id])


@bot.callback_query_handler(func=lambda message: True)
def process_call_back(message):
    chat_id = message.from_user.id
    new_state_class = get_state(chat_id).process_call_back(message)
    get_template(new_state_class, chat_id)
    clients[chat_id] = new_state_class
    display(chat_id)


@bot.message_handler(func=lambda message: clients[message.chat.id] not in direct_list)
def echo_all(message: telebot.types.Message):
    chat_id = message.chat.id
    new_state_class = get_state(chat_id).process_text_message(message)
    clients[chat_id] = new_state_class
    display(chat_id)


@bot.message_handler(func=lambda message: clients[message.chat.id] in direct_list)
def text_form(message: telebot.types.Message):
    chat_id = message.chat.id
    choice_text_processing(chat_id, message)


@bot.message_handler(content_types=['photo'])
def photo(message):
    chat_id = message.from_user.id
    state_variable = clients[chat_id]
    save_jpg(state_variable, message, chat_id)


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
    text_processing(clients[chat_id], message, chat_id)


def text_processing(state, message, chat_id):
    new_state_variable = state(bot, chat_id)
    new_state_variable.save_text(message)
    returned_step(new_state_variable, chat_id)
    display(chat_id)


def returned_step(state, chat_id):
    returned_state_step = state.return_step()
    clients[chat_id] = returned_state_step


if __name__ == '__main__':
    bot.infinity_polling()
