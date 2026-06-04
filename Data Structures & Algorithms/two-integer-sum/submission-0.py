''' oq qro fazer
1 -> percorrer o array 
2-> olhar para o passado quanto falta = atual - target
exemplo:
nums = [1,2,3,3] target = 6
        ^ 6-1 = 5 
historico = {5:0}
nums = [1,2,3,3]      
          ^ 6-2 = 4 
historico = {5:0,4:1}
nums = [1,2,3,3] 
            ^ 6-3 = 3
historico = {5:0,4:1,3:2}
nums = [1,2,3,3] 
              ^ 6-3= 3
3 está no historico! fim achei
3 -> se estiver no historico achamos! se não, adiciona no historico
4-> retorne a posiçao
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        historic = {}
        for i in range(len(nums)): #1
            numnow = nums[i]
            t = target - numnow #2
            if t in historic:
                return [historic[t],i ] #4
            else:
                historic[numnow] = i #3
'''COMPLEXY
TIME: O(n)
SPACE: O(n) -> in the worst case, store all the subtractions in the array
'''

