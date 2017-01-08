
def GetNumber():

	print("How Many Number Of Jobs You Want to Enter : ")
	return input()

def GetInput(num,dictlist):

	num1 = 0

	while(num1 < num):

		info = {}
		info['name']=raw_input ("Input Name : ")
		info['arrive']=input ("Input A.Time : ")
		info['process']=input ("Input P.Time : ")
		dictlist.append(info)
		num1 = num1+1

	return

def SRTF(num,dictlist):

	print "SHORTEST REMAINING TIME FIRST"
	total = 0
	loop = num
	ready = []

	from operator import itemgetter
	dictlist.sort(key = itemgetter('arrive'))
	temp = dictlist[0]
	del dictlist[0]
	total = temp['arrive']

	while(loop):

		if(len(dictlist) != 0):

			if(dictlist[0]['arrive'] <= total):
				ready += [dictlist[0]]
				del dictlist[0]

		if(len(ready) != 0):
			ready.sort(key = itemgetter('process'))

		if(len(ready) != 0 ):
			if(temp['process'] > ready[0]['process']):
				ready += [temp]
				temp = ready[0]
				del ready[0]

		temp['process'] -= 1
		total += 1
		if(temp['process'] == 0):
			print "%s Turn Around Time Is : %d  Waiting Time Is : %d" % (temp['name'],total,total-(temp['arrive']+temp['process']))

			loop = loop - 1
			if(len(ready) != 0):

				temp = ready[0]
				del ready[0]

num = GetNumber()
dictlist = []
GetInput(num,dictlist)
SRTF(num,dictlist)
