class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        Return True if the the total amount of candies the kid has is bigger 
        than everyone else in the list after the adding extraCandies
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        list = []
        i = 0
        max = candies[0]
        for i in range(0, len(candies), 1):
            if (candies[i] > max):
                max = candies[i]
                break
        index = 0
        while(index < len(candies)):
            if (candies[index] + extraCandies >= max):
                list.append(True)
            else:
                list.append(False)
            index += 1
        return list
