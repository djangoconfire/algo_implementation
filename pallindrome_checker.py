from deque import *

def pallindrome_checker(string):
    pallindrome_deque=Deque()

    for char in str(string):
        pallindrome_deque.addRear(char)

    equal=True

    while pallindrome_deque.size() > 1 and equal:
        front=pallindrome_deque.removeFront()
        rear=pallindrome_deque.removeRear()

        if front != rear:
            equal=False

    return equal


print pallindrome_checker('SAAS')
