class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShipInDays(capacity):
            total = 0
            day_count = 1
            for weight in weights:
                if total + weight > capacity:
                    day_count += 1
                    total = weight
                    if day_count > days:
                        return False
                else:
                    total += weight
            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if canShipInDays(mid):
                right = mid
            else:
                left = mid + 1

        return left
