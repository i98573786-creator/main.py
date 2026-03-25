from telethon import TelegramClient, events

api_id = 123456
api_hash = "API_HASH"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        await event.reply(
            "⚠️ Аккаунт під контролем системи: fTvY1\n\n"
            "Напишіть власнику:\n"
            "https://t.me/your_username"
        )

client.start()
client.run_until_disconnected()
