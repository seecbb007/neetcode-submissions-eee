class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)
        sum_cost = sum(cost)
        if sum_gas < sum_cost:
            return -1
        start_station = 0
        curr_tank = 0
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start_station = i + 1
                curr_tank = 0

        return start_station