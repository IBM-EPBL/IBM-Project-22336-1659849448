import random

def detect(tem,humi):
    if(humi<30):
        if(tem>30):
            print("Humidity : ",humi,"Temperature :",tem,"Alarm Turned On")
for i in range(0,15):
    temp=random.randint(10,50)
    humi=random.randint(15,50)
    detect(tem,humi)
    import random

 