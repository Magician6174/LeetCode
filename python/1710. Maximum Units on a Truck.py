class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        sorted_boxTypes = sorted(boxTypes,key=lambda l: l[1],reverse=True)
        totalUnits = 0
        for boxes,units in sorted_boxTypes:
            if boxes >= truckSize:
                totalUnits += (truckSize * units)
                return totalUnits
            else:
                totalUnits += (boxes * units)
                truckSize = truckSize - boxes
                
        return totalUnits
