class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        0 represents empty pot, 1 represents planted pot, flower cannot be planted in adjacent positions.
        Returns true if can plant n or more flowers in the row of pot, false if not
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        plantable = 0
        index = 0

        while index < len(flowerbed):

            if flowerbed[index] == 0:
                prev = flowerbed[index - 1] if index > 0 else 0
                next = flowerbed[index +
                                 1] if index < len(flowerbed) - 1 else 0
                if prev == 0 and next == 0:
                    flowerbed[index] = 1
                    plantable += 1
                    if plantable >= n:
                        return True
                    index += 1
            index += 1
        return plantable >= n
