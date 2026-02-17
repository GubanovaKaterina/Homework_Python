#weekDays = [
	#"Понедельник",
	#"Вторник",
	#"Среда",
	#"Четверг",
	#"Пятница",
	#"Суббота",
	#"Воскресенье"
#]
#length = len(weekDays)
#print(length)

#monday = weekDays[0]
#print(monday)

#whatIf = weekDays[-2]
#print(whatIf)

#print(weekDays[5])

#def sum_numbers():
    #print("меня вызвали 1")
    #print("меня вызвали 2")
    #print("меня вызвали 3")
    #print("меня вызвали 4")
    #print("меня вызвали 5")

#print("меня вызвали x")
#sum_numbers()

#def greet(name):
    #print("Привет, " + name)

#greet("Alex")
#greet("Mark")

#def sum_numbers(num_1, num_2):
    #print("Слагаемое 1 = ", num_1)
    #print("Слагаемое 2 = ", num_2)
    #result = num_1+num_2
    #print("Сумма = ", num_1+num_2)
    #return result

#x = sum_numbers(1000,5)
#print(x)

#def sum(num_1, num_2):
    #result = num_1+num_2
    #return result

#x = sum(1000,5)
#print(x)

#def multiply(x,y):
    #return x*y

#m= multiply(3,4)
#print(m)

#def sub(a,b):
    #return a-b

#s= sub(5,2)
#print(s)

#def div(t,p):
    #return t/p

#d= div(6,3)
#print(d)

globalVar = 1

def printGlobal():
    print(globalVar)

def printLocal():
    local = 2
    print(local)

printGlobal()
printLocal()
