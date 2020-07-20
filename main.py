import syscoinBot

compteur = 0
syscoin = syscoinBot.syscoinBot()
while compteur != 20000:
    syscoin.mine()
    syscoin.already_mined()
    if syscoin.already_mined == False:
        compteur = compteur + 1
    syscoin.quit()