import sys
input = sys.stdin.readline

stair_num = int(input())
nums = [0] * 101
nums[1] = 9
def stairs(num):
    nums[num] = (nums[num-1]-1) * 2 + 1
    return nums[num]

print(stairs(stair_num))