class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_speed_map = {}
        for i in range(len(position)):
            car_speed_map[position[i]] = speed[i]
        # reverse the posiitons
        position.sort(reverse=True)
        fleet_count = 0
        curret_fleet_time = (target - position[0])/car_speed_map[position[0]]
        for i in range(1, len(position)):
            finishTime = (target - position[i])/car_speed_map[position[i]]
            if finishTime >curret_fleet_time:
                fleet_count +=1
                curret_fleet_time = finishTime
        fleet_count +=1
        return fleet_count

        