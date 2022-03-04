# import openpyxl module 
#import openpyxl 
import excel
import patients 
import doctors
import appointments
# Give the location of the file 
#loc = () 
#wb = openpyxl.load_workbook("hospital.xlsx") 
  
# Get workbook active sheet   
# from the active attribute 
#sheet = wb.active 
  
# Cell objects also have row, column 
# and coordinate attributes that provide 
# location information for the cell. 
  
# Note: The first row or column integer 
# is 1, not 0. Cell object is created by 
# using sheet object's cell() method. 
#c1 = sheet.cell(row = 1, column = 1) 
  
# writing values to cells 
#c1.value = "ANKIT"
  
# Once have a Worksheet object, one can 
# access a cell object by its name also. 
# A2 means column = 1 & row = 2. 
#c3 = sheet['A2'] 
#c3.value = "RAHUL"
  
#wb.save("hospital.xlsx")

  
# For row 0 and column 0 
#print(sheet.cell(row= 1 , column = 2).value)



departments = ["emergency department", "burn unit", "surgery", "urgent care", "cardiology", "intensive care unit", "neurology", "Urology", "cancer center", "obstetrics and gynecology"]
excel.Read("doctors", doctors.doctors, doctors.dindex)
while 1:
    print("********************************\n* 1- User Mode.                *\n* 2- Admin Mode.               *\n* 3- Press any key to exit.    *\n********************************"+str(len(doctors.doctors)))
    mode = input()
    
    if mode == "1":
        while 1:
            option = input("********************************\n* 1- View departments.         *\n* 2- View doctors.             *\n* 3- View patients.            *\n* 4- View specific patient.    *\n* 5- View appointments.        *\n* 6- Press any key to go back. *\n********************************\n")
            if option == "1":
                i = 1
                for dep in departments:
                    print(str(i) + "- " + dep)
                    i+=1
            elif option == "2":
                doctors.Display()
            elif option == "3":
                patients.Display()
            elif option == "4":
                patients.View()
            elif option == "5":
                appointments.Display()
            else:
                break
    elif mode == "2":
        password = "1234"
        trails = 3
        while(trails>0):
            userpass = input("Enter Password : ")
            if userpass != password:
                if trails != 1:
                    print("Incorrect Password!!\nPlease try again")
                else:
                    print("System is closed!!")
            else:
                break
            trails-=1
        while 1:  
            manage = input("********************************\n1- Manage Patient.\n2- Manage Doctors.\n3- Book an appointment.\n5- Press any key to go back.\n")
            if manage == "1":
                while 1:
                    choise = input("********************************\n* 1- Add Patient.              *\n* 2- Delete Patient.           *\n* 3- Edit Patient.             *\n* 4- Display Patients.         *\n* 5- Press any key to go back. *\n********************************\n")
                    if choise == "1":
                        patients.Add()
                    elif choise == "2":
                        patients.Delete()
                    elif choise == "3":
                        patients.Edit()
                    elif choise == "4":
                        patients.Display()
                    else:
                        print("********************************")
                        break
            elif manage == "2":
                while 1:
                    choise = input("********************************\n* 1- Add Doctor.               *\n* 2- Delete Doctor.            *\n* 3- Edit Doctor.              *\n* 4- Display Doctors.          *\n* 5- Press any key to go back. *\n********************************\n")
                    if choise == "1":
                        doctors.Add()
                    elif choise == "2":
                        doctors.Delete()
                    elif choise == "3":
                        doctors.Edit()
                    elif choise == "4":
                        doctors.Display()
                    else:
                        print("********************************")
                        break
                
            elif manage == "3":
                while 1:
                    choise = input("********************************\n* 1- Book an appointment.      *\n* 2- Cancel an appointment.    *\n* 3- Edit an appointment.      *\n* 4- Press any key to go back. *\n********************************\n")
                    if choise == "1":
                        appointments.Book()
                    elif choise == "2":
                        appointments.cancel()
                    elif choise == "3":
                        appointments.Edit()
                    else:
                        print("********************************")
                        break
            else:
                break
            
    else:
        
        excel.Write("appointments", appointments.available, 2)
        print("System is closed!!")
        break
        
        
excel.Write("doctors", doctors.doctors, doctors.dindex)        
        
        
        