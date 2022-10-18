car_parts = {
    "model": "Benz",
    "engineNo": "GHW123",
    "ChasisNo": "ert0987",
    "Owner": "Adetomiwa",
    "type": "automatic",
    "gear": "4wheelDrive",
    "ignition": "pushToStart"
}

print(car_parts)
print(car_parts.get("model")) #to get the value of a key
#print(car_parts.items()) #to turn it to a list of tuples
print(car_parts.keys()) #to return the keys in the dictionary
print(car_parts.values()) #to return the values in the dictionary
car_parts.pop("gear") #to remove a key from a dictionary
print(car_parts)
car_parts.update({"gear": "4wheelDrive", "color": "red"})
print(car_parts)
print(car_parts.popitem()) #to print out the last key in the dictionary, the original dictionary would not contain the key removed.
print(car_parts)