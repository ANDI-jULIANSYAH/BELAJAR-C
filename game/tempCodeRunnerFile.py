a = {
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
            bot.send_message(chat_id, f'Berhasil membuat akun Discord spam dengan usern