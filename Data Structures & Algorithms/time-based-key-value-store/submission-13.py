from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
        # self.timestamp = []
        # self.timestampSize = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp,value))
        # self.timestamp.append(timestamp)
        # self.timestampSize+=1

    def get(self, key: str, timestamp: int) -> str:
        # print(self.hm)
        
        if key not in self.hm:
            return ""
        l = 0
        r = len(self.hm[key]) - 1

        if timestamp < self.hm[key][l][0]:
            return ""

        while l <= r :
            mid = (l + r ) // 2
            if self.hm[key][mid][0] == timestamp:
                return self.hm[key][mid][1]
            
            elif self.hm[key][mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1

        return self.hm[key][r][1]

        
