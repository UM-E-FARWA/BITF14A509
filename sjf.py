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

def SJF(num,dictlist):

	print "SHORTEST JOB FIRST"
	total = 0
	loop = 0
	from operator import itemgetter
	dictlist.sort(key = itemgetter('arrive','process'))
	while(loop < num):

		if loop == 0:

			total = total + dictlist[loop]['arrive'] + dictlist[loop]['process']

		elif total > dictlist[loop]['arrive']:

			total = total + dictlist[loop]['process']

		else:

			total = dictlist[loop]['arrive']  + dictlist[loop]['process']

		print "%s Turn Around Time Is : %d  Waiting Time Is : %d" % (dictlist[loop]['name'],total,total-(dictlist[loop]['arrive'] + dictlist[loop]['process']))

		loop = loop+1

num = GetNumber()
dictlist =[]
GetInput(num,dictlist)
SJF(num,dictlist)


