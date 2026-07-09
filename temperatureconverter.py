def convert_temp():
    print("temperature converter")
    print("1.celcius to fahrenheit")
    print("2.fahrenheit to calcius")
    choose=input("choose option 1 or 2 \n")

    if choose =="1":
        calcius=float(input("enter temperature in calcius \n"))
        fahrenheit=(calcius*9/5)+32
        print(f"{calcius}c is {fahrenheit:2f}f")

    elif choose=="2":
        fahrenheit=float(input("enter temperature in fahrenheit \n"))
        calcius=(fahrenheit-32)*5/9
        print(f"{fahrenheit}f is {calcius}c")

    else:
        print("invalid choose")

convert_temp()     
    

    
    
    
