from stack import *

def dec_to_binary(decimal_number,base):
	digits='0123456789ABCDEF'
	remainder_stack=Stack()
	while decimal_number > 0:
		remainder=decimal_number % base
		remainder_stack.add(remainder)
		decimal_number=decimal_number // base

	new_string=""
	while not remainder_stack.is_empty():
		new_string=new_string + digits[remainder_stack.pop()]

	return new_string

print dec_to_binary(233,16)			

	


