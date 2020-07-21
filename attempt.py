from boa.interop.Neo.Runtime import GetTrigger, CheckWitness
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.Neo.TriggerType import Application,Verification


"""
The government may deploy and own this contract.
Other nodes can sign up to specific groups, which would ideally (in the future) be cross checked.

Governments can then freely send funds to those groups with equal distribution.
"""

# Set government address as owner of contract
OWNER = b'\x03\x19\xe0)\xb9%\x85w\x90\xe4\x17\x85\xbe\x9c\xce\xc6\xca\xb1\x98\x96'


ctx = GetContext()

# Check whether invoker is allowed to perform operation
def security_check():
    owner = Get(ctx, name)
    if owner is None:
        return False
    if not CheckWitness(OWNER):
        return False

# Contract: Group Users and distribute funds
def Main(operation, addr, group="", value=0):

	groups = {
	"elderly": [],
	"disabled": []
	}

	# Get trigger to determine interaction
	trigger = GetTrigger()

	# address of node that calls contract
	caller = addr

	# Used to spend assets on behalf of contract's address
	if trigger == Verification():
	
		if CheckWitness(OWNER):
			return True
	
		return False
	
	# Main body of Smart Contract
	elif trigger == Application():
		

		if operation == 'balance':
			return Get(ctx, addr)

		elif operation == 'register':

			groups[group] = groups[group].append(addr)

		elif operation == 'add':
			assert security_check()==True
	        balance = Get(ctx, addr)
	        new_balance = balance + value
	        Put(ctx, addr, new_balance)
	        return new_balance

    	elif operation == 'subtract':
			assert security_check()==True
	        balance = Get(ctx, addr)
	        Put(ctx, addr, balance - value)
	        return balance - value

		elif operation == 'totalSupply':
			return totalSupply()

		return 'unknown operation'
