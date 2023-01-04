n, s = list(map(int, input().split()))

input_nums = list(map(int, input().split()))
input_nums.sort()
count = 0


def getSequence(idx, _sum):
    global count
    if idx >= n:
        return

    _sum += input_nums[idx]

    if _sum == s:
        count += 1
    
    getSequence(idx + 1, _sum)
    getSequence(idx + 1, _sum - input_nums[idx])
    

getSequence(0, 0)
print(count)
