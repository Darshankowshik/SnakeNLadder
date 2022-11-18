import random

#initilizing the required variables,play as player,pos as position of the player,winpos as final placement,win as what is winning place 
play=[]
pos=[]
winpos=[]
win=100


class Game:
    #constructor to initilize player name and position
    def __init__(self,n):
        self.checkplayer=n
        if(n<=1):
            print("No of players is too less Enter more players to win the game")
            main()
        else:
            for initilize in range(n):
                play.append(input("Enter player {} name:\t".format(initilize+1)))
                pos.append(0)
        return

    #snake and ladder mechanism
    def snakeOrLadder(self,diceno1,playing):
        #temp is initial pos and temp 1 is final pos if ladder or snake is the possibility
        temp=pos[playing]
        print("You got {} and you are at position {}\n".format(diceno1,temp))
        if temp==1:
            temp1=38
        elif temp==4:
            temp1=14
        elif temp==8:
            temp1=30
        elif temp==28:
            temp1=76
        elif temp==21:
            temp1=42
        elif temp==50:
            temp1=67
        elif temp==71:
            temp1=92
        elif temp==80:
            temp1=99
        elif temp==36:
            temp1=6
        elif temp==32:
            temp1=10
        elif temp==48:
            temp1=26
        elif temp==62:
            temp1=18
        elif temp==95:
            temp1=56
        elif temp==88:
            temp1=24
        elif temp==97:
            temp1=78
        else:
            return

        if temp1>temp:
                pos[playing]=temp1
                print("You got the ladder\nYou are at the position: {}\n".format(pos[playing]))
                return
        elif temp>temp1:
                pos[playing]=temp1
                print("You got bitten by snake\nyou are at the position: {}\n".format(pos[playing]))
                return        
    
    #verifiy input mechanism for the roll dice
    def verifyIf(self):
        verify=(input("Enter p to roll the dice\n"))
        if verify=='p':
            return
        else:
            print("Wrong input please enter p")
            self.verifyIf()

    #to check if player has win or not
    def checkWinif(self,playing,diceno2):
        temp=pos[playing]
        temp+=diceno2
        if temp>win:
            return 1
        elif temp==win: 
            return 0
        else:
            return -1

    #mechanism to roll the dice 
    def rollDice(self,playing):
        self.diceno=random.randint(1,6)
        x=self.checkWinif(playing,self.diceno)
        if x==1:
            print("You got {} Can't play as you got greater no then you need".format(self.diceno))
            print("You are at {}\n".format(pos[playing]))
            return
        if x==0:
            pos[playing]=100
            print("HurraY! you won\n")
            return
        
        pos[playing]=pos[playing]+self.diceno
        self.snakeOrLadder(self.diceno,playing)
        if self.diceno==6:
            print("As you got 6 you get another chance")
            self.rollDice(playing)
        return


def main():
    i=-1
    #Entering the no of players 
    n=int(input("Enter the no of players in the game(At least 2 players):\n"))
    snl=Game(n)

    while(snl.checkplayer>0):
        for playing in range(len(pos)):
            #for updating final winning position
            if pos[playing]==win:
                winpos.append(play[playing])
                play.remove(play[playing])
                pos.remove(pos[playing])
                snl.checkplayer-=1
                if snl.checkplayer==1:
                    finalDisplay(playing,n)
            else:
                print("{} is playing".format(play[playing]))
                snl.verifyIf()
                snl.rollDice(playing)

#displaying a final winning position
def finalDisplay(playing,n):
    winpos.append(play[playing])
    play.remove(play[playing])
    pos.remove(pos[playing])
    print("Winning Place\t|\tPlayer")
    for wining,winning in winpos,range(n):
       print("{}\t\t|\t{}".format(winning,wining)) 

    exit(0)


if __name__=="__main__":
    main()