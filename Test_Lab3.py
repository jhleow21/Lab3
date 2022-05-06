import Lab3

print("Test_Lab3")

def req01():
    result=[]
    order = Lab3.SORT_DESCENDING
    input_arr = [64,34,25,12,22,11,90,88,99,100]
    test_arr = [11,22,33,44,55,66,77,88,99,100]
    result = Lab3.bubble_sort(input_arr,order)
    result.append(10)
    assert (result == test_arr)

def req02():
    result=[]
    input_arr = [64,34,25,12,22,11,90,88,99,100,111]
    result = Lab3.bubble_sort(input_arr,2)
    assert(result==1)

def req03():
    result=[]
    input_arr = [64,34,25,12,22,11,90,88]
    result = Lab3.bubble_sort(input_arr,2)
    assert(result==2)

def req04():
    result=[]
    input_arr = []
    result = Lab3.bubble_sort(input_arr,2)
    assert(result==0)


