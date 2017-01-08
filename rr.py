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
		info['brust'] = 0
		info['wait'] = 0
		dictlist.append(info)
		num1 = num1+1

	return
