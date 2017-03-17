def binary_search(list,item):
    low=0
    high=len(list)-1
    found=False

    while low<=high and not found:
        midpoint=(low+high)//2
        print midpoint
        print '###############'
        if list[midpoint]==item:
            found=True
        else:
            if item > list[midpoint]:
                low = midpoint + 1
            else:
                high = midpoint - 1

    return found


array=[2,4,6,1,45,6]
b=binary_search(array,45)

print b