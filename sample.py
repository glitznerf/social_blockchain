from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.Neo.TriggerType import Application,Verification

# Check whether invoker is allowed to perform operation
def security_check():
    owner = Get(ctx, name)
    if owner is None:
        return False
    if not CheckWitness(owner):
        return False

# Contract: Pay at Shop
def Main(operation, addr, value):
	# Get trigger to determine interaction
	trigger = GetTrigger()

	# Used to spend assets on behalf of contract's address
	if trigger == Verification():
	
		if CheckWitness(OWNER):
			return True
	
		return False
	
	# Main body of Smart Contract
	elif trigger == Application():
		
		ctx = GetContext()

		if operation == 'balance':
			return Get(ctx, addr)

		elif operation == 'add':
			assert security_check()==True
		        balance = Get(ctx, addr)
	        	new_balance = balance + value
	        	Put(ctx, addr, new_balance)
	       		return new_balance

    		elif operation == 'remove':
			assert security_check()
			balance = Get(ctx, addr)
			Put(ctx, addr, balance - value)
			return balance - value

		elif operation == 'totalSupply':
			return totalSupply()

		return 'unknown operation'
