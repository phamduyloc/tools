import sys

# total arguments
n = len(sys.argv)

if(n<2):
    exit()

strResult=""
strYear=sys.argv[1]
strMonth=""
strDay=""
strHour=""
strMinute=""
strSecond=""



def writeresult(res, month):
    f = open(strYear + month + ".txt", "a")
    f.writelines(res + "\n")
    f.close()


for month in range(1,13):
    if(month<10):
        strMonth="0" + str(month)
    else:
        strMonth = str(month)

    print("Month: " + strMonth)
    for day in range(1,32):
        if(day<10):
            strDay="0" + str(day)
        else:
            strDay=str(day)  
        #print("Day: " + strDay)
        for hour in range(24):
            if(hour<10):
                strHour="0" + str(hour)
            else:
                strHour=str(hour)  
            #print("Hour: " + strHour)

            for minute in range(60):
                if(minute<10):
                    strMinute="0" + str(minute)
                else:
                    strMinute=str(minute)  
                #print(strMinute)
                for second in range(60):
                    if(second<10):
                        strSecond="0" + str(second)
                    else:
                        strSecond=str(second)  
                    #print(strSecond)
                    
                    strResult = strYear + strMonth + strDay + strHour + strMinute + strSecond
                    writeresult(strResult, strMonth)


