import random

Mothers = [[random.choice([1,2]) for x in xrange(0,4)] for x in xrange(0,4)]

FirstDaughter = [x[0] for x in Mothers]
SecondDaughter = [x[1] for x in Mothers]
ThirdDaughter = [x[2] for x in Mothers]
FourthDaughter = [x[3] for x in Mothers] 

def my_func(val):
	if val == 1:
		return val
	if val == 0:
		return val+2

def func(my_func,seq):
	return [my_func(n) for n in seq]

FirstNiece = map(sum, zip(Mothers[0],Mothers[1]))
FirstNiece = [FirstNiece[i]%2 for i in range(0,len(FirstNiece))]
FirstNiece = func(my_func,FirstNiece)

SecondNiece = map(sum, zip(Mothers[2],Mothers[3]))
SecondNiece = [SecondNiece[i]%2 for i in range(0,len(SecondNiece))]
SecondNiece = func(my_func,SecondNiece)

Daughters = [FirstDaughter, SecondDaughter, ThirdDaughter, FourthDaughter]

ThirdNiece = map(sum, zip(Daughters[0],Daughters[1]))
ThirdNiece = [ThirdNiece[i]%2 for i in range(0,len(ThirdNiece))]
ThirdNiece = func(my_func,ThirdNiece)

FourthNiece = map(sum, zip(Daughters[2],Daughters[3]))
FourthNiece = [FourthNiece[i]%2 for i in range(0,len(FourthNiece))]
FourthNiece = func(my_func,FourthNiece)

Nieces = [FirstNiece, SecondNiece, ThirdNiece, FourthNiece]

FirstWitness = map(sum, zip(Nieces[0],Nieces[1]))
FirstWitness = [FirstWitness[i]%2 for i in range(0,len(FirstWitness))]
FirstWitness = func(my_func,FirstWitness)

SecondWitness = map(sum, zip(Nieces[2],Nieces[3]))
SecondWitness = [SecondWitness[i]%2 for i in range(0,len(SecondWitness))]
SecondWitness = func(my_func,SecondWitness)

Witnesses = [FirstWitness, SecondWitness]

Judge = map(sum, zip(Witnesses[0],Witnesses[1]))
Judge = [Judge[i]%2 for i in range(0,len(Judge))]
Judge = func(my_func,Judge)

Reconciler = map(sum, zip(Mothers[0],Judge))
Reconciler = [Reconciler[i]%2 for i in range(0,len(Reconciler))]
Reconciler = func(my_func,Reconciler)

def PrintShield():
	print 'GEOMANTIC FIGURES OF THE SHIELD CHART:\n','Mothers = ',Mothers,'\n','Daughters = ',Daughters,'\n','Nieces = ',Nieces,'\n','Witnesses = ',Witnesses,'\n','Judge = ',Judge,'\n','Reconciler = ',Reconciler,'\n'

def one():
	print " ",u'\uFFFD',"\n"

def two():
	print u'\uFFFD'," ",u'\uFFFD',"\n"

def prettyPoints(n):
	if n == 1:
		one()
	elif n == 2:
		two()
	else:
		pass

def funkyPrint(ls):
	for i in ls:
		prettyPoints(i)

