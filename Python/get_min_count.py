import math

def isSquare(num):
    if num > 0 and (math.sqrt(num)) % 1 == 0:
        return math.floor(math.sqrt(num))
    else:
        return False

def get_min_count(num):
    cur = num
    count = 0
    while cur > 1:
        sq = isSquare(cur)
        if sq:
            cur = sq
        else:
            cur = cur - 1
        count = count + 1
    return count

if __name__ == '__main__':
    print(get_min_count(625))  #5
    print(get_min_count(100))  #5
    print(get_min_count(14))   #8
