class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: count how many times each number appears
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        # Step 2: turn the dictionary into a list of [count, number] pairs
        pairs = []
        for number in count_dict:
            count = count_dict[number]
            pairs.append([count, number])
        
        # Step 3: sort the pairs - since count is first, normal sort works
        pairs.sort(reverse=True)
        
        # Step 4: take the top k numbers
        output = []
        for i in range(k):
            output.append(pairs[i][1])
        
        return output