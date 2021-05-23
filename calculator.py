from math import sqrt
def is_prime(x):
	if x <=1:
		return False
	if x <= 3:
		return True
	for i in range(2, int(sqrt(x))+1):
		if x%i == 0:
			return False
	return True

def prime_factors(x):
	while x%2 == 0:
		yield(2)
		x = x/2
	if is_prime(x):
		yield(int(x))
	else:
		for i in range(3, int(sqrt(x))+1, 2):
			if x < i:
				break
			if not is_prime(i):
				continue
			while x%i == 0:
				yield(int(i))
				x = x/i
		if x != 1:
			yield(int(x))

def fractionalise(x):
	decimal_place = len(str(x)) - str(x).index('.') - 1
	lower = 10**decimal_place
	upper = int(x*lower)
	upper = list(prime_factors(upper))
	lower = list(prime_factors(lower))
	tem = upper.copy()
	for i in range(len(upper)):
		if tem[i] in lower:
			upper.remove(tem[i])
			lower.remove(tem[i])
	if len(upper) == 0:
		upper = [1,]
	if len(lower) == 0:
		lower = [1,]
	ans = list()
	u = 1
	for nums in upper:
		u = u*nums
	l = 1 
	for nums in lower:
		l = l*nums
	upper = u
	lower = l
	if lower ==1:
		ans.append(upper)
	elif upper>lower:
		ans.append(upper//lower)
		ans.append(upper%lower)
		ans.append(lower)
	else:
		ans.append(upper)
		ans.append(lower)
	return(ans)

def evaluate_num(exp):
	pass

def evaluate(exp, key_value):
	pass
