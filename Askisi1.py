import random
import math



laburin8os=[['O' for a in range(10)] for a in range(10) ]
agr=random.randrange(0,9)
bgr=random.randrange(0,9)
aseir=random.randrange(0,9)
bseir=random.randrange(0,9)
while aseir==agr and bseir==bgr:
	aseir=random.randrange(0,9)
	bseil=random.randrange(0,9)
laburin8os[aseir][bseir]='X'
apostasi=math.fabs(aseir-agr)+math.fabs(bseir-bgr)
print 'you are at:',aseir+1,bseir+1,'and your distance from the treasure is:',apostasi,'blocks.'
for a in range(10):
	print laburin8os[a]
stoxos=True if aseir==agr and bseir==bgr else False
while stoxos==False:
	proorismos=raw_input('Do you want to go UP,DOWN,LEFT or RIGHT?')
	if (proorismos=='RIGHT'):
		if (bseir+1<10):
			laburin8os[aseir][bseir]='0'
			bseir=bseir + 1
			laburin8os[aseir][bseir]='X'
			apostasi=math.fabs(aseir-agr)+math.fabs(bseir-bgr)
			print 'you are at:',aseir+1,bseir+1,'and your distance from the treasure is:',apostasi,'blocks'
	elif (proorismos=='LEFT'):
		if (bseir-1>-1):
			laburin8os[aseir][bseir]='0'
			bseir=bseir-1
			laburin8os[aseir][bseir]='X'
			apostasi=math.fabs(aseir-agr)+math.fabs(bseir-bgr)
			print 'you are at:',aseir+1,bseir+1,'and your distance from the treasur is:',apostasi,'blocks.'
	elif (proorismos=='UP'):
		if (aseir-1>-1):
			laburin8os[aseir][bseir]='0'
			aseir=aseir-1
			laburin8os[aseir][bseir]='X'
			apostasi=math.fabs(aseir-agr)+math.fabs(bseir-bgr)
			print 'you are at:',aseir+1,bseir+1,'and your distance from the treasue is:',apostasi,'blocks.'
	elif (proorismos=='DOWN'):
		if (aseir+1<10):
			laburin8os[aseir][bseir]='0'
			aseir=aseir+1
			laburin8os[aseir][bseir]='X'
			apostasi=math.fabs(aseir-agr)+math.fabs(bseir-bgr)
			print 'you are at:',aseir+1,bseir+1,'and your distance from the treasure is:',apostasi,'blocks.'	
	else:
		print 'you didnt give a valid input'
	stoxos=True if aseir==agr and bseir==bgr else False
	for a in range(10):
		print laburin8os[a]
print 'you found the treasure.'
