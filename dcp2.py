#This problem was asked by Uber.

#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Follow-up: what if you can't use division?

# First use division approach

def dcp2_wDiv(num_array):
    product = 1
    for num in num_array:
        product = product * num
    for i in range(len(num_array)):
        num_array[i] = product / num_array[i]

    return num_array

#print(dcp2_wDiv([1,2,3,4,5]))

# Now, if you cant divide?
def dcp2_woDiv(num_array):

    # exclusively multiply everything
    count = 0
    new_num_array = []
    for i in range(len(num_array)):
        product = 1
        print "\n\ni = " + str(i)
        for j in range(0,i): #nums before current num
            print "product =" + str(product) + "*" + str(num_array[j])
            product = product * num_array[j]
            count += 1
        for k in range(i+1, len(num_array)):
            print "product =" + str(product) + "*" + str(num_array[k])
            product = product * num_array[k]
            count += 1
        print "product = " + str(product)
        new_num_array.append(product)
    print("Count =", count)

    return new_num_array

#print(dcp2_woDiv([1,2,3,4,5]))

def newdcp2(num_array):
    temp = 1

    products = [None] * len(num_array)
    for j in range(0, len(num_array)):
        products[j] = 1;

    for i in range(0,len(num_array)):
        products[i] = temp
        temp = temp * num_array[i]

    # init temp to one for product on right side
    for i in range(len(num_array) - 1, -1,-1):
        products[i] = products[i] * temp
        temp = temp * num_array[i]

    return products

#print(newdcp2([1,2,3,4,5])

