class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        # remove ties
        deltas = [(A[i]-A[i-1]) for i in range(1,len(A)) if A[i]-A[i-1] != 0]

        for i in range(1,len(deltas)):
            if deltas[i]*deltas[i-1]<0:
                return False       
        return True
