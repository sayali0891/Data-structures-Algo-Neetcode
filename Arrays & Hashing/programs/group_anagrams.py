'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example : 
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''


'''
You should use defaultdict when you expect to access or update keys that don't exist yet.
A standard Python dict throws a KeyError if you try to modify or access a missing key. defaultdict (imported from the collections module) automatically initializes any missing key with a default value of your choice.
'''
from collections import defaultdict

def group_anagrams(list_arr: list[str]) -> list[list[str]]:
    hashMap = defaultdict(list)
    for word in list_arr:
        count_list = [0] * 26
        for char in word:
            count_list[ord(char) - ord('a')] += 1
            # print(f"char : {char} : {count_list}")
        key = tuple(count_list)                 # because key needs to be immutable hence we converted it into a tuple
        hashMap[key].append(word)
        print(hashMap)

    return hashMap.values()


if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    print(group_anagrams(strs))