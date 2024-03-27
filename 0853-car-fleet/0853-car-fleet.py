class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort (make pair (position, speed)) by position 
        # target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        # after sorting, sortbyposition = [[0, 1], [3,3],[5, 1], [8, 4], [10, 2]]
        # distance = target - sportbyposition[0]
        # for the first element of sortbyposition, 
        # the distance is 12 and the time to arrive the target -> time = distance/sortbyposition[1]
        # time will be -> [12, 4, 7, 1, 1]
        # loop over the time from the end -> [1, 1, 7, 3, 12] -> time[앞에 있는것] >=time [뒤에 있는거]: count +=1
        # return the count 
        
        pair = [[p, s] for p, s in zip(position, speed)]
        # print(pair)
        sorP = sorted(pair, key =lambda pair:pair[0], reverse = True)
        # print(sorP) -> [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]
        
        distance =[]
        time =[]
        stack = []
        
        for val in sorP:
            tempD = target - val[0]
            distance.append(tempD)
        # print(distance) [2, 4, 7, 9, 12]
            tempT = tempD/val[1]
            time.append(tempT)
        #print(time) [1.0, 1.0, 7.0, 3.0, 12.0]
        
        for t in time:
            stack.append(t)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
            
            
        
        
        #sorP = sorted(pair, key=lambda x: x[0])
        
        