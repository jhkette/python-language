nums =[1,2,3]
doubles = map(lambda x: x*2, nums)

x = list(doubles)

print(x)

# just maps through a list - very similar to map in javascript
# need to use list method to turn it into a list


def decrement_list(nums):
    return list(map(lambda x: x-1, nums))