from GUI import Mancala
class AI:

    def __init__(self,bits): 
        self.bits = bits
        #self.mancala = Mancala()

    def CalculateState(self,bits,pos,player):
        temp = bits.copy()
        score = temp[pos]
        temp[pos] = 0
        while(score > 0):
            pos = (pos+1)%len(temp)
            if(player == 0 and pos == 13):
                continue
            elif(player == 1 and pos == 6):
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
    def possible_player_moves(self,player):
        if player==0:
            for i, a in enumerate(self.bits[0:6]):
                if a > 0:
                    yield i
        else:
             for i, a in enumerate(self.bits[7:13]):
                if a > 0:
                    yield i+7
        
                
    def find_all_moves(self,player=0):
        all_moves = []  
        for i in self.possible_player_moves(player):
            all_moves.append([i,self.CalculateState(self.bits,i,player)])
        return all_moves  

    def isGameEnd(self,bits):
        if(sum(bits[0:6]) == 0 or sum(bits[7:13]) == 0):
            return True
        return False
   
    def mini_max(self,bits,depth=2, maximizing_player=True):
        if depth == 0 or self.isGameEnd(bits):
            return self.get_diff_score(bits)
        
        if maximizing_player:
            best_value = -1000
            
            for move, board in self.find_all_moves(1):
                
                val = self.mini_max(board,depth - 1, not maximizing_player)
               # best_value = max(best_value, val)
                index=0
                if val>best_value:
                   index=move
                   best_value=val
                #print(val)
                #print(move)
                #print(board)
            return index
        
        else:
            best_value = 1000
            for move, board in self.find_all_moves(1):
                
                val = self.mini_max(board,depth - 1, not maximizing_player)
                #best_value = min(best_value, val)
                if val<best_value:
                   index=move
                   best_value=val
                #print(board)
                
            return index



       

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
   




         
#bits=[0, 0, 0, 0, 9, 1, 5, 4, 4, 4, 4, 4, 4 , 10 ]
bits=[0, 0, 0, 0, 9, 1, 5, 0, 0, 0, 0, 9, 1 , 10 ]
test = AI(bits)
#print(test.mini_max(bits))
print(test.find_all_moves(1))


