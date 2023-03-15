import tkinter as tk
import Student_Course_Attendance_Class
from tkinter import *
from tkinter import messagebox


class CourseManagementGUI:
    def __init__(self, master, student_register, course_register):
        self.master = master
        self.student_register = student_register
        self.course_register = course_register
        master.title("Student and Course Management System")

        # Create labels and entry widgets for student name, student number
        self.student_label = tk.Label(master, text="Student Name:")
        self.student_label.grid(row=0, column=0)
        self.student_entry = tk.Entry(master)
        self.student_entry.grid(row=0, column=1)

        self.student_number_label = tk.Label(master, text="Student Number:")
        self.student_number_label.grid(row=1, column=0)
        self.student_number_entry = tk.Entry(master)
        self.student_number_entry.grid(row=1, column=1)

        # Create labels and entry widgets for course name
        self.course_label = tk.Label(master, text="Course Name:")
        self.course_label.grid(row=0, column=2)
        self.course_entry = tk.Entry(master)
        self.course_entry.grid(row=0, column=3)

        # Create buttons for adding, updating, and deleting courses
        self.add_student_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_student_button.grid(row=2, column=0)

        self.delete_student_button = tk.Button(master, text="Delete Student", command=self.delete_student)
        self.delete_student_button.grid(row=3, column=0)

        # Create buttons for adding, updating, and deleting courses
        self.add_course_button = tk.Button(master, text="Add Course", command=self.add_course)
        self.add_course_button.grid(row=2, column=2)

        self.delete_course_button = tk.Button(master, text="Delete Course", command=self.delete_course)
        self.delete_course_button.grid(row=3, column=2)

        # Create buttons assotiating student to course
        self.assotiate_button = tk.Button(master, text="Add Student to Course", command=self.add_student_to_course)
        self.assotiate_button.grid(row=2, column=4)

        self.show_course_participants = tk.Button(master, text="Show Participants", command=self.show_participants)
        self.show_course_participants.grid(row=3, column=4)

        # Create table to display students
        self.students_listbox = Listbox(master, bg='grey')
        self.students_listbox.grid(row=4, column=0, columnspan=2)

        # Create table to display courses
        self.courses_listbox = Listbox(master, bg='grey')
        self.courses_listbox.grid(row=4, column=2, columnspan=2)

        # Create table to display courses participants
        self.course_participants_listbox = Listbox(master, bg='grey')
        self.course_participants_listbox.grid(row=4, column=4, columnspan=2)

    def update_student_listbox(self):
        self.students_listbox.delete(0, tk.END)
        students = student_register.return_register()
        for student in students:
            student_info = f"{student.name} ({student.number})"
            self.students_listbox.insert(tk.END, student_info)

    def update_course_listbox(self):
        self.courses_listbox.delete(0, tk.END)
        courses = course_register.return_register()
        for course in courses:
            course_info = f"{course.name}"
            self.courses_listbox.insert(tk.END, course_info)

    def update_participants_listbox(self):
        self.course_participants_listbox.delete(0, tk.END)
        course_name = self.course_entry.get()
        if course_register.exists(course_name):
            course = course_register.find_course(course_name)
            students = course.students.return_register()
            for student in students:
                student_info = f"{student.name} - {course.name}"
                self.course_participants_listbox.insert(tk.END, student_info)
    
    def add_student(self):
        name = self.student_entry.get()
        number = self.student_number_entry.get()
        if name != "" and number != "":
            student_register.add(name, number)
        self.update_student_listbox()

    def delete_student(self):
        name = self.student_entry.get()
        number = self.student_number_entry.get()
        student_register.delete(name, number)
        self.update_student_listbox()

    def add_course(self):
        name = self.course_entry.get()
        if name != "":
            course_register.add(name)
        self.update_course_listbox()

    def delete_course(self):
        name = self.course_entry.get()
        course_register.delete(name)
        self.update_course_listbox()

    def add_student_to_course(self):
        name = self.student_entry.get()
        number = self.student_number_entry.get()
        course_name = self.course_entry.get()
        if course_register.exists(course_name):
            if student_register.exists(name, number):
                course = course_register.find_course(course_name)
                student = student_register.find_student(name, number)
                print(f"Adding student {name} to course {course_name}")
                course.add_student(student)
                print(f"Updated participants for course {course_name}")
        self.update_participants_listbox()

    def show_participants(self):
        course_name = self.course_entry.get()
        if course_register.exists(course_name):
            course = course_register.find_course(course_name)
            students = course.students.return_register()
            participants = []
            for student in students:
                participant_info = f"{student.name} - {course.name}"
                participants.append(participant_info)
                message = "\n".join(participants)
                messagebox.showinfo(title="Participants", message=message)
            else:
                messagebox.showwarning(title="Course not found", message="The course does not exist in the register.")

student_register = Student_Course_Attendance_Class.StudentRegister()
course_register = Student_Course_Attendance_Class.CourseRegister("Courses")
root = tk.Tk()
app = CourseManagementGUI(root, student_register,course_register)
root.mainloop()