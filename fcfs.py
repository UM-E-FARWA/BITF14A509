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

def FCFS(num,dictlist):

	print "FIRST COME FIRST SERVE "
	total = 0
	loop = 0
	from operator import itemgetter
	dictlist.sort(key = itemgetter('arrive'))
	while(loop < num):

		if loop == 0:

			total = total + dictlist[loop]['arrive'] + dictlist[loop]['process']

		elif total > dictlist[loop]['arrive']:

			total = total + dictlist[loop]['process']

		else:

			total = dictlist[loop]['arrive']  + dictlist[loop]['process']

		print "%s Takes %d sec to complete its processing" % (dictlist[loop]['name'],total)

		loop = loop+1

num = GetNumber()
dictlist = []
GetInput(num,dictlist)
FCFS(num,dictlist)

