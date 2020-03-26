# PizzPazz
# Print numbers 1 - 100
# BUT:
#   - If number divisible by 3, print Pizz instead.
#   - If number divisible by 5, print Pazz instead.
#   - If number divisible by 3 & 5, print PizzPazz.
# See https://github.com/Static-Void-Academy/Module0-Challenges/blob/master/M0_C3.md

# Iterate through nums 1-100
for x in range(1, 101):
	# Only executes one of the following branches
	if x % 3 == 0 and x % 5 == 0:
		print("PizzPazz")
	elif x % 3 == 0: # Divisible by 3
		print("Pizz")
	elif x % 5 == 0: # Divisible by 5
		print("Pazz")
	else:
		print(x)
