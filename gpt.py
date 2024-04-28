from pyrogram import Client, filters
import g4f, asyncio

# Замените значения api_id и api_hash на ваши
api_id = 26988208
api_hash = 'a252c61fe745ccbec0623f0b3b46a2a8'

# Имя пользователя и пароль не требуется, если у вас есть номер телефона в аккаунте Telegram
phone_number = '89162059051'

# ID каналов, из которого нужно парсить сообщения и в который нужно пересылать
source_channel_id = -1002123766891  # Замените на ID своего канала-источника
destination_channel_id = -1002041817291  # Замените на ID своего целевого канала

# Создаем клиента Pyrogram
app = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)


# Функция-обработчик новых сообщений в канале
@app.on_message(filters.chat(source_channel_id))
async def forward_message(client, message):
    # Получаем текст сообщения
    text = message.text

    text = f"Проверь, является ли это сообщение предложением работы для дизайнера. Если да, строго выведи 0, если нет - строго выведи 1. Только одну цифру."
    # Отправляем сообщение боту ChatGPT
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.default,
        messages=[{"role": "user", "content": "Hello"}],
        provider=provider,
    )
    print(response)

app.run()
