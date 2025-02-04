# Functions 1    Task 4

def filter_Prime(nums):
    cnt = 0
    if nums < 2:
        return False
    for i in range(2, nums - 1):
        if nums % i == 0:
            cnt += 1
    if cnt == 0:
        print(nums)

thislist = list(map(int, input().split()))

for i in thislist:
    filter_Prime(i)