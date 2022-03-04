doctors = dict()
dindex = int()


def Add():
   # patient = list()
    global dindex
    dindex += 1
    id = "D2020" + str(dindex)
    doctors[id] = [input("Enter Department Name : "), 
                    input("Enter Doctor's Name : "),
                    input("Enter Doctor's Adress : "), 
                    input("Enter Doctor's Phone Number : ")]
    print("Doctor has been added succssfuly!!")
    
def Delete():
    id =  input("Enter Doctor's ID : ")
    if id in doctors:
        doctors.pop(id)
        print("Doctor has been deleted succssfuly!!")
    else:
        print("Doctor is not existed!!")

def Edit():
    id =  input("Enter Doctor's ID : ")
    if id in doctors:
        doctors[id] = [input("Enter Department Name : "), 
                    input("Enter Doctor's Name : "),
                    input("Enter Doctor's Adress : "), 
                    input("Enter Doctor's Phone Number : ")]
        print("Doctor has been edited succssfuly!!")
    else:
        print("Doctor is not existed!!")
            
def Display():
    for doctor in doctors:
        if doctor != None:
            print("********************************")
            print("Doctor's ID : " + doctor)
            print("Department Name : " + doctors[doctor][0])
            print("Doctor's Name : " + doctors[doctor][1])
            print("Doctor's Adress : " + doctors[doctor][2]) 
            print("Doctor's Phone Number : " + doctors[doctor][3]) 
            print("********************************")