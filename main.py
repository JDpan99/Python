# PAN JIAN DONG
# TP062206

def get_contact():
    while True:
        contact_number = input("Enter contact number: ")
        while len(contact_number) < 10:
            print("Invalid contact number. Please enter at least 10 number.")
            contact_number = input("Enter contact number: ")

        contact_number = ''.join(contact_number.split())

        if contact_number.isdigit():
            print("Your contact number is: ", contact_number)
            return contact_number
        else:
            print("Invalid contact number. Must be numeric only. Please try again.")


def Get_email():
    while True:
        email = input("Enter your email address :")
        if "@gmail.com" not in email:
            print("Invalid email. Please register with @gmail.com.")
        else:
            print("Your email address is: ", email)
            return email


def get_name():
    while True:
        new_name = input("Enter your name: ")
        new_name = ' '.join(new_name.split())
        temp_name = new_name.replace(" ", "")
        if temp_name.isalpha():
            print("Your name is: ", new_name)
            break
        else:
            print("Invalid Name. Must be alphabet only. Please try again.")
    return new_name


def get_age():
    while True:
        age_register = input("Enter your age: ")
        if age_register.isdigit():
            print("Your age is: ", age_register)
            break
        else:
            print("Invalid age. Must be numeric only. Please try again.")
    return age_register


def vaccine_table(age_required):
    if age_required > 45:
        print("VACCINE CODE   DOSAGE        INTERVAL BETWEEN DOSES       AGE REQUIREMENTS")
        print("   AF            2            2 weeks (or 14 days)          12 and above  ")
        print("   BV            2            2 weeks (or 14 days)          18 and above  ")
        print("   DM            2            4 weeks (or 28 days)          12 and above  ")
        print("   EC            1                    -                     18 and above  ")
    else:
        if (age_required >= 18) and (age_required <= 45):
            print("VACCINE CODE   DOSAGE        INTERVAL BETWEEN DOSES       AGE REQUIREMENTS")
            print("   AF            2            2 weeks (or 14 days)          12 and above  ")
            print("   BV            2            2 weeks (or 14 days)          18 and above  ")
            print("   CZ            2            3 weeks (or 21 days)          12 - 45  ")
            print("   DM            2            4 weeks (or 28 days)          12 and above  ")
            print("   EC            1                    -                     18 and above  ")
        else:
            if (age_required >= 12) and (age_required < 18):
                print("VACCINE CODE   DOSAGE        INTERVAL BETWEEN DOSES       AGE REQUIREMENTS")
                print("   AF            2            2 weeks (or 14 days)          12 and above  ")
                print("   CZ            2            3 weeks (or 21 days)          12 - 45  ")
                print("   DM            2            4 weeks (or 28 days)          12 and above  ")
            else:
                print("Underage. Not valid for vaccine.")
                exit()

    vaccine_check = ["AF", "DM", "BV", "EC", "CZ"]
    vaccine_choose = input("Please Enter Vaccine Selection: ").upper()
    while vaccine_choose not in vaccine_check:
        print("Invalid Input. Follow the VACCINE CODE. Please try again!")
        vaccine_choose = input("Please Enter Vaccine Selection: ").upper()
    else:
        pass

    return vaccine_choose


def get_patient_id():
    list_GetID = []
    count = 1
    with open("patients.txt", "r") as ID_file:
        for data in ID_file:
            data = data.strip("\n")
            data = data.split(", ")
            list_GetID.append(data)

    for x in list_GetID:
        count += 1

    if len(str(count)) >= 2:
        count = "0" + str(count)
    else:
        count = "00" + str(count)

    return count


def new_registration():
    file_new = open("patients.txt", "a")
    file_new.close()
    print("------------------ New Registration ------------------")
    list_patient = []
    detail_patient = []
    vc_option = ["VC1", "VC2"]
    vaccine_centre = input("Enter your vaccination centre [VC1 / VC2]? : ").upper()
    while True:
        if vaccine_centre not in vc_option:
            print("Invalid Input. Please enter correct detail.")
            vaccine_centre = input("Enter your vaccination centre [VC1 / VC2]? : ").upper()
        else:
            name_patient = get_name()
            age_patient = int(get_age())

            vaccine_code = vaccine_table(age_patient)
            print("Your vaccine selection is: ", vaccine_code)

            email_patient = Get_email()
            contact_patient = get_contact()

            id_patient = get_patient_id()
            print("Register Successfully, your patient id is:", id_patient)

            detail_patient.append(id_patient)
            detail_patient.append(name_patient)
            detail_patient.append(str(age_patient))
            detail_patient.append(email_patient)
            detail_patient.append(str(contact_patient))
            detail_patient.append(vaccine_centre)
            detail_patient.append(vaccine_code)
            list_patient.append(detail_patient)

            file_save = open("patients.txt", "a")
            for detail in list_patient:
                file_save.write(", ".join(detail) + "\n")

            print("✓ You have completed the registration.")

            break
    return


def check_detail():
    check_id = False
    VC = ""
    vaccine = ""
    id_check = Check_Id()

    file_open = open("patients.txt", "r")
    for detail in file_open:
        detail = detail.strip("\n")
        detail = detail.split(", ")

        if id_check in detail:
            check_id = True
            vaccine = detail[-1]
            VC = detail[-2]

    file_open.close()
    result = [id_check, vaccine, VC]
    if check_id:
        return result
    else:
        print("Patient ID Not Found. Please go registration first.")
        return None


def Check_Vac(VacId_Check):
    List_Vac = []
    with open("vaccination.txt", "r") as Vac_Check_File:
        for data in Vac_Check_File:
            data = data.split(", ")
            List_Vac.append(data)

    for Id in List_Vac:
        if VacId_Check == Id[0]:
            return True

    return False


def vaccine_administration():
    list_vaccination = []
    list_admin = []
    print("---------------- Vaccine Administration ----------------")
    file_vac = open("vaccination.txt", "a")
    file_vac.close()
    result = check_detail()
    if result is None:
        return None

    Id_Vac, vaccine_selected, vc = result
    VacId_Check = Check_Vac(Id_Vac)
    if VacId_Check:
        print("You have done the vaccine administration. Back to Main Menu.")
        return

    print("1. COMPLETED-D1.")
    print("2. COMPLETED.")
    dose_completed = input("Enter the dose have completed: ")
    while True:
        if dose_completed == "1" or dose_completed == "2":
            break
        else:
            print("Invalid Choice. Please enter the correct choice.")
            dose_completed = input("Enter the dose have completed: ")

    if dose_completed == "1":
        if vaccine_selected == "AF":
            print("Completed Dose 1", vaccine_selected, "Please come after 2 weeks.")
        else:
            if vaccine_selected == "BV":
                print("Completed Dose 1", vaccine_selected, "Please come after 3 weeks.")
            else:
                if vaccine_selected == "CZ":
                    print("Completed Dose 1", vaccine_selected, "Please come after 3 weeks.")
                else:
                    if vaccine_selected == "DM":
                        print("Completed Dose 1", vaccine_selected, "Please come after 4 weeks.")
                    else:
                        if vaccine_selected == "EC":
                            print("Completed Dose 1", vaccine_selected, "Completed Vaccination.")
    else:
        if dose_completed == "2":
            print("You have completed second dose, completed the vaccination.")

    list_vaccination.append(Id_Vac)
    list_vaccination.append(vaccine_selected)
    list_vaccination.append(vc)
    list_vaccination.append(dose_completed)
    list_admin.append(list_vaccination)

    file_save = open("vaccination.txt", "a")  # <-----
    for detail in list_admin:
        file_save.write(", ".join(detail) + "\n")
    file_save.close()

    return


def Check_Id():
    ID_Input = input("Enter your patient's ID: ")
    Id_List = []
    with open("patients.txt", "r") as file_Id:
        for data in file_Id:
            data = data.strip("\n")
            data = data.split(", ")
            Id_List.append(data)

    for i in Id_List:
        if ID_Input == i[0]:
            print("Correct ID. Please proceed.")
            return ID_Input

    print("Invalid ID. Please try again.")
    return


def Search_Record():
    print("---------------- Search Record ----------------")
    Id_Search = Check_Id()
    Patient_Search = []
    Vac_Search = []

    with open("patients.txt", "r") as file_O:
        for Data_Patient in file_O:
            Data_Patient = Data_Patient.strip("\n")
            Data_Patient = Data_Patient.split(", ")
            Patient_Search.append(Data_Patient)

    with open("vaccination.txt", "r") as file_Status:
        for Data_Status in file_Status:
            Data_Status = Data_Status.strip("\n")
            Data_Status = Data_Status.split(", ")
            Vac_Search.append(Data_Status)

    for Id in Patient_Search:
        if Id_Search == Id[0]:
            Get_Record(Id)
            break

    for Vac in Vac_Search:
        if Id_Search == Vac[0]:
            Get_Status(Vac)
            return

    print("ID not found. Please try again.")


def Get_Record(data):
    print("---------Patient's Detail---------")
    print("Patient ID       :", data[0])
    print("Patient Name     :", data[1])
    print("Age              :", data[2])
    print("Email Address    :", data[3])
    print("Contact Number   :", data[4])
    print("Vaccine Centre   :", data[5])
    print("Vaccine Code     :", data[6])


def Check_dose(code, dose):
    if code == "EC":
        return "COMPLETED. You are fully vaccinated."

    if dose == "1":
        return "COMPLETED-D1, remain 1 dose."
    else:
        return "COMPLETED. You are fully vaccinated."


def Get_Status(data):
    print("---------Vaccination Status---------")
    print("Patient ID      :", data[0])
    print("Vaccine Code    :", data[1])
    print("Vaccine Centre  :", data[2])
    print("Dose completed  :", Check_dose(data[1], data[3]))


def Statistical_Information():
    List_Statistic = []
    VC1_First, VC1_Second, VC2_First, VC2_Second = 0, 0, 0, 0
    VC1_EC, VC2_EC = 0, 0
    with open("vaccination.txt", "r") as file_Statistic:
        for detail in file_Statistic:
            detail = detail.strip("\n")
            detail = detail.split(", ")
            List_Statistic.append(detail)

    for sta in List_Statistic:
        if sta[2] == "VC1":
            if sta[1] == "EC":
                VC1_EC += 1
            if sta[-1] == "1":
                VC1_First += 1
            elif sta[-1] == "2":
                VC1_Second += 1

        if sta[2] == "VC2":
            if sta[1] == "EC":
                VC2_EC += 1
            if sta[-1] == "1":
                VC2_First += 1
            elif sta[-1] == "2":
                VC2_Second += 1

    if VC1_First > 0:
        VC1_First = VC1_First - VC1_EC
    if VC2_First > 0:
        VC2_First = VC2_First - VC2_EC

    VC1_Completed = VC1_EC + VC1_Second
    VC2_Completed = VC2_EC + VC2_Second

    print("-------------Vaccine Centre-------------      VC1            VC2      ")
    print(" People who are waiting for dose 2.           ", VC1_First, "           ", VC2_First)
    print(" People who have completed vaccination.       ", VC1_Completed, "           ", VC2_Completed)


def Modify_Data():
    listP_Modify = []
    listV_Modify = []

    with open("patients.txt", "r") as Patient_Modify:
        for pat_data in Patient_Modify:
            pat_data = pat_data.strip("\n")
            pat_data = pat_data.split(", ")
            listP_Modify.append(pat_data)

    with open("vaccination.txt", "r") as Vac_Modify:
        for vac_data in Vac_Modify:
            vac_data = vac_data.strip("\n")
            vac_data = vac_data.split(", ")
            listV_Modify.append(vac_data)

    while True:
        print("-------Modify Data-------")
        print("1. Modify Patient's Data")
        print("2. Update Vaccination Status")
        print("3. Back to Main Menu")
        Choice_Modify = input("Enter the choice : ")
        if Choice_Modify == "1":
            Modify_Patient(listP_Modify, listV_Modify)
        elif Choice_Modify == "2":
            Update_VacStatus(listV_Modify)
        elif Choice_Modify == "3":
            break
        else:
            print("Invalid Choice. Please enter the correct one!")


def Modify_Patient(Modify_listPat, Modify_listVac):
    Id_Pat = Check_Id()
    if Id_Pat is None:
        return Modify_Data()

    for i in Modify_listPat:
        if Id_Pat == i[0]:
            Get_Record(i)
            while True:
                print("-----------Modify Detail-----------")
                print("Select the detail want to modify : ")
                print("1. Name")
                print("2. Age")
                print("3. Email Address")
                print("4. Contact Number")
                print("5. Vaccine Code")
                print("6. Vaccine Centre")
                print("7. Save And Exit")
                Choice_Patient = input("Enter the choice : ")
                if Choice_Patient == "1":
                    New_Name = get_name()
                    i[1] = i[1].replace(i[1], New_Name)
                    print("Updated successfully!")
                elif Choice_Patient == "2":
                    New_Age = str(get_age())
                    i[2] = i[2].replace(i[2], New_Age)
                    print("Updated successfully!")
                elif Choice_Patient == "3":
                    New_Email = Get_email()
                    i[3] = i[3].replace(i[3], New_Email)
                    print("Updated successfully!")
                elif Choice_Patient == "4":
                    New_Contact = str(get_contact())
                    i[4] = i[4].replace(i[4], New_Contact)
                    print("Updated successfully!")
                elif Choice_Patient == "5":
                    New_Code = vaccine_table(int(i[2]))
                    i[6] = i[6].replace(i[6], New_Code)
                    for vac_status in Modify_listVac:
                        if Id_Pat == vac_status[0]:
                            vac_status[1] = vac_status[1].replace(vac_status[1], New_Code)
                elif Choice_Patient == "6":
                    vc_option = ["VC1", "VC2"]
                    New_VC = input("Enter your vaccination centre [VC1 / VC2]? : ").upper()
                    while True:
                        if New_VC not in vc_option:
                            print("Invalid Input. Please enter correct detail.")
                            New_VC = input("Enter your vaccination centre [VC1 / VC2]? : ").upper()
                        else:
                            break

                    i[5] = i[5].replace(i[5], New_VC)
                    for vac_status in Modify_listVac:
                        if Id_Pat == vac_status[0]:
                            vac_status[2] = vac_status[2].replace(vac_status[2], New_VC)
                    print("Updated successfully!")

                elif Choice_Patient == "7":
                    with open("patients.txt", "w") as Modify_Pat_file:
                        for data in Modify_listPat:
                            Modify_Pat_file.write(", ".join(data) + "\n")

                    with open("vaccination.txt", "w") as Modify_Vac_file:
                        for vac_data in Modify_listVac:
                            Modify_Vac_file.write(", ".join(vac_data) + "\n")

                    return Modify_Data()
                else:
                    print("Invalid Input. Please try again.")


def Update_VacStatus(Modify_listVac):
    Id_Vac = Check_Id()
    if Id_Vac is None:
        return Modify_Data()

    for vac in Modify_listVac:
        if Id_Vac == vac[0]:
            Get_Status(vac)

            while True:
                print("-----------Modify Status-----------")
                print("Select the detail want to modify : ")
                print("1. Update dose completed")
                print("2. Save And Exit")
                Choice_vac = input("Enter the choice : ")
                if Choice_vac == "1":
                    vac[-1] = vac[-1].replace(vac[-1], "2")
                    print("Updated dose successfully!")
                elif Choice_vac == "2":
                    with open("vaccination.txt", "w") as update_file:
                        for detail in Modify_listVac:
                            update_file.write(", ".join(detail) + "\n")

                    return Modify_Data()
                else:
                    print("Invalid input. Please try again.")


while True:
    print("Welcome to COVID-19 VACCINATION RECORD MANAGEMENT SYSTEM.")
    print("-----------------------Menu-----------------------")
    print("1. New Patient Registration					     ")
    print("2. Vaccine Administration  					     ")
    print("3. Search Patient Record and Vaccination Status   ")
    print("4. Statistical Information on Patients Vaccinated ")
    print("5. Modify Data of Patient                         ")
    print("6. Exit ")

    Choice_Input = input("Enter your choice :")
    if Choice_Input == "1":
        new_registration()
    elif Choice_Input == "2":
        vaccine_administration()
    elif Choice_Input == "3":
        Search_Record()
    elif Choice_Input == "4":
        Statistical_Information()
    elif Choice_Input == "5":
        Modify_Data()
    elif Choice_Input == "6":
        break
    else:
        print("Invalid Choice. Please enter the correct choice !")
