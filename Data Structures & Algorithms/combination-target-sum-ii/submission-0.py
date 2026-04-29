class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        def backtrack(start, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(path.copy())
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if curr_sum + candidates[i] > target:
                    break
                curr_sum += candidates[i]
                path.append(candidates[i])
                backtrack(i + 1, curr_sum) 
                curr_sum -= path.pop()

        backtrack(0,0)
        return res
                


            
            