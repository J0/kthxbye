import os
import datetime
from telethon import TelegramClient, events

# Remember to use your own values from my.telegram.org!
api_id = os.environ["api_id"]
api_hash = os.environ["api_hash"]
phone = os.environ["phone"]
client = TelegramClient("anon", api_id, api_hash)
session_file = os.environ["session_file"]

def time_in_range(start: datetime, end:datetime, time: datetime):
    if start <= end:
        return start <= time <= end
    else:
        return start <= time<= end

def isWeekday():
    return 1 <= datetime.date.today().weekday() <= 5

def utc_to_local(utc_dt, timezone="Asia/Singapore"):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=timezone)

if __name__ == "__main__":
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)

    @client.on(events.NewMessage(incoming=True))
    async def handle_incoming_message(event):
        if event.is_private and isWeekday() and time_in_range(time(10,0), time(18,0), datetime.datetime.now().time()):
            await event.respond(
                "** This is an automatically generated message**\n Hi friend, \n I'll be away till 2021 to reflect on 2020 and set goals for 2021. Thank you for great company in 2020. If you're reading this you have been and (hopefully) will continue to be an important part of my life. I am very thankful for your patience and continuous support throughout this messy year. Next year will be better. Have a merry christmas and a restful new year. See you in 2021! :)"
            )

    client.start(phone, "")
    client.run_until_disconnected()
