#Dictionaries Used to store data that are key value pairs
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access Items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify key exists
print("guitar" in band)
print("triangle" in band)

# change values 
band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

#Delete and Clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#copy dictionaires

"""band2 = band #creates reference
print("bad copy")
print(band2)
print(band)##
band2["drums"] = "Dave"
print(band) """

band2=band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

#or use dict() constructor function

band3=dict(band)
print("Good copy!")
print(band3)

# Nested Dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2

}


#Sets

nums = {1,2,3,4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#No duplicates allowed in sets

nums = {1,2,2,3}
print(nums)

#True is a dupe of 1, false is dupe of 0
nums = {1,True,2,False,3,4, 0}
print(nums)

#check if value is in a set

print(2 in nums)

#but you cant refer to element in set with an index position or a key
nums.add(8)
print(nums)

#Add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with lists,tuples, and dictionaries

#merge two sets to create new set

one = {1,2,3}
two = {4,5,6}

mynewset= one.union(two)
print(mynewset)

# keep only the duplicates
one = {1,2,3}
two = {4,5,3}

one.intersection_update(two)
print(one)

#keep everything except the duplicates
one = {1,2,3}
two = {4,5,3}
one.symmetric_difference_update(two)
print(one)