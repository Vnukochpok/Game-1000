def m_strit(arr):
    arr.sort()
    sec_arr = [1, 2, 3, 4, 5]

    if arr == sec_arr:
        return [125, 0]
    else:
        return [0, 5]


def b_strit(arr):
    arr.sort()
    sec_arr = [2, 3, 4, 5, 6]

    if arr == sec_arr:
        return [250, 0]
    else:
        return [0, 5]


def triple(arr):
    current_arr = list(arr)
    setted_arr = set(current_arr)

    for i in setted_arr:
        if current_arr.count(i) == 3:

            points = 0

            if i == 1:
                points = 100
            elif i == 2:
                points = 20
            elif i == 3:
                points = 30
            elif i == 4:
                points = 40
            elif i == 5:
                points = 50
            elif i == 6:
                points = 60

            new_arr = []
            removed_count = 0

            for item in current_arr:
                if item == i and removed_count < 3:
                    removed_count += 1
                else:
                    new_arr.append(item)

            return [points, classic(new_arr)]

    return [0, 5]


def fourle(arr):
    current_arr = list(arr)
    setted_arr = set(current_arr)

    for i in setted_arr:
        if current_arr.count(i) == 4:

            points = 0

            if i == 1:
                points = 200
            elif i == 2:
                points = 40
            elif i == 3:
                points = 60
            elif i == 4:
                points = 80
            elif i == 5:
                points = 100
            elif i == 6:
                points = 120

            new_arr = []
            removed_count = 0

            for item in current_arr:
                if item == i and removed_count < 4:
                    removed_count += 1
                else:
                    new_arr.append(item)

            return [points, classic(new_arr)]

    return [0, 5]


def fivele(arr):
    setted_arr = set(arr)
    for i in setted_arr:
        if i == 1 and arr.count(i) == 5:
            return [1000, 0]
        elif i == 2 and arr.count(i) == 5:
            return [200, 0]
        elif i == 3 and arr.count(i) == 5:
            return [300, 0]
        elif i == 4 and arr.count(i) == 5:
            return [400, 0]
        elif i == 5 and arr.count(i) == 5:
            return [500, 0]
        elif i == 6 and arr.count(i) == 5:
            return [600, 0]
    return [0, 5]


def classic(arr):
    score = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            score += 10
        elif arr[i] == 5:
            score += 5
        else:
            pass

    target_digits = {2, 3, 4, 6}
    reroll_dice = 0
    for item in arr:
        if item in target_digits:
            reroll_dice += 1
    return [score, reroll_dice]
