#########################################################################################################
#Python Tennis Simulator                                                                                #
#########################################################################################################
from random import randrange
from time import sleep 
SLEEP_TIME=0.1
SETS=3
#########################################################################################################
players=[['Novak Djokovic','22/05/1987',30,510],
      ['Rafael Nadal','03/06/1986',17,480],
      ['Roger Federer','08/08/1981',27,490],
      ['Dominic Thiem','03/09/1996',14,300],
      ['Kei Nishikori','29/12/1989',23,500],
      ['Alexander Zverev','20/04/1997',18,320],
      ['Stefanos Tsitsipas','12/08/1998',17,450],
      ['Daniil Medvedev','11/02/1996',16,340],
      ['Karen Khachanov','21/05/1996',14,380],
      ['Fabio Fognini','24/05/1987',27,350],  ]
#########################################################################################################
def doMatch(player1,player2):
    """Simulates a match between 2 players and return the result: 1 if the first player wins, 2 if the second.
        setWins - keeps track of each players number of sets won. 2 sets means that players is the winner.
        gameCount - keep track of how many games were played."""
    setWins=[0,0]
    gameCount=1
    print('<Match {0} - {1}>'.format(player1[0],player2[0]))
    sleep(SLEEP_TIME)
    def doSet(Set):
        """Simulates a set of games between 2 players. When a set is won setWins of the player will increase by 1.
            setWinner - stores the player that won the current set.
            gameWins - keeps track of how many games each player won."""
        setWinner=None
        gameWins=[0,0]
        nonlocal setWins
        nonlocal gameCount
        def doGame():
            """Simulates a single game between 2 players.
                gammeWinner - stores the winner of the current game.
                points - keeps track of how many points each players got in the current game."""
            gameWinner=None
            points=[0,0]
            nonlocal gameCount
            print('game {:>2}: '.format(gameCount),end='')
            sleep(SLEEP_TIME)
            #Randomly picks the first players to score points in the current game
            x=randrange(0,2)
            points[x]+=15
            #The loop runs until on player gets more than 40 points. That player is the winner of the current game
            while not gameWinner:
                print('{:0<2}-{:0<2}'.format(points[0],points[1]),end=',')
                sleep(SLEEP_TIME)
                x=randrange(0,2)
                if points[x]<30:
                    points[x]+=15
                elif points[x]<40:
                    points[x]+=10
                else:
                    gameWins[x]+=1
                    if x:
                        gameWinner=player2
                    else:
                        gameWinner=player1
            print('game winner: {} {}:{}'.format(gameWinner[0],gameWins[0],gameWins[1]))
        sleep(SLEEP_TIME)
        print('<set {}>'.format(Set))
        sleep(SLEEP_TIME)
        #The loop runs until one player wins 6 games with 2 or more wins over the other player or until a player wins 7 games.
        while not setWinner:
            doGame()
            gameCount+=1
            if gameWins[0]==6 and gameWins[0]-gameWins[1]>=2:
                setWins[0]+=1
                setWinner=player1
            elif gameWins[1]==6 and gameWins[1]-gameWins[0]>=2:
                setWins[1]+=1
                setWinner=player2
            elif gameWins[0]==7:
                setWins[0]+=1
                setWinner=player1
            elif gameWins[1]==7:
                setWins[1]+=1
                setWinner=player2
        print('set winner {} {}:{}'.format(setWinner[0],setWins[0],setWins[1]))
        sleep(SLEEP_TIME)
    #The loop runs a maximum of 3 times or until one player wins 2 sets
    for i in range(SETS):
        doSet(i+1)
        if setWins[0]==2:
            print('match winner: {}'.format(player1[0]))
            sleep(SLEEP_TIME)
            return 1
        elif setWins[1]==2:
            print('match winner: {}'.format(player2[0]))
            sleep(SLEEP_TIME)
            return 2
#########################################################################################################
def doTournament(tname,plist,pamount):
    '''Simulates a tennis tournament between 2^n players that are picked randomly from the player list.
        matchWinner - stores the player that won the tournament.
        nextBracket - stores the players that go to the next phase of the tournament until only one player is left.'''
    matchWinner=None
    nextBracket=[]
    def choicePlayers(playerList,playerNum):
        '''Recieves a list of players and a number and picks that number of players randomly from the list.
            players - stores the players that were picked. the function returns that list.
            The players that were picked are removed from the main list'''
        players=[]
        for i in range(playerNum):
            x=randrange(0,len(playerList))
            players.append(playerList[x])
            playerList.remove(playerList[x])
        return players
    #tplist - the list of the players participating in the tournament
    tplist=choicePlayers(plist,pamount)
    print('Tournament '+tname)
    sleep(SLEEP_TIME)
    print('players:',end=' ')
    sleep(SLEEP_TIME)
    for i in range(pamount):
        print(tplist[i][0],end=', ')
        sleep(SLEEP_TIME)
    #The loop runs until only one player is left. That player is the winner
    while len(tplist)>1:
        print('\n'+'-'*40)
        sleep(SLEEP_TIME)
        #mplist - contains the 2 players for the current match. picks the randomly from tplist
        mplist=choicePlayers(tplist,2)
        matchWinner=doMatch(mplist[0],mplist[1])
        #After the match arrenges the list so the winner is first and the loser is second
        mplist=[mplist[matchWinner-1],mplist[matchWinner%2]]
        #Increase the loser's tournament played count by one
        mplist[1][2]+=1
        #Remove the loser from the list and return him to the main list of player
        plist.insert(0,mplist.pop())
        #Add 10 points to the winner
        mplist[0][3]+=10
        #Store the winner in the list for the next phase
        nextBracket.append(mplist[0])
        if len(tplist)==0:
            tplist=nextBracket
            nextBracket=[]
    #Increas the tournament winner's tournamet count and points and return him to the main player list
    tplist[0][2]+=1
    tplist[0][3]+=10
    print('-'*40)
    sleep(SLEEP_TIME)
    print('Tournament {} winner - {}'.format(tname,tplist[0][0]))
    sleep(SLEEP_TIME)
    plist.insert(0,tplist.pop())
#########################################################################################################
def printPlayer(player):
    '''Recieves a player and prints his infromation.
        width - used for formatting spaces'''
    width=(20,12,4,0)
    for i in range(len(player)):
        print('{:<{w}}'.format(player[i],w=width[i]),end='')
        sleep(SLEEP_TIME)
    print()
#########################################################################################################
def printPlayers(plist,num=0):
    '''Recieves a list of players and a number and prints the players:
        n=0 - prints all the players
        n<0: prints the players from index length-n to the last
        n>0: prints the players from index 0 to n'''
    if num>0:
        for i in range(num):
            printPlayer(plist[i])
            sleep(SLEEP_TIME)
    elif num<0:
        for i in range(len(plist)+num,len(plist)):
            printPlayer(plist[i])
            sleep(SLEEP_TIME)
    else:
        for i in range(len(plist)):
            printPlayer(plist[i])
            sleep(SLEEP_TIME)
    print()
#########################################################################################################
def sortPlayers(plist):
    '''Recieves a list of players and sorts the by points in descending order'''
    for i in range(len(plist)):
        for j in range(i,len(plist)-1):
            if plist[i][3]<plist[j+1][3]:
                plist[i],plist[j+1]=plist[j+1],plist[i]
#########################################################################################################
def addPlayer(plist):
    '''Recieves a list of players. Asks the user for info on the new player and then inserts him into the end of the list'''
    newPlayer=[]
    newPlayer.append(input('Enter name: '))
    newPlayer.append(input('Enter birthday[dd/mm/yyyy]: '))
    newPlayer.append(int(input('Enter number of tournaments played: ')))
    newPlayer.append(int(input('Enter number of points: ')))
    plist.append(newPlayer)
#########################################################################################################
def removePlayer(plist):
    '''Recieves a list of players, checks which one has the least amount of points and the removes him from the list'''
    playerToRemove=plist[0]
    for i in range(1,len(plist)):
        if playerToRemove[3]>plist[i][3]:
            playerToRemove=plist[i]
    print('Player {0} was removed from player list'.format(playerToRemove[0]))
    plist.remove(playerToRemove)
#########################################################################################################
def menu(plist):
    '''Prints a menu for the user and runs the functions based on their choice. all input validity check happen here'''
    flag=True
    menu='''---------------------
--Tennis--Simulator--
---------------------
------Main Menu------
[1] Print player list
[2] Print player
[3] Sort player list
[4] Add new player
[5] Remove player
[6] Play a match
[7] Play a tournament
[8] Exit'''
    while flag:
        print(menu)
        sleep(SLEEP_TIME)
        choice=int(input('Enter your choice: '))
        if choice==1:
            print('[-1 - {}] print from the end of the list\n[0] print all players\n[1 - {}] print from start of list'.format(len(plist)*-1,len(plist)))
            choice=int(input('Enter your choice: '))
            #check if the number entered is inside the list index range
            while choice>len(plist) or choice<len(plist)*-1:
                choice=int(input('Invalid input! Try again: '))
            printPlayers(plist, choice)
        elif choice==2:
            #check if the number entered is inside the list index range
            choice=int(input('Enter a number between 1 and {}: '.format(len(plist))))
            while choice<1 or choice>len(plist):
                choice=int(input('Invalid input! Try again: '))
            printPlayer(plist[choice-1])
        elif choice==3:
            sortPlayers(plist)
            print('Player list was sorted!')
            sleep(SLEEP_TIME)
            printPlayers(plist)
        elif choice==4:
            addPlayer(plist)
            printPlayers(plist)
        elif choice==5:
            removePlayer(plist)
            printPlayers(plist)
        elif choice==6:
            player1=int(input('Enter a number between 1 and {}: '.format(len(plist))))
            #check if the number entered is inside the list index range
            while player1<1 or player1>len(plist):
                player1=int(input('Invalid input! Enter a number between 1 and {}: '.format(len(plist))))
            player2=int(input('Enter a number between 1 and {}: '.format(len(plist))))
            #check if the number entered is inside the list index range and not the same player that was already chosen
            while player2<1 or player2>len(plist) or player1==player2:
                if player2<1 or player2>len(plist):
                    player2=int(input('Invalid input! Enter a number between 1 and {}: '.format(len(plist))))
                if player1==player2:
                    player2=int(input('Player already chosen! Try again: '.format(len(plist))))
            doMatch(plist[player1-1],plist[player2-1])
        elif choice==7:
            tname=input('Enter tournament name: ')
            pamount=int(input('Enter number of players(powers of 2): '))
            def checkInput(x):
                '''Recieves a number and checks if it's a power of 2. Retruns true is it is and false if it isn't'''
                temp=x
                if x>len(plist):
                    print('Number of players cannot be larger then player list!')
                while x>2:
                    x/=2
                return int(x)==2 and temp<=len(plist)
            while not checkInput(pamount):
                pamount=int(input('Numer of players must be power of 2! Try again: '))
            doTournament(tname,plist,pamount)
        elif choice==8:
            print('Goodbye!')
            flag=False
        else:
            print('Invalid input! Try again!')
#########################################################################################################
def main():
    print('<Print list players>')
    printPlayers(players)
    
    print('<Print list players>')
    printPlayers(players,4)
    print('<Print list players>')
    printPlayers(players,-3)

    print('<Sort list players>')
    sortPlayers(players)
    print('<Print list players>')
    printPlayers(players)

    print('<Add player>')
    addPlayer(players)
    print('<Print list players>')
    printPlayers(players)

    print('<Remove player>')
    removePlayer(players)
    print('<Print list players>')
    printPlayers(players)
 
    print('<Tournamen>')
    doTournament('Wimbledon',players,4)
    print('<Print list players>')
    printPlayers(players)
#########################################################################################################
menu(players)