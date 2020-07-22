import syscoinBot

compteur = 0
syscoin = syscoinBot.syscoinBot()
while compteur != 1:
    syscoin.mine()
    syscoin.already_mined()
    syscoin.quit()
