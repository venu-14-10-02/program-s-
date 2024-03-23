class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        stt = ''`
        arr=list(num_map.keys())
        for n in arr[::-1]:
            while n<=num:
                stt=stt+num_map[n]
                num=num-n
            if num==0:
                break
        return stt
sol=Solution()
print(sol.intToRoman(99))

