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
			self.CalculateState(i,[], all_moves)
		return all_moves  


   
    def mini_max(self,depth=2, maximizing_player=False):
        if depth == 0 or isGameEnd():
            return get_diff_score()
        
        if maximizing_player:
            best_value = -1000
            for move, board in get_opponent_board().find_all_moves():
                val = board.mini_max(depth - 1, not maximizing_player)
                best_value = max(best_value, val)
            return best_value
        
        else:
            best_value = 1000
            for move, board in get_opponent_board().find_all_moves():
                val = board.mini_max(depth - 1, not maximizing_player)
                best_value = min(best_value, val)
            return best_value



       

'''
    
def mini_max_alpha_beta(self,depth=2, maximizing_player=False):
    if depth == 0 or isGameEnd():
        return get_diff_score()
    
    if maximizing_player:
        best_value = -1000
        for move, board in get_opponent_board().find_all_moves():
            val = board.mini_max(depth - 1, not maximizing_player)
            best_value = max(best_value, val)
        return best_value
    
    else:
        best_value = 1000
        for move, board in get_opponent_board().find_all_moves():
            val = board.mini_max(depth - 1, not maximizing_player)
            best_value = min(best_value, val)
        return best_value




def mini_max_alpha_beta(self, depth=2, alpha=-999, beta=+999, maximizing_player=False):
    if depth == 0 or isGameEnd():
        return get_diff_score()
    
    if maximizing_player:
        best_value = -999
        for move, board in self.get_opponent_board().find_all_moves():
            best_value = max(best_value,board.mini_max(depth - 1, alpha, beta, not maximizing_player),)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = 999
        for move, board in self.get_opponent_board().find_all_moves():
            best_value = min(
                    best_value, board.mini_max(depth - 1, not maximizing_player)
                )
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value










def compute(x):
    move_sequence, board = x
    return [x + 1 for x in move_sequence],mini_max(DEPTH)
'''            
   




         
bits=[4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4 , 0 ]
print(AI.find_all_moves(bits))

