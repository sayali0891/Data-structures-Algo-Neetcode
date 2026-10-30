#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1 : 
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2 : 
# Input: nums = [1, 2, 3, 4]
# Output: false


def check_duplicates_hashing(nums : list[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False

# The javascript equivalent : 
def check_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return "Number found is : " + str(arr[i])
                
    return "Number not found"

# --- Testing the function ---
if __name__ == '__main__':
    test_array = [1, 2, 3, 3, 5]
    print(check_duplicates(test_array))
    # Output: Number found is : 3
    print(check_duplicates_hashing(test_array))
