import random
def check(temperature,humidity):
    if(humidity<25):
        if(temperature>25):
            print("Temperature : ",temperature,"***Beep***")
for i in range(0,20):
    temperature = random.randint(10,100)
    humidity = random.randint(10,100)
    check(temperature,humidity)