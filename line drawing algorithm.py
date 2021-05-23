import matplotlib.pyplot as plt


def plot(id=None, xlabel='x-axis', ylabel='y-axis', title="", groups=[('plot',{'x':[0,], 'y':[0,], 'label':"Test"}),]):
	plt.figure(id)

	plt.grid(b=True, which='major', color='#666666', linestyle='-')
	plt.minorticks_on()
	plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

	plt.xlabel(xlabel) 
	plt.ylabel(ylabel) 
	plt.title(title)
	min_ = 0
	max_ = 0

	has_legend = False

	for group in groups:
		x = group[1]['x']
		y = group[1]['y']

		if group[1].get('label', None):
			has_legend = True

		del(group[1]['x']) # now they don't
		del(group[1]['y']) # fuck the **param

		if group[0] == 'plot':
			plt.plot(x, y, **group[1])
		elif group[0] == 'scatter':
			plt.scatter(x, y, **group[1])

		min_ = min([min_, *x, *y])
		max_ = max([max_, *x, *y])

	max_ += 10

	plt.xlim(min_, max_)
	plt.ylim(min_, max_)

	if has_legend:
		plt.legend()


def dda(x1, y1, x2, y2):
	print(f"Q: Find co-ordinates to plot to obtain a line ({x1},{y1}) - ({x2},{y2}) using DDA(Digital Difference Analyser) line drawing algorithm.")
	print(f"\n\nA:\nGiven line:\t({x1},{y1}) ----------------------------- ({x2},{y2})")

	dx = x2-x1
	dy = y2-y1

	step = abs(dy) if dy>dx else abs(dx)

	print("\n\nDifferences(distance) between the points individually on x and y axis. (dx, dy):")
	print(f"\tdx = x2-x1\n\tdx = {x2}-{x1}\n\tdx = {dx}")
	print(f"\n\tdy = y2-y1\n\tdy = {y2}-{y1}\n\tdy = {dy}")
	print("\n\nStep is calculated as largest vale among absolute dx and absolute dy:")
	print(f"\tstep = {step}")

	xinc = dx/step
	yinc = dy/step

	print("\n\nIncrement on each step for individual axis. (xinc, yinc):")
	print(f"\txinc = dx/step\n\txinc = {dx}/{step}\n\txinc = {xinc}")
	print(f"\n\tyinc = dy/step\n\tyinc = {dy}/{step}\n\tyinc = {yinc}")

	header = "\n\n\ti\t\tx-float\t\ty-float\t\tx-round\t\ty-round"
	header += "\n\t" + "-"*len(header)
	print(header)

	print(f"\n\t0\t\t{x1}\t\t{y1}\t\t{int(x1)}\t\t{int(y1)}")

	i, x ,y = 1, x1, y1
	xflist = [x,]
	yflist = [y,]
	xrlist = [x,]
	yrlist = [y,]
	while True:
		x = x + xinc
		y = y + yinc
		xflist.append(x)
		yflist.append(y)
		xrlist.append(round(x))
		yrlist.append(round(y))
		print(f"\t{i}\t\t{x}\t\t{y}\t\t{round(x)}\t\t{rounds(y)}")
		i += 1
		step -= 1

		if step == 0:
			break

	print("\n\n\t\t So we obtained coordinates to plot to archieve the given line.")

	return xflist, yflist, xrlist, yrlist


def bla(x1, y1, x2, y2):
	print(f"Q: Find co-ordinates to plot to obtain a line ({x1},{y1}) - ({x2},{y2}) using BLA(Bresenham's line algorithm).")
	print(f"\n\nA:\nGiven line:\t({x1},{y1}) ----------------------------- ({x2},{y2})")

	dx = x2-x1
	dy = y2-y1
	p = 2*dy-dx

	print("\n\nDifferences(distance) between the points individually on x and y axis. (dx, dy):")
	print(f"\tdx = x2-x1\n\tdx = {x2}-{x1}\n\tdx = {dx}")
	print(f"\n\tdy = y2-y1\n\tdy = {y2}-{y1}\n\tdy = {dy}")
	text = "\n\nSince "
	if dy>dx:
		text += "dy>dx, "
	elif dy==dx:
		text += "dy=dx, "
	else:
		text += "dx>dy, "

	text += "Initial decision parameter(p0) is calculated as "
	if dy<dx:
		text += "(2dy-dx):"
	else:
		text += "(2dx-dy):"

	if dy<dx:
		text += f"\n\tp0 = 2dy-dx\n\tp0 = 2*{dy}-{dx}\n\tp0 = {2*dy}-{dx}"
	else:
		text += f"\n\tp0 = 2dx-dy\n\tp0 = 2*{dx}-{dy}\n\tp0 = {2*dx}-{dy}"

	text += f"\n\tp={p}"

	print(text)

	text = "\n\n\tk\t\tp\t\t\t\t\t\tx\t\ty\t\tcondition"
	text += "\n\t" + "-"*len(text)*5
	print(text)

	print(f"\n\t0\t\t{p}\t\t\t\t\t\t{x1}\t\t{y1}\t\tinitial")

	k, x ,y = 1, x1, y1
	xlist = [x,]
	ylist = [y,]
	while True:
		if p<0:
			if dy<dx:
				p = p+2*dy
				x = x+1
				print(f'\t{k}\t\tp{k}=p{k-1}+2dy={p-2*dy}+2*{dy}={p}\t\t\t\t\t\t{x}\t\t{y}\t\tp{k-1}<0')
			else:
				p = p+2*dx
				y = y+1
				print(f'\t{k}\t\tp{k}=p{k-1}+2dx={p-2*dx}+2*{dx}={p}\t\t\t\t\t\t{x}\t\t{y}\t\tp{k-1}<0')
			xlist.append(x)
			ylist.append(y)
		else:
			if dy<dx:
				p = p+2*dy-2*dx
				ptext = f"p{k}=p{k-1}+2dy-2dx={p-2*dy+2*dx}+2*{dy}-2*{dx}={p}"
			else:
				p = p+2*dx-2*dy
				ptext = f"p{k}=p{k-1}+2dx-2dy={p-2*dx+2*dy}+2*{dx}-2*{dy}={p}"
			x = x+1
			y = y+1
			xlist.append(x)
			ylist.append(y)
			print(f'\t{k}\t\t{ptext}\t\t\t\t\t\t{x}\t\t{y}\t\tp{k-1}>=0')

		if dy<dx:
			if k == abs(dx):
				break
		else:
			if k == abs(dy):
				break

		k += 1

	print("\n\n\t\t So we obtained coordinates to plot to archieve the given line.")

	return xlist, ylist


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

data = dda(x1, y1, x2, y2)
plot(1, title='Line Drawing algo!', groups=[('scatter', {'x':data[0], 'y': data[1], 'label':"Float", 'marker': '.'}),('scatter', {'x':data[2], 'y': data[3], 'label':"Int", 'marker': '.'}),])
plot(2, title='Line Drawing algo!', groups=[('plot', {'x':data[0], 'y': data[1], 'label':"Float"}),('plot', {'x':data[2], 'y': data[3], 'label':"Int"}),])

data = bla(x1, y1, x2, y2)
plot(3, title='Line Drawing algo!', groups=[('scatter', {'x':data[0], 'y': data[1],}),])
plot(4, title='Line Drawing algo!', groups=[('plot', {'x':data[0], 'y': data[1],}),])

plt.show()
