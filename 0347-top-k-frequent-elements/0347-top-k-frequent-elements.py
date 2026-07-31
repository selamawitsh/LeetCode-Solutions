class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict={}
        for num in nums:
            if num in count_dict:
                count_dict[num]+=1
            else:
                count_dict[num]=1
        
        pairs=[]
        for num in count_dict:
            count=count_dict[num]
            pairs.append([count,num])

        pairs.sort(reverse=True)

        output=[]
        for i in range(k):
            output.append(pairs[i][1])
        return output
