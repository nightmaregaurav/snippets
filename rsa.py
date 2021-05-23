import sympy


def gcd(a,b):
	while a != b:
		if a>b:
			a -= b
		else:
			b -= a
	return a


flag = True
while flag:
	p = int(input('P: '))
	if not sympy.isprime(p):
		print("P is not prime, Try again...")
	else:
		flag = False
flag = True
while flag:
	q = int(input('Q: '))
	if not sympy.isprime(q):
		print("Q is not prime, Try again...")
	elif q == p:
		print("Q & P cannot be same, Try again...")
	else:
		flag = False

n = p*q
pi = (p-1)*(q-1)

print(f'n = {n}')
print(f'pi(n) = {pi}')

while True:
	e = int(input('e: '))
	if e <= 1 or e >= pi:
		print("1<e<pi(n) did not satisfied, Try again...")
	elif gcd(e, q) != 1:
		print(f"e and pi(n) have common divisor: {gcd(e, q)}. Not a co-prime, Try again...")
	else:
		break

for i in range(1,10): 
	x = 1 + i*pi 
	if x % e == 0: 
		d = int(x/e) 
		break

print(f'd = {d}')