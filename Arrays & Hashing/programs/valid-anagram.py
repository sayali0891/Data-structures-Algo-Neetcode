'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.
'''
from collections import Counter     #Specifically designed for counting objects(dict)

# Using hashing
def valid_anagram_hashing(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hashMapS, hashMapT = {}, {}
    for char in s:
        hashMapS[char] = 1 + hashMapS.get(char, 0)
        hashMapT[char] = 1 + hashMapT.get(char, 0)

    print(f"hashMaps : {hashMapS}")

    for key in hashMapS :
        if hashMapS[key] != hashMapT[key]:
            return False

    return True


def  valid_anagram_sorting(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)  

def  valid_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    str1 = "carrace"
    str2 = "racecar"
    print(valid_anagram_hashing(str1, str2))
    print(valid_anagram_sorting(str1, str2))
    print(valid_anagram_counter(str1, str2))