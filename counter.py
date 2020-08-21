test_str =  input("enter a word ")

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print ("Count of all characters in INPUT is :\n "
                                        +  str(all_freq))
