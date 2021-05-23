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