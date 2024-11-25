#Write a Python program to sort a list of dictionaries based on a specific key.

def sortListOfDicts(data, key):

    if not all(key in item for item in data):
        raise KeyError(f"Not all dictionaries have the key '{key}'.")

    return sorted(data, key=lambda x: x[key])

listOfDicts = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_list = sortListOfDicts(listOfDicts, "age")
print("Sorted list based on 'age':", sorted_list)

sorted_list = sortListOfDicts(listOfDicts, "name")
print("Sorted list based on 'name':", sorted_list)