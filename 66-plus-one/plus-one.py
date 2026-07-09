class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_str = ""
        for d in digits:
            number_str = number_str + str(d)
        number = int(number_str)
        
        number = number + 1
  
        number_str = str(number)
        result = []
        for ch in number_str:
            result.append(int(ch))
        
        return result