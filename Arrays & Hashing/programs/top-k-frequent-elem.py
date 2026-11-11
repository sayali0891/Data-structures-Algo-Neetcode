'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Basically top 2 frequent elements in a list
'''
def top_k_freq_elems(nums: list[int], k: int) -> list[int]:
    hashMap = {}
    freq = [[] for i in range(len(nums) + 1)]
    print(freq)

    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1

    print(hashMap)

    for value, count in hashMap.items():
        freq[count].append(value)
    print(freq)            

    res = []
    for i in range(len(freq) - 1, 0, -1):
        print(freq[i])
        # if len(freq[i]) > 0:
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            
            

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(top_k_freq_elems(nums, k))

