import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            dist = -(x**2 + y**2)
            
            # se a heap ainda não tem 'k' elementos, adicionamos direto
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, [x, y]))
            else:
                # se o ponto atual for mais próximo (distância menos negativa) 
                # do que o pior ponto atual da heap (max_heap[0][0])
                if dist > max_heap[0][0]:
                    heapq.heappushpop(max_heap, (dist, [x, y]))
        
        # no final, extraímos apenas as coordenadas [x, y] que sobraram na heap
        return [ponto for dist, ponto in max_heap]