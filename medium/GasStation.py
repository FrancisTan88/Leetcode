from typing import List

class Solution:
    """
    time: O(n^2)
    space: O(1)
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        while start < len(gas):
            tmp = start
            residual = 0
            curr_gas = gas[start]
            while curr_gas >= cost[tmp]:
                residual = curr_gas - cost[tmp]
                if tmp != len(gas) - 1:
                    tmp += 1
                else:
                    tmp = 0
                if tmp == start:
                    return start
                curr_gas = gas[tmp] + residual
            start += 1
        return -1

    """
    time: O(n)
    space: O(1)
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus = 0
        curr_surplus = 0
        start = 0
        for i in range(len(gas)):
            total_surplus += gas[i] - cost[i]
            curr_surplus += gas[i] - cost[i]
            if curr_surplus < 0:
                curr_surplus = 0
                start = i + 1
        return -1 if total_surplus < 0 else start