def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


# * this will unpack the list aur 3 diff/individual values pass krdega!

coins = {"galleons" : 100,
         "sickles": 50,
         "knuts":25}

# print(total(coins["galleons"], coins["galleons"], coins["sickles"]),"knuts")

print(total(**coins), "Knuts")
