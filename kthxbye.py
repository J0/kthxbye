from telethon import TelegramClient, events

# Remember to use your own values from my.telegram.org!
api_id = os.environ["api_id"]
api_hash = os.environ["api_hash"]
phone = os.environ["phone"]
client = TelegramClient("anon", api_id, api_hash)
session_file = os.environ["session_file"]


if __name__ == "__main__":
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)

    @client.on(events.NewMessage(incoming=True))
    async def handle_incoming_message(event):
        if event.is_private:
            await event.respond("Sorry, I'll  be away till 2021. See you then!")

    client.start(phone, "")
    client.run_until_disconnected()
