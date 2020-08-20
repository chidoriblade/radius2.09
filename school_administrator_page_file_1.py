# Project 1 : building a school administrator page
import csv
def write_info_csv_file(info_list):
    with open("student_info.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
           writer.writerow(["Name" , "Age" , "Contact_number" , "Email_ID"])
        writer.writerow(info_list)
if __name__ == '__main__':
   condition = True
   student_num = 1

   while(condition):
     student_info = input("Enter student information for student #{} in the following format (Name Age Contact_number Email_ID): ".format(student_num))

     student_info_list = student_info.split(' ')
     print("The entered informatio is -\nName: {} \nAge: {} \nContact_number: {} \nEmail_ID: {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
     choice_check = input("Is the entered information correct (yes/no)?\n ")

     if choice_check == "yes":
         write_info_csv_file(student_info_list)

         continuity = input("Do you want to continue to enter more information? (yes/no) ")

         if continuity == "yes":
             condition = True
             student_num = student_num + 1
         elif continuity == "no":
             condition = False
     elif choice_check == "no":
          print("please re-enter the values!")
