
'''
2. Given two lists, produce a list of pairs of
 elements from both, e.g. , given
[1,2,3] and [7,8] the result should be a
 list: [[1,7], [1, 8], [2, 7], [2, 8], [3, 7], [3, 8]]
'''
lst1 = [1,2,3] 
lst2 = [7,8] 
result = []
# go through the fist list's elements
for item1 in lst1:
    #go through the second list's elements
    for item2 in lst2:
        #combine the elements and add to result list
        elem = [item1,item2]
        result.append(elem)
        print(result)
        


