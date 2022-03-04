import patients
import doctors
available = ["from 1:00 to 1:30", "from 1:30 to 2:00", "from 2:00 to 2:30", "from 2:30 to 3:00", "from 3:00 to 3:30", "from 3:30 to 4:00", "from 4:00 to 4:30", "from 4:30 to 5:00"]
booked = dict()

def Book():
    while 1:
        id = str()
        type = input("********************************\n* 1- New Patient.              *\n* 2- Existing Patient.         *\n* 3- Press any key to go back. *\n********************************\n")
        if (type == "1") or (type == "2"):
            if(type == "1"):
                patients.Add()
                id = "P2020" + str(patients.pindex)
            else :
            #if type == 2:
                id = input("Please enter patient's ID : ")
                if id in booked:
                    print("ID already exists!!")
                    break
            #booking
            i = 0
            for period in available:
                print(str(i+1) + "- " + period)
                i+=1
            
            time = int(input("Choose the suitable period : "))-1
            booked[id] = available.pop(time)
            print(booked)
            
        else:
            break


def cancel():
    while 1:
        id = input("Please enter patient's ID : ")
        if id in booked:
            print("Your appointment is " + booked[id])
            for_sure = input("Please click 'Enter' botton to cancel appointment and any key to go back.\n")
            
            if for_sure == "":
                available.append( booked.pop(id))
                available.sort()
            else:
                break
                
            print(available)
            print(booked)
            break
        else  :      
            print("You have no appointment!!\n")  
            break
                

def Edit():
    while 1:
        id = input("Please enter patient's ID : ")
        if id in booked:
            print("Your appointment is " + booked[id])
        
            print("Available appointments :")
            i = 0
            for period in available:
                print(str(i+1) + "- " + period)
                i+=1
            for_sure = int(input("Please choose another period or any number to go back.\n"))-1
            if (for_sure <=i) or (for_sure >=0):
                available.append( booked.pop(id))
                booked[id] = available.pop(for_sure)
                available.sort()
            else:
                break
            print(available)
            print(booked)
            break
        else:
            print("You have no appointment!!\n")  
            break


def Display():
    doctor = input("Please enter doctor's ID : ")
    if doctor in doctors.doctors:
        i = 1
        for app in booked:
            print(str(i) + "- " + booked[app])
            i+=1
    else:
        print("Doctor is not existed!!")



     
                