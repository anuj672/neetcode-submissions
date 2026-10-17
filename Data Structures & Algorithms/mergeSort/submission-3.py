# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if not pairs or len(pairs)<=1:
            return pairs

        def helper(pairs):
        
            if len(pairs)>1:
                
                left_arr = pairs[ :len(pairs)//2]
                right_arr = pairs[len(pairs)//2:]

                helper(left_arr)
                helper(right_arr)

                i,j,k = 0,0,0

                while i < len(left_arr) and j < len(right_arr):

                    if left_arr[i].key <= right_arr[j].key:
                        pairs[k] = left_arr[i]
                        i+=1
                    elif left_arr[i].key > right_arr[j].key:
                        pairs[k] = right_arr[j]
                        j+=1                        
                    k+=1

                while i < len(left_arr):
                    pairs[k] = left_arr[i]
                    i+=1
                    k+=1


                while j < len(right_arr):
                    pairs[k] = right_arr[j]
                    j+=1
                    k+=1

                return pairs     
        return helper(pairs)


