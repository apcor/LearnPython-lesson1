inp_list1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
inp_list2 = [[1, 4], [4, 5]]
inp_list3 = [[6, 8], [1, 9], [2, 4], [4, 7]]
inp_list4 = [[1,4],[5,6]]
inp_list5 = [[1,4], [4,5], [6,7]]
inp_list6 = [[1,4],[0,2],[3,5]]

def mergelists(intervals):
    # sort the input list elements by the 1st value of each
    intervals.sort(key = lambda x: x[0])
    # prepare an empty list for our result
    res_list = []
    # looping over each element in the list of intervals
    for el in intervals:
        # if res_list returns False if res_list is empty
        # If the next interval starts before the previous ends,
        # we merge them in the result_list
        if res_list and el[0] <= res_list[-1][1]:
            res_list[-1][1] = max(res_list[-1][1], el[1])
        else:
            res_list += [el]
    return res_list           

#print(inp_list1)
#print(mergelists(inp_list1))

#print(mergelists(inp_list2))
#print(mergelists(inp_list3))

#print(inp_list4)
#print(mergelists(inp_list4))

#print(inp_list5)
#print(mergelists(inp_list5))

print(inp_list6)
print(mergelists(inp_list6))