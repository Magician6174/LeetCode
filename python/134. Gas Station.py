class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        surplus = 0
        deficit = 0
        start = 0
        for i in range(len(gas)):
            surplus = surplus + gas[i] - cost[i]
            
            if (surplus < 0):
                start = i+1
                deficit += surplus
                surplus = 0
        
        if surplus + deficit >= 0:
            return start
        else:
            return -1
        
        
        
        """----------------------Brute Force--------------------------"""
        # gas_sum = sum(gas)
        # cost_sum = sum(cost)
        # stations = len(gas)
        # if (gas_sum - cost_sum) < 0:
        #     return -1
        # else:
        #     for i, station in enumerate(gas):
        #         s = 0
        #         for j in range(stations):
        #             s += gas[(i+j)%stations]-cost[(i+j)%stations]
        #             if s < 0:
        #                 answer = False
        #                 break
        #             else:
        #                 answer = True
        #         if answer:
        #             return i
                    
