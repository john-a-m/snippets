def bubble_sort(nums):
    for passnum in range(len(nums) - 1, 0, -1):
        for i in range(passnum):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

if __name__ == "__main__":
    
    nums = [54,26,93,17,77,31,44,55,20]
    bubble_sort(nums)
    print nums
