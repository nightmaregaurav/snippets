import os

file_list = list(os.scandir(os.path.abspath(r'macs')))
outfile = open('mac_out.txt', 'w')
outText = '{\n'
for file in file_list:
	computername = file.name.split('.')[0]
	outText += "\t'" + computername + "': {\n"
	fileText = open(file.path).read()

	fileTextList = fileText.split('\n\n')

	mainList = fileTextList[1].strip().split('\n')
	for main_ in mainList:
		if main_.startswith('Host Name'):
			hn = main_.strip().split(': ')[-1]
			outText += f"\t\t'Host Name': '{hn}',\n"

	fileTextList = fileTextList[2:]
	i = 1
	txt = ''
	for fileText_ in fileTextList:
		if i%2 != 0:
			if not (fileText_.endswith('Wi-Fi:') or fileText_.endswith('Ethernet:') or fileText_.endswith('Bluetooth Network Connection:')):
				continue
			txt += "\t\t'" +fileText_.strip().split('\n')[-1].strip()[:-1] + "': "
		else:
			ftbreak = fileText_.strip().split('\n')
			for a in ftbreak:
				if a.strip().startswith('Physical Address'):
					txt += "'" + a.split(': ')[-1].strip() + "',\n"
		i += 1
	outText += txt + '\t},\n\n'
outText += '}'

print(outText)
outfile.write(outText)
outfile.close()