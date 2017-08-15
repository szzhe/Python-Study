#encodong:utf-8

nums = [6,11,7,9,4,2,1]
for x in range(len(nums)):
    for y in range(len(nums)-1):
        if nums[y] > nums[y+1]:
            temp = nums[y]
            nums[y] = nums[y+1]
            nums[y+1] = temp
        # print(nums)
print(nums)