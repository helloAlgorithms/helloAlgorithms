class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_damage = 0;
        current_time = 0;
        end_time = 0;

        for attack in timeSeries:
            current_time = attack
            if current_time < end_time:
                total_damage -= (end_time - current_time)
            total_damage += duration
            end_time = current_time + duration
        return total_damage