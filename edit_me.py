#finished quality content
def find_max(lst):


    current_max = lst[0]
    #lists the max

    for i in range(1, len(lst)):
        if lst[i] > current_max:
            current_max = lst[i]

    return current_max
    #returns the max

test_list = [2112*i % 2024 for i in range(10000)]

print(find_max(test_list))
