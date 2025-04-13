# # #  While Loop
# # count=1
# # while count<=5:
# #     print("count is :",count)
# #     count += 1

# #  Printing list elements using a loop
# # lisT=["sarthak","patro",1,7,8,900]
# lisT=("sarthak","patro",1,7,8,88,1,1,1,1,1,1,1,900)
# i=0
# while i<len(lisT):
#     print(lisT[i])
#     i=i+1


# # Break keyword is used to terminate the loop and loop se bahar aajayega
# # Continue current ITERATION ko terminate kar dega and neXT iteration pe switch kr dega  

# # ----------------------------------------------------------------------------------------------------------------------

# #  For Loop
LIst=[1,"Sarthak","is","enough","for","the whole world",9999999999999999999999999999999999999999]
# for element in LIst:
#     print(element)

#  Now lets read about range() function
# range() function is used to generate a sequence of numbers starting from 0 up to but not
# including the stop value. It is used to generate a sequence of numbers in a loop.
for i in range(2,101,2):  # range(satrt?,stop,step?) where ? means optional values , but stop is mandatory in range function
    print(i) # prints even numbers

# print(range(5))
