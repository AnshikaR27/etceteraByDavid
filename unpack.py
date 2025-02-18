def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

# * this will unpack the list aur 3 diff/individual values pass krdega!
print(total(*coins),"knuts")
