# class ATM:
#     def __init__(self):
#         self.notes = {
#             20: 0,
#             50: 0,
#             100: 0,
#             200: 0,
#             500: 0
#         }
#         self.standard = [20, 50, 100, 200, 500]
#         self.reference = {
#             20: 0, 
#             50: 1,
#             100: 2,
#             200: 3,
#             500: 4
#         }
    
#     def deposit(self, banknotesCount):
#         for i in range(5):
#             self.notes[self.standard[i]] = banknotesCount[i]
#     def withdraw(self, amount):
#         temp = amount
#         ans = {}
#         i = 4
#         while i >= 0 and amount > 0:
#             contains = amount // self.standard[i]
#             if contains > self.notes[self.standard[i]]:
#                 reduct = self.notes[self.standard[i]] * self.standard[i]
#                 amount -= reduct
#                 self.notes[self.standard[i]] = 0  
#             else:
#                 reduct = contains * self.standard[i]
#                 amount -= reduct
#                 self.notes[self.standard[i]] -= contains  
            
#             ans[self.standard[i]] = reduct // self.standard[i]
#             i -= 1

#         if amount == 0:
#             temp = [0] * 5
#             for key in ans:
#                 temp[self.reference[key]] = ans[key]
#             return temp

#         back_to_dic = temp - amount
#         idx = 4
#         while back_to_dic > 0 and idx >= 0:
#             contains = back_to_dic // self.standard[idx]
#             self.notes[self.standard[idx]] += contains
#             back_to_dic -= contains * self.standard[idx] 
#             idx -= 1
#         return [-1]

class ATM:
    bank, val = [0] * 5, [20, 50, 100, 200, 500]
    
    def deposit(self, banknotesCount: List[int]) -> None:
        self.bank = [a + b for a, b in zip(self.bank, banknotesCount)]
    
    def withdraw(self, amount: int) -> List[int]:
        take = [0] * 5
        for i in range(4, -1, -1):
            take[i] = min(self.bank[i], amount // self.val[i])
            amount -= take[i] * self.val[i]
        if amount == 0:
            self.bank = [a - b for a, b in zip(self.bank, take)]
        return [-1] if amount else take