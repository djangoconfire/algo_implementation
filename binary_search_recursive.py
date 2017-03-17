def binary_search(list,item):
    print list
    print '@@@@@@@@@@@@@@'
    # base condition
    if len(list)==0:
        return False
    else:
        midpoint=len(list)//2
        print midpoint
        print '##############'
        if list[midpoint]==item:
            return True
        else:
            if item<list[midpoint]:
                return binary_search(list[:midpoint],item)
            else:
                return binary_search(list[midpoint+1:],item)


array=[2,4,12,14,48,89]
b=binary_search(array,48)

print b

