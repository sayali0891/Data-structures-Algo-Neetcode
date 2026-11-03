items = ["apple", "banana", "cherry"]


for i in range(len(items)):
    print(i, items[i])


for item in items:
    print(item)

for i, item in enumerate(items):
    print(i, item)

# By adding start=1, the 'index' variable begins at 1 instead of 0
for index, item in enumerate(items, start=1):
    print(f"Items {index}: {item}")          # Displays all 3 items only index is displayed at 1. 
#The loop still safely visits every single item in the list from the beginning, but your print statement looks natural to a human reader.


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(name, score)


user = {"name": "Alex", "role": "Developer", "language": "Python"}
for key, value in user.items():
    print(key, "->", value)


# Following creates an error : 
# user = [
#     {"name": "Alex", "role": "Developer", "language": "Python"},
#     {"name": "Sayali", "role": "Developer", "language": "Javascript"}
# ]
# for key, value in user.items():
#     print(key, "->", value)

users = [
    {"name": "Alex", "role": "Developer", "language": "Python"},
    {"name": "Sayali", "role": "Developer", "language": "Javascript"}
]


for user_dict in users:
    print(f"--- Timeline Entry for {user_dict['name']} ---")

    for key, value in user_dict.items():
        print(f"{key} -> {value}")


for user in users:
    # Pluck out exactly what you need
    name = user["name"]
    lang = user["language"]
    
    print(f"{name} writes code in {lang}.")



# Use .get() to Prevent Crashes
for user in users:
    # If "language" doesn't exist, it defaults to "Unknown" instead of crashing
    lang = user.get("language", "Unknown") 
    print(f"{user['name']} speaks {lang}")



# for-else block : 
users = ["Alex", "Sayali", "Bob"]
search_target = "Charlie"

for user in users:
    if user == search_target:
        print("Found them!")
        break  # Triggers if we find the target, skips the else block entirely
else:
    # This ONLY runs if the loop finished looking at EVERYONE and never hit a 'break'
    print("Search complete: Target user was not found in the list.")



# In Python, you do not need a for loop to check if an item exists or to find its position inside a list.
# If you simply want to know if the item exists in the list, use the in keyword
users = ["Alex", "Sayali", "Bob"]
search_target = "Charlie"

# No loop required! Python checks the list instantly.
if search_target in users:
    print("Found them!")
else:
    print("Search complete: Target user was not found.")



# If you want the index/position of where it was found : 
if search_target in users:
    # Directly gives you the index without a loop
    position = users.index(search_target)
    print(f"Found {search_target} at index {position}!") 
    # Output: Found Sayali at index 1!
else:
    print("Not found.")



################    QUIZ    ####################

arr = [0, 1, 2, 3, 4, 5]
print(arr[1:5:2])               # [1,3]  
#   [start:stop:step]


colors = ['red', 'green', 'blue']
res = list(enumerate(colors, start=10))
print(res[0])


nums = [10, 20, 30, 20, 40]
try:
    print(nums.index(20, 2, 5))
except ValueError:
    print("Not found")
# .index(val, start, stop) searches within the slice nums[2:5] ([30, 20, 40]), finds 20 there, and returns its index relative to the entire list (3).


users = [{'name': 'Alice', 'role': 'admin'}, {'name': 'Bob', 'role': 'user'}]
names = [u.get('name', 'Guest') for u in users]
print(names)






