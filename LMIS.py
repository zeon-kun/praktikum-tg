def length_of_lis(nums):
    n = len(nums)

    if n == 0:
        return 0

    lis_ends = [nums[0]]

    for num in nums[1:]:
        if num > lis_ends[-1]:
            lis_ends.append(num)
        else:
            low, high = 0, len(lis_ends) - 1
            while low < high:
                mid = low + (high - low) // 2
                if lis_ends[mid] < num:
                    low = mid + 1
                else:
                    high = mid

            lis_ends[low] = num
            print("List: {}".format(lis_ends))
    return len(lis_ends)

if __name__ == "__main__":
    nums = [4, 1, 13, 7, 0, 2, 8, 11, 3]

    print("Length of LIS is", length_of_lis(nums))
