#  Dictionary basically objects hi hai thats it, bas ek cheez hai yaha pe keys humesha " " andar rahega agar string hai toh
dict={

    "key1":"value1",
    "key1":"value2",  # aise agar same key baar baar dalenge toh it wont work it will consider one key val pair only
    2.87:"value with float key",
    (1,2):"value with tuple key"
}
print(dict)

print(dict[2.87])
print(dict[(1,2)])
# adding a key val pair in dict
dict[9.99]="new value added with float key"
print(dict)

# ------------------------------------------------------------------------------------------------------------------

