import json
import os
print("Calculating...")
toplethal = 0
toptime = 0
name = "none"
for filename in os.listdir("./output"):
    if filename.endswith(".json"):
        data = json.load(open(f"./output/{filename}", "r"))
        lethal = data['activePlayer']['championStats']['physicalLethality']
        time = data['gameData']['gameTime']
        if lethal > toplethal:
            toplethal = lethal
            toptime = time
            name = filename
print(toplethal)
print(f"{toptime / 60}")
print(name)