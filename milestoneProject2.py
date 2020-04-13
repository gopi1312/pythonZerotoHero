# The Black Jack Game

import random
import sys

##Variable Declaration 



class Account():

    def __init__(self,playerName,inputCash):
        self.playerName = playerName
        #self.Balance = inputCash
        self.inputCash = inputCash
        self.availCash = inputCash
        self.bidCoin = 0
        
    def bid(self):
        while True:
            try:
                print(f"AvailCash : {self.inputCash}")
                userInputBid = int(input("Enter Your Bid Amount or Press 0 to Abort: "))
                if(userInputBid == 0):
                    print("Game Abort...")
                    break
                    
                elif(userInputBid > self.availCash):
                    print(f"Invalid Bid. Avail Amount Less than bid.\nAvail Amount : {self.availCash}")
                    continue


                elif(userInputBid <= self.availCash):
                    print(f"The bid Amount is {userInputBid}.")
                    userBidConfirm = (input("Press Y to confirm or N to rebid : ")).upper()

                    if userBidConfirm == 'Y':
                        print("BidPlaced")
                        self.bidCoin = userInputBid
                        self.availCash -= self.bidCoin
                        print(f"BidAmount Rs: {self.bidCoin}\nAvailableCash Rs:{self.availCash}")
                        break

                    elif userBidConfirm == "N":
                        print("Resetting the Game to ReBid")
                        continue

                    else:
                        print("Invalid Input Try Again. Game Reset")
                        continue

            except:
                print("Input Error Try Again")
            else:
                print("Starting The Game...")

class Deck():

    def __init__(self):
        self.deckCard = dict()
        self.deckSize = 0
        self.card = ""
        self.cardValue = 0

        self.cardType = ['Spade','Clubs','Hearts','Dimonds']
        self.cardNum = [x for x in range(2,11)]
        self.cardNum += ['A','K','Q','J']
        for i in self.cardType:
            for j in self.cardNum:
                k = str(j)+"-"+i
                if j == 'K' or j == 'Q' or j == 'J':
                    dump = {k:10}
                elif j == 'A':
                    dump = {k:1}
                else:
                    dump = {k:j}
                self.deckCard.update(dump)

    #def newDeckCreate(self):
    #    self.cardType = ['Spade','Clubs','Hearts','Dimonds']
    #    self.cardNum = [x for x in range(2,11)]
    #    self.cardNum += ['A','K','Q','J']
    #    for i in self.cardType:
    #        for j in self.cardNum:
    #            k = str(j)+"-"+i
    #            if j == 'K' or j == 'Q' or j == 'J':
    #                dump = {k:10}
    #            else:
    #                dump = {k:j}
    #            self.deckCard.update(dump)
    #    self.deckSize = len(self.deckCard)
    #    return self.deckCard
        
    def popCard(self):
        self.card = key = random.choice(list(self.deckCard.keys()))
        self.cardValue=int(self.deckCard.pop(self.card))
        self.deckSize = len(self.deckCard)

    def __str__(self):
        return str(self.deckSize)



def func_hit(deckCreate):
    deckCreate.popCard()
    hitCard = deckCreate.card
    hitCardValue = deckCreate.cardValue
    return [hitCard,hitCardValue] 


def playerGame(deckCreate,playerHand,playerHandValue,dealerHand,dealerHandValue,playerCash,playerBid):

    while playerHandValue < 22:
        if playerHandValue == 21:
            print("blackJack")
            dealerGame(deckCreate,playerHand,playerHandValue,dealerHand,dealerHandValue,playerCash,playerBid)
            break
        else:
            userInputOption = (input("Would you like to (HIT/STAND) :")).upper()
            if(userInputOption == "HIT"):
                userHit = func_hit(deckCreate)
                playerHand += [userHit[0]]
                playerHandValue += userHit[1]
                aceCheck(playerHand,playerHandValue)
                print(f"Player{playerHand},{playerHandValue}\nDealer : {dealerHand}")
            elif(userInputOption == "STAND"):
                dealerGame(deckCreate,playerHand,playerHandValue,dealerHand,dealerHandValue,playerCash,playerBid)            
                break
    dealerGame(deckCreate,playerHand,playerHandValue,dealerHand,dealerHandValue,playerCash,playerBid)


def dealerGame(deckCreate,playerHand,playerHandValue,dealerHand,dealerHandValue,playerCash,playerBid):    
    
    while (dealerHandValue < 22) and (dealerHandValue <= playerHandValue) and (playerHandValue < 22):
        dealerHit = func_hit(deckCreate)
        dealerHand += [dealerHit[0]]
        dealerHandValue += dealerHit[1]
        aceCheck(playerHand,playerHandValue)
    winningStrategy(deckCreate,playerHand,playerHandValue,dealerHand,dealerHandValue,playerCash,playerBid)

def winningStrategy(deckCreate,playerHand,playerHandValue,dealerHand,dealerHandValue,playerCash,playerBid):
    
    if dealerHandValue == 21 and playerHandValue == 21 :
        print("Push")
        print(f"Player{playerHand},{playerHandValue}\nDealer : {dealerHand},{dealerHandValue}")
        playerCash += playerBid
        print(f"PlayerCash : {playerCash} ")
    
    elif playerHandValue > 21:
        print("PlayerBust.. Dealer Win")
        print(f"Player{playerHand},{playerHandValue}\nDealer : {dealerHand},{dealerHandValue}")
        print(f"PlayerCash : {playerCash} ")
    
    elif dealerHandValue > 21:
        print("Dealer Bust.. Player Win")
        print(f"Player{playerHand},{playerHandValue}\nDealer : {dealerHand},{dealerHandValue}")
        playerCash += (playerBid*2)
        print(f"PlayerCash : {playerCash} ")
    
    elif dealerHandValue < 21 and dealerHandValue > playerHandValue:
        print("Dealer Win")
        print(f"Player{playerHand},{playerHandValue}\nDealer : {dealerHand},{dealerHandValue}")
        print(f"PlayerCash : {playerCash} ")
    

    userContInput = (input("would you like to continue(Y/N):")).upper()
    if userContInput == 'Y':
        if playerCash == 0:
            print("You Run out of cash. Invest some cash and start the game again.")
            sys.exit("Game Exit as you run out of Cash")
        else:
            startGame(deckCreate,name,playerCash)
    elif userContInput == 'N':
        sys.exit("Game Exits")
    



def startGame(deckCreate,name,cashIn):
    accountCreate = Account(name,cashIn)
    accountCreate.bid()
    playerHand = list()
    dealerHand = list()
    playerHandValue = 0
    dealerHandValue = 0
    playerCash = accountCreate.availCash
    playerBid = accountCreate.bidCoin
    while len(playerHand) < 2:
        deckCreate.popCard()
        playerHand += [deckCreate.card]
        playerHandValue += deckCreate.cardValue
    while len(dealerHand) < 2:
        deckCreate.popCard()
        dealerHand += [deckCreate.card]
        dealerHandValue += deckCreate.cardValue
        aceCheck(playerHand,playerHandValue)
    print(f"\nplayerHand : {playerHand}, PlayerHandValue : {playerHandValue}")
    print(f"dealerHand : {dealerHand}\n")

    playerGame(deckCreate,playerHand,playerHandValue,dealerHand,dealerHandValue,playerCash,playerBid)


def aceCheck(hand,cValue):
    aceCards = ['A-Dimonds','A-Clubs','A-Hearts','A-Spade']
    for x in aceCards:
        if x in hand:
            if cValue < 11:
                cValue = cValue
            else:
                cValue += 10
    return cValue



if __name__ == "__main__":
    name = input("Enter the player Name : ")
    cashIn = int(input("Enter the Amount you are cash in for playing Rs. "))
    deckCreate = Deck ()
    startGame(deckCreate,name,cashIn)
