class Solution:
    def findMinDifference(self, timepoints: List[str]) -> int:
        
        def hourToMin(time :str) -> int:
            
            h , m = map( int , time.split(":"))
            return h*60 + m

        minutes = sorted(hourToMin(time) for time in timepoints)

        min_diff = float('inf')

        for i in range(len(minutes) - 1):
            min_diff = min(min_diff , minutes[i+1] - minutes[i] )
        min_diff = min(min_diff, (minutes[0] + 1440) - minutes[-1])
        return min_diff
        