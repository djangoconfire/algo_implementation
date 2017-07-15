text= "she sells sea shells on the sea shore"
pattern="shells"


def string_match(text,pattern):
    n=len(text)
    m=len(pattern)
    for i in range(0,(n-m)):
        j=0
        while j<m and pattern[j] == text[i+j]:
            j = j + 1

        if j == m :
            return i

    return -1


if __name__=='__main__':
    index=string_match(text,pattern)
    print 'string match at index {}'.format(index)
