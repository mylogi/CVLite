from telebot import types

MESSAGES: dict = {}


class BaseState:
    text = ""

    def __init__(self, bot, chat_id):
        self.bot = bot
        self.chat_id = chat_id

    def display(self):
        try:
            if MESSAGES[self.chat_id]:
                self.bot.delete_message(self.chat_id, MESSAGES[self.chat_id], timeout=0)
                message_from_bot = self.bot.send_message(self.chat_id, self.text, reply_markup=self.get_keyboard(),
                                                         parse_mode='HTML')
                MESSAGES[self.chat_id] = message_from_bot.id
        except KeyError:
            message_from_bot = self.bot.send_message(self.chat_id, self.text, reply_markup=self.get_keyboard(),
                                                     parse_mode='HTML')
            MESSAGES[self.chat_id] = message_from_bot.id

    def send_warning(self, text):
        self.bot.send_message(self.chat_id, text)

    def get_keyboard(self):
        return None

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        return self.__class__

    def process_text_message(self, message: types.Message) -> 'BaseState':
        return self.__class__
