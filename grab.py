import requests
import psutil
from time import sleep
response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False)
print("League of Legends.exe" in (i.name() for i in psutil.process_iter()))
gameOpen = "League of Legends.exe" in (i.name() for i in psutil.process_iter())
while open == False:
    print("Waiting for league to start...")
    sleep(0.5)
    
count = 0
while gameOpen:
    print(count)
    #response = requests.get("https://127.0.0.1:2999/liveclientdata/allgamedata", verify=False)
    print("Request made.")
    str(count)
    with open("response" + str(count) + ".json", "w") as f:
        print("Writing to response" + str(count) + ".json.")
        f.write(response.text)
    gameOpen = "League of Legends.exe" in (i.name() for i in psutil.process_iter())
    count+= 1
    sleep(0.5)
print("Finished.")