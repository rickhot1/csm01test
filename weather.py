import math
def weatherMessage(temp,low,med):
	
	if temp<low:
		print("wear wool trousers")
	elif temp<med:
		print("wear trousers")
	else:
		print("wear shorts")
import random
def predictTomorrowsTemp(todaysTemp):
	change= random.choice(range(-1,2))
	newTemp=todaysTemp+change
	return newTemp

def main():
	temp=10
	for day in range(1,8):
		temp=predictTomorrowsTemp(temp)
		print("Day "+str(day))
		print("Tomorrow will be:"+str(temp))

if __name__=="__main__":
	main()

main()
