# You are given three inputs: a string, one letter, and a second letter.

# Write a function that returns `True` if every instance of the first letter
# occurs before every instance of the second letter.

# Look at the String Methods to possibly help you find some methods that can
# make this easier.
# https://docs.python.org/3.9/library/stdtypes.html?highlight=strings#string-methods

# Write your function here.
def first_before_second(str,a,b):
    # #complicated method
    # #do 2 loops to identy the last position of a and b
    # position_a=-1
    # position_b=-1

    # i=0
    # while i< len(str):
    #     if str[i]==a:
    #         position_a=i
    #     i+=1

    # j=0
    # while j<len(str):
    #     if str[j]==b:
    #         position_b=j
    #         break
    #     j+=1

    # return position_a<position_b

    # simple method

    return str.rfind(a) < str.find(b)

print(first_before_second("a rabbit jumps joyfully", "a", "j"))
#> True
# Every instance of "a" occurs before every instance of "j".

print(first_before_second("knaves knew about waterfalls", "k", "w"))
#> True

print(first_before_second("happy birthday", "a", "y"))
#> False
# The "a" in "birthday" occurs after the "y" in "happy".

print(first_before_second("precarious kangaroos", "k", "a"))
#> False

