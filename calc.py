import json
import os
print("Calculating...")
topms = -1
topad = -1
topap = -1
tophp = -1
toptenacity = -1
toptime = -1
topmr = -1
toparmor = -1
name = "none"
for filename in os.listdir("./output"):
    if filename.endswith(".json"):
        data = json.load(open(f"./output/{filename}", "r"))
        ms = data['activePlayer']['championStats']['moveSpeed']
        ad = data['activePlayer']['championStats']['attackDamage']
        ap = data['activePlayer']['championStats']['abilityPower']
        hp = data['activePlayer']['championStats']['maxHealth']
        tenacity = data['activePlayer']['championStats']['tenacity']
        armor = data['activePlayer']['championStats']['armor']
        mr = data['activePlayer']['championStats']['magicResist']
        time = data['gameData']['gameTime']
        if ms > topms:
            topms = ms
            mstime = time
            msname = filename
        if ad > topad:
            topad = ad
            adtime = time
            adname = filename
        if ap > topap:
            topap = ap
            aptime = time
            apname = filename
        if hp > tophp:
            tophp = hp
            hptime = time
            hpname = filename
        if tenacity > toptenacity:
            toptenacity = tenacity
            tenacitytime = time
            tenacityname = filename
        if mr > topmr:
            topmr = mr
            mrtime = time
            mrname = filename
        if armor > toparmor:
            toparmor = armor
            armortime = time
            armorname = filename
        
ad = [topad, adtime, adname]
ap = [topap, aptime, apname]
ms = [topms, mstime, msname]
hp = [tophp, hptime, hpname]
tenacity = [toptenacity, tenacitytime, tenacityname]
armor = [toparmor, armortime, armorname]
mr = [topmr, mrtime, mrname]
print(ad)
print(ap)
print(ms)
print(hp)
print(tenacity)
print(armor)
print(mr)

