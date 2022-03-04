patients = dict()
pindex = 0

def Add():
    global pindex
    pindex += 1
    id = "P2020" + str(pindex)
    patients[id] = [input("Enter Department Name : "), 
                    input("Enter Doctor's Name : "),
                    input("Enter Patient's Name : "),
                    input("Enter Patient's Age : "), 
                    input("Enter Patient's Gender : "), 
                    input("Enter Patient's Adress : "), 
                    input("Enter Patient's Phone Number : "), 
                    input("Enter Patient's Room Number : "), 
                    input("Enter Patient's Condition : ")]
    print("Patient has been added succssfuly!!\n")

    
def Delete():
    id =  input("Enter Doctor's ID : ")
    if id in patients:
        patients.pop(id)
        print("Patient has been deleted succssfuly!!")
    else :
        print("ID entered is not existed!!\n")


def Edit():
    id =  input("Enter Doctor's ID : ")
    if id in patients:
        patients[id] = [input("Enter Department Name : "), 
                    input("Enter Doctor's Name : "),
                    input("Enter Patient's Name : "),
                    input("Enter Patient's Age : "), 
                    input("Enter Patient's Gender : "), 
                    input("Enter Patient's Adress : "), 
                    input("Enter Patient's Phone Number : "), 
                    input("Enter Patient's Room Number : "), 
                    input("Enter Patient's Condition : ")]
        print("Patient has been edited succssfuly!!")
    else:
       print("ID entered is not existed!!\n")
 
 
def Display():
    for patient in patients:
        print("********************************")
        print("Patient's ID : " + patient)
        print("Department Name : " + patients[patient][0])
        print("Doctor's Name : " + patients[patient][1])
        print("Patient's Name : " + patients[patient][2])
        print("Patient's Age : " + patients[patient][3]) 
        print("Patient's Gender : " + patients[patient][4]) 
        print("Patient's Adress : " + patients[patient][5]) 
        print("Patient's Phone Number : " + patients[patient][6]) 
        print("Patient's Room Number : " + patients[patient][7]) 
        print("Patient's Condition : " + patients[patient][8])
        print("********************************")
    
    
def View():
    patient = input("Please enter patient's ID : ")
    if patient in patients:
        print("********************************")
        print("Patient's ID : " + patient)
        print("Department Name : " + patients[patient][0])
        print("Doctor's Name : " + patients[patient][1])
        print("Patient's Name : " + patients[patient][2])
        print("Patient's Age : " + patients[patient][3]) 
        print("Patient's Gender : " + patients[patient][4]) 
        print("Patient's Adress : " + patients[patient][5]) 
        print("Patient's Phone Number : " + patients[patient][6]) 
        print("Patient's Room Number : " + patients[patient][7]) 
        print("Patient's Condition : " + patients[patient][8])
        print("********************************")
    else:
        print("Patient is not existed!!")
    
    
    