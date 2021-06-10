class AI:
	def CalculateState(bits,pos,player,stealing=True):
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


    



	def get_diff_score(self,bits):
	    if not reversed:
	        return bits[6] - bits[13]
	    else:
	        return bits[13] - bits[6]
    
    
    
	def possible_player_moves(self,bits):
	    for i, a in enumerate(bits[0:7]):
	        if a > 0:
	            yield i



    def find_all_moves(self):
        all_moves = []
        for i in self.possible_player_moves():
            self.get_player_moves(i, [], all_moves)
        return all_moves            



            
            
bits=[4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4 , 0 ]
print(AI.CalculateState(bits,5,0))

