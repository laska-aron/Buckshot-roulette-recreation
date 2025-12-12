import random
import time

run = True
while run == True:
    print("[1] Játék indítása / Újrapróbálkozás")
    print("[2] Kilépés")
    valaszt1 = input(">>>")
    if valaszt1 == "1":
        megy = True
        isfirstgo = True
        while megy == True:
            if isfirstgo == True:
                playerhp = 4
                dealerhp = 4
                shotgunendcut = False
                playeriscuffed = False
                dealeriscuffed = False
                isfirstgo = False
                thereareroundsleft = True
                rounds = []
                roundstext = []
                print("A töltények:",end=" ")
                for i in range(8):
                    round = random.randint(0,2)
                    rounds.append(round)
                    if round == 1:
                        roundstext.append("Éles")

                    elif round == 2:
                        roundstext.append("Vak")

                    else:
                        pass

                print(', '.join(map(str,roundstext)))
                time.sleep(3)
                items = []
                itemstext = []
                print("A tárgyak:",end=" ")
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
                time.sleep(3)
                tevés = True
                while tevés == True:
                    print("Mit szertnél tenni?")
                    print("[1] Az ellenfél / osztó lelövése")
                    print("[2] Önmagad lelövése")
                    print("[3] Tárgy(ak) használata")
                    valaszt2 = input(">>>")
                    if valaszt2 == "1":
                        print("OK")

                    elif valaszt2 == "2":
                        print("OK2")

                    elif valaszt2 == "3":
                        print("A használható tárgyak:", end=" ")
                        print(', '.join(map(str, itemstext)))
                        print("Kérlek írd be a választott tárgy nevét!")
                        valaszt3 = input(">>>")
                        itemfound = False
                        rohadjmeg = False
                        for elem in itemstext:
                            if elem.lower() == valaszt3.lower():
                                itemfound = True
                                print(valaszt3)
                                if valaszt3.lower() == "cigi":
                                    if playerhp == 4 and (valaszt3 == "Cigi" or "cigi"):
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
                                    if thereareroundsleft == True:
                                        sörsors = random.choice(roundstext)
                                        print(sörsors)
                                        print(roundstext)
                                        sörroundfound = False
                                        for roundssör in roundstext:
                                            if (sörsors == roundssör) and sörroundfound == False:
                                                roundstext.remove(roundssör)
                                                sörroundfound = True

                                            else:
                                                pass

                                        print(f"Egy {sörsors} töltény kiszedve!")
                                        print("Egy sör elhasználva!")
                                        itemstext.remove(elem)
                                        print("A megmardt tárgyak:", end=" ")
                                        print(', '.join(map(str, itemstext)))
                                        print(roundstext)

                                    else:
                                        pass
                                    
                                elif valaszt3.lower() == "nagyító":
                                    pass

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


    elif valaszt1 == "2":
        print("Leállítás...")
        time.sleep(3)
        run = False
    else:
        print("Hibás parancs!")
        time.sleep(1)