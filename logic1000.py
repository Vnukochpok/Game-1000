import random


def throw(x):
    i = 1
    array = []
    while i <= x:
        kubik = random.randint(1, 6)
        array.append(kubik)
        i += 1
    return array


s = throw(5)
print(s)


class Combination():
    def m_strit(self, arr):
        arr.sort()
        sec_arr = [1,2,3,4,5]

        if arr == sec_arr:
            return "Combination: small street"
        else:
            return "No"

    def b_strit(self, arr):
        arr.sort()
        sec_arr = [2,3,4,5,6]

        if arr == sec_arr:
            return "Combination: big street"
        else:
            return "No"

    def double(self, arr):
        setted_arr = set(arr)
        for i in setted_arr:
            if arr.count(i) == 3:
                return f"{i} встречаются 3 раза"
            elif arr.count(i) == 4:
                return f"{i} встречаются 4 раза"
            elif arr.count(i) == 5:
                return f"{i} встречаются 5 раз"
        return f"No doubles"

    def classic(self, arr):
        score = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                score+=10
            elif arr[i] == 5:
                score+=5
            else:
                pass
        return score


p = Combination()
print(p.m_strit(s))
print(p.b_strit(s))
print(p.double(s))
print(p.classic(s))