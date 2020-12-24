from itertools import groupby
from operator import itemgetter

def main():
    global hand
    global flop
    global river
    global deck
    global allcards

    deck = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
            "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD",
            "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
            "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]

    hand = raw_input("What card do you have?(card,card):")
    flop = raw_input("What is the flop?(card,card,card):")

    h = hand.split(",")
    f = flop.split(",")
    river = [f[0], f[1], f[2]]
    allcards = [h[0],h[1],f[0],f[1],f[2]]
    deck.remove(f[0])
    deck.remove(f[1])
    deck.remove(f[2])
    deck.remove(h[0])
    deck.remove(h[1])

    print_odds()

    for x in range(2):
        card = raw_input("Next card: ")
        river.append(card)
        allcards.append(card)
        #straight()
        #print_odds()




#return the odds of getting a flush

def flush():
    h = hand.split(",")
    num = 0
    h1 = 1
    h2 = 1

    #allsuits = list()

    #for x in range(0,len(allcards)):
    #    if allcards[x][0] == '1':
    #        allsuits.append(allcards[x][2])
    #    else:
    #        allsuits.append(allcards[x][1])

    if h[0][1] == h[1][1]:
        num = 2
        for x in range(0, len(river)):
            if river[x][0] != "1":
                if river[x][1] == h[0][1]:
                    num = num + 1
            else:
                if river[x][2] == h[0][1]:
                    num = num + 1
        if len(river) == 3:
            if num == 5:
                return 100
            elif num < 3:
                return 0
            else:
                outs = 13.0-num
                per = (1.0 - ((47.0-outs)/47.0)*((46.0-outs-1)/46.0))*100
                return round(per,2)
        if len(river) == 4:
            if num < 4:
                return 0
            elif num == 5:
                return 100
            else:
                outs = 13.0-num
                per = (1.0-((46.0-outs)/46.0))*100
                return round(per,2)
        if len(river) == 5:
            if num == 5:
                return 100
            else:
                return 0
    else:
        for x in range(0, len(river)):
            if river[x][0] != "1":
                if river[x][1] == h[0][1]:
                    h1 = h1 + 1
                if river[x][1] == h[1][1]:
                    h2 = h2 + 1
            else:
                if river[x][2] == h[0][1]:
                    h1 = h1 + 1
                if river[x][2] == h[1][1]:
                    h2 = h2 + 1

        if len(river) == 3:
            if h1 == 5 or h2 == 5:
                return 100
            elif h1 < 3 and h2 < 3:
                return 0
            else:
                per = (1.0 - (((47.0 - 13-greaterVal(h1,h2)) / 47.0) * ((46.0 - 12-greaterVal(h1,h2)) / 46.0)))*100
                return round(per,2)
        if len(river) == 4:
            if h1 < 4 and h2 < 4:
                return 0
            elif h1 == 5 or h2 == 5:
                return 100
            else:
                per = (1.0 - ((46.0 - 13 - greaterVal(h1,h2)) / 46.0)) * 100
                return round(per, 2)
        if len(river) == 5:
            if h1 == 5 or h2 == 5:
                return 100
            else:
                return 0

def handpair():
    h = hand.split(",")
    for x in range(0, len(river)):
        if h[0][0] == river[x][0]:
            return True
        if h[1][0] == river[x][0]:
            return True
    return False

def riverPair():
    r = river.split(",")
    for x in range(0, len(river)-2):
        if r[x][0] == r[(len(river)-1)][0]:
            return True
        elif r[0][0] == r[1][0]:
            return True

def threeOfAKind():
    h = hand.split(",")
    trh1 = 1
    trh2 = 1
    if h[0][0] == h[1][0]:
        trip = 2
        for x in range(0, len(river)):
            if h[0][0] == river[x][0]:
                trip = trip + 1
        if len(river) == 3:
            if trip >= 3:
                return 100
            else:
                outs = 2
                per = (1.0 - ((47.0-outs)/47.0))*100
                return round(per,2)
        if len(river) == 4:
            if trip >= 3:
                return 100
            else:
                outs = 2
                per = (1.0-((46.0-outs)/46.0))*100
                return round(per, 2)
        if len(river) == 5:
            if trip >= 3:
                return 100
            else:
                return 0
    else:
        for x in range(0, len(river)):
            if river[x][0] == h[0][0]:
                trh1 = trh1 + 1
            if river[x][0] == h[1][0]:
                trh2 = trh2 + 1

        if len(river) == 3:
            if greaterVal(trh1,trh2) >= 3:
                return 100
            else:
                if greaterVal(trh1,trh2) >= 2:
                    per = (1.0 - ((47.0 - (4 - greaterVal(trh1,trh2))) / 47.0)) * 100
                else:
                    per = ((4 - greaterVal(trh1,trh2)) / 47.0) * ((3 - greaterVal(trh1,trh2)) / 46.0) * 100
                return round(per, 2)
        if len(river) == 4:
            if greaterVal(trh1,trh2) >= 3:
                return 100
            elif greaterVal(trh1,trh2) <= 1:
                return 0
            else:
                per = (1.0 - ((46.0 - (4 - greaterVal(trh1,trh2))) / 46.0)) * 100
                return round(per, 2)
        if len(river) == 5:
            if trh1 >= 3 or trh2 >= 3:
                return 100
            else:
                return 0

def fourOfAKind():

    h = hand.split(",")
    fh1 = 1
    fh2 = 1
    for x in range(0, len(river)):
        if river[x][0] == h[0][0]:
            fh1 = fh1 + 1
        if river[x][0] == h[1][0]:
            fh2 = fh2 + 1

    if threeOfAKind() == 100:
        if len(river) == 3:
            if greaterVal(fh1,fh2) != 4:
                per = (1.0 - ((47.0 - 1) / 47.0)) * 100
                return round(per,2)
            else:
                return 100
        if len(river) == 4:
            if greaterVal(fh1,fh2) != 4:
                per = (1.0 - ((46.0 - 1) / 46.0)) * 100
                return round(per, 2)
            else:
                return 100
        if len(river) == 5:
            if greaterVal(fh1,fh2) != 4:
                return 0
            else:
                return 100
    else:
        if len(river) == 3:
            if greaterVal(fh1,fh2) <= 1:
                return 0
            else:
                per = ((((4 - greaterVal(fh1,fh2)))/47.0) * ((3 - greaterVal(fh1,fh2)) / 46.0)) * 100
                return round(per,2)
        if len(river) == 4:
            if greaterVal(fh1,fh2) <= 2:
                return 0
            else:
                per = (1.0 - ((46.0 - 1) / 46.0)) * 100
                return round(per, 2)
        if len(river) == 5:
            if greaterVal(fh1,fh2) < 5:
                return 0
            else:
                return 100

def straight():
    h = hand.split(",")
    numarray = []
    sorts = []
    for x in range(0,len(allcards)):
        if allcards[x][0] == '1':
            numarray.append(10)
        elif allcards[x][0] == 'J':
            numarray.append(11)
        elif allcards[x][0] == 'Q':
            numarray.append(12)
        elif allcards[x][0] == 'K':
            numarray.append(13)
        elif allcards[x][0] == 'A':
            numarray.append(2)
            numarray.append(14)
        else:
            numarray.append(int(allcards[x][0]))
    print numarray
    print sorted(numarray)
    for k, g in groupby(enumerate(sorted(numarray)), lambda (i, x): i - x):
        print len(list(map(itemgetter(1), g)))
        sorts.append(len(list(map(itemgetter(1),g))))
        print sorts





def fullHouse():
    h = hand.split(",")
    p = 0
    numero = 1
    for num in range(0, len(allcards)):
        for x in range(numero,len(allcards)):
            if allcards[num][0] == allcards[x][0]:
                #print "allcards["+str(num)+"][0] == allcards["+str(x)+"][0]"
                p = p + 1
                #print "p = " + str(p)
            numero = numero + 1

    #print allcards
    #print p
    if p == 1:
        return "pair"
    if p == 2:
        return "trip"
    else:
        return "none"

def print_odds():
    #print("\nFlush odds: "+str(flush())+"%")
    print("Straight odds: "+str(straight()))
    #print("Full House odds: "+str(fullHouse())+"%")
    #print("Three of a kind odds: "+str(threeOfAKind())+"%")
    #print("Four of a kind odds: "+str(fourOfAKind())+"%"+"\n")

def greaterVal(a,b):
    if a > b:
        return a
    else:
        return b

if __name__ == '__main__':
    main()