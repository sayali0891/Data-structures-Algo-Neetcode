def hashing_two_map(nums, target):
    prevMap = {}    # value : index

    for i, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[num] = i

    return None


if __name__ == "__main__": 
    print(hashing_two_map([3,4,5,6], 9))