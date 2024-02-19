class Solution:
    def minimumSteps(self, s: str) -> int:
        size = len(s)
        binary = list(s)
        start = 0
        end = size-1
        counter = 0
        while start < end:
            if binary[start]=="1" and binary[end]=="0":
                binary[start], binary[end]= binary[end], binary[start]
                
                counter += (end-start)
                start += 1
                end -= 1
            elif binary[start] == "1" and  binary[end] == "1":
                end -= 1
            elif binary[start]=="0" and binary[end]=="0":
                start += 1
            else:
                start += 1
                end -= 1
        return counter

            

                