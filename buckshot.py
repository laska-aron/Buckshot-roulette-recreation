import random
import time

run = True
while run == True:
    print("[1] Játék indítása / Újrapróbálkozás")
    print("[2] Kilépés")
    valaszt1 = input(">>>")
    if valaszt1 == "1":
        playerhp = 4
        dealerhp = 4
        while dealerhp > 0 and playerhp > 0:
            rounds = []
            roundstext = []
            while "Éles" not in roundstext or "Vak" not in roundstext:
                for i in range(8):
                    round = random.randint(0,2)
                    rounds.append(round)
                    if round == 1:
                        roundstext.append("Éles")

                    elif round == 2:
                        roundstext.append("Vak")

                    else:
                        pass
            while len(roundstext) > 0:
                shotgunendcut = False
                playeriscuffed = False
                dealeriscuffed = False
                print("A töltények:",end=" ")
                thereareroundsleft = True
                print(', '.join(map(str,roundstext)))
                time.sleep(3)
                items = []
                itemstext = []
                print("A tárgyaid:",end=" ")
                for i in range(4):

                    item = random.randint(1,5)
                    items.append(item)
                    if item == 1:
                        itemstext.append("Nagyító")

                    elif item == 2:
                        itemstext.append("Kés")

                    elif item == 3:
                        itemstext.append("Cigi")

                    elif item == 4:
                        itemstext.append("Sör")

                    elif item == 5:
                        itemstext.append("Bilincs")

                    else:
                        pass

                print(', '.join(map(str, itemstext)))
                random.shuffle(itemstext)
                time.sleep(3)
                dealeritems = []
                dealeritemstext = []
                print("Az osztó/ellenfél tárgyai:",end=" ")
                for i in range(4):
                    item = random.randint(1,5)
                    dealeritems.append(item)
                    if item == 1:
                        dealeritemstext.append("Nagyító")

                    elif item == 2:
                        dealeritemstext.append("Kés")

                    elif item == 3:
                        dealeritemstext.append("Cigi")

                    elif item == 4:
                        dealeritemstext.append("Sör")

                    elif item == 5:
                        dealeritemstext.append("Bilincs")

                    else:
                        pass

                print(', '.join(map(str, dealeritemstext)))
                random.shuffle(dealeritemstext)
                time.sleep(3)
                dealerisnext = False
                while dealerisnext == False:
                    print("Mit szertnél tenni?")
                    print("[1] Az ellenfél / osztó lelövése")
                    print("[2] Önmagad lelövése")
                    print("[3] Tárgy(ak) használata")
                    valaszt2 = input(">>>")
                    if valaszt2 == "1":
                        if roundstext[0] == "Éles":
                            print("Egy éles tölténnyel lelőtted az osztót/ellenfelet!")
                            if shotgunendcut == True:
                                dealerhp -= 2
                                print("Mivel a shotgun vége le volt vágva, az ellenfél/osztó élete 2 ponttal csökkent.")
                                if dealerhp == 0:
                                    print("Az osztó/ellenfél meghalt!")
                                    print("Nyertél!")
                                    break
                            else:
                                dealerhp -= 1
                                print("Az osztó/ellenfél élete 1 ponttal csökkent.")
                                if dealerhp == 0:
                                    print("Az osztó/ellenfél meghalt!")
                                    print("Nyertél!")
                                    break

                            print(f"Az osztó maradék élete: {dealerhp}")
                            roundstext.pop(0)
                            if dealeriscuffed == False:
                                if len(roundstext) > 0 and dealerhp > 0:
                                    print("Most az osztó/ellenfél következik.")
                                    dealerisnext = True
                                    shotgunendcut = False
                                    break
                                    
                            else:
                                print("Mivel megbilincselted az osztót/ellenfelet, kimarad a következő körből és ismét te következel.")

                        else:
                            print("Megpróbáltad lelőni az osztót/ellenfelet, de vak töltény volt.")
                            roundstext.pop(0)
                            if dealeriscuffed == False:
                                if len(roundstext) > 0:
                                    print("Most az osztó/ellenfél következik.")
                                    dealerisnext = True
                                    shotgunendcut = False
                                    break

                    elif valaszt2 == "2":
                        if roundstext[0] == "Éles":
                            print("Lelőtted magad egy éles tölténnyel!")
                            if shotgunendcut == True:
                                shotgunendcut = False
                                playerhp -= 2
                                print("Mivel a shotgun vége le volt vágva, az életerőd 2 ponttal csökkent.")
                                if playerhp == 0:
                                    print("Meghaltál!")
                                    print("Vesztettél!")
                                    break
                                else: pass
                            else:
                                playerhp -= 1
                                print("Az életerőd 1 ponttal csökkent.")
                                if playerhp == 0:
                                    print("Meghaltál!")
                                    print("Vesztettél!")
                                    break

                            print(f"A megmaradt életed: {playerhp}")
                            roundstext.pop(0)
                            if playeriscuffed == False:
                                if len(roundstext) > 0 and playerhp > 0:
                                    print("Most az osztó/ellenfél következik.")
                                    dealerisnext = True
                                    break
                                

                    elif valaszt2 == "3":
                        print("A használható tárgyak:", end=" ")
                        print(', '.join(map(str, itemstext)))
                        print("Kérlek írd be a választott tárgy nevét!")
                        valaszt3 = input(">>>")
                        itemfound = False
                        for elem in itemstext:
                            if elem.lower() == valaszt3.lower():
                                itemfound = True
                                if valaszt3.lower() == "cigi":
                                    if playerhp == 4 and (valaszt3.lower() == "cigi"):
                                        print("Max életen vagy, nem használhatsz cigit!")
                                            
                                    else:
                                        playerhp += 1
                                        itemstext.remove(elem)
                                        print("Egy cigi elhasználva!")
                                        print("Az életpontjaid: ", playerhp)
                                        print("A megmardt tárgyak:", end=" ")
                                        print(', '.join(map(str, itemstext)))
                                        time.sleep(1.5)
                                        pass

                                elif valaszt3.lower() == "kés":
                                    if shotgunendcut == True:
                                        print('Nem használhatod a kést, mert a shotgun vége már le van vágva!')
                                        
                                    else:
                                        print('A shotgun vége levágva!')
                                        print('Egy kés elhasználva!')
                                        shotgunendcut = True
                                        itemstext.remove(elem)
                                        print("A megmardt tárgyak:", end=" ")
                                        print(', '.join(map(str, itemstext)))
                                    
                                elif valaszt3.lower() == "bilincs":
                                    if dealeriscuffed == False:
                                        print('Az osztó / ellenfél megbilincselve!')
                                        print('Egy bilincs elhasználva!')
                                        dealeriscuffed = True
                                        itemstext.remove(elem)
                                        print("A megmardt tárgyak:", end=" ")
                                        print(', '.join(map(str, itemstext)))
                                            
                                    else:
                                        print('Az osztó / ellenfél már meg van bilincselve!')

                                elif valaszt3.lower() == "sör":
                                    print("Egy sör elhasználva!")
                                    print(f"Egy {roundstext[0]} töltény kiszedve!")
                                    itemstext.remove(elem)
                                    print("A megmardt tárgyak:", end=" ")
                                    print(', '.join(map(str, itemstext)))

                                elif valaszt3.lower() == "nagyító":
                                    print("Egy nagyító elhasználva!")
                                    print(f"A soron következő töltény egy {roundstext[0]} töltény.")
                                    itemstext.remove(elem)
                                    print("A megmardt tárgyak:", end=" ")
                                    print(', '.join(map(str, itemstext)))
                                    break

                                else:
                                    pass

                            else:
                                pass

                        if itemfound == False:
                            print("A megadott tárgy nem található!")

                        else:
                            pass
                            
                    else:
                        print("Hibás parancs!")
                        time.sleep(1)
                while dealerisnext == True:
                    if "Cigi" in dealeritemstext and dealerhp < 4:
                        dealerhp += 1
                        dealeritemstext.remove("Cigi")
                        print("Az osztó/ellenfél használt egy cigit és 1 pont életerőt nyert.")
                        print(f"Az osztó/ellenfél megmaradt életereje: {dealerhp}")
                        print("Az osztó/ellenfél megmaradt tárgyai:", end=" ")
                        print(', '.join(map(str, dealeritemstext)))
                        time.sleep(1.5)

                    if "Kés" in dealeritemstext:
                        shotgunendcut == True
                        dealeritemstext.remove("Kés")
                        print("Az osztó/ellenfél levágta a shotgun végét és elhasznált egy kést.")
                        print("Az osztó/ellenfél megmaradt tárgyai:", end=" ")
                        print(', '.join(map(str, dealeritemstext)))
                        time.sleep(1.5)

                    if "Bilincs" in dealeritemstext and playeriscuffed == False:
                        playeriscuffed = True
                        dealeritemstext.remove("Bilincs")
                        print("Az osztó/ellenfél megbilincselt és elhasznált egy bilincset.")
                        print("Az osztó/ellenfél megmaradt tárgyai:", end=" ")
                        print(', '.join(map(str, dealeritemstext)))
                        time.sleep(1.5)

                    if "Nagyító" in dealeritemstext:
                        print(f"Az osztó/ellenfél elhasznált egy nagyítót.")
                        nextround = roundstext[0]
                        dealeritemstext.remove("Nagyító")
                        print("Az osztó/ellenfél megmaradt tárgyai:", end=" ")
                        print(', '.join(map(str, dealeritemstext)))
                        time.sleep(1.5)

                    else:
                        nextround = None

                    if "Sör" in dealeritemstext and (nextround == "Vak" or nextround == None):
                        dealeritemstext.remove("Sör")
                        roundstext.pop(0)
                        print("Az osztó/ellenfél elhasznált egy sört és kiszedett egy vak töltényt.")
                        print("Az osztó/ellenfél megmaradt tárgyai:", end=" ")
                        print(', '.join(map(str, dealeritemstext)))
                        time.sleep(1.5)

                    if nextround == "Éles":
                        print("Az osztó/ellenfél lelőtt téged egy éles tölténnyel!")
                        if shotgunendcut == True:
                            shotgunendcut = False
                            playerhp -= 2
                            print("Mivel a shotgun vége le volt vágva, az életerőd 2 ponttal csökkent.")
                            if playerhp == 0:
                                print("Meghaltál!")
                                print("Vesztettél!")
                                break
                            else: pass

                        else:
                            playerhp -= 1
                            print("Az életerőd 1 ponttal csökkent.")
                            if playerhp == 0:
                                print("Meghaltál!")
                                print("Vesztettél!")
                                break

                        print(f"A megmaradt életed: {playerhp}")
                        roundstext.pop(0)
                        if playeriscuffed == False:
                            if len(roundstext) > 0 and playerhp > 0:
                                print("Most te következel.")
                                dealerisnext = False
                                break
                                
                        else:
                            if len(roundstext) >0:
                                print("Mivel megbilincselt az osztó/ellenfél, ismét ő következik.")
                                dealerisnext = True
                            else:
                                print("Elfogyott a töltény!")
                                pass
                        
                    if nextround == "Vak":
                        print("Az osztó/ellenfél lelőtte magát egy vak tölténnyel,",end=" ")
                        print("ezért ismét ő következik")
                        roundstext.pop(0)
                        dealerisnext = True

                    else:
                        dealerchoice = random.randint(1,2)
                        if dealerchoice == 1:
                            if roundstext[0] == "Éles":
                                print("Az osztó/ellenfél lelőtt téged egy éles tölténnyel!"); print(shotgunendcut) #BUG: Nem emlékszik, hogy levágta
                                if shotgunendcut == True:
                                    shotgunendcut = False
                                    playerhp -= 2
                                    print("Mivel a shotgun vége le volt vágva, az életerőd 2 ponttal csökkent.")
                                    if playerhp == 0:
                                        print("Meghaltál!")
                                        print("Vesztettél!")
                                        break
                                    else: pass

                                else:
                                    playerhp -= 1
                                    print("Az életerőd 1 ponttal csökkent.")
                                    if playerhp == 0:
                                        print("Meghaltál!")
                                        print("Vesztettél!")
                                        break

                                print(f"A megmaradt életed: {playerhp}")
                                roundstext.pop(0)
                                if playeriscuffed == False:
                                    if len(roundstext) > 0 and playerhp > 0:
                                        print("Most te következel.")
                                        dealerisnext = False
                                        pass #BUG: Nem jó helyre ugrik vissza, nem kellene új töltényeket és itemeket adjon - Elvileg fixed, csak item problem
                                        
                                else:
                                    if len(roundstext) >0:
                                        print("Mivel megbilincselt az osztó/ellenfél, ismét ő következik.")
                                        dealerisnext = True
                                    else:
                                        print("Elfogyott a töltény!")
                                        pass

                            if roundstext[0] == "Vak":
                                print("Az osztó/ellenfél megpróbált lelőni téged, de vak töltény volt.")
                                roundstext.pop(0)
                                if playeriscuffed == False:
                                    dealerisnext = False
                                    if len(roundstext) > 0:
                                        print("Most te következel.")
                                        break
                                    else:
                                        print("Elfogyott a töltény!")
                                        pass
                                        
                                #BUG: Nem szedi le a bilincset a player-ről, pedig megvolt az 1 köt kimaradás
                        if dealerchoice == 2:
                            if roundstext[0] == "Éles":
                                print("Az osztó/ellenfél lelőtte magát egy éles tölténnyel!")
                                if shotgunendcut == True:
                                    dealerhp -= 2
                                    print("Mivel a shotgun vége le volt vágva, az ellenfél/osztó élete 2 ponttal csökkent.")
                                    if dealerhp == 0:
                                        print("Az osztó/ellenfél meghalt!")
                                        print("Nyertél!")
                                        break
                                else:
                                    dealerhp -= 1
                                    print("Az osztó/ellenfél élete 1 ponttal csökkent.")
                                    if dealerhp == 0:
                                        print("Az osztó/ellenfél meghalt!")
                                        print("Nyertél!")
                                        break

                                print(f"Az osztó/ellenfél maradék élete: {dealerhp}")
                                roundstext.pop(0)
                                shotgunendcut = False
                                if len(roundstext) > 0 and dealerhp > 0:
                                    print("Most te következel.")
                                    dealerisnext = False
                                    break
                                
                            if roundstext[0] == "Vak":
                                print("Az osztó/ellenfél lelőtte magát egy vak tölténnyel, ezért ismét ő következik.")
                                roundstext.pop(0)
                                if len(roundstext) > 0:
                                    dealerisnext = True
                                    break
                            
    elif valaszt1 == "2":
        print("Leállítás...")
        time.sleep(3)
        run = False
    else:
        print("Hibás parancs!")
        time.sleep(1)

def make_sticky_scrolling_work():
    return "Fuck Microsoft!"