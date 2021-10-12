from algo import game



print('Done')
class algo():
	running_game = game()


	@classmethod 
	def main(cls, string):
		# first we have to create checkBoard from string 
		oldboard = cls.string_to_board(string)
		print('very oldboard->', oldboard)


		# then we have to find the newcheck board
		newboard = cls.new_checkboard(oldboard)
		print('very oldboard*->', oldboard)

		# then we have to find the change in checkboard
		candidate = cls.find_change(oldboard, newboard)


		# then we will return the the change in checkborad as new candidate
		return(candidate)

	@classmethod
	def find_change(cls, oldboard, newboard):
		for i in range(1, 10):
			if (oldboard[i] != newboard[i]):
				return(str(i))

	@classmethod
	def new_checkboard(cls, oldboard):
		#cls.running_game.checkBoard = oldboard.copy() # we have to copy means creating a new list
		newboard = cls.running_game.turn(oldboard.copy())
		print('oldboard->', oldboard)
		print('newboard->', newboard)
		return(newboard)  

	@classmethod
	def string_to_board(cls, string):
		checkBoard = {
            1 : None, 2 : None, 3 : None, 4 : None, 5 : None, 6 : None, 7 : None, 8 : None, 9 : None 
        }
        
		for i in range(len(string)):
        	# odd places are for player
			if ((i+1)%2==0):
				checkBoard[int(string[i])] = 'p2'
			else:
				checkBoard[int(string[i])] = 'p1'
		return(checkBoard)
