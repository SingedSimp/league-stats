import requests
import psutil
from time import sleep
# response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False)
print("Waiting for league to start...")
# print("League of Legends.exe" in (i.name() for i in psutil.process_iter()))
gameOpen = "League of Legends.exe" in (i.name() for i in psutil.process_iter())

while gameOpen == False:
    sleep(0.5)
    gameOpen = "League of Legends.exe" in (i.name() for i in psutil.process_iter())
    
count = 0
while gameOpen:
    print(count)
    try:
        response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False)
    except:
        sleep(1)
        pass
    else:
        print("Request made.")
        str(count)
        with open("./output/response" + str(count) + ".json", "w") as f:
            print(f"Writing to response{str(count)}.json.")
            f.write(response.text)
        gameOpen = "League of Legends.exe" in (i.name() for i in psutil.process_iter())
        count+= 1
        sleep(0.5)
    gameOpen = "League of Legends.exe" in (i.name() for i in psutil.process_iter())
print("Finished.")