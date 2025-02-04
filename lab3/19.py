# Function 1     Task 8

def spy_game(nums):
    kernel = []
    for i in range(len(nums)):
        if nums[i] == 0 or nums[i] == 7:
            kernel.append(nums[i])
    far = ""
    for i in range(len(kernel)):
        far = far + str(kernel[i])
        if far == '007':
            return True
    return False

Thislist = list(map(int, input().split()))
print(spy_game(Thislist))