#275
#medium

#Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in ascending order, return the researcher's h-index.

#According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

#You must write an algorithm that runs in logarithmic time.

 

#Example 1:

#Input: citations = [0,1,3,5,6]
#Output: 3
#Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
#Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.



#correct python3 solution (could not understand the question):

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = []
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c > i:
                res.append(c)
        return len(res)
