from pyrogram import Client, filters
from g4f import ChatCompletion, models

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Замените значения api_id и api_hash на ваши
api_id = 26988208
api_hash = 'a252c61fe745ccbec0623f0b3b46a2a8'

# ID каналов, из которого нужно парсить сообщения и в который нужно пересылать
source_channel_id = -1002123766891  # Замените на ID своего канала-источника
destination_channel_id = -1002041817291  # Замените на ID своего целевого канала

# Создаем клиента Pyrogram
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Функция для проверки сообщения
def check_message(message):
    text = message.text
    prompt = f"Опредили, является ли это сообщение предложением работы для дизайнера. Если да, строго выведи 0, если нет - строго выведи 1. Только одну цифру. {text}"
    response = ChatCompletion.create(
        model=models.gpt_4,
        messages=[{"role": "user", "content": prompt}],
    )
    print(response)
    if response == '0':
        app.send_message(destination_channel_id, text)

# Функция-обработчик новых сообщений в канале
@app.on_message(filters.chat(source_channel_id))
def forward_message(client, message):
    check_message(message)

# Запускаем клиента
app.run()
