class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i = 0 
        stone1 =0
        stone2=0
        colision = 0
        while len(stones)>1:  #because the list stones change value all the time
            stones.sort()
            stone1 = stones.pop() #first bigger
            stone2 = stones.pop() #second bigger
    
            if stone1 != stone2:
                colision = stone1-stone2
                stones.append(colision)

        if stones: # se n ta vazia vamo retornar os pesos
            return stones[0]
        else:
            return 0