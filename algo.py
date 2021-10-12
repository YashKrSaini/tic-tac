class game:
    def __init__(self):
        self.checkBoard = {
            1 : None, 2 : None, 3 : None, 4 : None, 5 : None, 6 : None, 7 : None, 8 : None, 9 : None 
        }
    
    def winCheck(self, playerName):
        winList = [
            [1,2,3],[4,5,6],[7,8,9], # Horizontals wins case
            [1,4,7],[2,5,8],[3,6,9], # verticalls wins case
            [1,5,9],[3,5,7]            # diagonally wins case
        ]
        for array in winList:
            if (self.checkBoard[array[0]]==self.checkBoard[array[1]]==self.checkBoard[array[2]]==playerName):
                return (True)
        return(False)
    
    def move(self,playerName,position): # player Name :- p1 or p2
        if (self.checkBoard[position] == None):
            self.checkBoard[position] = playerName
            return ('done')
        else:
            print('Wrong Input')
            return('wrong')
            
    def autoMove(self):
        # first it will check if computer is wining or not if yes then it will take that move
        for move in self.checkBoard:
            if (self.checkBoard[move] == None): # search available spaces
                self.checkBoard[move] = 'p2' # assume its value
                if (self.winCheck('p2') == True): # check for win 
                    return ('You Loss')
                else:
                    self.checkBoard[move] = None # if not then make it none again 
        
        # first it will check if another player is winning somewhere if yes then it will take its position
        for move in self.checkBoard:
            if (self.checkBoard[move] == None):
                self.checkBoard[move] = 'p1'
                if (self.winCheck('p1') == True): # check for target 
                    self.checkBoard[move] = 'p2' # take target position
                    return ('next')
                else:
                    self.checkBoard[move] = None
        # if nothing happens
        for move in self.checkBoard:
            if (self.checkBoard[move] == None):
                self.checkBoard[move] = 'p2'
                return ('next')
        return ('dead end')
    
    def space(self):
        for move in self.checkBoard:
            if (self.checkBoard[move] == None):
                return(True)
        return(False)
    
    def status(self):
        print(self.checkBoard)


    def turn(self, checkBoard): # this function will take the checkborad, playerName and give the answer
        self.checkBoard = checkBoard
        self.autoMove()
        print('algo.py (after autoMove)->',self.checkBoard)
        return (self.checkBoard)
    
    def start(self):
        game = True
        playerWon = None
        while (game==True):
            position = int(input('Enter ->'))
            case = self.move('p1',position) # player 1 move
            if (case == 'wrong'):
                continue
            print('player 1')
            self.status()
            # checking status
            if (self.winCheck('p1') == True):
                playerWon = 'p1'
                game = False
                break
            if (self.space==False):
                playerWon = None
                game = False
                break
            else:
                
                # checking status
                case = self.autoMove()
                print('player 2')
                self.status()
                if (case == 'You Loss'):
                    playerWon = 'p2'
                    game = False
                    break
                if (self.space==False):
                    playerWon = None
                    game = False
                    break
        # when everything pass it will show status 
        if (playerWon == 'p1'):
            print('You won')
        elif (playerWon == 'p2'):
            print('You Loss')
        else:
            print('Tie')
            
            
            
            