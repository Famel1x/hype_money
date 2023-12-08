from telethon import TelegramClient
import time
import datetime
# Use your own values from my.telegram.org

def working():
    api_id = 23275887
    api_hash = '2101344edb515d37db3b5df81304460b'

    # The first parameter is the .session file name (absolute paths allowed)
    with TelegramClient('anon', api_id, api_hash, system_version="4.16.30-vxCUSTOM") as client:
        client.loop.run_until_complete(client.send_message('me', f"Hello, myself! {datetime.datetime.now()}"))

    async def main():
        await client.send_message("@eda_new_year_bot", '/fire')
        time.sleep(1)
        await client.send_message("@eda_new_year_bot", '/tree')
        


    with client:
        client.loop.run_until_complete(main())


def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    try:
        working()
        countdown(int(21600))
    except:
        print("Ошибка в логине")

while True:
    try:
    # input time in seconds 
        hours = int(input("Введите количество часов"))
        mins = int(input("Введите количество минут"))
        # function call 
        countdown(int((hours*60*60)+(mins*60))) 
        break


    except:
        print("Ошибка вводе времени")

