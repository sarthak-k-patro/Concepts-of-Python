#  Dictionary basically objects hi hai thats it, bas ek cheez hai yaha pe keys humesha " " andar rahega agar string hai toh
dict={

    "key1":"value1",
    "key1":"value2",  # aise agar same key baar baar dalenge toh it wont work it will consider one key val pair only
    2.87:{

    1:"value with float key",
    "sarthak":True
    },
    (1,2):"value with tuple key"
}
print(dict)

print(dict[2.87])
print(dict[(1,2)])
# adding a key val pair in dict
dict[9.99]="new value added with float key"
print(dict)
# print(dict[2.87]["sarthak"])
if(dict[2.87]["sarthak"]==True):
    print("exist karta hai ")

print(dict.get(9.999)) # get value of a particular key
print(dict.keys()) # get value of all keys
print(type(dict.keys())) 
print(dict.values()) # get value of all values
print(type(dict.values())) 

print(dict.pop(9.99)) # deletes a particular key-value pair expects a key in function
print(dict)


# ------------------------------------------------------------------------------------------------------------------