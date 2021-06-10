class AI:
	def CalculateState(bits,pos,player):
		temp = bits.copy()
		score = temp[pos]
		temp[pos] = 0
		while(score > 0):
			pos = (pos+1)%len(temp)
			if(player == 0 and pos == 14):
				continue
			elif(player == 1 and pos == 7):
				continue
			temp[pos] = temp[pos]+1
			#if(bit[pos] == 0 and stealing == True):


			score = score -1
		return temp
	def bestpostion(bits,player,depth):
		score = 0
		best  =  0
		if(player == 1):
			for i in range(8,13):
				Temp = bits.copy()
				calculateState(Temp,i,1)
				if(Temp[14] > score):
					score = temp
					best = i
			return best





	def winner(self,bits):
	    if int(bits[13]) < int(bits[6]):
	        print("Player One has won the game!")
	    elif int(bits[13]) > int(bits[6]):
	        print("Player Two has won the game!")
	    else:
	        print("The game ended in a tie.")


	def isGameEnd(self,bits):
	    south = 0
	    north = 0
	    for j in range(6):
	        south = int(south ) + int(bits[j])
	        north = int(north) + int(bits[j+7])
	    
	        if(int(south) == 0 or int(north) == 0):
	            return  winner(bits)
	            #return True
	            bits[6] = int(bits[6]) + int(south)
	            bits[13] = int(bits[13]) + int(north)
	            for k in range(6):
	                bits[k] = 0
	                bits[k+7] = 0
	    return False
	def get_diff_score(self):
	    if not reversed:
	        return player_points - opponent_points
	    else:
	        return opponent_points - player_points
	def possible_player_moves(self,board):
	    for i, a in enumerate(board[1:7]):
	        if a > 0:
	            yield i
	def find_all_moves(self):
	    all_moves = []
	    for i in self.possible_player_moves():
 	    	self.get_player_moves(i, [], all_moves)
	    return all_moves
bits=[4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4 , 0 ]
print(AI.CalculateState(bits,6,0))

