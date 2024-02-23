import os
import requests
import telebot
from telebot import types

TELEGRAM_BOT_TOKEN = '6840325077:AAF6yjrq7oWdpHUpMfEywx8WlVILbCf2jX0'
DISCORD_BOT_TOKEN = 'your_discord_bot_token'
TELEGRAM_CHAT_ID = '@Any_123bot'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Halo! Saya akan membuat akun Discord spam secara otomatis.')
    create_discord_accounts(message.chat.id)

def create_discord_accounts(chat_id):
    for i in range(10):
        username = f'SpamBot{i + 1}'
        email = f'{username}@example.com'
        password = 'spambotpassword'

        data = {
            'username': username,
            'email': email,
            'password': password
        }

        headers = {
            'Authorization': f'Bot {DISCORD_BOT_TOKEN}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post('https://discordapp.com/api/v9/auth/register', json=data, headers=headers)
            bot.send_message(chat_id, f'Berhasil membuat akun Discord spam dengan username: {username}')
        except Exception as e:
            bot.send_message(chat_id, f'Gagal membuat akun Discord spam dengan username: {username}\nError: {str(e)}')

if __name__ == '__main__':
    bot.polling()