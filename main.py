import os
import telebot

from dotenv import load_dotenv

from states.base import BaseState
from states.hello import Hello, FirstTemplate, SecondTemplate, CreateCV, AddName

load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_SECRET'))
clients: dict = {}
current_template: dict = {}


# data_for_cv: dict = {}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    greetings = Hello(bot, message.chat.id)
    greetings.display()
    clients[message.chat.id] = Hello


@bot.callback_query_handler(func=lambda message: True)
def process_call_back(message):
    chat_id = message.from_user.id
    new_state_class = get_state(chat_id).process_call_back(message)
    get_template(new_state_class, chat_id)
    clients[chat_id] = new_state_class
    display(chat_id)


@bot.message_handler(func=lambda message: True)
def echo_all(message: telebot.types.Message):
    chat_id = message.chat.id
    new_state_class = get_state(chat_id).process_text_message(message)
    clients[chat_id] = new_state_class
    display(chat_id)


@bot.message_handler(content_types=['photo'])
def photo(message):
    chat_id = message.from_user.id
    state_variable = clients[chat_id]
    if state_variable == CreateCV:
        new_state_variable = CreateCV(bot, chat_id)
        new_state_variable.save_jpg(message)
        new_state_variable.display_new()
    else:
        bot.send_message(chat_id, "<b>Now it's useless.</b>", parse_mode='HTML')
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


# def save_jpg(state, message, chat_id):
#     if state == CreateCV:
#         file_id = message.photo[-1].file_id
#         data_for_cv['photo'] = file_id
#         file_info = bot.get_file(file_id)
#         downloaded_file = bot.download_file(file_info.file_path)
#         with open('image.jpg', 'wb') as new_file:
#             new_file.write(downloaded_file)
#         return True
#     else:
#         bot.send_message(chat_id, "<b>Now it's useless.</b>", parse_mode='HTML')
#         display(chat_id)
#         return False


if __name__ == '__main__':
    bot.infinity_polling()
