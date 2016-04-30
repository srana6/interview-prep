"""

Incomplete

"""

def recursive_hanoi(disks, stack_from, stack_to, stack_aux):
	if not disks and stack_to:
		return True

	if stack_from and stack_from[-1] < stack_to:
		return recursive_hanoi(disks - 1, stack_from[:-2], stack_to.push)
