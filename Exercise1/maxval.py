def maxval(some_list):
    max_val = None
    for val in some_list:
        if val > max_val:
            max_val = val
            return max_val

def onebelowmin(some_list, minval):
    belowmin = False
    for val in some_list:
        if val < minval:
            belowmin = True
    return belowmin

def allbelowmin(some_list, minval):
    belowmin = True
    for val in some_list:
        if val > minval:
            belowmin = False
    return belowmin

print allbelowmin([1,5,3,4], 6)
print allbelowmin([5,3,7,5], 6)

print onebelowmin([7,8,7,9], 6)
print onebelowmin([7,2,5,8], 6)
