import tkinter as tk
from typing import Tuple
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageSequence
from datetime import datetime, date
from time import strftime
from tkinter import filedialog
import os
import tkcalendar
from tkinter import ttk
import mysql.connector as mycon
from tkinter import messagebox
import win32api
import textwrap
import warnings
import requests
import time
import tkintermapview
from threading import Thread
import yagmail

class HoverColor:
    def __init__(self,button, image_name, image_name1):
        # self.home_button.bind("<Enter>", lambda e : self.home_button.configure(fg_color = "white", image = self.home_image1, text_color = "#1D49CB"))
        # self.home_button.bind("<Leave>", lambda e : self.home_button.configure(fg_color = "#0766AD", image = self.home_image, text_color = "white"))
        button.bind("<Enter>", lambda e : button.configure(fg_color = "white", image = image_name, text_color = "#1D49CB"))
        button.bind("<Leave>", lambda e : button.configure(fg_color = "#0766AD", image = image_name1, text_color = "white"))

class ChangeLabel(ctk.CTkLabel):
    def __init__(self, parent_frame, text ):
        self.my_label = ctk.CTkLabel(parent_frame, text = text, width = 1092, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
        self.my_label.place(x = 0, y = 0)

class HeadingFrame(ctk.CTkFrame):
    def __init__(self, parent_frame, width = 1526, height = 90, heading_image_path = "image/heading_image.png",heading_logo_path = "image/slogo.png", fg_color = "white", border_width = 1, border_color = "green", corner_radius = 1):
        super().__init__(parent_frame, width=width, height=height, fg_color=fg_color, border_width=border_width, border_color=border_color,corner_radius=corner_radius)

        self.heading_logo_path = heading_logo_path
        self.heading_image_path = heading_image_path

        self.create_widgets()
        self.date()
        self.time()

    def create_widgets(self):
        self.heading_logo = ctk.CTkImage(light_image=Image.open("image/slogo.png"), dark_image=Image.open("image/slogo.png"), size = (75, 75))
        self.heading_logo_label = ctk.CTkLabel(self, text = "", image = self.heading_logo)
        self.heading_logo_label.place(x = 140, y = 5)

        self.heading_image = ctk.CTkImage(light_image=Image.open("image/heading_image.png"), dark_image=Image.open("image/heading_image.png"), size = (1000, 80))
        self.heading_label = ctk.CTkLabel(self, text = "", image = self.heading_image)
        self.heading_label.place(x = 250, y = 5)

        self.date_label = ctk.CTkLabel(self, text = "date", font = ("Consolas", 20), text_color="green")
        self.date_label.place(x = 1375, y = 10)
        self.time_label = ctk.CTkLabel(self, text = "time", font = ("Consolas", 20), text_color="green")
        self.time_label.place(x = 1375, y = 40)

    #date and time function
    def date(self):
        today_date = datetime.today()
        day = today_date.day
        month = today_date.month
        year = today_date.year
        self.date_label.configure(text = f"{day}-{month}-{year}")

    def time(self):
        minute = strftime("%M")
        hours = strftime("%I")  #I - for 12 hours clock
        second = strftime("%S")
        am_pm = strftime("%p")

        self.time_label.configure(text = f"{hours}:{minute}:{second} {am_pm}")
        self.time_label.after(1000, self.time)

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="white")
        self.title("School Management System")
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}-10-7")
        self.iconbitmap("image/school_icon.ico")

    #========functions=============# 
    def home_page(self):
        self.x = 1
        def move():
            global x
            img1 = ctk.CTkImage(light_image=Image.open("image/slideshow1.png"), dark_image=Image.open("image/slideshow1.png"), size = (995, 500))
            img2 = ctk.CTkImage(light_image=Image.open("image/slideshow2.png"), dark_image=Image.open("image/slideshow2.png"), size = (995, 500))
            img3 = ctk.CTkImage(light_image=Image.open("image/slideshow3.png"), dark_image=Image.open("image/slideshow3.png"), size = (995, 500))
            img4 = ctk.CTkImage(light_image=Image.open("image/slideshow4.png"), dark_image=Image.open("image/slideshow4.png"), size = (995, 500))
            
            if self.x == 1:
                self.slide_label.configure(image = img1)
            elif self.x == 2:
                self.slide_label.configure(image = img2)
            elif self.x == 3:
                self.slide_label.configure(image = img3)
            elif self.x == 4:
                self.slide_label.configure(image = img4)
            elif self.x == 5:
                self.x= -1
            self.x = self.x + 1
            self.after(1000, move)
        
        #=====calling the admin_login_page=========#
        def admin_login_page():
            self.withdraw()
            new_window = AdminLoginWindow()
            new_window.title("School Management System")

        def ask_a_question_page():
            self.withdraw()
            askquestion_window = AskAQuestionWindow()
            askquestion_window.title("School Management System")

        def announcement_page():
            self.withdraw()
            notice_window = AnnouncementWindow()
            notice_window.title("School Management System")

        def rules_regulation_pages():
            self.withdraw()
            rules_window = RulesRegulationsWindow()
            rules_window.title("School Management System")

        def contact_us_page():
            self.withdraw()
            contac_window = ContactUsWindow()
            contac_window.title("School Management System")

        def again_home_page():
            self.home_page()

        def facilty_page():
            self.withdraw()
            facility_window = FacilityWindow()
            facility_window.title("School Management System")

        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        #=====tabs menu========#
        self.tab_frame = ctk.CTkFrame(self, width = 1526, height = 60, fg_color="#0766AD", corner_radius=0, border_width=0, border_color="black")

        self.home_image = ctk.CTkImage(light_image=Image.open("image/home_icon (2).png"), dark_image=Image.open("image/home_icon (2).png"), size = (30, 30))
        self.home_image1 = ctk.CTkImage(light_image=Image.open("image/house.png"), dark_image=Image.open("image/house.png"), size = (30, 30))

        self.home_button = ctk.CTkButton(self.tab_frame, text = "Home", width = 200, height = 52, border_width=0, border_color="green", font = ("Verdana Pro",18), text_color="white", fg_color="#0766AD", corner_radius=0, hover_color="white", cursor = "hand2", command=again_home_page, image=self.home_image)
        self.home_button.place(x = 1, y = 0)
        HoverColor(self.home_button, image_name=self.home_image1, image_name1=self.home_image)

        self.admin_image = ctk.CTkImage(light_image=Image.open("image/settings.png"), dark_image=Image.open("image/settings.png"), size = (30, 30))
        self.admin_image1 = ctk.CTkImage(light_image=Image.open("image/admin.png"), dark_image=Image.open("image/admin.png"), size = (30, 30))

        self.admin_button = ctk.CTkButton(self.tab_frame, text = "Admin Panel"
        , width = 200, height = 52, border_width=0, border_color="green", font = ("Verdana Pro", 18), text_color="white", fg_color="#0766AD", corner_radius=0, hover_color="white", cursor = "hand2", command = admin_login_page, image = self.admin_image)
        self.admin_button.place(x = 200 , y = 0)
        HoverColor(self.admin_button, image_name=self.admin_image1, image_name1=self.admin_image)

        self.announcement_image = ctk.CTkImage(light_image=Image.open("image/attention.png"), dark_image=Image.open("image/attention.png"), size = (30, 30))
        self.announcement_image1 = ctk.CTkImage(light_image=Image.open("image/attention (2).png"), dark_image=Image.open("image/attention (2).png"), size = (30, 30))

        self.announcement_button = ctk.CTkButton(self.tab_frame, text = "Announcement", width = 200, height = 52, border_width=0, border_color="green", font = ("Verdana Pro", 18), text_color="white", fg_color="#0766AD", corner_radius=0, hover_color="white", cursor = "hand2", command=announcement_page, image = self.announcement_image)
        self.announcement_button.place(x = 400, y = 0)
        HoverColor(self.announcement_button, image_name=self.announcement_image1, image_name1=self.announcement_image)

        self.facility_image = ctk.CTkImage(light_image=Image.open("image/facility.png"), dark_image=Image.open("image/facility.png"), size = (30, 30))
        self.facility_button = ctk.CTkButton(self.tab_frame, text = "Facility", width = 200, height = 52, border_width=0, border_color="green", font = ("Verdana Pro", 18), text_color="white", fg_color="#0766AD", corner_radius=0, hover_color="white", cursor = "hand2", command=facilty_page, image = self.facility_image)
        self.facility_button.place(x = 600, y = 0)
        HoverColor(self.facility_button, image_name=self.facility_image, image_name1= self.facility_image)

        self.question_image = ctk.CTkImage(light_image=Image.open("image/question-and-answer (1).png"), dark_image=Image.open("image/question-and-answer (1).png"), size = (30, 30))
        self.question_image1 = ctk.CTkImage(light_image=Image.open("image/question-and-answer.png"), dark_image=Image.open("image/question-and-answer.png"), size = (30, 30))

        self.ask_a_question_button = ctk.CTkButton(self.tab_frame, text = "Ask a question", width = 200, height = 52, border_width=0, border_color="green", font = ("Verdana Pro", 18), text_color="white", fg_color="#0766AD", corner_radius=0, hover_color="white", cursor = "hand2", command=ask_a_question_page, image = self.question_image)
        self.ask_a_question_button.place(x = 800, y = 0)
        HoverColor(self.ask_a_question_button, image_name=self.question_image1, image_name1= self.question_image)

        self.guideline_image = ctk.CTkImage(light_image=Image.open("image/regulations (1).png"), dark_image=Image.open("image/regulations (1).png"), size = (30, 30))
        self.guideline_image1 = ctk.CTkImage(light_image=Image.open("image/regulations.png"), dark_image=Image.open("image/regulations.png"), size = (30, 30))

        self.guideline_button = ctk.CTkButton(self.tab_frame, text = "Guidelines", width = 200, height = 52, border_width=0, border_color="green", font = ("Verdana Pro", 18), text_color="white", fg_color="#0766AD", corner_radius=0, hover_color="white", cursor = "hand2", command = rules_regulation_pages, image = self.guideline_image)
        self.guideline_button.place(x = 1000, y = 0)
        HoverColor(self.guideline_button, image_name=self.guideline_image1, image_name1= self.guideline_image)

        self.contact_image = ctk.CTkImage(light_image=Image.open("image/contact-mail (1).png"), dark_image=Image.open("image/contact-mail (1).png"), size = (30, 30))
        self.contact_image1 = ctk.CTkImage(light_image=Image.open("image/contact-mail.png"), dark_image=Image.open("image/contact-mail.png"), size = (30, 30))

        self.contact_us = ctk.CTkButton(self.tab_frame, text = "Contact Us", width = 200, height = 52, border_width=0, border_color="green", font = ("Verdana Pro", 18), text_color="white", fg_color="#0766AD", corner_radius=0, hover_color="white", cursor = "hand2", command = contact_us_page, image = self.contact_image)
        self.contact_us.place(x = 1200, y = 0)
        HoverColor(self.contact_us, image_name=self.contact_image1, image_name1=self.contact_image)

        self.tab_frame.pack_propagate(False)
        self.tab_frame.place(x = 5, y = 94)
        
        #======main_frame========#
        self.main_frame = ctk.CTkFrame(self, width = 1526, height = 690, fg_color="white", corner_radius=1, border_width=1, border_color="green")

        #+========left side frame==========#
        self.leftside_frame = ctk.CTkFrame(self.main_frame, width = 440, height = 670, fg_color="white", corner_radius=1, border_width=0, border_color="green")

        def student_login():
            global student_email_entry, student_password_entry
            #====show password====#
            self.show = "*"
            def show_password():
                global show
                if self.show  == "*":
                    self.hide_image_button.configure(image = self.show_image)
                    student_password_entry.configure(show = "")
                    self.show = ""
                else:
                    self.hide_image_button.configure(image = self.hide_image)
                    student_password_entry.configure(show = "*")
                    self.show = "*"      
        
            #=======main login frame==============#
            self.student_login_frame = ctk.CTkFrame(self.leftside_frame, width = 420, height = 335, fg_color="white", corner_radius=1, border_width=1, border_color="blue")

            #=======button frame================#
            self.button_frame = ctk.CTkFrame(self.student_login_frame, width = 420, height = 40, fg_color="white")

            self.my_account_button = ctk.CTkButton(self.button_frame, text = "My Account", font = ("Verdana Pro", 18), corner_radius=0, fg_color="#074173", text_color="white", width = 210, height = 40)
            self.my_account_button.place(x = 0, y = 0)

            self.registration_button = ctk.CTkButton(self.button_frame, text = "Registration", font = ("Verdana Pro", 18), corner_radius=0, fg_color="#378CE7", text_color="white", width = 212, height = 40, command = self.teacher_registration)
            self.registration_button.place(x = 209, y = 0)

            self.button_frame.place(x = 0, y = 0)

            #=========student email entry=============#
            student_email_entry = ctk.CTkEntry(self.student_login_frame, border_width=0, border_color="black", width = 320, height = 30, corner_radius=0, font = ("Verdana Pro", 15), placeholder_text="Email", fg_color="white")
            student_email_entry.place(x = 18, y = 70)
            student_email_entry.bind("<FocusIn>", lambda e : self.line1.config(bg = "#074173"))
            student_email_entry.bind("<FocusOut>", lambda e : self.line1.config(bg = "grey"))

            self.line1 = tk.Label(self.student_login_frame, bg="grey")
            self.line1.place(x = 30, y = 130, width = 440, height = 2)

            #=======student password entry===========#
            student_password_entry = ctk.CTkEntry(self.student_login_frame, border_width=0, border_color="black", width = 320, height = 30, corner_radius=0, font = ("Verdana Pro", 16), placeholder_text="Password", fg_color="white", show = "*")
            student_password_entry.place(x = 18, y = 130)
            student_password_entry.bind("<FocusIn>", lambda e : self.line2.config(bg = "#074173"))
            student_password_entry.bind("<FocusOut>", lambda e : self.line2.config(bg = "grey"))

            self.line2 = tk.Label(self.student_login_frame, bg="grey")
            self.line2.place(x = 30, y = 205, width = 445, height = 2)

            #========hide image=========#
            self.hide_image = ctk.CTkImage(light_image=Image.open("image/hide.png"), dark_image=Image.open("image/hide.png"), size = (25, 25))

            self.show_image = ctk.CTkImage(light_image=Image.open("image/eye.png"), dark_image=Image.open("image/eye.png"), size = (25, 25))

            self.hide_image_button = ctk.CTkButton(self.student_login_frame, text = "", image = self.hide_image, width = 0, height = 0, hover="disabled", fg_color="transparent", bg_color="transparent", cursor = "hand2", command = show_password)
            self.hide_image_button.place(x = 342, y = 130)
            
            #========login button==========#
            self.student_login_button = ctk.CTkButton(self.student_login_frame, text = "LOGIN", font = ("Verdana Pro", 18), fg_color="#074173", corner_radius=0, width = 120, height = 35, command=self.student_login)
            self.student_login_button.place(x = 25, y = 200)

            #========message frame==========#
            self.student_message_frame = ctk.CTkFrame(self.student_login_frame, width = 420 ,height = 65, fg_color="#378CE7", corner_radius=0, border_width=0)

            self.student_image = ctk.CTkImage(light_image=Image.open("image/student (3).png"), dark_image=Image.open("image/student (3).png"), size = (50, 50))
                
            self.student_image_label = ctk.CTkLabel(self.student_message_frame, text = "", image = self.student_image)
            self.student_image_label.place(x = 5, y = 5)

            self.student_text_label = ctk.CTkLabel(self.student_message_frame, text = "Student Login with username and password and view reports", wraplength=350, font = ("Verdana Pro", 15), text_color="white")
            self.student_text_label.place(x = 60, y = 10)

            self.student_message_frame.place(x = 0, y = 270)

            self.student_login_frame.place(x = 10, y = 10) 

        #======================================#
        def teacher_login():
            global teacher_email_entry, teacher_password_entry
            #====show password====#
            self.show = "*"
            def show_password():
                global show
                if self.show  == "*":
                    self.hide_image_button.configure(image = self.show_image)
                    teacher_password_entry.configure(show = "")
                    self.show = ""
                else:
                    self.hide_image_button.configure(image = self.hide_image)
                    teacher_password_entry.configure(show = "*")
                    self.show = "*"      
        
            #=======main login frame==============#
            self.teacher_login_frame = ctk.CTkFrame(self.leftside_frame, width = 420, height = 335, fg_color="white", corner_radius=0, border_width=1, border_color="blue")

            #=======button frame================#
            self.button_frame = ctk.CTkFrame(self.teacher_login_frame, width = 420, height = 40, fg_color="white")

            self.my_account_button = ctk.CTkButton(self.button_frame, text = "My Account", font = ("Verdana Pro", 18), corner_radius=0, fg_color="#074173", text_color="white", width = 210, height = 40)
            self.my_account_button.place(x = 0, y = 0)

            self.registration_button = ctk.CTkButton(self.button_frame, text = "Registration", font = ("Verdana Pro", 18), corner_radius=0, fg_color="#378CE7", text_color="white", width = 212, height = 40, command=self.teacher_registration)
            self.registration_button.place(x = 209, y = 0)

            self.button_frame.place(x = 0, y = 0)

            #=========teacher email entry=============#
            teacher_email_entry = ctk.CTkEntry(self.teacher_login_frame, border_width=0, border_color="black", width = 320, height = 30, corner_radius=0, font = ("Verdana Pro", 15), placeholder_text="Email", fg_color="white")
            teacher_email_entry.place(x = 18, y = 70)
            teacher_email_entry.bind("<FocusIn>", lambda e : self.line1.config(bg = "#074173"))
            teacher_email_entry.bind("<FocusOut>", lambda e : self.line1.config(bg = "grey"))

            self.line1 = tk.Label(self.teacher_login_frame, bg="grey")
            self.line1.place(x = 30, y = 130, width = 440, height = 2)

            #=======teacher password entry===========#
            teacher_password_entry = ctk.CTkEntry(self.teacher_login_frame, border_width=0, border_color="black", width = 320, height = 30, corner_radius=0, font = ("Verdana Pro", 16), placeholder_text="Password", fg_color="white", show = "*")
            teacher_password_entry.place(x = 18, y = 130)
            teacher_password_entry.bind("<FocusIn>", lambda e : self.line2.config(bg = "#074173"))
            teacher_password_entry.bind("<FocusOut>", lambda e : self.line2.config(bg = "grey"))

            self.line2 = tk.Label(self.teacher_login_frame, bg="grey")
            self.line2.place(x = 30, y = 205, width = 440, height = 2)

            #========hide image=========#
            self.hide_image = ctk.CTkImage(light_image=Image.open("image/hide.png"), dark_image=Image.open("image/hide.png"), size = (25, 25))

            self.show_image = ctk.CTkImage(light_image=Image.open("image/eye.png"), dark_image=Image.open("image/eye.png"), size = (25, 25))

            self.hide_image_button = ctk.CTkButton(self.teacher_login_frame, text = "", image = self.hide_image, width = 0, height = 0, hover="disabled", fg_color="transparent", bg_color="transparent", cursor = "hand2", command=show_password)
            self.hide_image_button.place(x = 342, y = 130)
            
            #========login button==========#
            self.teacher_login_button = ctk.CTkButton(self.teacher_login_frame, text = "LOGIN", font = ("Verdana Pro", 18), fg_color="#074173", corner_radius=0, width = 120, height = 35, command=self.teacher_login)
            self.teacher_login_button.place(x = 25, y = 200)

            #========message frame==========#
            self.teacher_message_frame = ctk.CTkFrame(self.teacher_login_frame, width = 420 ,height = 65, fg_color="#378CE7", corner_radius=0, border_width=0)

            self.teacher_image = ctk.CTkImage(light_image=Image.open("image/teacher (1).png"), dark_image=Image.open("image/teacher (1).png"), size = (50, 50))
                
            self.teacher_image_label = ctk.CTkLabel(self.teacher_message_frame, text = "", image = self.teacher_image)
            self.teacher_image_label.place(x = 5, y = 5)

            self.teacher_text_label = ctk.CTkLabel(self.teacher_message_frame, text = "Staff can make attendance of student and generate reports after login to system", wraplength=350, font = ("Verdana Pro", 15), text_color="white")
            self.teacher_text_label.place(x = 60, y = 10)

            self.teacher_message_frame.place(x = 0, y = 270)

            self.teacher_login_frame.place(x = 10, y = 10) 

        #========student and teacher choose button===========#
        self.ask_teacher_image = ctk.CTkImage(light_image=Image.open("image/school.png"), dark_image=Image.open("image/school.png"), size = (60, 60))
        self.ask_teacher_label = ctk.CTkLabel(self.leftside_frame, text = "", image = self.ask_teacher_image)
        self.ask_teacher_label.place(x = 10, y = 500)

        self.choose_teacher_button = ctk.CTkButton(self.leftside_frame, text = "Staff", font = ("Verdana Pro", 18), fg_color="#074173", corner_radius=1, width = 120, height = 35, command = teacher_login, cursor = "hand2")
        self.choose_teacher_button.place(x = 80, y = 510)

        self.ask_student_image = ctk.CTkImage(light_image=Image.open("image/reading-book (1).png"), dark_image=Image.open("image/reading-book (1).png"), size = (60, 60))
        self.ask_student_label = ctk.CTkLabel(self.leftside_frame, text = "", image = self.ask_student_image)
        self.ask_student_label.place(x = 10, y = 580)

        self.choose_student_button = ctk.CTkButton(self.leftside_frame, text = "Student", font = ("Verdana Pro", 18), fg_color="#074173", corner_radius=1, width = 120, height = 35, command = student_login, cursor = "hand2")
        self.choose_student_button.place(x = 80, y = 590)

        #======calling the function===========#
        student_login()

        self.leftside_frame.place(x = 10, y = 10)
        #========================================#

        #====slide show============#
        self.slideshow_frame = ctk.CTkFrame(self.main_frame, width = 985, height = 670, fg_color="white", corner_radius=1, border_width=2, border_color="green")

        #===========================
        self.inside_frame = ctk.CTkFrame(self.slideshow_frame, width = 985, height = 500, fg_color="white", corner_radius=1, border_width=2, border_color="green")

        self.slide_label = ctk.CTkLabel(self.inside_frame, text = "")
        self.slide_label.place(x = 0, y = 0)
        move()         #calling move function

        self.inside_frame.place(x = 0, y = 0)
        #===========================
        self.quote_image = ctk.CTkImage(light_image=Image.open("image/quote_image.png"), dark_image=Image.open("image/quote_image.png"), size = (985, 170))

        self.quote_label = ctk.CTkLabel(self.slideshow_frame, text = "", image = self.quote_image)
        self.quote_label.place(x = 0, y = 500)

        self.slideshow_frame.place(x = 530, y = 10)

        self.main_frame.place(x = 5, y = 145)
        self.main_frame.pack_propagate(False)

    #=======student personal detail page===========#
    def student_registration(self):
        self.withdraw() 
        new_window = StudentWindow()
        new_window.title("Student Management System")

    #=======Teacher personal detail page===========#
    def teacher_registration(self):
        self.withdraw()
        new_window=TeacherWindow()
        new_window.title("School Management System")

    def student_login(self):
        global student_username, student_password
        #========email and password from entry box=========#
        student_username = student_email_entry.get()
        student_password = student_password_entry.get()

        '''#========check username and password from database=======#
        if student_username == "" and student_password == "":
            messagebox.showerror("Empty Fields", "Please enter both email and password.")
            return
        if student_username == "":
            messagebox.showerror("Missing Email", "Please enter your email address.")
            return
        if student_password == "":
            messagebox.showerror("Missing Password", "Please enter your password.")
            return
        else:        
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #fetch username and password
                cur.execute("select email, concat(first_name,'@',student_id) as password from student where email = %s and concat(first_name,'@',student_id) = %s", (student_username, student_password))

                db_records = cur.fetchone()
                if student_username == db_records[0] and student_password == db_records[1]:
                    #======open home window===========#
                    self.withdraw()
                    new_window = StudentHomeWindow()
                    new_window.title("School Management System")
                    new_window.profile_frame()
                    messagebox.showinfo("Login Successful", "Welcome back!")
                else:
                    messagebox.showerror("Login Failed", "Invalid email or password. Please try again.")

                #clear the textbox
                student_email_entry.delete(0, tk.END)
                student_password_entry.delete(0, tk.END)

                #close the connection
                con.close()

            except Exception as e:
                print("Error :", e)'''
        self.withdraw()
        new_window = StudentHomeWindow()
        new_window.title("School Management System")
        new_window.profile_frame()

    #=========Teacher home page===========#
    def teacher_login(self):
        global teacher_username, teacher_password
        #========email and password from entry box=========#
        teacher_username = teacher_email_entry.get()
        teacher_password = teacher_password_entry.get()

        '''#========check username and password from database=======#
        if teacher_username == "" and teacher_password == "":
            messagebox.showerror("Empty Fields", "Please enter both email and password.")
            return
        if teacher_username == "":
            messagebox.showerror("Missing Email", "Please enter your email address.")
            return
        if teacher_password == "":
            messagebox.showerror("Missing Password", "Please enter your password.")
            return
        else:        
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #fetch username and password
                cur.execute("select email, concat(first_name,'@',staff_id) as password from staff where email = %s and concat(first_name,'@',staff_id) = %s", (teacher_username,teacher_password))

                db_records = cur.fetchone()
                
                if not db_records:
                    messagebox.showerror("Login Failed", "Invalid email or password. Please try again.")
                    # return
                else:
                    print(db_records)
                    if teacher_username == db_records[0] and teacher_password == db_records[1]:
                        #======open home window===========#
                        self.withdraw()
                        new_window=TeacherHomeWindow()
                        new_window.title("School Management System")
                        new_window.profile_frame()
                        messagebox.showinfo("Login Successful", "Welcome back!")

                #clear the textbox
                teacher_email_entry.delete(0, tk.END)
                teacher_password_entry.delete(0, tk.END)

                #close the connection
                con.close()

            except Exception as e:
                print("Error :", e)'''

        self.withdraw()
        new_window=TeacherHomeWindow()
        new_window.title("School Management System")
        new_window.profile_frame()
        messagebox.showinfo("Login Successful", "Welcome back!")

class AdminLoginWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="#B5FF7D")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        #===call the return to main
        def return_to_home():
            self.destroy()
            root.deiconify()

        def underline_to_label(event):
            self.underline_label = tk.Label(self.admin_login_frame,bg="blue")
            self.underline_label.place(x = 163, y = 350, width = 150, height=4)

        def noline_to_label(event):
            self.underline_label = tk.Label(self.admin_login_frame,bg="white")
            self.underline_label.place(x = 163, y = 350, width = 150, height=4)

        def admin_home_page():
            admin_username = self.admin_username_entry.get()
            admin_password = self.admin_password_entry.get()

            '''if not admin_username and not admin_password:
                messagebox.showerror("Error", "Please enter a username and password.")
                return
            if not admin_username:
                messagebox.showerror("Error", "Please enter a username.")
                return 
            if not admin_password:
                messagebox.showerror("Error", "Please enter a password.")
                return
            if admin_username == "admin" and admin_password == "secret":
                self.destroy()
                new_window = AdminHomeWindow()
                new_window.title("School Management System")
                new_window.add_standard_frame()
                messagebox.showinfo("Login Successful","Welcome back, Administrator!")
            else:
                messagebox.showerror("Login Failed", "Invalid admin login credentials. Please try again.")'''
                
            self.destroy()
            new_window = AdminHomeWindow()
            new_window.title("School Management System")
            new_window.add_standard_frame()

        #====show password====#
        self.show = "*"
        def show_password():
            global show
            if self.show  == "*":
                self.hide_image_button.configure(image = self.show_image)
                self.admin_password_entry.configure(show = "")
                self.show = ""
            else:
                self.hide_image_button.configure(image = self.hide_image)
                self.admin_password_entry.configure(show = "*")
                self.show = "*" 
 
        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        self.admin_login_frame = ctk.CTkFrame(self, width = 420, height=300, corner_radius=0, border_width=2, border_color="green", fg_color="white")

        # #======other widgets=========#
        self.admin_login_panel = ctk.CTkLabel(self.admin_login_frame, text = "Admin Login Panel", text_color="white", font = ("Verdana Pro", 18), width = 420, height = 40, fg_color="#1D49CB")
        self.admin_login_panel.place(x = 0, y = 0)

        #========admin username===========#
        self.admin_username_entry = ctk.CTkEntry(self.admin_login_frame, border_width=0, border_color="black", width = 320, height = 30, corner_radius=0, font = ("Verdana Pro", 15), placeholder_text="Admin username", fg_color="white")
        self.admin_username_entry.place(x = 18, y = 70)
        self.admin_username_entry.bind("<FocusIn>", lambda e : self.line1.config(bg = "#074173"))
        self.admin_username_entry.bind("<FocusOut>", lambda e : self.line1.config(bg = "grey"))

        self.line1 = tk.Label(self.admin_login_frame, bg="grey")
        self.line1.place(x = 30, y = 130, width = 440, height = 2)

        #===========admin password===========#
        self.admin_password_entry = ctk.CTkEntry(self.admin_login_frame, border_width=0, border_color="black", width = 320, height = 30, corner_radius=0, font = ("Verdana Pro", 16), placeholder_text="Admin password", fg_color="white", show = "*")
        self.admin_password_entry.place(x = 18, y = 130)
        self.admin_password_entry.bind("<FocusIn>", lambda e : self.line2.config(bg = "#074173"))
        self.admin_password_entry.bind("<FocusOut>", lambda e : self.line2.config(bg = "grey"))

        self.line2 = tk.Label(self.admin_login_frame, bg="grey")
        self.line2.place(x = 30, y = 205, width = 440, height = 2)

        #========hide image=========#
        self.hide_image = ctk.CTkImage(light_image=Image.open("image/hide.png"), dark_image=Image.open("image/hide.png"), size = (25, 25))

        self.show_image = ctk.CTkImage(light_image=Image.open("image/eye.png"), dark_image=Image.open("image/eye.png"), size = (25, 25))

        self.hide_image_button = ctk.CTkButton(self.admin_login_frame, text = "", image = self.hide_image, width = 0, height = 0, hover="disabled", fg_color="transparent", bg_color="transparent", cursor = "hand2", command=show_password)
        self.hide_image_button.place(x = 342, y = 130)
            
        #========login button==========#
        self.admin_login_button = ctk.CTkButton(self.admin_login_frame, text = "LOGIN", font = ("Verdana Pro", 18), fg_color="#074173", corner_radius=0, width = 120, height = 35, command=admin_home_page)
        self.admin_login_button.place(x = 25, y = 200)

        #=====back to home==========#
        self.admin_logout_button = ctk.CTkButton(self.admin_login_frame, text = "Back to Home",width = 0, height = 0, font = ("Consolas", 18), text_color="blue", hover = "disabled", cursor = "hand2", fg_color="transparent" , command= return_to_home)
        self.admin_logout_button.place(x = 130, y = 250)

        self.admin_logout_button.bind("<Enter>", underline_to_label)
        self.admin_logout_button.bind("<Leave>", noline_to_label)

        self.admin_login_frame.place(x = 550 , y = 200)

class StudentWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="#B5FF7D")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        #======functions=======#
        self.file = ""
        def upload_photo():
            global file
            photo_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("JPG Files", "*.jpg"),("PNG Files", "*.png"),("All files", "*.*")], initialdir="C:/Users/vikas/OneDrive/Documents", title="Open File")

            if photo_path:
                self.file = photo_path
                self.file_path_label.configure(text = f"{os.path.basename(photo_path)}", text_color = "red")

        def open_calendar():
            global cal
            calendar_window = ctk.CTkToplevel(self)
            calendar_window.geometry("300x200+950+700")
            calendar_window.title("Calendar")
            calendar_window.resizable(False, False)

            cal = tkcalendar.Calendar(calendar_window,date_pattern = "yyyy-mm-dd" ,background = "#388E3C")
            cal.pack(fill = "both", expand = True)
            cal.bind("<<CalendarSelected>>", lambda e : grab_date(cal))

            calendar_window.grab_set()

        def grab_date(event):
            global cal
            self.dob_entry.delete(0, tk.END)
            self.dob_entry.insert(tk.END, cal.get_date())

        def return_to_main():
            self.destroy()
            root.deiconify()

        #=======fetch standard record ==========#
        def fetch_std_record():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                cur.execute("select std_name from standard")

                records = cur.fetchall()

                std_list = []
                for record in records:
                    std_list.append(record[0])
                
                #======configure the option menu for standard values
                self.standard_values = std_list
                self.standard_option.configure(values = self.standard_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        
        #=======fetch division record ==========#
        def fetch_div_record():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                cur.execute("select div_name from division group by div_name")

                records = cur.fetchall()

                div_list = []
                for record in records:
                    div_list.append(record[0])
                
                #======configure the option menu for standard values
                self.division_values= div_list
                self.division_option.configure(values = self.division_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        def student_registration():
            first_name = self.firstname_entry.get()
            last_name = self.lastname_entry.get()
            std = std_var_reg.get()
            div = div_var_reg.get()
            father_name = self.father_entry.get()
            mother_name = self.mother_entry.get()
            gender = gender_value.get()
            contact = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_textbox.get("0.0", tk.END)
            city = self.city_entry.get()
            pincode = self.pincode_var.get()
            dob = self.dob_var.get()
            nationality = self.nationality_entry.get()
            religion = self.religion_entry.get()
            mother_tongue = self.mothertongue_entry.get()
            image_path = self.file

            if (first_name or last_name or std or div or father_name or mother_name or gender or contact or email or address or city or pincode or dob or nationality or religion or mother_tongue or image_path) == "":
                messagebox.showerror("Error", "Please fill out all required fields before submitting.")
            
            else:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    insert_query = "insert into student(first_name, last_name, std_name, div_name, father_name , mother_name, gender, mobile, email, address, city, pincode, dob, nationality, religion, mother_tongue, image_path) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    insert_value = (first_name, last_name, std, div, father_name, mother_name, gender, contact, email, address, city, pincode, dob, nationality, religion, mother_tongue, image_path)

                    #executing the insert query
                    cur.execute(insert_query, insert_value)
                    
                    #commit the changes
                    con.commit()

                    #show message box after inserting values
                    messagebox.showinfo("Registration Successfull", "Registration submitted! You will receive an email notification once your account is activated.")

                    #close the connection
                    con.close()

                    #return to main_window
                    return_to_main()

                except Exception as e:
                    print("Error ", e)

        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        #======Student===========#
        self.student_register_frame = ctk.CTkFrame(self, width = 800, height=700, corner_radius=0, border_width=2, border_color="green", fg_color="white")

        self.personal_heading_label = ctk.CTkLabel(self.student_register_frame, text = "Student Personal Information", fg_color="green", text_color="white", width = 800, height = 45, font=("Consolas", 30))
        self.personal_heading_label.place(x = 0, y = 0)

        #=======label and entry========
        self.reg_no_label = ctk.CTkLabel(self.student_register_frame, text = "Gen .Reg. No.", font = ("Consolas", 20))
        self.reg_no_label.place(x = 10, y = 60)

        self.firstname_label = ctk.CTkLabel(self.student_register_frame, text = "First Name", font = ("Consolas", 20))
        self.firstname_label.place(x = 10, y = 100)

        self.firstname_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.firstname_entry.place(x = 180, y = 100)

        self.lastname_label = ctk.CTkLabel(self.student_register_frame, text = "Last Name", font = ("Consolas", 20))
        self.lastname_label.place(x = 10, y = 150)

        self.lastname_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.lastname_entry.place(x = 180, y = 150)

        self.std_label = ctk.CTkLabel(self.student_register_frame, text = "Standard", font = ("Consolas", 20))
        self.std_label.place(x = 10, y = 200)

        self.standard_values = []
        std_var_reg = tk.StringVar(value="")
        self.standard_option = ctk.CTkOptionMenu(self.student_register_frame, width = 200, height = 30, corner_radius=2, values=self.standard_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=std_var_reg)
        self.standard_option.place(x = 180, y = 200)

        self.section_label = ctk.CTkLabel(self.student_register_frame, text = "Section", font = ("Consolas", 20))
        self.section_label.place(x = 10, y = 250)

        self.division_values = []
        div_var_reg = tk.StringVar(value="")
        self.division_option = ctk.CTkOptionMenu(self.student_register_frame, width = 200, height = 30, corner_radius=2, values=self.division_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18),variable=div_var_reg)
        self.division_option.place(x = 180, y = 250)
        
        self.father_label = ctk.CTkLabel(self.student_register_frame, text = "Father Name", font = ("Consolas", 20))
        self.father_label.place(x = 10, y = 300)

        self.father_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.father_entry.place(x = 180, y = 300)

        self.mother_label = ctk.CTkLabel(self.student_register_frame, text = "Mother Name", font = ("Consolas", 20))
        self.mother_label.place(x = 10, y = 350)

        self.mother_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.mother_entry.place(x = 180, y = 350)

        self.gender_label = ctk.CTkLabel(self.student_register_frame, text = "Gender", font = ("Consolas", 20))
        self.gender_label.place(x = 10, y = 400)

        gender_value= ctk.StringVar(value = "other")
        self.male_radio=ctk.CTkRadioButton(self.student_register_frame,text="Male",value="Male",variable=gender_value,font=("Consolas",17), fg_color="green", hover_color="green")
        self.male_radio.place(x=180,y=400)

        self.female_radio=ctk.CTkRadioButton(self.student_register_frame,text="Female",value="Female",variable=gender_value,font=("Consolas",17), fg_color="green",hover_color="green")
        self.female_radio.place(x=280,y=400)

        self.phone_label = ctk.CTkLabel(self.student_register_frame, text = "Contact No.", font = ("Consolas", 20))
        self.phone_label.place(x = 10, y = 450)

        self.phone_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.phone_entry.place(x = 180, y = 450)

        self.email_label = ctk.CTkLabel(self.student_register_frame, text = "Parent's Email", font = ("Consolas", 20))
        self.email_label.place(x = 10, y = 500)

        self.email_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.email_entry.place(x = 180, y = 500)

        self.address_label = ctk.CTkLabel(self.student_register_frame, text = "Residential Address", font = ("Consolas", 20), wraplength=125)
        self.address_label.place(x = 10, y = 550)

        self.address_textbox = ctk.CTkTextbox(self.student_register_frame, height = 80, corner_radius=0, border_width=2, border_color="grey", scrollbar_button_hover_color="green", font = ("Consolas", 20), wrap = "word")
        self.address_textbox.place(x = 180, y = 550)

        self.city_label = ctk.CTkLabel(self.student_register_frame, text = "City", font = ("Consolas", 20), wraplength=125)
        self.city_label.place(x = 10, y = 650)

        self.city_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.city_entry.place(x = 180, y = 650)

        self.pincode_label = ctk.CTkLabel(self.student_register_frame, text = "Pincode", font = ("Consolas", 20), wraplength=125)
        self.pincode_label.place(x = 400, y = 100)

        self.pincode_var = tk.IntVar()
        self.pincode_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30, textvariable=self.pincode_var)
        self.pincode_entry.place(x = 580, y = 100)

        self.dob_label = ctk.CTkLabel(self.student_register_frame, text = "Date of Birth", font = ("Consolas", 20))
        self.dob_label.place(x = 400, y = 150)

        self.dob_var = tk.StringVar()
        self.dob_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 171, border_color="grey", corner_radius=0, height= 30, textvariable=self.dob_var)
        self.dob_entry.place(x = 580, y = 150)

        self.calendar_image = ctk.CTkImage(light_image=Image.open("image/calendar.png"), dark_image=Image.open("image/calendar.png"), size = (30, 30))

        self.calendar_button = ctk.CTkButton(self.student_register_frame, width = 0, height = 0, fg_color="transparent", hover="disabled", bg_color="transparent", text = "", image = self.calendar_image, command=open_calendar)
        self.calendar_button.place(x = 750, y = 145)
        
        self.nationality_label = ctk.CTkLabel(self.student_register_frame, text = "Nationality", font = ("Consolas", 20))
        self.nationality_label.place(x = 400, y = 200)

        self.nationality_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.nationality_entry.place(x = 580, y = 200)

        self.religion_label = ctk.CTkLabel(self.student_register_frame, text = "Religion", font = ("Consolas", 20))
        self.religion_label.place(x = 400, y = 250)

        self.religion_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.religion_entry.place(x = 580, y = 250)

        self.mothertongue_label = ctk.CTkLabel(self.student_register_frame, text = "Mother Tongue", font = ("Consolas", 20))
        self.mothertongue_label.place(x = 400, y = 300)

        self.mothertongue_entry = ctk.CTkEntry(self.student_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.mothertongue_entry.place(x = 580, y = 300)

        self.upload_photo_label = ctk.CTkLabel(self.student_register_frame, text = "Upload Photo", font = ("Consolas", 20))
        self.upload_photo_label.place(x = 400, y = 350)

        self.upload_photo_button = ctk.CTkButton(self.student_register_frame, text = "Choose File", width = 150, height = 35, border_width=2, border_color="black", font = ("Consolas", 20), text_color="black", fg_color="#D8D9DA", corner_radius=50, hover_color="white", cursor = "hand2", command=upload_photo)
        self.upload_photo_button.place(x = 580, y = 350)

        self.file_path_label = ctk.CTkLabel(self.student_register_frame, text = "No File Choosen", font = ("Consolas", 17), text_color="black")
        self.file_path_label.place(x = 580, y = 390)

        self.register_button = ctk.CTkButton(self.student_register_frame, text = "Register", width = 150, height = 40, border_width=2, border_color="green", font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=student_registration)
        self.register_button.place(x = 500, y = 450)
        HoverColor(self.register_button)

        #============calling the function=========#
        fetch_std_record()
        fetch_div_record()

        self.student_register_frame.place(x = 370, y = 120)

#======Teacher personal detail page=====#
class TeacherWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="#B5FF7D")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        self.file = ""
        def upload_photo():
            global file
            photo_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("JPG Files", ".jpg"),("PNG Files", ".png"),("All files", ".")], initialdir="C:/Users/Vikas/OneDrive/Documents", title="Open File")

            if photo_path:
                self.file = photo_path
                self.file_path_label.configure(text = f"{os.path.basename(photo_path)}", text_color = "red")
    
        def return_to_main():
            self.destroy()
            root.deiconify()

        def teacher_registration():
            global file
            first_name = self.firstname_entry.get()
            last_name = self.lastname_entry.get()
            email = self.email_entry.get()
            mobile = self.mobile_entry.get()
            qualification = self.qualification_entry.get()
            address = self.address_textbox.get("0.0", tk.END)
            city = self.city_entry.get()
            pincode = self.pincode_entry.get()
            gender = self.gender_value.get()
            path = self.file
            
            if not first_name or not last_name or not email or not mobile or not qualification or not address or not city or not pincode or not gender or not path:
                messagebox.showerror("Error", "Please fill out all required fields before submitting.")
            
            else:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    insert_query = "insert into staff(first_name, last_name, email, mobile, qualification, address, city, pincode, gender, image_path) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    insert_value = (first_name, last_name, email, mobile, qualification, address, city, pincode, gender, path)

                    #executing the insert query
                    cur.execute(insert_query, insert_value)
                    
                    #commit the changes
                    con.commit()

                    #show message box after inserting values
                    messagebox.showinfo("Registration Successfull", "Registration submitted! You will receive an email notification once your account is activated.")

                    #close the connection
                    con.close()

                    

                except Exception as e:
                    print("Error ", e)

            #return to main_window
            return_to_main()

        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        #=======================#
        self.teacher_register_frame = ctk.CTkFrame(self, width = 800, height=700, corner_radius=0,  border_width=2, border_color="green", fg_color="white")

        self.teacher_personal_heading_label = ctk.CTkLabel(self.teacher_register_frame, text = "Teacher Personal Information", fg_color="green", text_color="white", width = 800, height = 45, font=("Consolas", 30))
        self.teacher_personal_heading_label.place(x = 0, y = 0)

        #=======label and entry========
        self.firstname_label = ctk.CTkLabel(self.teacher_register_frame, text = "First Name:", font = ("Consolas", 20))
        self.firstname_label.place(x = 200, y = 60)

        self.firstname_entry = ctk.CTkEntry(self.teacher_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.firstname_entry.place(x = 370, y = 60)

        self.lastname_label = ctk.CTkLabel(self.teacher_register_frame, text = "Last Name:", font = ("Consolas", 20))
        self.lastname_label.place(x = 200, y = 100)

        self.lastname_entry = ctk.CTkEntry(self.teacher_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.lastname_entry.place(x = 370, y = 100)

        self.email_label = ctk.CTkLabel(self.teacher_register_frame, text = "Email:", font = ("Consolas", 20))
        self.email_label.place(x = 200, y = 150)

        self.email_entry = ctk.CTkEntry(self.teacher_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.email_entry.place(x = 370, y = 150)

        self.mobile_label = ctk.CTkLabel(self.teacher_register_frame, text = "Mobile no:", font = ("Consolas", 20))
        self.mobile_label.place(x = 200, y = 200)

        self.mobile_entry = ctk.CTkEntry(self.teacher_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.mobile_entry.place(x = 370, y = 200)
        
        self.qualification_label = ctk.CTkLabel(self.teacher_register_frame, text = "Qualification:", font = ("Consolas", 20))
        self.qualification_label.place(x = 200, y = 250)

        self.qualification_entry = ctk.CTkEntry(self.teacher_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.qualification_entry.place(x = 370, y = 250)

        self.address_label = ctk.CTkLabel(self.teacher_register_frame, text = "Residential Address:", font = ("Consolas", 20), wraplength=125)
        self.address_label.place(x = 200, y = 300)

        self.address_textbox = ctk.CTkTextbox(self.teacher_register_frame, height = 80, corner_radius=0, border_width=2, border_color="grey", scrollbar_button_hover_color="green", font = ("Consolas", 20), wrap = "word")
        self.address_textbox.place(x = 370, y = 300)

        self.city_label = ctk.CTkLabel(self.teacher_register_frame, text = "City:", font = ("Consolas", 20), wraplength=125)
        self.city_label.place(x = 200, y = 400)

        self.city_entry = ctk.CTkEntry(self.teacher_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.city_entry.place(x = 370, y = 400)

        self.pincode_label = ctk.CTkLabel(self.teacher_register_frame, text = "Pincode:", font = ("Consolas", 20), wraplength=125)
        self.pincode_label.place(x = 200, y = 450)

        self.pincode_entry = ctk.CTkEntry(self.teacher_register_frame, font = ("Consolas", 20), width = 200, border_color="grey", corner_radius=0, height= 30)
        self.pincode_entry.place(x = 370, y = 450)

        self.gender_label = ctk.CTkLabel(self.teacher_register_frame, text = "Gender:", font = ("Consolas", 20))
        self.gender_label.place(x = 200, y = 500)

        self.gender_value=ctk.StringVar(value="")
        self.male_radio=ctk.CTkRadioButton(self.teacher_register_frame,text="Male",value="Male",variable=self.gender_value,font=("Consolas",17), fg_color="green", hover_color="green")
        self.male_radio.place(x=370,y=500)

        self.female_radio=ctk.CTkRadioButton(self.teacher_register_frame,text="Female",value="Female",variable=self.gender_value,font=("Consolas",17), fg_color="green", hover_color="green")
        self.female_radio.place(x=460,y=500)

        self.upload_photo_label = ctk.CTkLabel(self.teacher_register_frame, text = "Upload Photo:", font = ("Consolas", 20))
        self.upload_photo_label.place(x = 200, y = 550)

        self.upload_photo_button = ctk.CTkButton(self.teacher_register_frame, text = "Choose File", width = 150, height = 35, border_width=2, border_color="black", font = ("Consolas", 20), text_color="black", fg_color="#D8D9DA", corner_radius=50, hover_color="white", cursor = "hand2", command=upload_photo)
        self.upload_photo_button.place(x = 370, y = 550)

        self.file_path_label = ctk.CTkLabel(self.teacher_register_frame, text = "No File Choosen", font = ("Consolas", 17), text_color="black")
        self.file_path_label.place(x = 380, y = 590)

        self.register_button = ctk.CTkButton(self.teacher_register_frame, text = "Register", width = 150, height = 40, border_width=2, border_color="green", font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=teacher_registration)
        self.register_button.place(x = 290, y = 630)
        HoverColor(self.register_button)

        self.teacher_register_frame.place(x = 370, y = 120)

class AdminHomeWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1536x864-10-7")

        #======switch_frame=======#
        def switch_frame(page):
            for frame in self.admin_rightside_frame.winfo_children():
                frame.destroy()
                self.update()
            page()

        #=====return to main window=======#
        def return_to_adminlogin():
            self.destroy()
            AdminLoginWindow()
        
        #=====fetching the std record=====#
        def fetch_all_std_value(e):
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                cur.execute("select std_name from standard")

                records = cur.fetchall()

                std_list = []
                for record in records:
                    std_list.append(record[0])
                
                #======configure the option menu for standard values
                self.select_standard_values = std_list
                self.select_standard_opt.configure(values = self.select_standard_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        #======student home frame=======#
        self.admin_homepage_frame = ctk.CTkFrame(self, width = 1526, height=730, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        self.admin_sidebar_frame = ctk.CTkFrame(self.admin_homepage_frame, width = 400, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        self.admin_sidebar_head_label = ctk.CTkLabel(self.admin_sidebar_frame, text = "Admin Menu", height = 40, width = 400, fg_color="green", font = ("Consolas", 25), text_color="white")
        self.admin_sidebar_head_label.place(x = 0, y = 0)

        #=======sidebar menu========#
        self.add_standard_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Add Standard", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command= lambda : switch_frame(page = self.add_standard_frame))
        self.add_standard_button.place(x = 5, y = 45)

        self.add_division_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Add Division", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command= lambda : switch_frame(page = self.add_divison_frame))
        self.add_division_button.place(x = 5, y = 90)
        self.add_division_button.bind("<Button-1>", fetch_all_std_value)

        self.add_subject_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Add Subject", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command= lambda : switch_frame(page = self.add_subject_frame))
        self.add_subject_button.place(x = 5, y = 135)
        # self.add_division_button.bind("<Button-1>", fetch_all_std_value)

        self.assign_class_all = ctk.CTkButton(self.admin_sidebar_frame, text = "Assign Teacher & Subjects", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command= lambda : switch_frame(page = self.assign_staff_frame))
        self.assign_class_all.place(x = 5, y = 180)

        self.staff_report_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Staff Report", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=lambda : switch_frame(page=self.staff_report_frame))
        self.staff_report_button.place(x = 5, y = 225)

        self.leave_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Leave", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command= lambda : switch_frame(page = self.leave_frame))
        self.leave_button.place(x = 5, y = 270)

        self.student_report_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Student Reports", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command= lambda : switch_frame(page = self.student_report_frame))
        self.student_report_button.place(x = 5, y = 315)

        self.feedback_report_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Feedback", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command= lambda : switch_frame(page = self.feedback_frame))
        self.feedback_report_button.place(x = 5, y = 360)

        self.admin_announcemnt_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Announcement", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command= lambda : switch_frame(page = self.make_announcement_frame))
        self.admin_announcemnt_button.place(x = 5, y = 405)

        self.logout_button = ctk.CTkButton(self.admin_sidebar_frame, text = "Logout", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=return_to_adminlogin)
        self.logout_button.place(x = 5, y = 450)

        self.admin_sidebar_frame.place(x = 10, y = 10)

        #=====rightside=========#
        self.admin_rightside_frame = ctk.CTkFrame(self.admin_homepage_frame, width = 1092, height=700, corner_radius=0,  border_width=None, fg_color="white")
        self.admin_rightside_frame.place(x = 420, y = 10)

        self.admin_homepage_frame.place(x = 5, y = 100)
    
    def add_standard_frame(self):
        self.standard_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=600, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.standard_page_frame, text = "Add Standard")
        #=======show record========#
        def show_std_record_auto():
            global count
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                cur.execute("select std_name from standard")

                records = cur.fetchall()

                #show record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_standard_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], ), tags=("evenrow",))
                    else:
                        self.add_standard_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], ), tags=("oddrow",))

                    self.count += 1

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #========add record==========#
        self.count = 0
        def add_std_record():
            global count
            standard = self.standard_entry.get().lower()

            if standard == "":
                messagebox.showerror("Error", "Please enter a standard.")
            else:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #insert data from entry box into treeview
                    if self.count % 2 == 0:
                        self.add_standard_tree.insert(parent = "", index = tk.END, iid = self.count, values=(standard, ), tags=("evenrow",))
                    else:
                        self.add_standard_tree.insert(parent = "", index = tk.END, iid = self.count, values=(standard, ), tags=("oddrow",))

                    self.count += 1

                    #insert data from entry box to database
                    insert_query = "insert into standard(std_name) values(%s)"
                    insert_value = (standard, )

                    cur.execute(insert_query, insert_value)
                    
                    self.std_msg_label.configure(text = "Standard Added Successfully", text_color = "red")

                    #commit the changes
                    con.commit()

                    #clear the entry box
                    self.standard_entry.delete(0, tk.END)

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)
        
        def clear_record():
            #=======delete selected record==========#
            data = self.add_standard_tree.selection() 

            empty_list = []
            for all in data:
                value = self.add_standard_tree.item(all, "values")
                empty_list.append(value[0])
                self.add_standard_tree.delete(all)

            for std in empty_list:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    delete_query = "delete from standard where std_name = %s"
                    delete_value = (std,)

                    #execute the cursor
                    cur.execute(delete_query, delete_value)

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

        #======treeview setting=========#
        #add some style
        style = ttk.Style()

        #pick a theme
        style.theme_use("alt")

        #configure the tree view color
        style.configure("Treeview", 
                        background = "#D3D3D3",
                        rowheight = 25,
                        fieldbackground = "#D3D3D3", font = ("Consolas", 14))
        
        style.configure("mystyle.Treeview", font=('Consolas', 15))

        #configure the selected color
        style.configure("Treeview", background = [("selected", "#347083")])

        #increse the font size of heading
        style.configure("Treeview.Heading", font=("Consolas", 18))

        self.data_frame = tk.Frame(self.standard_page_frame, bg = "lightgrey", borderwidth=5, relief="groove")
        self.data_frame.place(x = 500, y = 320, width = 300, height = 300)

        #create a scrollbar
        y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
        x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

        y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

        #create a treeview
        self.add_standard_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
        self.add_standard_tree.pack(fill = "both", expand= True)

        #define our columns
        self.add_standard_tree["columns"] = ("Standard Name",)

        #format column
        self.add_standard_tree.column("Standard Name", anchor="center", width = 100, minwidth=100)

        #create a heading
        self.add_standard_tree.heading("Standard Name", text = "Standard Name", anchor = "center")

        #Create striped to our tages
        self.add_standard_tree.tag_configure("oddrow", background="white")
        self.add_standard_tree.tag_configure("evenrow", background="lightblue")

        #========call the function==========#
        show_std_record_auto()

        #=====creating a entry box========#
        self.standard_label = ctk.CTkLabel(self.standard_page_frame, text = "Standard Name:", font = ("Consolas", 20), text_color="green")
        self.standard_label.place(x = 245, y = 100)

        self.standard_entry = ctk.CTkEntry(self.standard_page_frame, width = 210, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.standard_entry.place(x = 410, y = 100)

        self.add_button = ctk.CTkButton(self.standard_page_frame, text = "Add", width = 100, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=0, hover_color="white", cursor = "hand2", border_width=2, border_color="green", command = add_std_record)
        self.add_button.place(x = 410, y = 140)

        # self.edit_button = ctk.CTkButton(self.standard_page_frame, text = "Edit", width = 100, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=0, hover_color="white", cursor = "hand2", border_width=2, border_color="green", command = edit_standard_func)
        # self.edit_button.place(x = 520, y = 140)

        self.clear_button = ctk.CTkButton(self.standard_page_frame, text = "Clear", width = 100, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=0, hover_color="white", cursor = "hand2", border_width=2, border_color="green", command=clear_record)
        self.clear_button.place(x = 520, y = 140)

        self.std_msg_label = ctk.CTkLabel(self.standard_page_frame, text = "", font = ("Consolas", 20), text_color="green")
        self.std_msg_label.place(x = 365, y = 220)

        self.standard_page_frame.place(x = 0, y = 0)

    def add_divison_frame(self):
        self.divison_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=600, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.divison_page_frame, text = "Add Division")

        #=======show record========#
        def show_div_record_auto():
            global count
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                cur.execute("select div_name, std_name, seat from division")

                records = cur.fetchall()

                #show record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_division_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2]), tags=("evenrow",))
                    else:
                        self.add_division_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2]), tags=("oddrow",))
                    self.count += 1

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #=====add div record======#
        self.count = 0
        def add_div_record():
            global count
            division = self.division_entry.get().upper()
            seat = self.seat_entry.get()
            standard_opt = std_var.get()

            if not division and not seat and not standard_opt:
                messagebox.showerror("Error", "Please enter a standard.")
                return
            if not division:
                messagebox.showerror("Error", "Please enter a division.")
                return
            if not seat:
                messagebox.showerror("Error", "Please enter a seat.")
                return
            if not standard_opt:
                messagebox.showerror("Error", "Please choose a standard.")
                return
            else:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #insert data from entry box into treeview
                    if self.count % 2 == 0:
                        self.add_division_tree.insert(parent = "", index = tk.END, iid = self.count, values=(division, standard_opt, seat), tags=("evenrow",))
                    else:
                        self.add_division_tree.insert(parent = "", index = tk.END, iid = self.count, values=(division, standard_opt, seat), tags=("oddrow",))

                    self.count += 1

                    #insert data from entry box to database
                    insert_query = "insert into division(div_name, std_name, seat) values(%s, %s, %s)"
                    insert_value = (division, standard_opt, seat)

                    cur.execute(insert_query, insert_value)
                    
                    self.div_msg_label.configure(text = "Record Added Successfully", text_color = "red")

                    #commit the changes
                    con.commit()

                    #clear the entry box
                    self.division_entry.delete(0, tk.END)
                    self.seat_entry.delete(0, tk.END)
                    std_var.set("")

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)
        
        #========clear the div record from both db and treeview
        def clear_div_record():
            #=======delete selected record==========#
            data = self.add_division_tree.selection() 

            empty_div_list = []
            for all in data:
                # print(all)
                value = self.add_division_tree.item(all, "values")
                empty_div_list.append(value)
                self.add_division_tree.delete(all)

            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                delete_query = "delete from division where div_name = %s and std_name = %s and seat = %s"
                delete_value = empty_div_list

                #execute the delete query
                cur.executemany(delete_query, delete_value)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #=======treeview setting========#
        #add some style
        style = ttk.Style()

        #pick a theme
        style.theme_use("alt")

        #configure the tree view color
        style.configure("Treeview", 
                        background = "#D3D3D3",
                        rowheight = 25,
                        fieldbackground = "#D3D3D3", font = ("Consolas", 14))
        
        style.configure("mystyle.Treeview", font=('Consolas', 15))

        #configure the selected color
        style.configure("Treeview", background = [("selected", "#347083")])

        #increse the font size of heading
        style.configure("Treeview.Heading", font=("Consolas", 18))

        self.data_frame = tk.Frame(self.divison_page_frame, bg = "lightgrey", borderwidth=5, relief="groove")
        self.data_frame.place(x = 400, y = 430, height = 300)

        #create a scrollbar
        y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
        x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

        y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

        #create a treeview
        self.add_division_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
        self.add_division_tree.pack(fill = "both", expand= True)

        #define our columns
        self.add_division_tree["columns"] = ("Division Name", "Standard Name", "Seat")

        #format column
        self.add_division_tree.column("Division Name", anchor="center", width = 200, minwidth=200)
        self.add_division_tree.column("Standard Name", anchor="center", width = 200, minwidth=200)
        self.add_division_tree.column("Seat", anchor="center", width = 100, minwidth=100)

        #create a heading
        self.add_division_tree.heading("Division Name", text = "Division Name", anchor = "center")
        self.add_division_tree.heading("Standard Name", text = "Standard Name", anchor = "center")
        self.add_division_tree.heading("Seat", text = "Seat", anchor = "center")

        #Create striped to our tages
        self.add_division_tree.tag_configure("oddrow", background="white")
        self.add_division_tree.tag_configure("evenrow", background="lightblue")
        #==========================#

        #========call the function==========#
        show_div_record_auto()

        #=====creating a entry box========#
        self.division_label = ctk.CTkLabel(self.divison_page_frame, text = "Division Name:", font = ("Consolas", 20), text_color="green")
        self.division_label.place(x = 245, y =100)

        self.division_entry = ctk.CTkEntry(self.divison_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.division_entry.place(x = 410, y = 100)

        self.seat_label = ctk.CTkLabel(self.divison_page_frame, text = "Seat:", font = ("Consolas", 20), text_color="green")
        self.seat_label.place(x = 345, y =150)

        self.seat_entry = ctk.CTkEntry(self.divison_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.seat_entry.place(x = 410, y = 150)

        self.select_standard_label = ctk.CTkLabel(self.divison_page_frame, text = "Standard:", font = ("Consolas", 20), text_color="green")
        self.select_standard_label.place(x = 300, y = 200)

        self.select_standard_values = []
        std_var = tk.StringVar()        
        self.select_standard_opt = ctk.CTkOptionMenu(self.divison_page_frame, width = 200, height = 30, corner_radius=2, values=self.select_standard_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=std_var)
        self.select_standard_opt.place(x = 410, y = 200)

        self.add_divison_button = ctk.CTkButton(self.divison_page_frame, text = "Add", width = 100, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=0, hover_color="white", cursor = "hand2", border_width=2, border_color="green", command = add_div_record)
        self.add_divison_button.place(x = 410, y = 250)

        self.delete_divison_button = ctk.CTkButton(self.divison_page_frame, text = "Clear", width = 100, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=0, hover_color="white", cursor = "hand2", border_width=2, border_color="green", command = clear_div_record)
        self.delete_divison_button.place(x = 515, y = 250)

        self.div_msg_label = ctk.CTkLabel(self.divison_page_frame, text = "", font = ("Consolas", 20), text_color="green")
        self.div_msg_label.place(x = 365, y = 310)

        self.divison_page_frame.place(x = 0, y = 0)

    def add_subject_frame(self):
        self.subject_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.subject_page_frame, text = "Add Subject")

        #===========function============#

        def show_subject_record():
            global count
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                cur.execute("select subject_id, subject_name from subject")

                records = cur.fetchall()

                self.count = 0
                #show record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1]), tags=("evenrow",))
                    else:
                        self.add_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1] ), tags=("oddrow",))
                    self.count += 1

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        def add_subject_func():
            global count
            subject_name = self.add_subject_entry.get()

            if not subject_name:
                messagebox.showerror("Error", "Please enter a subject name.")
                return
            
            else:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #fetch max of rollno from database
                    cur.execute("select max(subject_id) from subject")
                    records = cur.fetchall()

                    for id in records:
                        list1 = list(id)
                        for i in list1:
                            pass

                    #insert data from entry box into treeview
                    if self.count % 2 == 0:
                        self.add_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(i + 1, subject_name,), tags=("evenrow",))
                    else:
                        self.add_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(i + 1 , subject_name,), tags=("oddrow",))

                    self.count += 1

                    #insert data from entry box to database
                    insert_query = "insert into subject(subject_id, subject_name) values(%s, %s)"
                    insert_value = (i + 1 , subject_name )

                    cur.execute(insert_query, insert_value)
                    
                    self.sub_msg_label.configure(text = "Subject Added Successfully", text_color = "red")

                    #commit the changes
                    con.commit()

                    #clear the entry box
                    self.add_subject_entry.delete(0, tk.END)

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

        def delete_subject_func():
            #=======delete selected record==========#
            subject_data = self.add_subject_tree.selection() 

            empty_subject_list = []
            for all in subject_data:
                value = self.add_subject_tree.item(all, "values")
                empty_subject_list.append(value)
                self.add_subject_tree.delete(all)

            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                delete_query = "delete from subject where subject_id = %s and subject_name = %s"
                delete_value = empty_subject_list

                #execute the delete query
                cur.executemany(delete_query, delete_value)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        def select_record(e):
            #clear the textbox
            self.add_subject_entry.delete(0, tk.END)

            selected = self.add_subject_tree.focus()

            if selected:
                #grab record values
                values = self.add_subject_tree.item(selected, "values")

                #insert selected values
                self.add_subject_entry.insert(tk.END, values[1])

        def update_subject_func():
            #clear the treeview
            selected = self.add_subject_tree.focus()

            if selected:
                values = self.add_subject_tree.item(selected, "values")
            
            id = values[0]
    
            #Update the values
            records = self.add_subject_tree.item(selected, values = (id, self.add_subject_entry.get()))
            
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #update into database
                cur.execute("update subject set subject_name = %s where subject_id = %s", (self.add_subject_entry.get(), id))

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #======treeview setting=========#
        #add some style
        style = ttk.Style()

        #pick a theme
        style.theme_use("alt")

        #configure the tree view color
        style.configure("Treeview", 
                        background = "#D3D3D3",
                        rowheight = 25,
                        fieldbackground = "#F3FBF1", font = ("Consolas", 14))
        
        style.configure("mystyle.Treeview", font=('Consolas', 15))

        #configure the selected color
        style.configure("Treeview", background = [("selected", "#347083")])

        #increse the font size of heading
        style.configure("Treeview.Heading", font=("Consolas", 18))

        self.data_frame = tk.Frame(self.subject_page_frame, bg = "lightgrey", borderwidth=5, relief="groove")
        self.data_frame.pack_propagate(False)
        self.data_frame.place(x = 425, y = 350, width = 400, height = 400)

        #create a scrollbar
        y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
        x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

        y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

        #create a treeview
        self.add_subject_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
        self.add_subject_tree.pack(fill = "both", expand= True)
        self.add_subject_tree.bind("<<TreeviewSelect>>", select_record)

        #configure the scrollbar
        x_scroll.config(command = self.add_subject_tree.xview)
        y_scroll.config(command = self.add_subject_tree.yview)

        #define our columns
        self.add_subject_tree["columns"] = ("Subject ID", "Subject Name")

        #format column
        self.add_subject_tree.column("Subject ID", anchor="center", width = 100, minwidth=100)
        self.add_subject_tree.column("Subject Name", anchor="center", width = 300, minwidth=300)

        #create a heading
        self.add_subject_tree.heading("Subject ID", text = "Subject ID", anchor = "center")
        self.add_subject_tree.heading("Subject Name", text = "Subject Name", anchor = "center")

        #Create striped to our tages
        self.add_subject_tree.tag_configure("oddrow", background="white")
        self.add_subject_tree.tag_configure("evenrow", background="lightblue")

        #================================
        self.add_subject_label = ctk.CTkLabel(self.subject_page_frame, text = "Subject Name:", font = ("Consolas", 20), text_color="green")
        self.add_subject_label.place(x = 200, y = 130)

        self.add_subject_entry = ctk.CTkEntry(self.subject_page_frame, width = 300, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.add_subject_entry.place(x = 350, y = 130)

        self.add_subject_button = ctk.CTkButton(self.subject_page_frame, text = "Add", width = 100, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_width=2, border_color="green", command = add_subject_func)
        self.add_subject_button.place(x = 657, y = 128)

        self.delete_subject_button = ctk.CTkButton(self.subject_page_frame, text = "Delete", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_width=2, border_color="green", command = delete_subject_func)
        self.delete_subject_button.place(x = 350, y = 190)

        self.update_subject_button = ctk.CTkButton(self.subject_page_frame, text = "Update", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_width=2, border_color="green", command = update_subject_func)
        self.update_subject_button.place(x = 510, y = 190)

        self.sub_msg_label = ctk.CTkLabel(self.subject_page_frame, text = "", font = ("Consolas", 20), text_color="green")
        self.sub_msg_label.place(x = 350, y = 250)

        #==========calling the function========#
        show_subject_record()

        self.subject_page_frame.place(x = 0, y = 0)

    def assign_staff_frame(self):
        self.staff_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.staff_page_frame, text = "Assign Teacher & Subjects")

        def assign_class_teacher():
            self.assign_class_teacher_frame=ctk.CTkFrame(self.staff_page_frame, width = 1082, height=590, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

            #======function==============#
            #=======fetch standard record ==========#
            def fetch_std_record():
                try:
                    con = mycon.connect(host = "localhost", user = "root", password = "root", database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the cursor query
                    cur.execute("select concat(std_name, ' ', div_name) as grade from division group by div_id")

                    records = cur.fetchall()

                    std_list = []
                    for record in records:
                        std_list.append(record[0])
                    
                    #======configure the option menu for standard values
                    self.select_standard_values = std_list
                    self.select_standard_opt.configure(values = self.select_standard_values)

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

            #=========fetch staff record==========#
            def fetch_staff_record():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307,database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the cursor query
                    cur.execute("select srno from staff order by srno asc")

                    records = cur.fetchall()

                    staff_list = []
                    for record in records:
                        staff_list.append(str(record[0]))

                    #======configure the option menu for staff values
                    self.select_staff_values = staff_list
                    self.select_staff_opt.configure(values = self.select_staff_values)

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

            #======show record auto==========#
            def show_assign_record_auto():
                global count
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root",port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the cursor query
                    cur.execute("select concat(s.first_name,' ', s.last_name) as name, concat(d.std_name,' ', d.div_name) as std_div from class_teachers ct, division d, staff s where ct.srno = s.srno and d.div_id = ct.div_id")

                    records = cur.fetchall()

                    for record in records:
                        if self.count % 2 == 0:
                            self.assign_teacher_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record), tags=("evenrow",))
                        else:
                            self.assign_teacher_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record), tags=("oddrow",))

                        self.count += 1

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

            #=========assiging teacher , class and div=====#
            self.count = 0
            def assign_classteacher():
                global count
                staff_no = staff_var.get()
                std_name = std_var.get()

                if not staff_no or not std_name:
                    messagebox.showerror("Error", "Please select above details.")
                    return
                
                else:
                    try:
                        con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307,database = "software")

                        #create a cursor instance
                        cur = con.cursor()

                        #fetch the name of staff
                        cur.execute("select concat(first_name, ' ', last_name) as staff_name from staff where srno = %s", (staff_no,))
                        staff_record = cur.fetchall()
                        
                        for staff_name in staff_record:
                            for staff in staff_name:
                                continue
                        
                        #spliting the record of std div
                        result = std_name.split(" ")
                        std = " ".join([result[0], result[1]])
                        div = result[2]

                        #fetching the div id from division
                        cur.execute("select div_id from division where std_name = %s and div_name = %s", (std, div))
                        div_record = cur.fetchall()
                        for div_no in div_record:
                            continue

                        #fetch record in database#
                        select_query=f"select srno,div_id from class_teachers where srno={staff_no} and div_id={div_no[0]}"
                        cur.execute(select_query)
                        result=cur.fetchall()
                        if result:
                            messagebox.showinfo("Error","Class already assign")
                            return
                        else:
                            # self.count = 0
                            #insert data from option menu into treeview
                            if self.count % 2 == 0:
                                self.assign_teacher_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(staff, std_name), tags=("evenrow",))
                            else:
                                self.assign_teacher_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(staff, std_name), tags=("oddrow",))

                            self.count += 1

                            #add record in database
                            insert_query = "insert into class_teachers(srno, div_id) values(%s, %s)"
                            insert_values = (staff_no, div_no[0])

                            cur.execute(insert_query, insert_values)

                            #commit the changes
                            con.commit()

                            #close the connection
                            con.close()

                    except Exception as e:
                        print("Error ", e)
            
            #=================================#

            #====for assigning class and all to teacher==========#
            '''self.add_staff_entry = ctk.CTkEntry(self.staff_page_frame, width = 200, height = 30, corner_radius=2, font = ("Consolas", 20), border_color="green")
            self.add_staff_entry.place(x = 20, y = 80)'''

            self.search_staff_label = ctk.CTkLabel(self.assign_class_teacher_frame, text = "Select Staff", font = ("Consolas", 20), text_color="black")
            self.search_staff_label.place(x = 20, y = 50)

            self.select_staff_values = []
            staff_var = tk.StringVar()        
            self.select_staff_opt = ctk.CTkOptionMenu(self.assign_class_teacher_frame, width = 200, height = 30, corner_radius=2, values=self.select_staff_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=staff_var)
            self.select_staff_opt.place(x = 20, y = 90)

            self.search_std_label = ctk.CTkLabel(self.assign_class_teacher_frame, text = "Select Std & Div", font = ("Consolas", 20), text_color="black")
            self.search_std_label.place(x = 250, y = 50)

            self.select_standard_values = []
            std_var = tk.StringVar()        
            self.select_standard_opt = ctk.CTkOptionMenu(self.assign_class_teacher_frame, width = 200, height = 30, corner_radius=2, values=self.select_standard_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=std_var)
            self.select_standard_opt.place(x = 250, y = 90)

            self.assign_button = ctk.CTkButton(self.assign_class_teacher_frame, text = "Assign", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=assign_classteacher, border_color="green", border_width=2)

            self.assign_button.place(x = 500, y = 80)
    
            #=======treeview setting========#
            #add some style
            style = ttk.Style()

            #pick a theme
            style.theme_use("alt")

            #configure the tree view color
            style.configure("Treeview", 
                            background = "#EEF0E5",
                            rowheight = 25,
                            fieldbackground = "#F3FBF1", font = ("Consolas", 14))
            
            style.configure("mystyle.Treeview", font=('Consolas', 15))

            #configure the selected color
            style.configure("Treeview", background = [("selected", "#347083")])

            #increse the font size of heading
            style.configure("Treeview.Heading", font=("Consolas", 18))

            self.data_frame = tk.Frame(self.assign_class_teacher_frame, bg = "lightgrey", borderwidth=0, relief="solid")
            self.data_frame.pack_propagate(False)
            self.data_frame.place(x = 20, y = 200, height = 500, width = 1000)

            #create a scrollbar
            y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
            x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

            y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
            x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

            #create a treeview
            self.assign_teacher_subject_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
            self.assign_teacher_subject_tree.pack(fill = "both", expand= True)

            #configure the scrollbar
            x_scroll.config(command = self.assign_teacher_subject_tree.xview)
            y_scroll.config(command = self.assign_teacher_subject_tree.yview)

            #define our columns
            self.assign_teacher_subject_tree["columns"] = ("Staff Name", "Standard & Division Name")

            #format column
            self.assign_teacher_subject_tree.column("Staff Name", anchor="center", width = 250, minwidth=250)
            self.assign_teacher_subject_tree.column("Standard & Division Name", anchor="center", width = 250, minwidth=250)
            
            #create a heading
            self.assign_teacher_subject_tree.heading("Staff Name", text = "Staff Name", anchor = "center")
            self.assign_teacher_subject_tree.heading("Standard & Division Name", text = "Standard & Division Name", anchor = "center")
        
            #Create striped to our tages
            self.assign_teacher_subject_tree.tag_configure("oddrow", background="white")
            self.assign_teacher_subject_tree.tag_configure("evenrow", background="lightblue")
            #==========================#

            #=========calling the function==========#
            fetch_staff_record()
            fetch_std_record()
            show_assign_record_auto()

            self.assign_class_teacher_frame.place(x = 5, y = 105)

        def assign_subject():
            self.assign_subject_frame=ctk.CTkFrame(self.staff_page_frame, width = 1082, height=590, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

            #======function==============#
            #=======fetch standard record ==========#
            def fetch_std_record():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307,database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the cursor query
                    cur.execute("select concat(std_name, ' ', div_name) as grade from division group by div_id")

                    records = cur.fetchall()

                    std_list = []
                    for record in records:
                        std_list.append(record[0])
                    
                    #======configure the option menu for standard values
                    self.select_standard_values = std_list
                    self.select_standard_opt.configure(values = self.select_standard_values)

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)
        
            #=======fetch subject record ==========#
            def fetch_subject_record():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the cursor query
                    cur.execute("select subject_name from subject")

                    records = cur.fetchall()

                    subject_list = []
                    for record in records:
                        subject_list.append(record[0])
                    
                    #======configure the option menu for standard values
                    self.select_subject_values = subject_list
                    self.select_subject_opt.configure(values = self.select_subject_values)

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

            #=========fetch staff record==========#
            def fetch_staff_record():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307,database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the cursor query
                    cur.execute("select srno from staff order by srno asc")

                    records = cur.fetchall()

                    staff_list = []
                    for record in records:
                        staff_list.append(str(record[0]))

                    #======configure the option menu for staff values
                    self.select_staff_values = staff_list
                    self.select_staff_opt.configure(values = self.select_staff_values)

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

            #======show record auto==========#
            def show_assign_record_auto():
                global count
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307,database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the cursor query
                    cur.execute("select concat(staff.first_name,' ', staff.last_name) as name, concat(d.std_name,' ', d.div_name) as std_div, s.subject_name from teacher_assignments ta, division d, subject s , staff where ta.srno = staff.srno and d.div_id = ta.std_div_id and s.subject_id = ta.subject_id")

                    records = cur.fetchall()

                    for record in records:
                        if self.count % 2 == 0:
                            self.assign_teacher_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record), tags=("evenrow",))
                        else:
                            self.assign_teacher_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record), tags=("oddrow",))

                        self.count += 1

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

            #=========assiging teacher , class and div=====#
            self.count = 0
            def assign_teacher_subject():
                global count
                staff_no = staff_var.get()
                std_name = std_var.get()
                subject_name= subject_var.get()

                if not staff_no or not std_name or not subject_name:
                    messagebox.showerror("Error", "Please select above details.")
                    return
                
                else:
                    try:
                        con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                        #create a cursor instance
                        cur = con.cursor()

                        #fetch the name of staff
                        cur.execute("select concat(first_name, ' ', last_name) as staff_name from staff where srno = %s", (staff_no,))
                        staff_record = cur.fetchall()
                        
                        for staff_name in staff_record:
                            for staff in staff_name:
                                continue
                        
                        #spliting the record of std div
                        result = std_name.split(" ")
                        std = " ".join([result[0], result[1]])
                        div = result[2]

                        #fetching the div id from division
                        cur.execute("select div_id from division where std_name = %s and div_name = %s", (std, div))
                        div_record = cur.fetchall()
                        for div_no in div_record:
                            continue

                        #fetching the subject_id from division
                        cur.execute("select subject_id from subject where subject_name = %s", (subject_name,))
                        subject_record = cur.fetchall()
                        for sub in subject_record:
                            continue

                        #fetch record in database#
                        select_query=f"select srno,std_div_id,subject_id from teacher_assignments where srno={staff_no} and std_div_id={div_no[0]} and subject_id={sub[0]}"
                        cur.execute(select_query)
                        result=cur.fetchall()
                        if result:
                            messagebox.showinfo("Error","Subject already assign")
                            return
                        #fetch record in database#
                        select_query=f"select std_div_id,subject_id from teacher_assignments where std_div_id={div_no[0]} and subject_id={sub[0]}"
                        cur.execute(select_query)
                        result=cur.fetchall()
                        if result:
                            messagebox.showinfo("Error","Subject already assign")
                            return
                        else:
                            # self.count = 0
                            #insert data from option menu into treeview
                            if self.count % 2 == 0:
                                self.assign_teacher_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(staff, std_name, subject_name), tags=("evenrow",))
                            else:
                                self.assign_teacher_subject_tree.insert(parent = "", index = tk.END, iid = self.count, values=(staff, std_name, subject_name), tags=("oddrow",))

                            self.count += 1
                            #add record in database
                            insert_query = "insert into teacher_assignments(srno, std_div_id, subject_id) values(%s, %s, %s)"
                            insert_values = (staff_no, div_no[0], sub[0])

                            cur.execute(insert_query, insert_values)

                            #commit the changes
                            con.commit()

                            #close the connection
                            con.close()

                    except Exception as e:
                        print("Error ", e)
            
            #=================================#

            #====for assigning class and all to teacher==========#
            '''self.add_staff_entry = ctk.CTkEntry(self.staff_page_frame, width = 200, height = 30, corner_radius=2, font = ("Consolas", 20), border_color="green")
            self.add_staff_entry.place(x = 20, y = 80)'''

            self.search_staff_label = ctk.CTkLabel(self.assign_subject_frame, text = "Select Staff", font = ("Consolas", 20), text_color="black")
            self.search_staff_label.place(x = 20, y = 50)

            self.select_staff_values = []
            staff_var = tk.StringVar()        
            self.select_staff_opt = ctk.CTkOptionMenu(self.assign_subject_frame, width = 200, height = 30, corner_radius=2, values=self.select_staff_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=staff_var)
            self.select_staff_opt.place(x = 20, y = 90)

            self.search_std_label = ctk.CTkLabel(self.assign_subject_frame, text = "Select Std & Div", font = ("Consolas", 20), text_color="black")
            self.search_std_label.place(x = 250, y = 50)

            self.select_standard_values = []
            std_var = tk.StringVar()        
            self.select_standard_opt = ctk.CTkOptionMenu(self.assign_subject_frame, width = 200, height = 30, corner_radius=2, values=self.select_standard_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=std_var)
            self.select_standard_opt.place(x = 250, y = 90)

            self.search_subject_label = ctk.CTkLabel(self.assign_subject_frame, text = "Select Subject", font = ("Consolas", 20), text_color="black")
            self.search_subject_label.place(x = 480, y = 50)

            self.select_subject_values = []
            subject_var = tk.StringVar()        
            self.select_subject_opt = ctk.CTkOptionMenu(self.assign_subject_frame, width = 200, height = 30, corner_radius=2, values=self.select_subject_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=subject_var)
            self.select_subject_opt.place(x = 480, y = 90)

            self.assign_button = ctk.CTkButton(self.assign_subject_frame, text = "Assign", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=assign_teacher_subject, border_color="green", border_width=2)

            self.assign_button.place(x = 700, y = 80)
    
            #=======treeview setting========#
            #add some style
            style = ttk.Style()

            #pick a theme
            style.theme_use("alt")

            #configure the tree view color
            style.configure("Treeview", 
                            background = "#EEF0E5",
                            rowheight = 25,
                            fieldbackground = "#F3FBF1", font = ("Consolas", 14))
            
            style.configure("mystyle.Treeview", font=('Consolas', 15))

            #configure the selected color
            style.configure("Treeview", background = [("selected", "#347083")])

            #increse the font size of heading
            style.configure("Treeview.Heading", font=("Consolas", 18))

            self.data_frame = tk.Frame(self.assign_subject_frame, bg = "lightgrey", borderwidth=0, relief="solid")
            self.data_frame.pack_propagate(False)
            self.data_frame.place(x = 20, y = 200, height = 500, width = 1000)

            #create a scrollbar
            y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
            x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

            y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
            x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

            #create a treeview
            self.assign_teacher_subject_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
            self.assign_teacher_subject_tree.pack(fill = "both", expand= True)

            #configure the scrollbar
            x_scroll.config(command = self.assign_teacher_subject_tree.xview)
            y_scroll.config(command = self.assign_teacher_subject_tree.yview)

            #define our columns
            self.assign_teacher_subject_tree["columns"] = ("Staff Name", "Standard & Division Name","Subject Name")

            #format column
            self.assign_teacher_subject_tree.column("Staff Name", anchor="center", width = 250, minwidth=250)
            self.assign_teacher_subject_tree.column("Standard & Division Name", anchor="center", width = 250, minwidth=250)
            self.assign_teacher_subject_tree.column("Subject Name", anchor="center", width = 250, minwidth = 250)
            
            #create a heading
            self.assign_teacher_subject_tree.heading("Staff Name", text = "Staff Name", anchor = "center")
            self.assign_teacher_subject_tree.heading("Standard & Division Name", text = "Standard & Division Name", anchor = "center")
            self.assign_teacher_subject_tree.heading("Subject Name", text = "Subject Name", anchor = "center")
        
            #Create striped to our tages
            self.assign_teacher_subject_tree.tag_configure("oddrow", background="white")
            self.assign_teacher_subject_tree.tag_configure("evenrow", background="lightblue")
            #==========================#

            #=========calling the function==========#
            fetch_staff_record()
            fetch_std_record()
            fetch_subject_record()
            show_assign_record_auto()

            self.assign_subject_frame.place(x = 5, y = 105)

        self.assign_class_teacher_button = ctk.CTkButton(self.staff_page_frame, text = "Assgin Class Teacher", width = 200, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=assign_class_teacher)
        self.assign_class_teacher_button.place(x = 50, y = 60)

        self.assign_subject_button = ctk.CTkButton(self.staff_page_frame, text = "Assgin Subject", width = 200, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=assign_subject)
        self.assign_subject_button.place(x = 300, y = 60)

        self.staff_page_frame.place(x = 0, y = 0)

    def staff_report_frame(self):
        self.staff_report_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.staff_report_page_frame, text = "Staff Report")

        def show_staff_record_auto():
            global count
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                select_query = "select srno, staff_id, concat(first_name, ' ', last_name) as name, email, mobile, gender, qualification, city, pincode, selection_status from staff"

                #execute the select query
                cur.execute(select_query)

                records = cur.fetchall()

                #show record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_staff_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("evenrow",))
                    else:
                        self.add_staff_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("oddrow",))
                    self.count += 1

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #=====search staff record========#
        def search_staff_record():
            search_type = self.search_var.get()
            search_paramter = self.search_entry.get()

            # #clear the treeview
            for record in self.add_staff_tree.get_children():
                self.add_staff_tree.delete(record)

            #connection with database to pull out search records
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                if search_type == "Name":
                    cur.execute("select srno,staff_id, concat(first_name, ' ', last_name) as name, email, mobile, gender, qualification, city, pincode, selection_status from staff where concat(first_name, ' ', last_name) = %s", (search_paramter,))

                elif search_type == "Contact":
                    cur.execute("select srno,staff_id, concat(first_name, ' ', last_name) as name, email, mobile, gender, qualification, city, pincode, selection_status from staff where mobile = %s", (search_paramter,))
                
                records = cur.fetchall()

                self.count = 0
                #show search record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_staff_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],  record[9]), tags=("evenrow",))
                    else:
                        self.add_staff_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("oddrow",))
                    self.count += 1

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        
        def reset_std_record():
            #clear the treeview
            for record in self.add_staff_tree.get_children():
                self.add_staff_tree.delete(record)

            #show all record of staff
            show_staff_record_auto()

        def approve_staff_func():
            #grab a record number
            selected_approve_data = self.add_staff_tree.selection() 

            approve_list = []
            for all in selected_approve_data:
                value = self.add_staff_tree.item(all, "values")
                approve_list.append(value)

            for staff in approve_list:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the update query
                    update_query = "update staff set selection_status = %s where srno = %s"
                    update_value = (self.approve_button.cget("text"), staff[0])

                    cur.execute(update_query, update_value)

                    #clear the treeview
                    for record in self.add_staff_tree.get_children():
                        self.add_staff_tree.delete(record)

                    #executing select query 
                    select_query = "select srno, staff_id, concat(first_name, ' ', last_name) as name, email, mobile, gender, qualification, city, pincode, selection_status from staff"

                    cur.execute(select_query)

                    records = cur.fetchall()

                    #show record in treeview
                    for record in records:
                        if self.count %2 == 0:
                            self.add_staff_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("evenrow",))
                        else:
                            self.add_staff_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],  record[9]), tags=("oddrow",))
                        self.count += 1

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

        def reject_staff_func():
            #grab a record number
            selected_reject_data = self.add_staff_tree.selection() 

            reject_list = []
            for all in selected_reject_data:
                value = self.add_staff_tree.item(all, "values")
                reject_list.append(value)

            for staff in reject_list:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the update query
                    update_query = "update staff set selection_status = %s where srno = %s"
                    update_value = (self.reject_button.cget("text"), staff[0])

                    cur.execute(update_query, update_value)

                    #==========================
                    #clear the treeview
                    for record in self.add_staff_tree.get_children():
                        self.add_staff_tree.delete(record)

                    #executing select query 
                    select_query = "select srno, staff_id, concat(first_name, ' ', last_name) as name, email, mobile, gender, qualification, city, pincode, selection_status from staff"
                    
                    cur.execute(select_query)

                    records = cur.fetchall()

                    #show record in treeview
                    for record in records:
                        if self.count %2 == 0:
                            self.add_staff_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("evenrow",))
                        else:
                            self.add_staff_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("oddrow",))
                        self.count += 1

                    #commit the changes
                    con.commit()

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

        def update_staff_tree():
            #clear the treeview
            for record in self.add_staff_tree.get_children():
                self.add_staff_tree.delete(record)

            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the delete query
                cur.execute("delete from staff where selection_status = 'Reject'")

                #commit the changes
                con.commit()

                #calling the show_staff_record_auto func
                show_staff_record_auto()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #=====generate id=============#
        def generate_id():
            for record in self.add_staff_tree.get_children():
                self.add_staff_tree.delete(record)

            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                srno_list=[]
                #execute the delete query
                cur.execute("select srno from staff order by srno asc")
                records=cur.fetchall()
                for record in records:
                    for staff_no in record:
                        # print(staff_no)
                        srno_list.append(staff_no)
                       
                id=1001
                for i in range(len(srno_list)):
                    # print(srno_list[i])
                    cur.execute(f"update staff set staff_id={id} where srno={srno_list[i]}")
                    id=id+1

                #commit the changes
                con.commit()

                #calling the show_staff_record_auto func
                show_staff_record_auto()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #=======generate teacher id card==========#
        def generate_teacher_card(teacher_data):
            global records
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root",port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #fetch student_data
                cur.execute("select srno, mobile, address, image_path, concat(first_name,' ', last_name) as name, first_name from staff where srno = %s", (teacher_data[0],))

                records = cur.fetchone()

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
            
            teacher_id = records[0]
            contact = records[1]
            address = records[2]
            image_path = records[3]
            full_name = records[4]
            first_name = records[5].lower()
        
            wrapped_address = textwrap.fill(text=address, width=25)

            #==================================#
            teacher_frame_image = Image.open("image/teacher_id.png")
            teacher_image_pic = Image.open(f"{image_path}").resize((94, 98))

            #creating an object for using student_frame_image
            draw = ImageDraw.Draw(teacher_frame_image)
            text_font = ImageFont.truetype("tahomabd.ttf", 13)

            #showing student photo on id frame
            teacher_frame_image.paste(teacher_image_pic, (98,127)) 

            draw.text(xy = (98, 230), text = f"{full_name}", fill = (255, 0, 0), font = ImageFont.truetype("tahomabd.ttf", 15))
            draw.text(xy = (110, 277), text = f"{teacher_id}", fill = (0, 0, 0), font = text_font)
            # draw.text(xy = (97, 297), text = f"{dob}", fill = (0, 0, 0), font = text_font)
            draw.text(xy = (110, 302), text = f"{contact}", fill = (0, 0, 0), font = text_font)
            draw.text(xy = (110, 325), text = f"{wrapped_address}", fill = (0, 0, 0), font = text_font)

            teacher_id_window = ctk.CTkToplevel(fg_color="white")
            teacher_id_window.geometry("600x500+800+250")
            teacher_id_window.title("School Management System")

            #======card frame===========#
            self.teacher_card_page_frame = ctk.CTkFrame(teacher_id_window, border_width=2,border_color="green", fg_color="white", width = 580, height = 480, corner_radius=2)

            #======card label===========#
            self.head_label = ctk.CTkLabel(self.teacher_card_page_frame, text = "Identity Card",width = 580, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
            self.head_label.place(x = 0, y = 0)

            #====ignore warnings===========#
            warnings.filterwarnings("ignore", category=UserWarning)

            #=====iid card image label==========#
            id_card_image = ImageTk.PhotoImage(teacher_frame_image)
            self.teacher_card_label = ctk.CTkLabel(self.teacher_card_page_frame, text = "", image = id_card_image)
            self.teacher_card_label.place(x = 170, y = 50)

            # #===========save button=============#
            def save_teacher_card():
                file_name = "C:/Users/vikas/OneDrive/Documents/software project/teacher_id"

                if os.path.exists(f"{file_name}/{teacher_id}_{first_name} id_card.png"):
                    error_message = f"The file '{file_name}' already exists."
                    messagebox.showinfo("File Exists", message=error_message)
                else:
                    #convert photo_image into PIL image
                    image_to_save = ImageTk.getimage(id_card_image) 
                    image_to_save.save(f"{file_name}/{teacher_id}_{first_name} id_card.png")
                    success_message = f"The Teacher ID card for {full_name} has been saved successfully!"
                    messagebox.showinfo("Success", message=success_message)

            # #============print button===========#
            def print_teacher_card():
                path = filedialog.askdirectory()

                if path:
                    image_to_save = ImageTk.getimage(id_card_image) 
                    image_to_save.save(f"{path}/{teacher_id}_{first_name} id_card_print.png")
                    win32api.ShellExecute(0,"print", f"{path}/{teacher_id}_{first_name} id_card_print.png",None, ".", 0)
                    # print_message = f"The student ID card for {first_name} {last_name} has been printed successfully."
                    # messagebox.showinfo("Success", message=print_message)

            self.save_button = ctk.CTkButton(self.teacher_card_page_frame, text = "Save", width = 120, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=save_teacher_card)
            self.save_button.place(x = 160, y = 400)

            self.print_button = ctk.CTkButton(self.teacher_card_page_frame, text = "Print", width = 120, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=print_teacher_card)
            self.print_button.place(x = 300, y = 400)

            self.teacher_card_page_frame.place(x = 10, y = 10)

        def on_tree_view_selection():
            selected = self.add_staff_tree.selection()[0]
            teacher_data = self.add_staff_tree.item(selected, "values")
            generate_teacher_card(teacher_data = teacher_data)

        #=========Send Email======#
        def send_email():
            try:
                start_time=time.time()
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307,database = "software")

                #create a cursor instance
                cur = con.cursor()

                email_list=[]
                #fetch email query
                cur.execute("select email from staff order by srno asc")
                records=cur.fetchall()
                for record in records:
                    for staff_email in record:
                        email_list.append(staff_email)
                print(email_list)

                #fetch name query
                name_list=[]
                cur.execute("select first_name from staff order by srno asc")
                records=cur.fetchall()
                for record in records:
                    for student_name in record:
                        name_list.append(student_name)
                print(name_list)

                #fetch password
                password_list=[]
                cur.execute("select concat(first_name,'@',staff_id) as password from staff order by srno asc")
                records=cur.fetchall()
                for record in records:
                    for teacher_password in record:
                        password_list.append(teacher_password)
                print(password_list)

                for i in range(len(email_list)):
                    def send_email(subject, message, recipient_email, sender_email, sender_password):
                        try:
                            yag = yagmail.SMTP(sender_email, sender_password)
                            yag.send(to=recipient_email, subject=subject, contents=message)
                            print("Email sent successfully!")
                        except Exception as e:
                            print("Email failed to send. Error:", str(e))

                    subjects="Welcome to School Management System - Your Login Credentials"
                    body=f"Dear {name_list[i]},\n\nWe are pleased to inform you that your account for the Vivekandand Vidya Bhavan Management System has been successfully created.\n\nPlease find your login credentials below:\n\nUsername: {email_list[i]}\nPassword: {password_list[i]}\n\nIf you experience any issues or have any questions, please contact support at vvb.admin@gmail.com or +91 9619148774.\n\nThis message is generated automatically. Please do not reply to this email.\n\nThank you,\n\nVivekandand Vidya Bhavan Management System"

                    # Usage example:
                    send_email(subject=subjects, message=body,recipient_email=email_list[i], sender_email="vikas.kahar.4471804@ves.ac.in", sender_password="VIKAS@4471804")

                #commit the changes
                con.commit()
                end_time=time.time()
                total_time=end_time-start_time
                print(total_time)
                messagebox.showinfo("Login","Email Sent Successful")

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
            
        #==============================#

        #=======treeview setting========#
        #add some style
        style = ttk.Style()

        #pick a theme
        style.theme_use("alt")

        #configure the tree view color
        style.configure("Treeview", 
                        background = "#EEF0E5",
                        rowheight = 25,
                        fieldbackground = "#F3FBF1", font = ("Consolas", 14))
        
        style.configure("mystyle.Treeview", font=('Consolas', 15))

        #configure the selected color
        style.configure("Treeview", background = [("selected", "#347083")])

        #increse the font size of heading
        style.configure("Treeview.Heading", font=("Consolas", 18))

        self.data_frame = tk.Frame(self.staff_report_page_frame, bg = "lightgrey", borderwidth=0, relief="solid")
        self.data_frame.pack_propagate(False)
        self.data_frame.place(x = 20, y = 200, height = 550, width = 1320)

        #create a scrollbar
        y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
        x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

        y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

        #create a treeview
        self.add_staff_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
        self.add_staff_tree.pack(fill = "both", expand= True)

        #configure the scrollbar
        x_scroll.config(command = self.add_staff_tree.xview)
        y_scroll.config(command = self.add_staff_tree.yview)

        #define our columns
        self.add_staff_tree["columns"] = ("Sr No","Teacher ID","Name", "Email", "Mobile", "Gender", "Qualification", "City", "Pincode", "Selection Status")

        #format column
        self.add_staff_tree.column("Sr No", anchor="center", width = 100, minwidth=100)
        self.add_staff_tree.column("Teacher ID", anchor="center", width = 200, minwidth=200)
        self.add_staff_tree.column("Name", anchor="center", width = 300, minwidth=300)
        self.add_staff_tree.column("Email", anchor="center", width = 300, minwidth = 300)
        self.add_staff_tree.column("Mobile", anchor="center", width = 300, minwidth = 300)
        self.add_staff_tree.column("Gender", anchor="center", width = 300, minwidth = 300)
        self.add_staff_tree.column("Qualification", anchor="center", width = 300, minwidth = 300)
        self.add_staff_tree.column("City", anchor="center", width = 300, minwidth = 300)
        self.add_staff_tree.column("Pincode", anchor="center", width = 300, minwidth = 300)
        self.add_staff_tree.column("Selection Status", anchor="center", width = 300, minwidth = 300)
        
        #create a heading
        self.add_staff_tree.heading("Sr No", text = "Sr No", anchor = "center")
        self.add_staff_tree.heading("Teacher ID", text = "Teacher ID", anchor = "center")
        self.add_staff_tree.heading("Name", text = "Name", anchor = "center")
        self.add_staff_tree.heading("Email", text = "Email", anchor = "center")
        self.add_staff_tree.heading("Mobile", text = "Mobile", anchor = "center")
        self.add_staff_tree.heading("Gender", text = "Gender", anchor = "center")
        self.add_staff_tree.heading("Qualification", text = "Qualification", anchor = "center")
        self.add_staff_tree.heading("City", text = "City", anchor = "center")
        self.add_staff_tree.heading("Pincode", text = "Pincode", anchor = "center")
        self.add_staff_tree.heading("Selection Status", text = "Selection Status", anchor = "center")

        #Create striped to our tages
        self.add_staff_tree.tag_configure("oddrow", background="white")
        self.add_staff_tree.tag_configure("evenrow", background="lightblue")
        #==========================#
        
        #=====calling the show record function====#
        show_staff_record_auto()

        #======searching options=========#
        self.search_staff_label = ctk.CTkLabel(self.staff_report_page_frame, text = "Search By", font = ("Consolas", 20), text_color="black")
        self.search_staff_label.place(x = 15, y = 80)

        self.search_staff_by=["Name", "Contact"]
        self.search_var = tk.StringVar(value = "")
        self.search_staff_option=ctk.CTkOptionMenu(self.staff_report_page_frame,width=200,height=30,corner_radius=2,values=self.search_staff_by,fg_color="#D8D9DA",text_color="black",dropdown_font=("Consolas",18),font=("Consolas",18), variable=self.search_var)
        self.search_staff_option.place(x=140,y=80)

        self.search_entry = ctk.CTkEntry(self.staff_report_page_frame, width = 150, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.search_entry.place(x = 360, y = 78)

        self.search_button = ctk.CTkButton(self.staff_report_page_frame, text = "Search", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=search_staff_record)
        self.search_button.place(x = 530, y = 75)

        self.showall_button = ctk.CTkButton(self.staff_report_page_frame, text = "Show All", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command = reset_std_record)
        self.showall_button.place(x = 690, y = 75)

        #===button======#
        self.approve_button = ctk.CTkButton(self.staff_report_page_frame, text = "Approve", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=approve_staff_func)
        self.approve_button.place(x = 20, y = 630)

        self.reject_button = ctk.CTkButton(self.staff_report_page_frame, text = "Reject", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=reject_staff_func)
        self.reject_button.place(x = 200, y = 630)

        self.update_button = ctk.CTkButton(self.staff_report_page_frame, text = "Update", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=update_staff_tree)
        self.update_button.place(x = 380, y = 630)

        self.generate_id_button = ctk.CTkButton(self.staff_report_page_frame, text = "Generate", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=generate_id)
        self.generate_id_button.place(x = 560, y = 630)

        self.generate_teacher_card_button = ctk.CTkButton(self.staff_report_page_frame, text = "Generate ID Card", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=on_tree_view_selection)
        self.generate_teacher_card_button.place(x = 740, y = 630)

        self.send_email_button = ctk.CTkButton(self.staff_report_page_frame, text = "Send Email", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=send_email)
        self.send_email_button.place(x = 920, y = 630)

        self.staff_report_page_frame.place(x = 0, y = 0)

    def leave_frame(self):
        self.leave_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.leave_page_frame, text = "Leave")

        self.leave_page_frame.place(x = 0, y = 0)

    def student_report_frame(self):
        self.student_report_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.student_report_page_frame, text = "Student Reports")

        #===========function===============#

        '''def fetch_std(*args):
            global selected_std
            selected_std = std_var.get()
            print(selected_std)

        def fetch_div(*args):
            global selected_div
            selected_div = div_var.get()
            print(selected_div)

        def fetch_rollno():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the rollno query
                cur.execute("select srno from student where std_name = %s and div_name = %s", (selected_std, selected_div))

                rollno_record = cur.fetchall()
                rollno_list = []
                for rollno in rollno_record:
                    rollno_list.append(str(rollno[0]))
                
                self.choose_student_values = rollno_list
                self.choose_student_option.configure(values = self.choose_student_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)'''

        def fetch_std_div_rollno_record():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the std query
                cur.execute("select std_name from standard")

                std_record = cur.fetchall()
                std_list = []
                for std in std_record:
                    std_list.append(str(std[0]))
                
                self.standard_values_list = std_list
                self.selected_standard_option.configure(values = self.standard_values_list)

                #execute the div query
                cur.execute("select div_name from division group by div_name")

                div_record = cur.fetchall()
                div_list = []
                for div in div_record:
                    div_list.append(str(div[0]))
                
                self.division_values_list = div_list
                self.selected_division_option.configure(values = self.division_values_list)

                #execute the rollno query
                cur.execute("select srno from student")

                rollno_record = cur.fetchall()
                rollno_list = []
                for rollno in rollno_record:
                    rollno_list.append(str(rollno[0]))
                
                self.choose_student_values = rollno_list
                self.choose_student_option.configure(values = self.choose_student_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        
        #=======functions=======#
        def report_sumary_frame():
            #======checking the condition==========#
            std = std_var.get()
            div = div_var.get()
            rollno = rollno_var.get()
            
            def fetch_student_summary():
                if std == "" and div == "" or rollno == "":
                    messagebox.showerror("Error", "Empty Field.")
                else:
                    try:
                        con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                        #create a cursor instance
                        cur = con.cursor()

                        #execute the cursor query
                        cur.execute("select srno, concat(first_name, ' ', last_name) as name,  email, mobile, dob, address, city, pincode, image_path from student where srno = %s and std_name = %s and div_name = %s", (rollno, std, div))

                        records = cur.fetchall()
                        # print(records)

                        for record in records:
                            self.report_frame_label.configure(text = f"Student Name: {record[1]}")
                            self.student_rollno.configure(text = record[0])
                            self.student_email.configure(text = record[2])
                            self.student_mobile.configure(text = record[3])
                            self.student_birthdate.configure(text = record[4])
                            self.student_address.configure(text = record[5], wraplength = 300)
                            self.student_city.configure(text = record[6])
                            self.student_pincode.configure(text = record[7])
                            image_path = record[8]

                        try:
                            image = Image.open(image_path)

                        except FileNotFoundError:
                            print(f"Error: Could not find image at path: {image_path}")

                        #====configure the image===========#
                            
                        #base name of the image
                        image_file_name = os.path.basename(image_path)

                        #save the image
                        image.save(image_file_name)
                            
                        #open image in form of ctk.CTkImage
                        imageo = ctk.CTkImage(light_image=image, dark_image=image, size = (127, 147))

                        #configure the right side frame label
                        self.student_photo_label.configure(image = imageo)
                        self.student_photo_label.image = imageo

                        #commit the changes
                        con.commit()

                        #close the connection
                        con.close()

                    except Exception as e:
                        print("Error ", e)

            #===========================================#
            self.report_frame = ctk.CTkFrame(self.student_report_page_frame, width = 700, height=450, corner_radius=2,  border_width=2, border_color="green", fg_color="white")

            self.report_frame_label = ctk.CTkLabel(self.report_frame, width = 700, height = 40, text = "Student Name: ", font = ("Consolas", 25), fg_color="green", text_color="white")
            self.report_frame_label.place(x = 0, y = 0)

            #======other entries=======#
            self.rollno = ctk.CTkLabel(self.report_frame, text = "Roll No: ", font = ("Consolas", 20), text_color="green")
            self.rollno.place(x = 45, y = 50)

            self.student_rollno = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_rollno.place(x = 150, y = 50)

            self.email = ctk.CTkLabel(self.report_frame, text = "Email: ", font = ("Consolas", 20), text_color="green")
            self.email.place(x = 67, y = 90)

            self.student_email = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_email.place(x = 150, y = 90)

            self.mobile = ctk.CTkLabel(self.report_frame, text = "Mobile: ", font = ("Consolas", 20), text_color="green")
            self.mobile.place(x = 57, y = 130)

            self.student_mobile = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_mobile.place(x = 150, y = 130)

            self.birthdate = ctk.CTkLabel(self.report_frame, text = "Birth Date: ", font = ("Consolas", 20), text_color="green")
            self.birthdate.place(x = 10, y = 170)

            self.student_birthdate = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_birthdate.place(x = 150, y = 170)

            self.address = ctk.CTkLabel(self.report_frame, text = "Address: ", font = ("Consolas", 20), text_color="green")
            self.address.place(x = 45, y = 210)

            self.student_address = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_address.place(x = 150, y = 210)

            self.city = ctk.CTkLabel(self.report_frame, text = "City: ", font = ("Consolas", 20), text_color="green")
            self.city.place(x = 78, y = 290)

            self.student_city = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_city.place(x = 150, y = 290)

            self.pincode = ctk.CTkLabel(self.report_frame, text = "Pincode: ", font = ("Consolas", 20), text_color="green")
            self.pincode.place(x = 45, y = 330)

            self.student_pincode = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_pincode.place(x = 150, y = 330)

            self.student_photo_frame = ctk.CTkFrame(self.report_frame, width = 130, height=150, corner_radius=0,  border_width=3, border_color="black", fg_color="white")
            self.student_photo_frame.place(x = 540, y = 60)

            self.student_photo_label = ctk.CTkLabel(self.student_photo_frame, text = "", fg_color="grey", width = 127, height=147)
            self.student_photo_label.place(x = 1, y = 1)

            #=========calling the function===============#
            fetch_student_summary()
            
            self.report_frame.place(x = 200, y = 200)

        self.choose_standard_label = ctk.CTkLabel(self.student_report_page_frame, text = "Select Standard :", font = ("Consolas", 20), text_color="green")
        self.choose_standard_label.place(x = 30, y = 60)

        self.standard_values_list = []
        std_var = tk.StringVar(value = "")
        self.selected_standard_option = ctk.CTkOptionMenu(self.student_report_page_frame, width = 200, height = 30, corner_radius=2, values=self.standard_values_list, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=std_var)
        self.selected_standard_option.place(x = 240, y = 60)
        # std_var.trace("w", fetch_std)

        self.choose_division_label = ctk.CTkLabel(self.student_report_page_frame, text = "Select Division :", font = ("Consolas", 20), text_color="green")
        self.choose_division_label.place(x = 30, y =100)

        self.division_values_list = []
        div_var = tk.StringVar(value = "")
        self.selected_division_option = ctk.CTkOptionMenu(self.student_report_page_frame, width = 200, height = 30, corner_radius=2, values=self.division_values_list, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=div_var)
        self.selected_division_option.place(x = 240, y = 100)
        # div_var.trace("w", fetch_div)

        self.choose_rollno_label = ctk.CTkLabel(self.student_report_page_frame, text = "Select Student :", font = ("Consolas", 20), text_color="green")
        self.choose_rollno_label.place(x = 41, y = 140)

        self.choose_student_values = []
        rollno_var = tk.StringVar(value = "")
        self.choose_student_option = ctk.CTkOptionMenu(self.student_report_page_frame, width = 200, height = 30, corner_radius=2, values=self.choose_student_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=rollno_var)
        self.choose_student_option.place(x = 240, y = 140)

        self.select_button = ctk.CTkButton(self.student_report_page_frame, text = "Select", width = 120, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=report_sumary_frame, border_color="green", border_width=2)
        self.select_button.place(x = 455, y = 140)

        #===========calling the function============#
        fetch_std_div_rollno_record()
   
        self.student_report_page_frame.place(x = 0, y = 0)

    def feedback_frame(self):
        self.feedback_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.feedback_page_frame, text = "Feedback")

        #===========save feedback function===========#
        def save_feedback_question():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                cur = con.cursor()

                #insert feedback into table
                insert_query = "insert into feedback_question(question_text, choice1_text,choice2_text,choice3_text,choice4_text) values(%s, %s, %s, %s, %s)"
                insert_values = (self.feedback_question_entry.get(), self.option1_entry.get(),self.option2_entry.get(),self.option3_entry.get(),self.option4_entry.get())

                cur.execute(insert_query, insert_values)

                #commit the changes
                con.commit()

                messagebox.showinfo("Success", "Data is added successfully.")

                #close the connection
                con.close()

                #=========clear the textbox===========#
                self.feedback_question_entry.delete(0, tk.END)
                self.option1_entry.delete(0, tk.END)
                self.option2_entry.delete(0, tk.END)
                self.option3_entry.delete(0, tk.END)
                self.option4_entry.delete(0, tk.END)

            except Exception as e:
                print(e)

        #=============create feedback question entry===================#
        self.feedback_question = ctk.CTkLabel(self.feedback_page_frame, text = "Feedback question: ", font = ("Consolas", 20), text_color="green")
        self.feedback_question.place(x = 20, y = 60)

        self.feedback_question_entry = ctk.CTkEntry(self.feedback_page_frame, width = 400, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.feedback_question_entry.place(x = 230, y = 60)

        self.feedback_options = ctk.CTkLabel(self.feedback_page_frame, text = "Feedback Options: ", font = ("Consolas", 20), text_color="green")
        self.feedback_options.place(x = 30, y = 110)

        self.option1_label = ctk.CTkLabel(self.feedback_page_frame, text = "1. ", font = ("Consolas", 20), text_color="green")
        self.option1_label.place(x = 230, y = 110)

        self.option1_entry = ctk.CTkEntry(self.feedback_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.option1_entry.place(x = 260, y = 110)

        self.option2_label = ctk.CTkLabel(self.feedback_page_frame, text = "2. ", font = ("Consolas", 20), text_color="green")
        self.option2_label.place(x = 230, y = 150)

        self.option2_entry = ctk.CTkEntry(self.feedback_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.option2_entry.place(x = 260, y = 150)

        self.option3_label = ctk.CTkLabel(self.feedback_page_frame, text = "3. ", font = ("Consolas", 20), text_color="green")
        self.option3_label.place(x = 230, y = 190)

        self.option3_entry = ctk.CTkEntry(self.feedback_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.option3_entry.place(x = 260, y = 190)

        self.option4_label = ctk.CTkLabel(self.feedback_page_frame, text = "4. ", font = ("Consolas", 20), text_color="green")
        self.option4_label.place(x = 230, y = 230)

        self.option4_entry = ctk.CTkEntry(self.feedback_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
        self.option4_entry.place(x = 260, y = 230)

        self.add_button = ctk.CTkButton(self.feedback_page_frame, text = "Add", width = 120, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=save_feedback_question, border_color="green", border_width=2)
        self.add_button.place(x = 260, y = 300)

        self.feedback_page_frame.place(x = 0, y = 0)

    def make_announcement_frame(self):
        self.anouncement_page_frame = ctk.CTkFrame(self.admin_rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.anouncement_page_frame, text = "Make Announcement")

        #=========functions=========#
        def notice_frame():
            
            #=====inside frame======#
            self.make_notice = ctk.CTkFrame(self.anouncement_page_frame, width = 1072, height=500, corner_radius=0,  border_width=2, border_color="green", fg_color="white")

            #=======function============#
            def create_notices():
                #=======datetime========#
                current_date = date.today()
                hour = strftime("%I")          #for 12 hours = I and for 24 hours = H
                minute = strftime("%M")
                second = strftime("%S")
                time = f"{hour}:{minute}:{second}"
                date_time = f"{current_date} {time}"

                notice_subject = self.notice_entry.get()
                notice_content = self.notice_content_entry.get("0.0", tk.END)
                
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    cur = con.cursor()

                    cur.execute("insert into announcement(type, announcement_subject, announcement_content, edate) value(%s, %s, %s, %s)", ("Notice", notice_subject, notice_content, date_time))

                    #commit the changes
                    con.commit()

                    messagebox.showinfo("Successfull", "Notice created successfully!")

                    #close the connection
                    con.close()
                except Exception as e:
                    print(e)


            #==========subject=============#
            self.notice_subject = ctk.CTkLabel(self.make_notice, text="Enter notice subject",text_color="black",font=("Consolas",20))
            self.notice_subject.place(x = 15, y = 15)

            self.notice_entry = ctk.CTkEntry(self.make_notice, width = 300, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
            self.notice_entry.place(x = 250, y = 15)

            #=========main body=============#
            self.notice_content = ctk.CTkLabel(self.make_notice, text="Enter notice content",text_color="black",font=("Consolas",20))
            self.notice_content.place(x = 15, y = 60)

            self.notice_content_entry = ctk.CTkTextbox(self.make_notice, width = 300, height = 50, corner_radius=2, font = ("Consolas", 17), border_color="green", text_color="black", fg_color="white", border_width=2, wrap = "word")
            self.notice_content_entry.place(x = 250, y = 60)

            self.create_notice_button = ctk.CTkButton(self.make_notice, text = "Create Notice", width = 120, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=0, hover_color="white", cursor = "hand2", command=create_notices, border_color="green", border_width=2)
            self.create_notice_button.place(x = 250, y = 130)

            self.make_notice.place(x = 10, y = 150)

            #======function============#
        def open_calendar():
            global cal
            calendar_window = ctk.CTkToplevel(self)
            calendar_window.geometry("300x200+950+700")
            calendar_window.title("Calendar")
            calendar_window.resizable(False, False)

            cal = tkcalendar.Calendar(calendar_window,date_pattern = "yyyy-mm-dd" ,background = "#388E3C")
            cal.pack(fill = "both", expand = True)
            cal.bind("<<CalendarSelected>>", lambda e : grab_date(cal))
            
            calendar_window.grab_set()
        
        def grab_date(e):
            date = cal.get_date()
            

        def event_frame():
            #=====inside frame======#
            self.make_event = ctk.CTkFrame(self.anouncement_page_frame, width = 1072, height=500, corner_radius=0,  border_width=2, border_color="green", fg_color="white")

            #=======function============#
            def create_event():
                #=======datetime========#
                current_date = date.today()
                hour = strftime("%I")          #for 12 hours = I and for 24 hours = H
                minute = strftime("%M")
                second = strftime("%S")
                time = f"{hour}:{minute}:{second}"
                date_time = f"{current_date} {time}"

                event_subject = self.event_entry.get()
                event_content = self.event_content_entry.get("0.0", tk.END)
                event_venue = self.event_venue_entry.get("0.0", tk.END)
                event_date = self.event_date_entry.get()
                event_time = self.event_time_entry.get()

                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    cur = con.cursor()

                    cur.execute("insert into announcement(type, announcement_subject, announcement_content, event_date, event_time, event_venue, edate) value(%s, %s, %s, %s, %s,%s, %s)", ("Event", event_subject,event_content, event_date, event_time, event_venue, date_time))

                    #commit the changes
                    con.commit()

                    messagebox.showinfo("Successfull", "Event created successfully!")

                    #close the connection
                    con.close()
                except Exception as e:
                    print(e)

            #==========subject=============#
            self.event_subject = ctk.CTkLabel(self.make_event, text="Enter event subject",text_color="black",font=("Consolas",20))
            self.event_subject.place(x = 15, y = 15)

            self.event_entry = ctk.CTkEntry(self.make_event, width = 300, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
            self.event_entry.place(x = 250, y = 15)

            #=========main body=============#
            self.event_content = ctk.CTkLabel(self.make_event, text="Enter event content",text_color="black",font=("Consolas",20))
            self.event_content.place(x = 15, y = 60)

            self.event_content_entry = ctk.CTkTextbox(self.make_event, width = 300, height = 50, corner_radius=2, font = ("Consolas", 17), border_color="green", text_color="black", fg_color="white", border_width=2, wrap = "word")
            self.event_content_entry.place(x = 250, y = 60)

            #=========set event date=============#
            self.event_date = ctk.CTkLabel(self.make_event, text="Select event date",text_color="black",font=("Consolas",20))
            self.event_date.place(x = 15, y = 125)

            self.event_date_entry = ctk.CTkEntry(self.make_event, width = 265, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
            self.event_date_entry.place(x = 250, y = 125)

            self.calendar_image = ctk.CTkImage(light_image=Image.open("image/calendar.png"), dark_image=Image.open("image/calendar.png"), size = (35, 35))

            self.calendar_button = ctk.CTkButton(self.make_event, width = 0, height = 0, fg_color="transparent", hover="disabled", bg_color="transparent", text = "", image = self.calendar_image, command=open_calendar)
            self.calendar_button.place(x = 515, y = 120)

            #=========set event time==============#
            self.event_time = ctk.CTkLabel(self.make_event, text="Enter event time",text_color="black",font=("Consolas",20))
            self.event_time.place(x = 15, y = 175)

            self.event_time_entry = ctk.CTkEntry(self.make_event, width = 300, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green")
            self.event_time_entry.place(x = 250, y = 175)

            #=========set event time==============#
            self.event_venue = ctk.CTkLabel(self.make_event, text="Enter event venue",text_color="black",font=("Consolas",20))
            self.event_venue.place(x = 15, y = 220)

            self.event_venue_entry = ctk.CTkTextbox(self.make_event, width = 300, height = 50, corner_radius=2, font = ("Consolas", 17), border_color="green", text_color="black", fg_color="white", border_width=2, wrap = "word")
            self.event_venue_entry.place(x = 250, y = 220)

            self.create_event_button = ctk.CTkButton(self.make_event, text = "Create Event", width = 120, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=0, hover_color="white", cursor = "hand2", command=create_event, border_color="green", border_width=2)
            self.create_event_button.place(x = 250, y = 280)


            self.make_event.place(x = 10, y = 150)

        #=======notice======#
        self.send_notice_button = ctk.CTkButton(self.anouncement_page_frame, text = "Make Notice", width = 350, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=notice_frame)
        self.send_notice_button.place(x=10,y=80)

        #=======event======#
        self.send_event_button = ctk.CTkButton(self.anouncement_page_frame, text = "Make Event", width = 350, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=event_frame)
        self.send_event_button.place(x=420,y=80)

        self.anouncement_page_frame.place(x = 0, y = 0)
        

class StudentHomeWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1536x864-10-7")

        #======switch_frame=======#
        def switch_frame(page, indicator_button):
            for frame in self.rightside_frame.winfo_children():
                frame.destroy()
                self.update()
            page()

            for child in self.student_sidebar_frame.winfo_children():
                if isinstance(child, ctk.CTkButton):
                    child.configure(fg_color = "#2d6a4f")

            indicator_button.configure(fg_color= "#163020")

        #=====return to main window=======#
        def return_to_main():
            self.destroy()
            root.deiconify()

        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        #======student home frame=======#
        self.student_homepage_frame = ctk.CTkFrame(self, width = 1526, height=730, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        
        self.student_sidebar_frame = ctk.CTkFrame(self.student_homepage_frame, width=350,height=700, corner_radius=0,  border_width=0, border_color="green", fg_color="#2d6a4f")

        self.sidebar_head_label = ctk.CTkLabel(self.student_sidebar_frame, text = "", height = 5, width = 348, fg_color="#2d6a4f")
        self.sidebar_head_label.place(x = 0, y = 0)

        #======photo frame==========#
        self.student_photo_frame = ctk.CTkFrame(self.student_sidebar_frame, width = 150, height=170, corner_radius=0,  border_width=1, border_color="black", fg_color="white")
        self.student_photo_frame.place(x = 100, y = 50)

        self.student_photo_label = ctk.CTkLabel(self.student_photo_frame, text = "", width = 149, height=169)
        self.student_photo_label.place(x = 0, y = 0)

        self.student_greet_label = ctk.CTkLabel(self.student_sidebar_frame, text = "", font=("Consolas", 20), text_color="red")
        self.student_greet_label.place(x = 115, y = 240)

        #=======sidebar menu========#
        self.profile_image = ctk.CTkImage(light_image=Image.open("image/user.png"), dark_image=Image.open("image/user.png"), size = (25, 25))

        self.profile_button = ctk.CTkButton(self.student_sidebar_frame, text = "       My Profile     ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#2d6a4f", corner_radius=60, hover_color="#163020" ,cursor = "hand2", command= lambda : switch_frame(page = self.profile_frame, indicator_button=self.profile_button), image = self.profile_image, anchor="right")
        self.profile_button.place(x = 24, y = 290)

        self.home_image = ctk.CTkImage(light_image=Image.open("image/home-dashboard.png"), dark_image=Image.open("image/home-dashboard.png"), size = (25, 25))

        self.home_button = ctk.CTkButton(self.student_sidebar_frame, text = "       Home          ", width = 300, height = 45, font = ("Verdana Pro", 18) , text_color="white", fg_color="#2d6a4f", corner_radius=60, hover_color="#163020", cursor = "hand2", command= lambda : switch_frame(page = self.home_frame,indicator_button=self.home_button), image = self.home_image, anchor = "right")
        self.home_button.place(x = 24, y = 337)

        self.leave_image = ctk.CTkImage(light_image=Image.open("image/leave_icon.png"), dark_image=Image.open("image/leave_icon.png"), size = (28, 28))

        self.leave_button = ctk.CTkButton(self.student_sidebar_frame, text = "       Leave          ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#2d6a4f", corner_radius=60, hover_color="#163020", cursor = "hand2", command=lambda : switch_frame(page = self.leave_frame,indicator_button=self.leave_button), image = self.leave_image, anchor = "right")
        self.leave_button.place(x = 24, y = 382)

        self.complain_image = ctk.CTkImage(light_image=Image.open("image/feedback.png"), dark_image=Image.open("image/feedback.png"), size = (30, 30))
        self.complain_button = ctk.CTkButton(self.student_sidebar_frame, text = "      Complain      ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#2d6a4f", corner_radius=60, hover_color="#163020", cursor = "hand2", command=lambda : switch_frame(page = self.complain_frame,indicator_button=self.complain_button), image = self.complain_image, anchor = "right")
        self.complain_button.place(x = 24, y = 429)

        self.attendance_image = ctk.CTkImage(light_image=Image.open("image/view-attendance.png"), dark_image=Image.open("image/view-attendance.png"), size = (30, 30))
        self.attend_report_button = ctk.CTkButton(self.student_sidebar_frame, text = "      View Attendance", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#2d6a4f", corner_radius=60, hover_color="#163020", cursor = "hand2", command= lambda : switch_frame(page = self.attendance_frame,indicator_button=self.attend_report_button), image = self.attendance_image, anchor = "left")
        self.attend_report_button.place(x = 24, y = 474)

        self.feedback_image = ctk.CTkImage(light_image=Image.open("image/feedback_icon.png"), dark_image=Image.open("image/feedback_icon.png"), size = (28, 28))
        self.feedback_button = ctk.CTkButton(self.student_sidebar_frame, text = "     Feedback      ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#2d6a4f", corner_radius=60, hover_color="#163020", cursor = "hand2", command= lambda : switch_frame(page = self.feedback_frame,indicator_button=self.feedback_button), image = self.feedback_image, anchor = "right")
        self.feedback_button.place(x = 24, y = 521)

        self.logout_image = ctk.CTkImage(light_image=Image.open("image/logout_icon.png"), dark_image=Image.open("image/logout_icon.png"), size = (28, 28))
        self.logout_button = ctk.CTkButton(self.student_sidebar_frame, text = "      Logout        ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#2d6a4f", corner_radius=60, hover_color="#163020", cursor = "hand2", command=return_to_main, image = self.logout_image, anchor = "right")
        self.logout_button.place(x = 24, y = 566)

        self.student_sidebar_frame.place(x = 10, y = 10)

        #=====rightside=========#
        self.rightside_frame = ctk.CTkFrame(self.student_homepage_frame, width = 1092, height=700, corner_radius=0,  border_width=None, fg_color="white")
        self.rightside_frame.place(x = 420, y = 10)

        self.student_homepage_frame.place(x = 5, y = 100)

    def home_frame(self):
        self.home_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.home_page_frame, text = "Welcome to Attendance Portal")

        def attendance_detail():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #==fetch total count =========#
                cur.execute("select count(a.student_no) as total_count from student s, attendance a where s.srno = a.student_no and email = %s",(student_username,))

                total_count = cur.fetchall()
                for total in total_count:
                    self.total_count.configure(text = f"{total[0]}")

                #====fetch present count========#
                cur.execute("select count(a.student_no) as present from student s, attendance a where  s.srno = a.student_no and email = %s and attendance_status = 'Present'",(student_username,))

                present_count = cur.fetchall()
                for present in present_count:
                    self.present_count.configure(text = f"{present[0]}")
       
                #====fetch absent count========#
                cur.execute("select count(a.student_no) as absent from student s, attendance a where  s.srno = a.student_no and email = %s and attendance_status = 'Absent'",(student_username,))

                absent_count = cur.fetchall()
                for absent in absent_count:
                    self.absent_count.configure(text = f"{absent[0]}")

                #====fetch leave count========#
                cur.execute("select count(a.student_no) as absent from student s, attendance a where  s.srno = a.student_no and email = %s and attendance_status = 'Leave'",(student_username,))

                leave_count_records = cur.fetchall()
                for leave in leave_count_records:
                    self.leave_count.configure(text = f"{leave[0]}")
                    self.leave_count1.configure(text = f"{leave[0]}")

                #====fetch complain record=========#
                cur.execute("select count(c.rollno) as complain from student s, complain c where  s.srno = c.rollno and email = %s",(student_username,))

                complain_count_records = cur.fetchall()
                for complain in complain_count_records:
                    self.complain_count.configure(text = f"{complain[0]}")

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
            
        #=========inside widgets=======#
        #=======attendance frame========#
        self.attendance_page_frame = ctk.CTkFrame(self.home_page_frame, width = 992, height=170, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        #=======attendance label=======#
        self.attendance_head_label=ctk.CTkLabel(self.attendance_page_frame,text="My Attendance",width=992,height=50,fg_color="green",text_color="white",font=("Consolas",28))
        self.attendance_head_label.place(x=0,y=0)

        #=======Total label=======#
        self.total_label=ctk.CTkLabel(self.attendance_page_frame,text="Total",text_color="black",font=("Consolas",26))
        self.total_label.place(x=100,y=80)

        #=======Total count=======#
        self.total_count=ctk.CTkLabel(self.attendance_page_frame,text="0",text_color="black",font=("Consolas",26))
        self.total_count.place(x=120,y=110)

        #=======present label=======#
        self.present_label=ctk.CTkLabel(self.attendance_page_frame,text="Present",text_color="black",font=("Consolas",26))
        self.present_label.place(x=300,y=80)

        #=======present count=======#
        self.present_count=ctk.CTkLabel(self.attendance_page_frame,text="0",text_color="black",font=("Consolas",26))
        self.present_count.place(x=340,y=110)

        #=======Absent label=======#
        self.absent_label=ctk.CTkLabel(self.attendance_page_frame,text="Absent",text_color="black",font=("Consolas",26))
        self.absent_label.place(x=596,y=80)

        #=======Absent count=======#
        self.absent_count=ctk.CTkLabel(self.attendance_page_frame,text="0",text_color="black",font=("Consolas",26))
        self.absent_count.place(x=630,y=110)

        #=======leave label=======#
        self.leave_label=ctk.CTkLabel(self.attendance_page_frame,text="Leave",text_color="black",font=("Consolas",26))
        self.leave_label.place(x=800,y=80)

        #=======leave count=======#
        self.leave_count=ctk.CTkLabel(self.attendance_page_frame,text="0",text_color="black",font=("Consolas",26))
        self.leave_count.place(x=830,y=110)

        self.attendance_page_frame.place(x = 50, y = 100)

        #==========leave & complain frame==========#
        self.leave_complain_page_frame = ctk.CTkFrame(self.home_page_frame, width = 992, height=150, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        #====leave label=======#
        self.leave_head_label=ctk.CTkLabel(self.leave_complain_page_frame,text="My Leave",width=496,height=50,fg_color="green",text_color="white",font=("Consolas",28))
        self.leave_head_label.place(x=0,y=0)

        #====leave count=====#
        self.leave_count1=ctk.CTkLabel(self.leave_complain_page_frame,text="0",text_color="black",font=("Consolas",40))
        self.leave_count1.place(x=240,y=70)

        #======complain label=====#
        self.complain_head_label=ctk.CTkLabel(self.leave_complain_page_frame,text="My Complain",width=495,height=50,fg_color="green",text_color="white",font=("Consolas",28))
        self.complain_head_label.place(x=497,y=0)

        #====Complain count=====#
        self.complain_count=ctk.CTkLabel(self.leave_complain_page_frame,text="0",text_color="black",font=("Consolas",40))
        self.complain_count.place(x=736,y=70)

        self.leave_complain_page_frame.place(x = 50, y = 340)

        #=======calling the function=========#
        attendance_detail()
        
        self.home_page_frame.place(x = 0, y = 0)
    
    def profile_frame(self):
        self.profile_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=600, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.profile_page_frame, text = "My Profile")

        #========functions========#
        def show_profile():
            global path, imageo
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                select_query = "select concat(first_name,' ', last_name) as name, srno , email, mobile, address, city, pincode, image_path, first_name from student where email = %s"
                cur.execute(select_query,(student_username,))

                records = cur.fetchone()

                # show this detail in entry box
                self.name_entry.configure(text = records[0])
                self.rollno_entry.configure(text = records[1])
                email_var.set(value=records[2])
                contact_var.set(value = records[3])
                address_var.set(value = records[4])
                city_var.set(value=records[5])
                pincode_var.set(value=records[6])

                image_path = records[7]
                #print(image_path)

                #open the image
                try:
                    image = Image.open(image_path)
                except FileNotFoundError:
                    print(f"Error: Could not find image at path: {image_path}")

                #base name of the image
                image_file_name = os.path.basename(image_path)

                #save the image
                image.save(image_file_name)
                
                #open image in form of ctk.CTkImage
                imageo = ctk.CTkImage(light_image=image, dark_image=image, size = (146, 166))

                #configure the right side frame label
                self.photo_label.configure(image = imageo)
                self.photo_label.image = imageo

                #configure the left side frame label
                self.student_photo_label.configure(image = imageo)
                self.student_photo_label.image = imageo
                
                #configure the image welcome label
                self.student_greet_label.configure(text = f"Welcome {records[8]}")

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        def update_photo():
            global changed_image_path
            changed_image_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("JPG Files", ".jpg"),("PNG Files", ".png"),("All files", ".")], initialdir="C:/Users/vikas/OneDrive/Documents/software project/image", title="Open File")

            try:
                image = Image.open(changed_image_path)

            except FileNotFoundError:
                print(f"Error: Could not find image at path: {changed_image_path}")

            #====configure the image===========#
                
            #base name of the image
            image_file_name = os.path.basename(changed_image_path)

            #save the image
            image.save(image_file_name)
                
            #open image in form of ctk.CTkImage
            imageo = ctk.CTkImage(light_image=image, dark_image=image, size = (146, 166))

            #configure the right side frame label
            self.photo_label.configure(image = imageo)
            self.photo_label.image = imageo

            self.upload_photo_label.configure(text = f"{image_file_name}", wraplength = 100)

            #configure the left side frame label
            self.teacher_photo_label.configure(image = imageo)
            self.teacher_photo_label.image = imageo
                
        def add_photo_database():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #update the image_path
                update_query = "update student set image_path = %s where email = %s"
                update_value = (changed_image_path, self.email_entry.get())

                cur.execute(update_query, update_value)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #============fetch id card============#
        def view_id_card():
            id_card_window = ctk.CTkToplevel(fg_color="white")
            id_card_window.geometry("600x500+800+250")
            id_card_window.title("School Management System")

            #==========function==========#
            def show_id_card():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    cur.execute("select srno, first_name from student where email = %s", (student_username,))

                    result = cur.fetchone()
                    return result

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

            #======card frame===========#
            self.student_card_frame = ctk.CTkFrame(id_card_window, border_width=2,border_color="green", fg_color="white", width = 580, height = 480, corner_radius=2)

            #======card label===========#
            self.head_label = ctk.CTkLabel(self.student_card_frame, text = "Identity Card",width = 580, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
            self.head_label.place(x = 0, y = 0)

            # #====ignore warnings===========#
            warnings.filterwarnings("ignore", category=UserWarning)

            #==========call the show id card function==============#
            results = show_id_card()
            # print(results)

            # #=====iid card image label==========#
            file_name = "C:/Users/vikas/OneDrive/Documents/software project/student_id"
            student_image = Image.open(f"{file_name}/{results[0]}_{results[1]} id_card.png")

            id_card_image = ImageTk.PhotoImage(student_image)
            self.student_card_label = ctk.CTkLabel(self.student_card_frame, text = "", image = id_card_image)
            self.student_card_label.place(x = 170, y = 50)

            # #===========save button=============#
            def save_student_card():
                file_path = filedialog.askdirectory(initialdir="C:/Users/vikas/OneDrive/Documents/save id cards")

                if file_path:
                    # print(file_path)
                    if os.path.exists(f"{file_path}/{results[0]}_{results[1]} id_card.png"):
                        error_message = f"The file '{file_path}/{results[0]}_{results[1]} id_card.png' already exists."
                        messagebox.showinfo("File Exists", message=error_message)
                    else:
                        image_to_save = ImageTk.getimage(id_card_image) 
                        image_to_save.save(f"{file_path}/{results[0]}_{results[1]} id_card.png")
                        success_message = f"The student ID card for {results[1]} has been saved successfully!"
                        messagebox.showinfo("Success", message=success_message)

            #=========button===============#
            self.save_button = ctk.CTkButton(self.student_card_frame, text = "Save", width = 120, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=save_student_card)
            self.save_button.place(x = 220, y = 400)

            self.student_card_frame.place(x = 10, y = 10)

            #=====calling the function==========#
            show_id_card()
            
            id_card_window.grab_set()

        #=======inside widget========#
        self.name_label =  ctk.CTkLabel(self.profile_page_frame, text = "Name : ", text_color="green", font=("Consolas", 20))
        self.name_label.place(x = 110, y = 80)


        self.name_entry =  ctk.CTkLabel(self.profile_page_frame, text = "", text_color="red", font=("Consolas", 20))
        self.name_entry.place(x = 190, y = 80)

        self.rollno_label =  ctk.CTkLabel(self.profile_page_frame, text = "Roll No : ", text_color="green", font=("Consolas", 20))
        self.rollno_label.place(x = 75, y = 120)

        self.rollno_entry =  ctk.CTkLabel(self.profile_page_frame, text = "", text_color="red", font=("Consolas", 20))
        self.rollno_entry.place(x = 190, y = 120)

        self.email_label =  ctk.CTkLabel(self.profile_page_frame, text = "Email : ", text_color="green", font=("Consolas", 20))
        self.email_label.place(x = 98, y = 160)

        email_var = tk.StringVar()
        self.email_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green", textvariable=email_var, state="disabled")
        self.email_entry.place(x = 190, y = 160)

        self.contact_label =  ctk.CTkLabel(self.profile_page_frame, text = "Contact No : ", text_color="green", font=("Consolas", 20))
        self.contact_label.place(x = 42, y = 200)

        contact_var = tk.StringVar()
        self.contact_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green",textvariable=contact_var, state="disabled")
        self.contact_entry.place(x = 190, y = 200)

        self.address_label =  ctk.CTkLabel(self.profile_page_frame, text = "Address : ", text_color="green", font=("Consolas", 20))
        self.address_label.place(x = 75, y = 240)

        address_var = tk.StringVar()
        self.address_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 60, corner_radius=2, font = ("Consolas", 20), border_color="green",textvariable=address_var, state="disabled")
        self.address_entry.place(x = 190, y = 240)

        self.city_label =  ctk.CTkLabel(self.profile_page_frame, text = "City : ", text_color="green", font=("Consolas", 20))
        self.city_label.place(x = 108, y = 305)

        city_var = tk.StringVar()
        self.city_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green",textvariable=city_var, state="disabled")
        self.city_entry.place(x = 190, y = 305)

        self.pincode_label =  ctk.CTkLabel(self.profile_page_frame, text = "Pincode : ", text_color="green", font=("Consolas", 20))
        self.pincode_label.place(x = 75, y = 345)

        pincode_var = tk.StringVar()
        self.pincode_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 20), border_color="green",textvariable=pincode_var, state="disabled")
        self.pincode_entry.place(x = 190, y = 345)

        self.update_button = ctk.CTkButton(self.profile_page_frame, text = "Update", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=None, border_color="green", border_width=2)
        self.update_button.place(x = 190, y = 390)

        self.view_id_button = ctk.CTkButton(self.profile_page_frame, text = "View ID Card", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=view_id_card, border_color="green", border_width=2)
        self.view_id_button.place(x = 190, y = 435)

        self.upload_photo_button = ctk.CTkButton(self.profile_page_frame, text = "Choose File", width = 150, height = 35, border_width=2, border_color="black", font = ("Consolas", 20), text_color="black", fg_color="#D8D9DA", corner_radius=2, hover_color="white", cursor = "hand2", command = update_photo)
        self.upload_photo_button.place(x = 450, y = 160)

        self.upload_photo_label = ctk.CTkLabel(self.profile_page_frame, text = "No File Choosen", text_color="black", font=("Consolas", 17))
        self.upload_photo_label.place(x = 610, y = 160)

        self.add_photo_button = ctk.CTkButton(self.profile_page_frame, text = "Add", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=add_photo_database, border_color="green", border_width=2)
        self.add_photo_button.place(x = 780, y = 155)

        self.updated_photo_frame = ctk.CTkFrame(self.profile_page_frame, width = 150, height=170, corner_radius=0,  border_width=1, border_color="black", fg_color="white")
        self.updated_photo_frame.place(x=450,y=220)

        self.photo_label = ctk.CTkLabel(self.updated_photo_frame, text = "", fg_color="grey", width = 149, height=169)
        self.photo_label.place(x = 0, y = 0)

        self.profile_page_frame.place(x=0,y=0)

        #======calling the function======#
        show_profile()

        self.profile_page_frame.place(x = 0, y = 0)

    def leave_frame(self):
        self.leave_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.leave_page_frame, text = "Leave")

        #=========functions=========#
        def student_apply_leave_frame():
            #=====inside frame======#
            self.leave_main_frame = ctk.CTkFrame(self.leave_page_frame, width = 1072, height=270, corner_radius=0,  border_width=0, border_color="green", fg_color="white")

            #=======functions==============#
            def apply_for_leave():
                leave_msg = self.leave_textbox.get("1.0", tk.END)
                days = no_of_day_var.get()
                current_date = date.today()
                hour = strftime("%I")          #for 12 hours = I and for 24 hours = H
                minute = strftime("%M")
                second = strftime("%S")
                time = f"{hour}:{minute}:{second}"
                date_time = f"{current_date} {time}"

                #===connecting to the database and sending leave to teacher=========#
                if leave_msg == "" or days == "":
                    messagebox.showerror("Error","Please fill all the fields!")
                else:
                    try:
                        con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                        cur = con.cursor()
                        
                        #fetch some personal details
                        cur.execute("select srno, concat(first_name,' ',last_name) as name, std_name from student where email = %s",(student_username,))

                        std_record = cur.fetchone()
                        
                        #insert record in database
                        insert_query = "insert into student_leave(rollno, student_name, std_name, message, no_days, edate) value(%s, %s, %s, %s, %s, %s)"
                        insert_value = (std_record[0], std_record[1], std_record[2], leave_msg, days,date_time )

                        cur.execute(insert_query, insert_value)

                        #commit the changes
                        con.commit()

                        self.apply_leave_label.configure(text = "Apply for leave Successfully")

                        #close the connection
                        con.close()

                        #===clear the textbox========#
                        self.leave_textbox.delete("0.0", tk.END)
                        no_of_day_var.set("")

                    except Exception as e:
                        print(e)
                        # messagebox.showerror("Error", e)

            #======leave reason label=====#
            self.leave_label = ctk.CTkLabel(self.leave_main_frame, text = "Leave Reason:", font = ("Consolas", 20))
            self.leave_label.place(x = 300, y = 75)

            #======leave reason textbox=====#
            self.leave_textbox = ctk.CTkTextbox(self.leave_main_frame,width=300, height = 80, corner_radius=0, border_width=2, border_color="grey", scrollbar_button_hover_color="green", font = ("Consolas", 20), wrap = "word")
            self.leave_textbox.place(x = 450, y = 50)
            self.leave_textbox.bind("<KeyRelease>", lambda e: self.apply_leave_label.configure(text=""))

            #======no. of days label=====#
            self.days_label = ctk.CTkLabel(self.leave_main_frame, text = "No of Days:", font = ("Consolas", 20))
            self.days_label.place(x = 322, y = 150)

            #==========Drop down menu===========#
            self.select_days_values=["01","02","03","04","05","06","07","08","09","10"]
            no_of_day_var = tk.StringVar(value = "")
            self.select_days_option=ctk.CTkOptionMenu(self.leave_main_frame,width=80,height=30,corner_radius=2,values=self.select_days_values,fg_color="#D8D9DA",text_color="black",dropdown_font=("Consolas",18),font=("Consolas",18), variable=no_of_day_var)
            self.select_days_option.place(x=450,y=150)

            #========apply leave buttons=========#
            self.apply_leave_button = ctk.CTkButton(self.leave_main_frame, text = "Apply Leave", width = 200, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=apply_for_leave)
            self.apply_leave_button.place(x = 450, y = 190)

            self.apply_leave_label = ctk.CTkLabel(self.leave_main_frame, text = "", font = ("Consolas", 18), text_color="green")
            self.apply_leave_label.place(x = 410, y = 240)

            self.leave_main_frame.place(x = 10, y = 150)

        def student_leave_status_frame():
            #=====inside frame======#
            self.leave_status_frame = ctk.CTkFrame(self.leave_page_frame, width = 1072, height=270, corner_radius=0,  border_width=0, border_color="green", fg_color="white")

            #====================function====================#
            def show_leave_record():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #fetch the leave record detail to see status
                    cur.execute("select message, no_days, status from student_leave sl, student s where sl.rollno = s.srno and s.email = %s",(student_username,))

                    records = cur.fetchall()

                    self.count = 0
                    #show record in treeview
                    for record in records:
                        if self.count %2 == 0:
                            self.leave_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2]), tags=("evenrow",))
                        else:
                            self.leave_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2]), tags=("oddrow",))
                        self.count += 1
                    
                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)
                
            #=======treeview setting========#
            #add some style
            style = ttk.Style()

            #pick a theme
            style.theme_use("alt")

            #configure the tree view color
            style.configure("Treeview", 
                            background = "#EEF0E5",
                            rowheight = 25,
                            fieldbackground = "#F3FBF1", font = ("Consolas", 14))
            
            style.configure("mystyle.Treeview", font=('Consolas', 15))

            #configure the selected color
            style.configure("Treeview", background = [("selected", "#347083")])

            #increse the font size of heading
            style.configure("Treeview.Heading", font=("Consolas", 18))

            self.data_frame = tk.Frame(self.leave_status_frame, bg = "lightgrey", borderwidth=0, relief="solid")
            self.data_frame.pack_propagate(False)
            self.data_frame.place(x = 10, y = 50, height = 200, width = 1320)

            #create a scrollbar
            y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
            x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

            y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
            x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

            #create a treeview
            self.leave_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
            self.leave_tree.pack(fill = "both", expand= True)

            #configure the scrollbar
            x_scroll.config(command = self.leave_tree.xview)
            y_scroll.config(command = self.leave_tree.yview)

            #define our columns
            self.leave_tree["columns"] = ("Leave Reason", "Days", "Status")

            #format column
            self.leave_tree.column("Leave Reason", anchor="center", width = 300, minwidth=300)
            self.leave_tree.column("Days", anchor="center", width = 100, minwidth=100)
            self.leave_tree.column("Status", anchor="center", width = 100, minwidth = 100)
            
            #create a heading
            self.leave_tree.heading("Leave Reason", text = "Leave Reason", anchor = "center")
            self.leave_tree.heading("Days", text = "Days", anchor = "center")
            self.leave_tree.heading("Status", text = "Status", anchor = "center")
            
            #Create striped to our tages
            self.leave_tree.tag_configure("oddrow", background="white")
            self.leave_tree.tag_configure("evenrow", background="lightblue")

            #=======calling the function==========#
            show_leave_record()

            self.leave_status_frame.place(x = 10, y = 150)
        
        #========inside widgets=========#
        #=======apply for leave button======#
        self.apply_leave_button = ctk.CTkButton(self.leave_page_frame, text = "Apply for Leave", width = 350, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=student_apply_leave_frame)
        self.apply_leave_button.place(x=10,y=80)

        #=======leave status report button======#
        self.leave_status_button = ctk.CTkButton(self.leave_page_frame, text = "Leave Status Report", width = 350, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=student_leave_status_frame)
        self.leave_status_button.place(x=420,y=80)

        self.leave_page_frame.place(x = 0, y = 0)

    def complain_frame(self):
        self.complain_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.complain_page_frame, text = "Complain")

        def send_complain_func():
            subject = self.complain_entry.get()
            message = self.message_textbox.get("1.0", tk.END)
            current_date = date.today()
            hour = strftime("%I")          #for 12 hours = I and for 24 hours = H
            minute = strftime("%M")
            second = strftime("%S")
            time = f"{hour}:{minute}:{second}"
            date_time = f"{current_date} {time}"

            #================
            
            try:
                con = mycon.connect(host = "localhost", username = "root", password ="root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #fetch the leave record detail to see status
                cur.execute("select srno, concat(first_name,' ',last_name) as name from student where email = %s",(student_username,))

                records = cur.fetchall()

                if not self.complain_entry.get() and not self.message_textbox.get("0.0", tk.END) == "":
                    messagebox.showerror("Complain Error", "Fields are required!")
                    return
                
                for record in records:
                    # inserting the values
                    cur.execute("insert into complain(rollno, student_name, subject,message, edate) value(%s, %s, %s, %s, %s)", (record[0], record[1],subject, message, date_time))

                    #commit the changes
                con.commit()
                        
                self.complain_label.configure(text = f"Complain Sent")

                #clear the textbox
                self.complain_entry.delete(0, tk.END)
                self.message_textbox.delete("0.0", tk.END)

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
                con.rollback()
            
        def show_complain_record():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #fetch the detail of complain
                cur.execute("select subject, message, reply from complain c, student s where s.srno = c.rollno and s.email = %s",(student_username,))

                complain_record = cur.fetchall()

                #===showing the data in treeview=====#
                self.count = 0
                for fetch_record in complain_record:
                    if self.count %2 == 0:
                        self.complain_tree.insert(parent = "", index = tk.END, iid = self.count, values=(fetch_record[0], fetch_record[1], fetch_record[2]), tags=("evenrow",))
                    else:
                        self.complain_tree.insert(parent = "", index = tk.END, iid = self.count, values=(fetch_record[0], fetch_record[1], fetch_record[2]), tags=("oddrow",))
                    self.count += 1

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        
        # def remove_all(e):
        #     for record in self.complain_tree.get_children():
        #         self.complain_tree.delete(record)

        #========inside widgets=========#
        #======Complain label=====#
        self.complain_label = ctk.CTkLabel(self.complain_page_frame, text = "Complain About:", font = ("Consolas", 20))
        self.complain_label.place(x = 320, y = 100)

        #======Complain entry========#
        self.complain_entry = ctk.CTkEntry(self.complain_page_frame, width = 250, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
        self.complain_entry.place(x = 500, y = 100)
        self.complain_entry.bind("<KeyRelease>", lambda e : self.complain_label.configure(text = ""))
        # self.complain_entry.bind("<KeyRelease>", remove_all)

        #======message label=====#
        self.message_label = ctk.CTkLabel(self.complain_page_frame, text = "Message:", font = ("Consolas", 20))
        self.message_label.place(x = 398, y = 175)

        #======message textbox========#
        self.message_textbox = ctk.CTkTextbox(self.complain_page_frame, height = 80,width=250, corner_radius=0, border_width=2, border_color="grey", scrollbar_button_hover_color="green", font = ("Consolas", 20), wrap = "word")
        self.message_textbox.place(x = 500, y = 150)

        #====Send buttons======#
        self.send_button = ctk.CTkButton(self.complain_page_frame, text = "Send", width = 150, height = 35, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=send_complain_func)
        self.send_button.place(x = 500, y = 240)
        # self.send_button.bind("<Button-1>", show_complain_record)

        #======complaint label=====#
        self.complain_label = ctk.CTkLabel(self.complain_page_frame, text = "", font = ("Consolas", 18), text_color="green")
        self.complain_label.place(x = 500, y = 280)

        #=======treeview setting========#
        #add some style
        style = ttk.Style()

        #pick a theme
        style.theme_use("alt")

        #configure the tree view color
        style.configure("Treeview", 
                        background = "#EEF0E5",
                        rowheight = 25,
                        fieldbackground = "#F3FBF1", font = ("Consolas", 14))
                
        style.configure("mystyle.Treeview", font=('Consolas', 15))

        #configure the selected color
        style.configure("Treeview", background = [("selected", "#347083")])

        #increse the font size of heading
        style.configure("Treeview.Heading", font=("Consolas", 18))

        self.data_frame = tk.Frame(self.complain_page_frame, bg = "lightgrey", borderwidth=0, relief="solid")
        self.data_frame.pack_propagate(False)
        self.data_frame.place(x = 80, y = 420 , height = 200, width = 1200)

        #create a scrollbar
        y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
        x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

        y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

        #create a treeview
        self.complain_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
        self.complain_tree.pack(fill = "both", expand= True)

        #configure the scrollbar
        x_scroll.config(command = self.complain_tree.xview)
        y_scroll.config(command = self.complain_tree.yview)

        #define our columns
        self.complain_tree["columns"] = ("About", "Message", "Status")

        #format column
        self.complain_tree.column("About", anchor="center", width = 200, minwidth=300)
        self.complain_tree.column("Message", anchor="center", width = 300, minwidth=400)
        self.complain_tree.column("Status", anchor="center", width = 100, minwidth = 100)
                
        #create a heading
        self.complain_tree.heading("About", text = "About", anchor = "center")
        self.complain_tree.heading("Message", text = "Message", anchor = "center")
        self.complain_tree.heading("Status", text = "Status", anchor = "center")
                
        #Create striped to our tages
        self.complain_tree.tag_configure("oddrow", background="white")
        self.complain_tree.tag_configure("evenrow", background="lightblue") 

        #======calling the function============#
        show_complain_record()
        
        self.complain_page_frame.place(x = 0, y = 0)

    def attendance_frame(self):
        self.attendance_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=600, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        #=========calling the function====================#
        def show_attendance_student():
            month_name = month_var.get()

            if not month_name:
                messagebox.showerror("Error", "Please first select month.")
                return
            else:
                
                def show_attendance():
                    try:
                        con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                        #create a cursor instance
                        cur = con.cursor()

                        '''#fetch the detail of complain
                        cur.execute("select subject, message, reply from complain c, student s where s.srno = c.rollno and s.email = 'vikaskahar25077@gmail.com'")

                        complain_record = cur.fetchall()

                        #===showing the data in treeview=====#
                        self.count = 0
                        for fetch_record in complain_record:
                            if self.count %2 == 0:
                                self.complain_tree.insert(parent = "", index = tk.END, iid = self.count, values=(fetch_record[0], fetch_record[1], fetch_record[2]), tags=("evenrow",))
                            else:
                                self.complain_tree.insert(parent = "", index = tk.END, iid = self.count, values=(fetch_record[0], fetch_record[1], fetch_record[2]), tags=("oddrow",))
                            self.count += 1'''

                        #commit the changes
                        con.commit()

                        #close the connection
                        con.close()

                    except Exception as e:
                        print("Error ", e)
                


                #add some style
                style = ttk.Style()

                #pick a theme
                style.theme_use("alt")

                #configure the tree view color
                style.configure("Treeview", 
                                background = "#EEF0E5",
                                rowheight = 25,
                                fieldbackground = "#F3FBF1", font = ("Consolas", 14))
                        
                style.configure("mystyle.Treeview", font=('Consolas', 15))

                #configure the selected color
                style.configure("Treeview", background = [("selected", "#347083")])

                #increse the font size of heading
                style.configure("Treeview.Heading", font=("Consolas", 18))

                self.data_frame = tk.Frame(self.attendance_page_frame, bg = "lightgrey", borderwidth=0, relief="solid")
                self.data_frame.pack_propagate(False)
                self.data_frame.place(x = 50, y = 200 , height = 200, width = 1200)

                #create a scrollbar
                y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
                x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

                y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
                x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

                #create a treeview
                self.attendance_report_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
                self.attendance_report_tree.pack(fill = "both", expand= True)

                #configure the scrollbar
                x_scroll.config(command = self.attendance_report_tree.xview)
                y_scroll.config(command = self.attendance_report_tree.yview)

                #define our columns
                self.attendance_report_tree["columns"] = ("Attendance Date", "Attendance Status", "By Staff")

                #format column
                self.attendance_report_tree.column("Attendance Date", anchor="center", width = 200, minwidth=200)
                self.attendance_report_tree.column("Attendance Status", anchor="center", width = 200, minwidth=200)
                self.attendance_report_tree.column("By Staff", anchor="center", width = 100, minwidth = 100)
                        
                #create a heading
                self.attendance_report_tree.heading("Attendance Date", text = "Attendance Date", anchor = "center")
                self.attendance_report_tree.heading("Attendance Status", text = "Attendance Status", anchor = "center")
                self.attendance_report_tree.heading("By Staff", text = "By Staff", anchor = "center")
                        
                #Create striped to our tages
                self.attendance_report_tree.tag_configure("oddrow", background="white")
                self.attendance_report_tree.tag_configure("evenrow", background="lightblue") 

                show_attendance()

            
        #===========================================#
        ChangeLabel(self.attendance_page_frame, text = "Attendance")

        #=========inside widgets============#
        #======select month label=====#
        self.month_label = ctk.CTkLabel(self.attendance_page_frame, text = "Select Month:", font = ("Consolas", 20))
        self.month_label.place(x = 70, y = 70)

        #==========Drop down menu===========#
        self.select_month_values=["January","February","March","April","May","June","July","August","September","October","November","December"]
        month_var = tk.StringVar(value = "")
        self.select_month_option=ctk.CTkOptionMenu(self.attendance_page_frame,width=200,height=30,corner_radius=2,values=self.select_month_values,fg_color="#D8D9DA",text_color="black",dropdown_font=("Consolas",18),font=("Consolas",18), variable=month_var)
        self.select_month_option.place(x=230,y=70)

        #=====Report buttons=====#
        self.report_button = ctk.CTkButton(self.attendance_page_frame, text = "Report", width = 150, height = 35, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=show_attendance_student)
        self.report_button.place(x = 460, y = 68)

        self.attendance_page_frame.place(x = 0, y = 0)

    '''def password_frame(self):
        self.password_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=600, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.password_page_frame, text = "Password")

        #========inside widgets=========#
        #======Current password label=====#
        self.current_password_label = ctk.CTkLabel(self.password_page_frame, text = "Current Password:", font = ("Consolas", 20))
        self.current_password_label.place(x = 320, y = 100)

        #======current password entry========#
        self.current_password_entry = ctk.CTkEntry(self.password_page_frame, width = 250, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
        self.current_password_entry.place(x = 520, y = 100)

        #======new password label=====#
        self.new_password_label = ctk.CTkLabel(self.password_page_frame, text = "New Password:", font = ("Consolas", 20))
        self.new_password_label.place(x = 365, y = 150)

        #======new password entry========#
        self.new_password_entry = ctk.CTkEntry(self.password_page_frame, width = 250, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
        self.new_password_entry.place(x = 520, y = 150)

        #======confirm password label=====#
        self.confirm_password_label = ctk.CTkLabel(self.password_page_frame, text = "Confirm Password:", font = ("Consolas", 20))
        self.confirm_password_label.place(x = 320, y = 200)

        #======confirm password entry========#
        self.confirm_password_entry = ctk.CTkEntry(self.password_page_frame, width = 250, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
        self.confirm_password_entry.place(x = 520, y = 200)

        #====Change password buttons======#
        self.change_password_button = ctk.CTkButton(self.password_page_frame, text = "Change Password", width = 250, height = 35, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=None)
        self.change_password_button.place(x = 520, y = 250)

        self.password_page_frame.place(x = 0, y = 0)'''
    
    def feedback_frame(self):
        self.feedback_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")

        ChangeLabel(self.feedback_page_frame, text = "Feedback")
        #========feedback label============#
        self.feedback_label = ctk.CTkLabel(self.feedback_page_frame,font = ("Verdana Pro Semibold", 30),text = "FEEDBACK FORM", text_color="black")
        self.feedback_label.place(x = 400, y = 70)

        def save_feedback_response():
            choice_0_answer = self.first1_var.get()
            choice_1_answer = self.first2_var.get()
            choice_2_answer = self.first3_var.get()
            other_feedback0 = self.feedback_textbox1.get("0.0", tk.END)
            other_feedback1 = self.feedback_textbox2.get("0.0", tk.END)
            other_feedback2 = self.feedback_textbox3.get("0.0", tk.END)

            #=======datetime========#
            current_date = date.today()
            hour = strftime("%I")          #for 12 hours = I and for 24 hours = H
            minute = strftime("%M")
            second = strftime("%S")
            time = f"{hour}:{minute}:{second}"
            date_time = f"{current_date} {time}"

            #=======insert feedback into database============#
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                cur.execute("select student_id from feedback where student_id = %s group by student_id", (student_srno[0],))
                submitted = cur.fetchall()

                if submitted:
                    messagebox.showerror("Error", "Feedback already submitted. Thank you!")
                
                else:
                    insert_query = "insert into feedback(student_id, question_id, answer_choices, brief_answer_text, edate) values(%s, %s, %s, %s, %s)"
                    insert_values = [(student_srno[0], question_id_list[0], choice_0_answer, other_feedback0, date_time),(student_srno[0], question_id_list[1], choice_1_answer, other_feedback1, date_time),(student_srno[0], question_id_list[2], choice_2_answer, other_feedback2, date_time)]

                    cur.executemany(insert_query, insert_values)

                    #commit the changes
                    con.commit()

                    messagebox.showinfo("Success", "Thank you for your feedback!")

                #close the connection
                con.close()

                #=====clear the textbox============#
                self.first1_var.set(value = "")
                self.first2_var.set(value = "")
                self.first3_var.set(value = "")
                self.feedback_textbox1.delete("0.0", tk.END)
                self.feedback_textbox2.delete("0.0", tk.END)
                self.feedback_textbox3.delete("0.0", tk.END)

            except Exception as e:
                print("Error ", e)

        def question_frame(frame, question1, choice1, choice2, choice3, choice4, choice_var):
            global feedback_textbox
            please_label = ctk.CTkLabel(frame, text = "Please help us to serve you better by taking a couple of minutes", text_color="white", font = ("Consolas", 18))
            please_label.place(x = 25, y = 20)

            question1_label = ctk.CTkLabel(frame, text = f"{question1}", text_color="#5DEBD7", font = ("Consolas", 18))
            question1_label.place(x = 25, y = 60)

            choice1=ctk.CTkRadioButton(frame, text=choice1 ,value="choice1",variable = choice_var,font=("Consolas",18), fg_color="white", hover_color="yellow", text_color="white", border_color="white")
            choice1.place(x = 50, y = 100)

            choice2=ctk.CTkRadioButton(frame, text=choice2 ,value="choice2",variable = choice_var,font=("Consolas",18), fg_color="white", hover_color="yellow", text_color="white", border_color="white")
            choice2.place(x = 50, y = 140)

            choice3=ctk.CTkRadioButton(frame, text=choice3 ,value="choice3",variable = choice_var,font=("Consolas",18), fg_color="white", hover_color="yellow", text_color="white", border_color="white")
            choice3.place(x = 50, y = 180)

            choice4=ctk.CTkRadioButton(frame, text=choice4 ,value="choice4",variable = choice_var,font=("Consolas",18), fg_color="white", hover_color="yellow", text_color="white", border_color="white")
            choice4.place(x = 50, y = 220)

            specific_feedback = "If you have specific feedback please write to us."
            specific_feedback_label = ctk.CTkLabel(frame, text = specific_feedback, text_color="#5DEBD7", font = ("Consolas", 18))
            specific_feedback_label.place(x = 25, y = 260)

            # feedback_textbox = ctk.CTkTextbox(frame, width = 650, height = 130, corner_radius=4, font = ("Consolas", 18), border_color="white", text_color="white", fg_color="#272829", border_width=2, wrap = "word")
            # feedback_textbox.place(x = 25, y = 300)

        #=========fetch feedback from databass============#
        try:
            con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

            #create a cursor instance
            cur = con.cursor()

            #=====fetch feedback question and option=============#
            cur.execute("select * from feedback_question limit 3")

            feedback_record = cur.fetchall()

            question_id_list = []
            question_list= []
            option1_list= [] 
            option2_list= [] 
            option3_list= [] 
            option4_list= []
            for feedback in feedback_record:
                question_id_list.append(feedback[0])
                question_list.append(feedback[1])
                option1_list.append(feedback[2])
                option2_list.append(feedback[3])
                option3_list.append(feedback[4])
                option4_list.append(feedback[5])

            # #=========fetch student srno============#
            cur.execute("select srno from student where email = %s", (student_username,))

            student_srno = cur.fetchone()
        
            #commit the changes
            con.commit()

            #close the connection
            con.close()

        except Exception as e:
            print("Error ", e)

        #==========first frame===========#
        self.first_frame = ctk.CTkFrame(self.feedback_page_frame, width = 700, height=550, corner_radius=0,  border_width=1, border_color="green", fg_color="#36454F")

        self.first1_var = tk.StringVar(value = "")
        question_frame(frame = self.first_frame, question1=question_list[0], choice1=option1_list[0], choice2=option2_list[0], choice3 = option3_list[0], choice4 = option4_list[0], choice_var=self.first1_var)

        self.feedback_textbox1 = ctk.CTkTextbox(self.first_frame, width = 650, height = 130, corner_radius=4, font = ("Consolas", 18), border_color="white", text_color="white", fg_color="#272829", border_width=2, wrap = "word")
        self.feedback_textbox1.place(x = 25, y = 300)

        self.page1_page2_btn = ctk.CTkButton(self.first_frame, text = "NEXT", width = 100, height = 40, font = ("Consolas", 20), text_color="white", fg_color="#272829", corner_radius=4, hover_color=None, border_width=2, border_color="white", cursor = "hand2", command= lambda : self.second_frame.tkraise())
        self.page1_page2_btn.place(x = 575, y = 460)

        self.first_frame.place(x = 200, y = 120)
        #================================#

        #==========second frame=========#
        self.second_frame = ctk.CTkFrame(self.feedback_page_frame, width = 700, height=550, corner_radius=0,  border_width=1, border_color="green", fg_color="#36454F")

        self.first2_var = tk.StringVar(value = "")
        question_frame(frame = self.second_frame, question1=question_list[1], choice1=option1_list[1], choice2=option2_list[1], choice3 = option3_list[1], choice4 = option4_list[1], choice_var=self.first2_var)

        self.feedback_textbox2 = ctk.CTkTextbox(self.second_frame, width = 650, height = 130, corner_radius=4, font = ("Consolas", 18), border_color="white", text_color="white", fg_color="#272829", border_width=2, wrap = "word")
        self.feedback_textbox2.place(x = 25, y = 300)

        self.page2_page1_btn = ctk.CTkButton(self.second_frame, text = "PREVIOUS", width = 120, height = 40, font = ("Consolas", 20), text_color="white", fg_color="#272829", corner_radius=4, hover_color=None, border_width=2, border_color="white", cursor = "hand2", command= lambda : self.first_frame.tkraise())
        self.page2_page1_btn.place(x = 20, y = 460)
  
        self.page2_page3_btn = ctk.CTkButton(self.second_frame, text = "NEXT", width = 100, height = 40, font = ("Consolas", 20), text_color="white", fg_color="#272829", corner_radius=4, hover_color=None, border_width=2, border_color="white", cursor = "hand2", command= lambda : self.third_frame.tkraise())
        self.page2_page3_btn.place(x = 575, y = 460)

        self.second_frame.place(x = 200, y = 120)
        #================================#

        #==========third frame=========#
        self.third_frame = ctk.CTkFrame(self.feedback_page_frame, width = 700, height=550, corner_radius=0,  border_width=1, border_color="green", fg_color="#36454F")

        self.first3_var = tk.StringVar(value = "")
        question_frame(frame = self.third_frame, question1=question_list[2], choice1=option1_list[2], choice2=option2_list[2], choice3 = option3_list[2], choice4 = option4_list[2], choice_var=self.first3_var)

        self.feedback_textbox3 = ctk.CTkTextbox(self.third_frame, width = 650, height = 130, corner_radius=4, font = ("Consolas", 18), border_color="white", text_color="white", fg_color="#272829", border_width=2, wrap = "word")
        self.feedback_textbox3.place(x = 25, y = 300)

        self.page3_page2_btn = ctk.CTkButton(self.third_frame, text = "PREVIOUS", width = 120, height = 40, font = ("Consolas", 20), text_color="white", fg_color="#272829", corner_radius=4, hover_color=None, border_width=2, border_color="white", cursor = "hand2", command= lambda : self.second_frame.tkraise())
        self.page3_page2_btn.place(x = 20, y = 460)

        self.submit_btn = ctk.CTkButton(self.third_frame, text = "SUBMIT", width = 100, height = 40, font = ("Consolas", 20), text_color="white", fg_color="#272829", corner_radius=4, hover_color=None, border_width=2, border_color="white", cursor = "hand2", command= save_feedback_response)
        self.submit_btn.place(x = 575, y = 460)

        self.third_frame.place(x = 200, y = 120)
        #================================#

        #==========raise first frame=======#
        self.first_frame.tkraise()

        self.feedback_page_frame.place(x = 0, y = 0)

class TeacherHomeWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="white")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        #=======switch frame========#
        def switch_frame(page, indicator_button):
            for frame in self.rightside_frame.winfo_children():
                frame.destroy()
                self.update()
            page()

            for child in self.teacher_sidebar_frame.winfo_children():
                if isinstance(child, ctk.CTkButton):
                    child.configure(fg_color = "#1C1678")

            indicator_button.configure(fg_color= "#008DDA")
        
        #=====return to main window=======#
        def return_to_main():
            self.destroy()
            root.deiconify()

        #====calling heading label====#
        self.heading_frame=HeadingFrame(self)
        self.heading_frame.place(x=5,y=5)

        #=====teacher home frame=====#
        self.teacher_homepage_frame=ctk.CTkFrame(self,border_color="green",border_width=1,fg_color="white",width=1526,height=730,corner_radius=1)

        #======teacher sidebar frame=====#
        self.teacher_sidebar_frame=ctk.CTkFrame(self.teacher_homepage_frame,border_color="green",border_width=0,width=350,height=700, corner_radius=0,fg_color="#1C1678")

        #====heading label====#
        self.sidebar_head_label=ctk.CTkLabel(self.teacher_sidebar_frame,text="",width=348,height=5,fg_color="#008DDA")
        self.sidebar_head_label.place(x=0,y=0)

        #=======photo frame======#
        self.teacher_photo_frame = ctk.CTkFrame(self.teacher_sidebar_frame, width = 150, height=170, corner_radius=0,  border_width=2, border_color="black", fg_color="white")
        self.teacher_photo_frame.place(x=100,y=50)

        self.teacher_photo_label = ctk.CTkLabel(self.teacher_photo_frame, text = "", fg_color="white",width = 149, height=170)
        self.teacher_photo_label.place(x = 0, y = 0)

        self.teacher_greet_label = ctk.CTkLabel(self.teacher_sidebar_frame, text = "", font=("Consolas", 20), text_color="red")
        self.teacher_greet_label.place(x = 115, y = 240)

        #======Sidebar menu=======#
        self.image = ctk.CTkImage(light_image=Image.open("image/home_icon (2).png"), dark_image=Image.open("image/home_icon (2).png"), size = (25, 25))
        self.profile_button = ctk.CTkButton(self.teacher_sidebar_frame, text = "             My Profile    ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#008DDA", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=lambda :switch_frame(page=self.profile_frame, indicator_button=self.profile_button), image = self.image, compound="right", anchor="right")
        self.profile_button.place(x=24,y=290)

        # self.add_student_button = ctk.CTkButton(self.teacher_sidebar_frame, text = "Add Student", width = 348, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=0, hover_color=None, cursor = "hand2", command=lambda :switch_frame(page=self.add_student_frame), border_width=1, border_color="white")
        # self.add_student_button.place(x=0,y=335)

        self.result_student_button = ctk.CTkButton(self.teacher_sidebar_frame, text = "                   Result   ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=lambda :switch_frame(page=self.result_student_frame,indicator_button=self.result_student_button), image = self.image, compound="right", anchor = "right")
        self.result_student_button.place(x=24,y=335)

        self.student_report_button = ctk.CTkButton(self.teacher_sidebar_frame, text = "      Student Report   ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=lambda :switch_frame(page=self.student_report_frame,indicator_button=self.student_report_button), image = self.image, compound="right", anchor = "right")
        self.student_report_button.place(x=24,y=380)

        self.student_attendance_button = ctk.CTkButton(self.teacher_sidebar_frame, text = "           Attendance   ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=lambda :switch_frame(page=self.student_attendance_frame,indicator_button=self.student_attendance_button),image = self.image, compound="right", anchor = "right")
        self.student_attendance_button.place(x=24,y=425)

        self.student_attendance_report_button = ctk.CTkButton(self.teacher_sidebar_frame, text = "Attendance Report    ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=lambda :switch_frame(page=self.student_attendance_report_frame,indicator_button=self.student_attendance_report_button),image = self.image, compound="right", anchor = "right")
        self.student_attendance_report_button.place(x=24,y=470)

        self.student_advance_report_button  = ctk.CTkButton(self.teacher_sidebar_frame, text = "   Advance Reports    ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=lambda :switch_frame(page=self.advance_report_frame,indicator_button=self.student_advance_report_button),image = self.image, compound="right", anchor = "right")
        self.student_advance_report_button.place(x=24,y=515)

        self.student_complain_button  = ctk.CTkButton(self.teacher_sidebar_frame, text = "             Complain    ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=lambda :switch_frame(page=self.student_complain_frame,indicator_button=self.student_complain_button),image = self.image, compound="right", anchor = "right")
        self.student_complain_button.place(x=24,y=560)

        self.student_leave_button  = ctk.CTkButton(self.teacher_sidebar_frame, text = "                 Leave    ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=lambda :switch_frame(page=self.student_leave_frame,indicator_button=self.student_leave_button),image = self.image, compound="right", anchor = "right")
        self.student_leave_button.place(x=24,y=605)

        self.student_logout_button  = ctk.CTkButton(self.teacher_sidebar_frame, text = "                Logout    ", width = 300, height = 45, font = ("Verdana Pro", 18), text_color="white", fg_color="#1C1678", corner_radius=50, hover_color="#008DDA", cursor = "hand2", command=return_to_main,image = self.image, compound="right", anchor = "right")
        self.student_logout_button.place(x=24,y=650)

        # # self.student_advance_att_report_button = ctk.CTkButton(self.teacher_sidebar_frame, text = "Advance Att Reports", width = 390, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=0, hover_color="green", cursor = "hand2", command=lambda :switch_frame(page=self.advance_att_report_frame))
        # # self.student_advance_att_report_button.place(x=5,y=560)

        self.teacher_sidebar_frame.place(x=10,y=10)

        #=======rightside=====#
        self.rightside_frame=ctk.CTkFrame(self.teacher_homepage_frame,width=1092,height=700,corner_radius=0,border_width=0,fg_color="white")
        self.rightside_frame.place(x=420,y=10)

        self.teacher_homepage_frame.place(x=5,y=100)

    def profile_frame(self):
        self.profile_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=660, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.profile_page_frame,text="My Profile")

        def show_profile():
            global path, imageo

            #=======fetch login email and password=============@
            teacher_email = teacher_username
            password = teacher_password 
            #===================================================#
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                select_query = "select concat(first_name,' ', last_name) as name , d.std_name, email, mobile, address, city, pincode, image_path, first_name from staff, teacher_assignments ta, division d where staff.srno = ta.srno and d.div_id = ta.std_div_id and email = %s and concat(first_name,'@',staff_id) = %s"
                select_value = (teacher_email, password)
                cur.execute(select_query,select_value )

                records = cur.fetchone()

                # show this detail in entry box
                self.name_entry.configure(text = records[0])
                self.standard_entry.configure(text = records[1])
                self.email_entry.insert(tk.END, records[2])
                self.contact_entry.insert(tk.END, records[3])
                self.address_entry.insert(tk.END, records[4])
                self.city_entry.insert(tk.END, records[5])
                self.pincode_entry.insert(tk.END, records[6])

                image_path = records[7]
                #print(image_path)

                #open the image
                try:
                    image = Image.open(image_path)
                except FileNotFoundError:
                    print(f"Error: Could not find image at path: {image_path}")

                #base name of the image
                image_file_name = os.path.basename(image_path)

                #save the image
                image.save(image_file_name)
                
                #open image in form of ctk.CTkImage
                imageo = ctk.CTkImage(light_image=image, dark_image=image, size = (146, 166))

                #configure the right side frame label
                self.photo_label.configure(image = imageo)
                self.photo_label.image = imageo

                #configure the left side frame label
                self.teacher_photo_label.configure(image = imageo)
                self.teacher_photo_label.image = imageo
                
                #configure the image welcome label
                self.teacher_greet_label.configure(text = f"Welcome {records[8]}")

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        def update_photo():
            global changed_image_path
            changed_image_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("JPG Files", ".jpg"),("PNG Files", ".png"),("All files", ".")], initialdir="C:/Users/vikas/OneDrive/Documents/software project/image", title="Open File")

            try:
                image = Image.open(changed_image_path)

            except FileNotFoundError:
                print(f"Error: Could not find image at path: {changed_image_path}")

            #====configure the image===========#
                
            #base name of the image
            image_file_name = os.path.basename(changed_image_path)

            #save the image
            image.save(image_file_name)
                
            #open image in form of ctk.CTkImage
            imageo = ctk.CTkImage(light_image=image, dark_image=image, size = (146, 166))

            #configure the right side frame label
            self.photo_label.configure(image = imageo)
            self.photo_label.image = imageo

            self.upload_photo_label.configure(text = f"{image_file_name}", wraplength = 100)

            #configure the left side frame label
            self.teacher_photo_label.configure(image = imageo)
            self.teacher_photo_label.image = imageo
                
        def add_photo_database():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #update the image_path
                update_query = "update staff set image_path = %s where email = %s"
                update_value = (changed_image_path, self.email_entry.get())

                cur.execute(update_query, update_value)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #============fetch id card============#
        def view_id_card():
            id_card_window = ctk.CTkToplevel(fg_color="white")
            id_card_window.geometry("600x500+800+250")
            id_card_window.title("School Management System")

            #==========function==========#
            def show_id_card():
                teacher_email = teacher_username
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    cur.execute("select srno, first_name from staff where email = %s", (teacher_email,))

                    result = cur.fetchone()
                    return result

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

            #======card frame===========#
            self.teacher_card_frame = ctk.CTkFrame(id_card_window, border_width=2,border_color="green", fg_color="white", width = 580, height = 480, corner_radius=2)

            #======card label===========#
            self.head_label = ctk.CTkLabel(self.teacher_card_frame, text = "Identity Card",width = 580, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
            self.head_label.place(x = 0, y = 0)

            # #====ignore warnings===========#
            warnings.filterwarnings("ignore", category=UserWarning)

            #==========call the show id card function==============#
            results = show_id_card()
            # print(results)

            # #=====iid card image label==========#
            file_name = "C:/Users/vikas/OneDrive/Documents/software project/teacher_id"
            teacher_image = Image.open(f"{file_name}/{results[0]}_{results[1].lower()} id_card.png")

            id_card_image = ImageTk.PhotoImage(teacher_image)
            self.teacher_card_label = ctk.CTkLabel(self.teacher_card_frame, text = "", image = id_card_image)
            self.teacher_card_label.place(x = 170, y = 50)

            # #===========save button=============#
            def save_teacher_card():
                file_path = filedialog.askdirectory(initialdir="C:/Users/vikas/OneDrive/Documents/save id cards")

                if file_path:
                    # print(file_path)
                    if os.path.exists(f"{file_path}/{results[0]}_{results[1].lower()} id_card.png"):
                        error_message = f"The file '{file_path}/{results[0]}_{results[1].lower()} id_card.png' already exists."
                        messagebox.showinfo("File Exists", message=error_message)
                    else:
                        image_to_save = ImageTk.getimage(id_card_image) 
                        image_to_save.save(f"{file_path}/{results[0]}_{results[1].lower()} id_card.png")
                        success_message = f"The Teacher ID card for {results[1].lower()} has been saved successfully!"
                        messagebox.showinfo("Success", message=success_message)

            #=========button===============#
            self.save_button = ctk.CTkButton(self.teacher_card_frame, text = "Save", width = 120, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=save_teacher_card)
            self.save_button.place(x = 220, y = 400)

            self.teacher_card_frame.place(x = 10, y = 10)

            #=====calling the function==========#
            show_id_card()
            
            id_card_window.grab_set()

        #=======inside widget========#
        self.name_label =  ctk.CTkLabel(self.profile_page_frame, text = "Name : ", text_color="green", font=("Consolas", 20))
        self.name_label.place(x = 110, y = 80)

        self.name_entry =  ctk.CTkLabel(self.profile_page_frame, text = "", text_color="red", font=("Consolas", 18))
        self.name_entry.place(x = 190, y = 80)

        self.standard_label =  ctk.CTkLabel(self.profile_page_frame, text = "Standard : ", text_color="green", font=("Consolas", 20))
        self.standard_label.place(x = 65, y = 120)

        self.standard_entry =  ctk.CTkLabel(self.profile_page_frame, text = "", text_color="red", font=("Consolas", 18))
        self.standard_entry.place(x = 190, y = 120)

        self.email_label =  ctk.CTkLabel(self.profile_page_frame, text = "Email : ", text_color="green", font=("Consolas", 20))
        self.email_label.place(x = 98, y = 160)

        self.email_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 18), border_color="green")
        self.email_entry.place(x = 190, y = 160)
    
        self.contact_label =  ctk.CTkLabel(self.profile_page_frame, text = "Contact No : ", text_color="green", font=("Consolas", 20))
        self.contact_label.place(x = 42, y = 200)

        self.contact_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 18), border_color="green")
        self.contact_entry.place(x = 190, y = 200)

        self.address_label =  ctk.CTkLabel(self.profile_page_frame, text = "Address : ", text_color="green", font=("Consolas", 20))
        self.address_label.place(x = 75, y = 240)

        self.address_entry = ctk.CTkTextbox(self.profile_page_frame, width = 200, height = 60, corner_radius=2, font = ("Consolas", 18), border_color="green", text_color="black", fg_color="white", border_width=2, wrap = "word")
        self.address_entry.place(x = 190, y = 240)

        self.city_label =  ctk.CTkLabel(self.profile_page_frame, text = "City : ", text_color="green", font=("Consolas", 20))
        self.city_label.place(x = 108, y = 305)

        self.city_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 18), border_color="green")
        self.city_entry.place(x = 190, y = 305)

        self.pincode_label =  ctk.CTkLabel(self.profile_page_frame, text = "Pincode : ", text_color="green", font=("Consolas", 20))
        self.pincode_label.place(x = 75, y = 345)

        self.pincode_entry = ctk.CTkEntry(self.profile_page_frame, width = 200, height = 35, corner_radius=2, font = ("Consolas", 18), border_color="green")
        self.pincode_entry.place(x = 190, y = 345)

        self.update_button = ctk.CTkButton(self.profile_page_frame, text = "Update", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=None, border_color="green", border_width=2)
        self.update_button.place(x = 190, y = 390)

        self.view_id_button = ctk.CTkButton(self.profile_page_frame, text = "View ID Card", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=view_id_card, border_color="green", border_width=2)
        self.view_id_button.place(x = 190, y = 435)

        self.upload_photo_button = ctk.CTkButton(self.profile_page_frame, text = "Choose File", width = 150, height = 35, border_width=2, border_color="black", font = ("Consolas", 20), text_color="black", fg_color="#D8D9DA", corner_radius=2, hover_color="white", cursor = "hand2", command=update_photo)
        self.upload_photo_button.place(x = 450, y = 160)

        self.upload_photo_label = ctk.CTkLabel(self.profile_page_frame, text = "No File Cho...", text_color="black", font=("Consolas", 17))
        self.upload_photo_label.place(x = 610, y = 160)

        self.add_photo_button = self.update_button = ctk.CTkButton(self.profile_page_frame, text = "Add", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=add_photo_database, border_color="green", border_width=2)
        self.add_photo_button.place(x = 760, y = 155)

        self.updated_photo_frame = ctk.CTkFrame(self.profile_page_frame, width = 150, height=170, corner_radius=0,  border_width=3, border_color="black", fg_color="white")
        self.updated_photo_frame.place(x=450,y=220)

        self.photo_label = ctk.CTkLabel(self.updated_photo_frame, text = "", fg_color="grey", width = 149, height=170)
        self.photo_label.place(x = 0, y = 0)

        #=======calling the function========#
        show_profile()
        

        self.profile_page_frame.place(x=0,y=0)

    def std_div_select_func(self, parent):
    
        #=======fetch standard record ==========#
        def fetch_std_record():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                cur.execute("select std_name from standard")

                records = cur.fetchall()

                std_list = []
                for record in records:
                    std_list.append(record[0])
                
                #======configure the option menu for standard values
                self.choose_division_values = std_list
                self.choose_standard_option.configure(values = self.choose_division_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        
        #=======fetch division record ==========#
        def fetch_div_record():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                cur.execute("select div_name from division group by div_name")

                records = cur.fetchall()

                div_list = []
                for record in records:
                    div_list.append(record[0])
                
                #======configure the option menu for standard values
                self.choose_division_values= div_list
                self.choose_division_option.configure(values = self.choose_division_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        #=================================#

        self.choose_standard_label = ctk.CTkLabel(parent, text = "Select Standard :", font = ("Consolas", 20), text_color="green")
        self.choose_standard_label.place(x = 30, y = 60)

        self.choose_standard_values = ["5th Std", "6th Std", "7th Std", "8th Std", "9th Std", "10th Std"]
        self.std_value = tk.StringVar(value="")
        self.choose_standard_option = ctk.CTkOptionMenu(parent, width = 200, height = 30, corner_radius=2, values=self.choose_standard_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=self.std_value)
        self.choose_standard_option.place(x = 240, y = 60)

        self.choose_division_label = ctk.CTkLabel(parent, text = "Select Division :", font = ("Consolas", 20), text_color="green")
        self.choose_division_label.place(x = 30, y =100)

        self.choose_division_values = ["A", "B", "C"]
        self.div_value = tk.StringVar(value = "")
        self.choose_division_option = ctk.CTkOptionMenu(parent, width = 200, height = 30, corner_radius=2, values=self.choose_division_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=self.div_value)
        self.choose_division_option.place(x = 240, y = 100)
        
        #==========calling the function===========#
        fetch_std_record()
        fetch_div_record()
        #==========================================#

    # def add_student_frame(self):
    #     self.add_student_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=600, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
    #     ChangeLabel(self.add_student_page_frame,text="Add Student")

    #     #calling the std_div_select_func
    #     self.std_div_select_func(self.add_student_page_frame) 

    #     self.add_student_page_frame.place(x=0,y=0)

    def result_student_frame(self):
        self.result_student_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.result_student_page_frame,text="Result")

        #calling the std_div_select_func
        self.std_div_select_func(self.result_student_page_frame)

        def generate_report_card():
            pass
#                 # global records
#                 '''try:
#                     con = mycon.connect(host = "localhost", username = "root", password = "root",port = 3307, database = "software")

#                     #create a cursor instance
#                     cur = con.cursor()

#                     #fetch student_data
#                     cur.execute("select srno, mobile, address, image_path, concat(first_name,' ', last_name) as name, first_name from staff where srno = %s", (teacher_data[0],))

#                     records = cur.fetchone()

#                     #commit the changes
#                     con.commit()

#                     #close the connection
#                     con.close()

#                 except Exception as e:
#                     print("Error ", e)'''
                
#                 subject_name  = '''
# English
# Hindi
# Marathi
# Mathematics
# EVS-I
# EVS-II

# '''
#                 grade_text = f'''
# {self.english_grade_label.cget("text")}
# {self.hindi_grade_label.cget("text")}
# {self.marathi_grade_label.cget("text")}
# {self.mathematics_grade_label.cget("text")}
# {self.evs_I_grade_label.cget("text")}
# {self.evs_II_grade_label.cget("text")}
# '''
#                 #==================================#
#                 result_frame_image = Image.open("image/result_card2.png").resize((700, 840))
#                 # teacher_image_pic = Image.open(f"{image_path}").resize((94, 98))

#                 #creating an object for using student_frame_image
#                 draw = ImageDraw.Draw(result_frame_image)
#                 text_font = ImageFont.truetype("consola.ttf", 17)

#                 # draw.text(xy = (98, 230), text = f"{full_name}", fill = (255, 0, 0), font = ImageFont.truetype("tahomabd.ttf", 15))

#                 #======subject name====#
#                 draw.multiline_text(xy = (240, 380), text = subject_name, fill = (0,0,0), font= text_font, spacing=18)

#                 #=====grade text=======#
#                 draw.multiline_text(xy = (500, 380), text = grade_text, fill = (0,0,0), font= text_font, spacing=18)

#                 #======new window===============#
#                 result_report_window = ctk.CTkToplevel(fg_color="white")
#                 result_report_window.geometry("600x800+750+20")
#                 result_report_window.title("School Management System")

#                 #======report frame===========#
#                 self.result_card_page_frame = ctk.CTkFrame(result_report_window, border_width=2,border_color="green", fg_color="white", width = 580, height = 780, corner_radius=2)

#                 #======report label===========#
#                 self.head_label = ctk.CTkLabel(self.result_card_page_frame, text = "Report Card",width = 580, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
#                 self.head_label.place(x = 0, y = 0)

#                 #====ignore warnings===========#
#                 warnings.filterwarnings("ignore", category=UserWarning)

#                 #=====report card image label==========#
#                 report_card_image = ImageTk.PhotoImage(result_frame_image)
#                 self.result_card_label = ctk.CTkLabel(self.result_card_page_frame, text = "", image = report_card_image)
#                 self.result_card_label.place(x = 15, y = 42)
#                 # self.result_card_label.image = report_card_image

#                 self.save_button = ctk.CTkButton(self.result_card_page_frame, text = "Save", width = 120, height = 38, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=None)
#                 self.save_button.place(x = 160, y = 730)

#                 self.print_button = ctk.CTkButton(self.result_card_page_frame, text = "Print", width = 120, height = 38, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=None)
#                 self.print_button.place(x = 300, y = 730)

#                 result_report_window.grab_set()

#                 self.result_card_page_frame.place(x = 10, y = 10)

        def print_std_value(*args):
            global div_value
            # print(self.std_value.get())
            if self.std_value.get()=="":
                messagebox.showerror("Marks","Please Select Standard")
                return
            if self.div_value.get()=="":
                messagebox.showerror("Marks","Please Select Division")
                return
            elif self.select_rollno_entry.get()=="":
                messagebox.showerror("Marks","Please Select Rollno")
            elif self.std_value.get()=="5th std":
                self.give_marks_button.configure(command=enter_marks5)
            elif self.std_value.get()=="6th std":
                self.give_marks_button.configure(command=enter_marks6)
            elif self.std_value.get()=="7th std":
                self.give_marks_button.configure(command=enter_marks78)
            elif self.std_value.get()=="8th std":
                self.give_marks_button.configure(command=enter_marks78)
            elif self.std_value.get()=="9th std":
                self.give_marks_button.configure(command=enter_marks910)
            elif self.std_value.get()=="10th std":
                self.give_marks_button.configure(command=enter_marks910)

        self.std_value.trace("w",print_std_value)

        # def print_div_value(*args):
        #     print(self.div_value.get())

        # self.div_value.trace("w",print_div_value)

        #======5th std======#
        def enter_marks5():
            self.enter_marks_frame = ctk.CTkFrame(self.result_student_page_frame, width = 1082, height=495, corner_radius=0,  border_width=1, border_color="green", fg_color="white") 

            #========Functions========#
            def calculate_grade():
                english=self.english_entry.get()
                hindi=self.hindi_entry.get()
                marathi=self.marathi_entry.get()
                mathematics=self.mathematics_entry.get()
                evs_I=self.evs_I_entry.get()
                evs_II=self.evs_II_entry.get()
                if english=="" or hindi=="" or marathi=="" or mathematics=="" or evs_I=="" or evs_II=="":
                    messagebox.showerror("Marks","Some subject is empty")
                    return
                # subjects = ['english', 'hindi', 'marathi', 'mathematics', 'evs_I', 'evs_II']
                grade_boundaries = {
                'A1': 90, 'A2': 80, 'B1': 70, 'B2': 60, 'C1': 50, 'C2': 40, 'D': 35, 'F': 0
                }
                subjects=[english,hindi,marathi,mathematics,evs_I,evs_II]
                label=[self.english_grade_label,self.hindi_grade_label,self.marathi_grade_label,self.mathematics_grade_label,self.evs_I_grade_label,self.evs_II_grade_label]
                for i in range(len(subjects)):
                    subjects[i] = int(subjects[i])
                    if subjects[i] < 0:
                        print("Marks cannot be negative")
                        continue
                    grade = next((grade for grade, boundary in grade_boundaries.items() if subjects[i] >= boundary), 'F')
                    # print(f"{subjects[i]} grade: {grade}")
                    label[i].configure(text=grade)
                total=int(english)+int(hindi)+int(marathi)+int(mathematics)+int(evs_I)+int(evs_II)
                percentage=(total/600)*100
                # print(round(percentage,2))

            #======heading======#
            self.marks_heading_label = ctk.CTkLabel(self.enter_marks_frame, text = "Calculating Marks", width = 1092, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
            self.marks_heading_label.place(x = 0, y = 0)

            #===Columns name====#
            self.subject_label = ctk.CTkLabel(self.enter_marks_frame, text = "Subjects", text_color="green", font = ("Consolas", 21))
            self.subject_label.place(x = 85, y = 45)

            self.marks_label = ctk.CTkLabel(self.enter_marks_frame, text = "Marks", text_color="green", font = ("Consolas", 21))
            self.marks_label.place(x = 220, y = 45)

            self.total_label = ctk.CTkLabel(self.enter_marks_frame, text = "Total", text_color="green", font = ("Consolas", 21))
            self.total_label.place(x = 440, y = 45)

            self.grade_label = ctk.CTkLabel(self.enter_marks_frame, text = "Grade", text_color="green", font = ("Consolas", 21))
            self.grade_label.place(x = 560, y = 45)


            #=====English=========#
            self.english_label=ctk.CTkLabel(self.enter_marks_frame,text="English :",font=("Consolas",20),text_color="green")
            self.english_label.place(x=85,y=80)

            self.english_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.english_entry.place(x = 200, y = 80)

            self.english_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.english_outof_label.place(x=320,y=80)

            eng_outof_var=ctk.StringVar()
            eng_outof_var.set("100")
            self.english_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=eng_outof_var,state="disabled")
            self.english_outof_entry.place(x = 420, y = 80)

            self.english_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.english_grade_label.place(x=575,y=80)

            #=========Hindi=========#
            self.hindi_label=ctk.CTkLabel(self.enter_marks_frame,text="Hindi :",font=("Consolas",20),text_color="green")
            self.hindi_label.place(x=107,y=120)

            self.hindi_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.hindi_entry.place(x = 200, y = 120)

            self.hindi_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.hindi_outof_label.place(x=320,y=120)

            hin_outof_var=ctk.StringVar()
            hin_outof_var.set("100")
            self.hindi_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=hin_outof_var,state="disabled")
            self.hindi_outof_entry.place(x = 420, y = 120)

            self.hindi_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.hindi_grade_label.place(x=575,y=120)

            #======Marathi========#
            self.marathi_label=ctk.CTkLabel(self.enter_marks_frame,text="Marathi :",font=("Consolas",20),text_color="green")
            self.marathi_label.place(x=85,y=160)

            self.marathi_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.marathi_entry.place(x = 200, y = 160)

            self.marathi_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.marathi_outof_label.place(x=320,y=160)

            mar_outof_var=ctk.StringVar()
            mar_outof_var.set("100")
            self.marathi_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=mar_outof_var,state="disabled")
            self.marathi_outof_entry.place(x = 420, y = 160)

            self.marathi_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.marathi_grade_label.place(x=575,y=160)

            #========mathematics======#
            self.mathematics_label=ctk.CTkLabel(self.enter_marks_frame,text="Mathematics :",font=("Consolas",20),text_color="green")
            self.mathematics_label.place(x=40,y=200)

            self.mathematics_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.mathematics_entry.place(x = 200, y = 200)

            self.mathematics_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.mathematics_outof_label.place(x=320,y=200)

            mat_outof_var=ctk.StringVar()
            mat_outof_var.set("100")
            self.mathematics_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=mat_outof_var,state="disabled")
            self.mathematics_outof_entry.place(x = 420, y = 200)

            self.mathematics_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.mathematics_grade_label.place(x=575,y=200)

            #======evs-I========#
            self.evs_I_label=ctk.CTkLabel(self.enter_marks_frame,text="EVS-I :",font=("Consolas",20),text_color="green")
            self.evs_I_label.place(x=107,y=240)

            self.evs_I_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.evs_I_entry.place(x = 200, y = 240)

            self.evs_I_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.evs_I_outof_label.place(x=320,y=240)

            evs_I_outof_var=ctk.StringVar()
            evs_I_outof_var.set("100")
            self.evs_I_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=evs_I_outof_var,state="disabled")
            self.evs_I_outof_entry.place(x = 420, y = 240)

            self.evs_I_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.evs_I_grade_label.place(x=575,y=240)

            #========evs-II========#
            self.evs_II_label=ctk.CTkLabel(self.enter_marks_frame,text="EVS-II :",font=("Consolas",20),text_color="green")
            self.evs_II_label.place(x=97,y=280)

            self.evs_II_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.evs_II_entry.place(x = 200, y = 280)

            self.evs_II_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.evs_II_outof_label.place(x=320,y=280)

            evs_II_outof_var=ctk.StringVar()
            evs_II_outof_var.set("100")
            self.evs_II_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=evs_II_outof_var,state="disabled")
            self.evs_II_outof_entry.place(x = 420, y = 280)

            self.evs_II_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.evs_II_grade_label.place(x=575,y=280)

            self.give_grade_button = ctk.CTkButton(self.enter_marks_frame, text = "Calculate Grade", width = 200, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=calculate_grade, border_color="green", border_width=2)
            self.give_grade_button.place(x = 100, y = 360)

            self.enter_marks_frame.place(x=5,y=200)

        #=====6th std========#
        def enter_marks6():
            self.enter_marks_frame = ctk.CTkFrame(self.result_student_page_frame, width = 1082, height=495, corner_radius=0,  border_width=1, border_color="green", fg_color="white") 

            #========Functions========#
            def calculate_grade():
                english=self.english_entry.get()
                hindi=self.hindi_entry.get()
                marathi=self.marathi_entry.get()
                mathematics=self.mathematics_entry.get()
                evs=self.evs_entry.get()
                sst=self.sst_entry.get()
                if english=="" or hindi=="" or marathi=="" or mathematics=="" or evs=="" or sst=="":
                    messagebox.showerror("Marks","Some subject is empty")
                    return
                # subjects = ['english', 'hindi', 'marathi', 'mathematics', 'evs_I', 'evs_II']
                grade_boundaries = {
                'A1': 90, 'A2': 80, 'B1': 70, 'B2': 60, 'C1': 50, 'C2': 40, 'D': 35, 'F': 0
                }
                subjects=[english,hindi,marathi,mathematics,evs,sst]
                label=[self.english_grade_label,self.hindi_grade_label,self.marathi_grade_label,self.mathematics_grade_label,self.evs_grade_label,self.sst_grade_label]
                for i in range(len(subjects)):
                    subjects[i] = int(subjects[i])
                    if subjects[i] < 0:
                        print("Marks cannot be negative")
                        continue
                    grade = next((grade for grade, boundary in grade_boundaries.items() if subjects[i] >= boundary), 'F')
                    # print(f"{subjects[i]} grade: {grade}")
                    label[i].configure(text=grade)
                total=int(english)+int(hindi)+int(marathi)+int(mathematics)+int(evs)+int(sst)
                percentage=(total/600)*100
                # print(round(percentage,2))

            #======heading======#
            self.marks_heading_label = ctk.CTkLabel(self.enter_marks_frame, text = "Calculating Marks", width = 1092, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
            self.marks_heading_label.place(x = 0, y = 0)

            #===Columns name====#
            self.subject_label = ctk.CTkLabel(self.enter_marks_frame, text = "Subjects", text_color="green", font = ("Consolas", 21))
            self.subject_label.place(x = 85, y = 45)

            self.marks_label = ctk.CTkLabel(self.enter_marks_frame, text = "Marks", text_color="green", font = ("Consolas", 21))
            self.marks_label.place(x = 220, y = 45)

            self.total_label = ctk.CTkLabel(self.enter_marks_frame, text = "Total", text_color="green", font = ("Consolas", 21))
            self.total_label.place(x = 440, y = 45)

            self.grade_label = ctk.CTkLabel(self.enter_marks_frame, text = "Grade", text_color="green", font = ("Consolas", 21))
            self.grade_label.place(x = 560, y = 45)


            #=====English=========#
            self.english_label=ctk.CTkLabel(self.enter_marks_frame,text="English :",font=("Consolas",20),text_color="green")
            self.english_label.place(x=85,y=80)

            self.english_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.english_entry.place(x = 200, y = 80)

            self.english_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.english_outof_label.place(x=320,y=80)

            eng_outof_var=ctk.StringVar()
            eng_outof_var.set("100")
            self.english_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=eng_outof_var,state="disabled")
            self.english_outof_entry.place(x = 420, y = 80)

            self.english_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.english_grade_label.place(x=575,y=80)

            #=========Hindi=========#
            self.hindi_label=ctk.CTkLabel(self.enter_marks_frame,text="Hindi :",font=("Consolas",20),text_color="green")
            self.hindi_label.place(x=107,y=120)

            self.hindi_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.hindi_entry.place(x = 200, y = 120)

            self.hindi_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.hindi_outof_label.place(x=320,y=120)

            hin_outof_var=ctk.StringVar()
            hin_outof_var.set("100")
            self.hindi_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=hin_outof_var,state="disabled")
            self.hindi_outof_entry.place(x = 420, y = 120)

            self.hindi_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.hindi_grade_label.place(x=575,y=120)

            #======Marathi========#
            self.marathi_label=ctk.CTkLabel(self.enter_marks_frame,text="Marathi :",font=("Consolas",20),text_color="green")
            self.marathi_label.place(x=85,y=160)

            self.marathi_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.marathi_entry.place(x = 200, y = 160)

            self.marathi_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.marathi_outof_label.place(x=320,y=160)

            mar_outof_var=ctk.StringVar()
            mar_outof_var.set("100")
            self.marathi_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=mar_outof_var,state="disabled")
            self.marathi_outof_entry.place(x = 420, y = 160)

            self.marathi_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.marathi_grade_label.place(x=575,y=160)

            #========mathematics======#
            self.mathematics_label=ctk.CTkLabel(self.enter_marks_frame,text="Mathematics :",font=("Consolas",20),text_color="green")
            self.mathematics_label.place(x=40,y=200)

            self.mathematics_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.mathematics_entry.place(x = 200, y = 200)

            self.mathematics_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.mathematics_outof_label.place(x=320,y=200)

            mat_outof_var=ctk.StringVar()
            mat_outof_var.set("100")
            self.mathematics_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=mat_outof_var,state="disabled")
            self.mathematics_outof_entry.place(x = 420, y = 200)

            self.mathematics_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.mathematics_grade_label.place(x=575,y=200)

            #======evs========#
            self.evs_label=ctk.CTkLabel(self.enter_marks_frame,text="EVS :",font=("Consolas",20),text_color="green")
            self.evs_label.place(x=129,y=240)

            self.evs_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.evs_entry.place(x = 200, y = 240)

            self.evs_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.evs_outof_label.place(x=320,y=240)

            evs_outof_var=ctk.StringVar()
            evs_outof_var.set("100")
            self.evs_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=evs_outof_var,state="disabled")
            self.evs_outof_entry.place(x = 420, y = 240)

            self.evs_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.evs_grade_label.place(x=575,y=240)

            #========SST========#
            self.sst_label=ctk.CTkLabel(self.enter_marks_frame,text="SST :",font=("Consolas",20),text_color="green")
            self.sst_label.place(x=129,y=280)

            self.sst_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.sst_entry.place(x = 200, y = 280)

            self.sst_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.sst_outof_label.place(x=320,y=280)

            sst_outof_var=ctk.StringVar()
            sst_outof_var.set("100")
            self.sst_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=sst_outof_var,state="disabled")
            self.sst_outof_entry.place(x = 420, y = 280)

            self.sst_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.sst_grade_label.place(x=575,y=280)

            self.give_grade_button = ctk.CTkButton(self.enter_marks_frame, text = "Calculate Grade", width = 200, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=calculate_grade, border_color="green", border_width=2)
            self.give_grade_button.place(x = 100, y = 360)

            self.enter_marks_frame.place(x=5,y=200)

        #=====7th and 8th std========#
        def enter_marks78():
            self.enter_marks_frame = ctk.CTkFrame(self.result_student_page_frame, width = 1082, height=495, corner_radius=0,  border_width=1, border_color="green", fg_color="white") 

            #========Functions========#
            def calculate_grade():
                english=self.english_entry.get()
                hindi=self.hindi_entry.get()
                marathi=self.marathi_entry.get()
                mathematics=self.mathematics_entry.get()
                science=self.science_entry.get()
                sst=self.sst_entry.get()
                if english=="" or hindi=="" or marathi=="" or mathematics=="" or science=="" or sst=="":
                    messagebox.showerror("Marks","Some subject is empty")
                    return
                # subjects = ['english', 'hindi', 'marathi', 'mathematics', 'evs_I', 'evs_II']
                grade_boundaries = {
                'A1': 90, 'A2': 80, 'B1': 70, 'B2': 60, 'C1': 50, 'C2': 40, 'D': 35, 'F': 0
                }
                subjects=[english,hindi,marathi,mathematics,science,sst]
                label=[self.english_grade_label,self.hindi_grade_label,self.marathi_grade_label,self.mathematics_grade_label,self.science_grade_label,self.sst_grade_label]
                for i in range(len(subjects)):
                    subjects[i] = int(subjects[i])
                    if subjects[i] < 0:
                        print("Marks cannot be negative")
                        continue
                    grade = next((grade for grade, boundary in grade_boundaries.items() if subjects[i] >= boundary), 'F')
                    # print(f"{subjects[i]} grade: {grade}")
                    label[i].configure(text=grade)
                total=int(english)+int(hindi)+int(marathi)+int(mathematics)+int(science)+int(sst)
                percentage=(total/600)*100
                # print(round(percentage,2))

            #======heading======#
            self.marks_heading_label = ctk.CTkLabel(self.enter_marks_frame, text = "Calculating Marks", width = 1092, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
            self.marks_heading_label.place(x = 0, y = 0)

            #===Columns name====#
            self.subject_label = ctk.CTkLabel(self.enter_marks_frame, text = "Subjects", text_color="green", font = ("Consolas", 21))
            self.subject_label.place(x = 85, y = 45)

            self.marks_label = ctk.CTkLabel(self.enter_marks_frame, text = "Marks", text_color="green", font = ("Consolas", 21))
            self.marks_label.place(x = 220, y = 45)

            self.total_label = ctk.CTkLabel(self.enter_marks_frame, text = "Total", text_color="green", font = ("Consolas", 21))
            self.total_label.place(x = 440, y = 45)

            self.grade_label = ctk.CTkLabel(self.enter_marks_frame, text = "Grade", text_color="green", font = ("Consolas", 21))
            self.grade_label.place(x = 560, y = 45)


            #=====English=========#
            self.english_label=ctk.CTkLabel(self.enter_marks_frame,text="English :",font=("Consolas",20),text_color="green")
            self.english_label.place(x=85,y=80)

            self.english_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.english_entry.place(x = 200, y = 80)

            self.english_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.english_outof_label.place(x=320,y=80)

            eng_outof_var=ctk.StringVar()
            eng_outof_var.set("100")
            self.english_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=eng_outof_var,state="disabled")
            self.english_outof_entry.place(x = 420, y = 80)

            self.english_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.english_grade_label.place(x=575,y=80)

            #=========Hindi=========#
            self.hindi_label=ctk.CTkLabel(self.enter_marks_frame,text="Hindi :",font=("Consolas",20),text_color="green")
            self.hindi_label.place(x=107,y=120)

            self.hindi_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.hindi_entry.place(x = 200, y = 120)

            self.hindi_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.hindi_outof_label.place(x=320,y=120)

            hin_outof_var=ctk.StringVar()
            hin_outof_var.set("100")
            self.hindi_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=hin_outof_var,state="disabled")
            self.hindi_outof_entry.place(x = 420, y = 120)

            self.hindi_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.hindi_grade_label.place(x=575,y=120)

            #======Marathi========#
            self.marathi_label=ctk.CTkLabel(self.enter_marks_frame,text="Marathi :",font=("Consolas",20),text_color="green")
            self.marathi_label.place(x=85,y=160)

            self.marathi_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.marathi_entry.place(x = 200, y = 160)

            self.marathi_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.marathi_outof_label.place(x=320,y=160)

            mar_outof_var=ctk.StringVar()
            mar_outof_var.set("100")
            self.marathi_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=mar_outof_var,state="disabled")
            self.marathi_outof_entry.place(x = 420, y = 160)

            self.marathi_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.marathi_grade_label.place(x=575,y=160)

            #========mathematics======#
            self.mathematics_label=ctk.CTkLabel(self.enter_marks_frame,text="Mathematics :",font=("Consolas",20),text_color="green")
            self.mathematics_label.place(x=40,y=200)

            self.mathematics_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.mathematics_entry.place(x = 200, y = 200)

            self.mathematics_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.mathematics_outof_label.place(x=320,y=200)

            mat_outof_var=ctk.StringVar()
            mat_outof_var.set("100")
            self.mathematics_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=mat_outof_var,state="disabled")
            self.mathematics_outof_entry.place(x = 420, y = 200)

            self.mathematics_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.mathematics_grade_label.place(x=575,y=200)

            #======Science========#
            self.science_label=ctk.CTkLabel(self.enter_marks_frame,text="Science :",font=("Consolas",20),text_color="green")
            self.science_label.place(x=85,y=240)

            self.science_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.science_entry.place(x = 200, y = 240)

            self.science_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.science_outof_label.place(x=320,y=240)

            science_outof_var=ctk.StringVar()
            science_outof_var.set("100")
            self.science_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=science_outof_var,state="disabled")
            self.science_outof_entry.place(x = 420, y = 240)

            self.science_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.science_grade_label.place(x=575,y=240)

            #========SST========#
            self.sst_label=ctk.CTkLabel(self.enter_marks_frame,text="SST :",font=("Consolas",20),text_color="green")
            self.sst_label.place(x=129,y=280)

            self.sst_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.sst_entry.place(x = 200, y = 280)

            self.sst_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.sst_outof_label.place(x=320,y=280)

            sst_outof_var=ctk.StringVar()
            sst_outof_var.set("100")
            self.sst_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=sst_outof_var,state="disabled")
            self.sst_outof_entry.place(x = 420, y = 280)

            self.sst_grade_label=ctk.CTkLabel(self.enter_marks_frame,text="",font=("Consolas",20),text_color="green")
            self.sst_grade_label.place(x=575,y=280)

            self.give_grade_button = ctk.CTkButton(self.enter_marks_frame, text = "Calculate Grade", width = 200, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=calculate_grade, border_color="green", border_width=2)
            self.give_grade_button.place(x = 100, y = 360)

            self.enter_marks_frame.place(x=5,y=200)

        #======9th std======#
        def enter_marks910():
            self.enter_marks_frame = ctk.CTkFrame(self.result_student_page_frame, width = 1082, height=495, corner_radius=0,  border_width=1, border_color="green", fg_color="white") 

            #========Functions========#
            def calculate_percentage():
                english=self.english_entry.get()
                hindi=self.hindi_entry.get()
                marathi=self.marathi_entry.get()
                mathematics=self.mathematics_entry.get()
                science=self.science_entry.get()
                sst=self.sst_entry.get()
                if english=="" or hindi=="" or marathi=="" or mathematics=="" or science=="" or sst=="":
                    messagebox.showerror("Marks","Some subject is empty")
                    return
                subjects=[english,hindi,marathi,mathematics,science,sst]
                subject=int(subjects[0])
                n=len(subjects)
                for i in range(n):
                    if subject>int(subjects[i]):
                        subject=int(subjects[i])
                subjects.remove(str(subject))
                # print(subjects)
                # print(subject)
                total=0
                for marks in range(len(subjects)):
                    total=total+int(subjects[marks])
                self.marks_obtained_label.configure(text=f"The total marks obtained is : {total}")
                percentage=(total/500)*100
                self.percentage_label.configure(text=f"Percentage is : {round(percentage,2)}")
                # print(round(percentage,2))

            #======heading======#
            self.marks_heading_label = ctk.CTkLabel(self.enter_marks_frame, text = "Calculating Marks", width = 1092, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
            self.marks_heading_label.place(x = 0, y = 0)

            #===Columns name====#
            self.subject_label = ctk.CTkLabel(self.enter_marks_frame, text = "Subjects", text_color="green", font = ("Consolas", 21))
            self.subject_label.place(x = 85, y = 45)

            self.marks_label = ctk.CTkLabel(self.enter_marks_frame, text = "Marks", text_color="green", font = ("Consolas", 21))
            self.marks_label.place(x = 220, y = 45)

            self.total_label = ctk.CTkLabel(self.enter_marks_frame, text = "Total", text_color="green", font = ("Consolas", 21))
            self.total_label.place(x = 440, y = 45)

            #=====English=========#
            self.english_label=ctk.CTkLabel(self.enter_marks_frame,text="English :",font=("Consolas",20),text_color="green")
            self.english_label.place(x=85,y=80)

            self.english_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.english_entry.place(x = 200, y = 80)

            self.english_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.english_outof_label.place(x=320,y=80)

            eng_outof_var=ctk.StringVar()
            eng_outof_var.set("100")
            self.english_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=eng_outof_var,state="disabled")
            self.english_outof_entry.place(x = 420, y = 80)

            #=========Hindi=========#
            self.hindi_label=ctk.CTkLabel(self.enter_marks_frame,text="Hindi :",font=("Consolas",20),text_color="green")
            self.hindi_label.place(x=107,y=120)

            self.hindi_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.hindi_entry.place(x = 200, y = 120)

            self.hindi_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.hindi_outof_label.place(x=320,y=120)

            hin_outof_var=ctk.StringVar()
            hin_outof_var.set("100")
            self.hindi_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=hin_outof_var,state="disabled")
            self.hindi_outof_entry.place(x = 420, y = 120)

            #======Marathi========#
            self.marathi_label=ctk.CTkLabel(self.enter_marks_frame,text="Marathi :",font=("Consolas",20),text_color="green")
            self.marathi_label.place(x=85,y=160)

            self.marathi_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.marathi_entry.place(x = 200, y = 160)

            self.marathi_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.marathi_outof_label.place(x=320,y=160)

            mar_outof_var=ctk.StringVar()
            mar_outof_var.set("100")
            self.marathi_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=mar_outof_var,state="disabled")
            self.marathi_outof_entry.place(x = 420, y = 160)

            #========mathematics======#
            self.mathematics_label=ctk.CTkLabel(self.enter_marks_frame,text="Mathematics :",font=("Consolas",20),text_color="green")
            self.mathematics_label.place(x=40,y=200)

            self.mathematics_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.mathematics_entry.place(x = 200, y = 200)

            self.mathematics_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.mathematics_outof_label.place(x=320,y=200)

            mat_outof_var=ctk.StringVar()
            mat_outof_var.set("100")
            self.mathematics_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=mat_outof_var,state="disabled")
            self.mathematics_outof_entry.place(x = 420, y = 200)

            #======Science========#
            self.science_label=ctk.CTkLabel(self.enter_marks_frame,text="Science :",font=("Consolas",20),text_color="green")
            self.science_label.place(x=85,y=240)

            self.science_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.science_entry.place(x = 200, y = 240)

            self.science_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.science_outof_label.place(x=320,y=240)

            science_outof_var=ctk.StringVar()
            science_outof_var.set("100")
            self.science_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=science_outof_var,state="disabled")
            self.science_outof_entry.place(x = 420, y = 240)

            #========SST========#
            self.sst_label=ctk.CTkLabel(self.enter_marks_frame,text="SST :",font=("Consolas",20),text_color="green")
            self.sst_label.place(x=129,y=280)

            self.sst_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
            self.sst_entry.place(x = 200, y = 280)

            self.sst_outof_label=ctk.CTkLabel(self.enter_marks_frame,text="out of",font=("Consolas",20),text_color="green")
            self.sst_outof_label.place(x=320,y=280)

            sst_outof_var=ctk.StringVar()
            sst_outof_var.set("100")
            self.sst_outof_entry = ctk.CTkEntry(self.enter_marks_frame, width = 100, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green",textvariable=sst_outof_var,state="disabled")
            self.sst_outof_entry.place(x = 420, y = 280)

            self.marks_obtained_label=ctk.CTkLabel(self.enter_marks_frame,text="The total marks obtained is : 0",font=("Consolas",20),text_color="green")
            self.marks_obtained_label.place(x=100,y=320)

            self.percentage_label=ctk.CTkLabel(self.enter_marks_frame,text="Percentage is : 0",font=("Consolas",20),text_color="green")
            self.percentage_label.place(x=100,y=350)

            self.give_grade_button = ctk.CTkButton(self.enter_marks_frame, text = "Calculate Percentage", width = 200, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=calculate_percentage, border_color="green", border_width=2)
            self.give_grade_button.place(x = 200, y = 390)

            self.enter_marks_frame.place(x=5,y=200)

        self.rollno_label=ctk.CTkLabel(self.result_student_page_frame,text="Select Rollno :",font=("Consolas",22),text_color="green") 
        self.rollno_label.place(x = 40, y = 140)

        self.select_rollno_entry = ctk.CTkEntry(self.result_student_page_frame, width = 200, height = 32, corner_radius=2, font = ("Consolas", 22), border_color="green")
        self.select_rollno_entry.place(x = 240, y = 140)

        self.give_marks_button = ctk.CTkButton(self.result_student_page_frame, text = "Enter Marks", width = 150, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=print_std_value, border_color="green", border_width=2)
        self.give_marks_button.place(x = 460, y = 140)

        self.result_student_page_frame.place(x=0,y=0)

    def student_report_frame(self):
        self.student_report_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.student_report_page_frame,text="Student Report")

        #=======function============#
        def show_student_record_auto():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #====fetch std and div========#
                cur.execute("select d.std_name, d.div_name from teacher_assignments ta, division d, staff s where ta.std_div_id = d.div_id and ta.srno = s.srno and s.email = %s", (teacher_username,))
                std_div_records = cur.fetchall()
                # print(std_div_records)

                #======fetch student details============#
                select_query = "select srno, student_id,concat(first_name, ' ' , last_name), gender, mobile, dob, email, city, pincode, selection_status from student"

                #execute the select query
                cur.execute(select_query)

                records = cur.fetchall()

                self.count = 0
                #show record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_student_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("evenrow",))
                    else:
                        self.add_student_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("oddrow",))
                    self.count += 1

                #count the record
                cur.execute("select count(*) from student")

                counts = cur.fetchall()
                
                for count in counts:
                    student_count = count[0]
                    self.total_student_count_label.configure(text = student_count)

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        def search_student_class_div():
            std = self.std_value.get()
            div = self.div_value.get()
            
            #clear the treeview
            for record in self.add_student_tree.get_children():
                self.add_student_tree.delete(record)

            #connection with database to pull out search records
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                cur.execute("select srno, student_id, concat(first_name, ' ' , last_name) as name, gender, mobile, dob, email, city, pincode, selection_status from student where std_name = %s and div_name = %s", (std, div))

                records = cur.fetchall()
                count = len(records)
    
                self.count = 0
                #show search record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_student_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8],  record[9]), tags=("evenrow",))
                    else:
                        self.add_student_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("oddrow",))
                    self.count += 1

                self.total_student_count_label.configure(text = count)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        def approve_student_func():
            #grab a record number
            selected_approve_data = self.add_student_tree.selection() 

            approve_list = []
            for all in selected_approve_data:
                value = self.add_student_tree.item(all, "values")
                approve_list.append(value)

            for student in approve_list:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the update query
                    update_query = "update student set selection_status = %s where srno = %s"
                    update_value = (self.approve_button.cget("text"), student[0])

                    cur.execute(update_query, update_value)

                    #clear the treeview
                    for record in self.add_student_tree.get_children():
                        self.add_student_tree.delete(record)

                    #executing select query 
                    select_query = "select srno,student_id, concat(first_name, ' ' , last_name), gender, mobile, dob, email, city, pincode, selection_status from student"

                    cur.execute(select_query)

                    records = cur.fetchall()

                    #show record in treeview
                    for record in records:
                        if self.count %2 == 0:
                            self.add_student_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("evenrow",))
                        else:
                            self.add_student_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("oddrow",))
                        self.count += 1

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

        def reject_student_func():
            #grab a record number
            selected_reject_data = self.add_student_tree.selection() 

            reject_list = []
            for all in selected_reject_data:
                value = self.add_student_tree.item(all, "values")
                reject_list.append(value)

            for student in reject_list:
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #execute the update query
                    update_query = "update student set selection_status = %s where srno = %s"
                    update_value = (self.reject_button.cget("text"), student[0])

                    cur.execute(update_query, update_value)

                    #==========================
                    #clear the treeview
                    for record in self.add_student_tree.get_children():
                        self.add_student_tree.delete(record)

                    #executing select query 
                    select_query = "select srno,student_id, concat(first_name, ' ' , last_name), gender, mobile, dob, email, city, pincode, selection_status from student"
                    
                    cur.execute(select_query)

                    records = cur.fetchall()

                    #show record in treeview
                    for record in records:
                        if self.count %2 == 0:
                            self.add_student_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("evenrow",))
                        else:
                            self.add_student_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0],record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9]), tags=("oddrow",))
                        self.count += 1

                    #commit the changes
                    con.commit()

                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)

        def update_student_tree():
            #clear the treeview
            for record in self.add_student_tree.get_children():
                self.add_student_tree.delete(record)

            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the delete query
                cur.execute("delete from student where selection_status = 'Reject'")

                #commit the changes
                con.commit()

                #calling the show_staff_record_auto func
                show_student_record_auto()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        
        #=======generate id ==============#
        def generate_id():
            std = self.std_value.get()
            div = self.div_value.get()
            #clear the treeview
            for record in self.add_student_tree.get_children():
                self.add_student_tree.delete(record)

            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root",port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                srno_list=[]
                #execute the delete query
                cur.execute("select srno from student order by srno asc")
                records=cur.fetchall()
                for record in records:
                    for student_no in record:
                        srno_list.append(student_no)
                print(srno_list)

                id="01"
                for i in range(len(srno_list)):
                    # print(std[0]+div[0]+id)
                    cur.execute(f"update student set student_id='{std[0]+div[0]+id}' where srno={srno_list[i]}")
                    id=str(int(id)+1).zfill(2)

                #commit the changes
                con.commit()

                #calling the show_staff_record_auto func
                # show_student_record_auto()
                # approve_student_func()
                search_student_class_div()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #==========generate student ID Card=============#
        def generate_student_card(student_data):
            global records
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root",port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #fetch student_data
                cur.execute("select std_name, div_name, dob , mobile, address, srno, image_path, father_name, first_name, last_name from student where srno = %s and concat(first_name,' ', last_name) = %s and selection_status = %s", (student_data[0], student_data[2], student_data[9]))

                records = cur.fetchone()

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
            
            std_name = records[0]
            div_name = records[1]
            dob = records[2]
            contact = records[3]
            address = records[4]
            rollno = records[5]
            image_path = records[6]
            father_fullname = records[7]
            first_name = records[8]
            last_name = records[9]
            wrapped_address = textwrap.fill(text=address, width=25)

            #======std and div==========#
            result = std_name.split(" ")
            std = result[0]

            result_father = father_fullname.split(" ")
            father_name = result_father[0]

            #==================================#
            student_frame_image = Image.open("image/student_id.png")
            student_image_pic = Image.open(f"{image_path}").resize((94, 98))

            #creating an object for using student_frame_image
            draw = ImageDraw.Draw(student_frame_image)
            text_font = ImageFont.truetype("tahomabd.ttf", 13)

            #showing student photo on id frame
            student_frame_image.paste(student_image_pic, (98,127)) 

            draw.text(xy = (98, 228), text = f"{first_name} {last_name}", fill = (255, 0, 0), font = ImageFont.truetype("tahomabd.ttf", 15))
            # draw.text(xy = (98, 244), text = f"{father_name}", fill = (0, 0, 0), font = ImageFont.truetype("tahomabd.ttf", 14))
            draw.text(xy = (97, 273), text = f"{std} {div_name}", fill = (0, 0, 0), font = text_font)
            draw.text(xy = (240, 273), text = f"{rollno}", fill = (0, 0, 0), font = text_font)
            draw.text(xy = (97, 297), text = f"{dob}", fill = (0, 0, 0), font = text_font)
            draw.text(xy = (97, 321), text = f"{contact}", fill = (0, 0, 0), font = text_font)
            draw.text(xy = (97, 345), text = f"{wrapped_address}", fill = (0, 0, 0), font = text_font)

            student_id_window = ctk.CTkToplevel(fg_color="white")
            student_id_window.geometry("600x500+800+250")
            student_id_window.title("School Management System")

            #======card frame===========#
            self.student_card_page_frame = ctk.CTkFrame(student_id_window, border_width=2,border_color="green", fg_color="white", width = 580, height = 480, corner_radius=2)

            #======card label===========#
            self.head_label = ctk.CTkLabel(self.student_card_page_frame, text = "Identity Card",width = 580, height = 40, fg_color="green", text_color="white", font = ("Consolas", 25))
            self.head_label.place(x = 0, y = 0)

            #====ignore warnings===========#
            warnings.filterwarnings("ignore", category=UserWarning)

            #=====iid card image label==========#
            id_card_image = ImageTk.PhotoImage(student_frame_image)
            self.student_card_label = ctk.CTkLabel(self.student_card_page_frame, text = "", image = id_card_image)
            self.student_card_label.place(x = 170, y = 50)

            #===========save button=============#
            def save_student_card():
                file_name = "C:/Users/vikas/OneDrive/Documents/software project/student_id"

                if os.path.exists(f"{file_name}/{rollno}_{first_name} id_card.png"):
                    error_message = f"The file '{file_name}' already exists."
                    messagebox.showinfo("File Exists", message=error_message)
                else:
                    #convert photo_image into PIL image
                    image_to_save = ImageTk.getimage(id_card_image) 
                    image_to_save.save(f"{file_name}/{rollno}_{first_name} id_card.png")
                    success_message = f"The student ID card for {first_name} {last_name} has been saved successfully!"
                    messagebox.showinfo("Success", message=success_message)

            #============print button===========#
            def print_student_card():
                path = filedialog.askdirectory()

                if path:
                    image_to_save = ImageTk.getimage(id_card_image) 
                    image_to_save.save(f"{path}/{rollno}_{first_name} id_card_print.png")
                    win32api.ShellExecute(0,"print", f"{path}/{rollno}_{first_name} id_card_print.png",None, ".", 0)
                    # print_message = f"The student ID card for {first_name} {last_name} has been printed successfully."
                    # messagebox.showinfo("Success", message=print_message)

            self.save_button = ctk.CTkButton(self.student_card_page_frame, text = "Save", width = 120, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=save_student_card)
            self.save_button.place(x = 160, y = 400)

            self.print_button = ctk.CTkButton(self.student_card_page_frame, text = "Print", width = 120, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=print_student_card)
            self.print_button.place(x = 300, y = 400)

            self.student_card_page_frame.place(x = 10, y = 10)

        def on_tree_view_selection():
            selected = self.add_student_tree.selection()[0]
            student_data = self.add_student_tree.item(selected, "values")
            generate_student_card(student_data = student_data)

        #=========Send Email======#
        def send_email():
            try:
                self.loading_screen=ctk.CTk()
                self.loading_screen.geometry("70x70+1170+550")
                #hide title bar
                self.loading_screen.overrideredirect(True)

                self.loading_frame=ctk.CTkFrame(self.loading_screen,width=70,height=70)
                self.my_label=ctk.CTkLabel(self.loading_frame,text="")
                self.my_label.pack(expand=True)
                self.loading_frame.pack()
                
                start_time=time.time()
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307,database = "software")

                #create a cursor instance
                cur = con.cursor()

                email_list=[]
                #fetch the email
                cur.execute("select email from student order by srno asc")
                records=cur.fetchall()
                for record in records:
                    for student_email in record:
                        email_list.append(student_email)
                print(email_list)

                #fetch name query
                name_list=[]
                cur.execute("select first_name from student order by srno asc")
                records=cur.fetchall()
                for record in records:
                    for student_name in record:
                        name_list.append(student_name)
                print(name_list)

                #fetch password
                password_list=[]
                cur.execute("select concat(first_name,'@',student_id) as password from student order by srno asc")
                records=cur.fetchall()
                for record in records:
                    for student_password in record:
                        password_list.append(student_password)
                print(password_list)

                #=======send email==========#
                for i in range(len(email_list)):
                    def send_email(subject, message, recipient_email, sender_email, sender_password):
                        try:
                            yag = yagmail.SMTP(sender_email, sender_password)
                            yag.send(to=recipient_email, subject=subject, contents=message)
                            print("Email sent successfully!")
                        except Exception as e:
                            print("Email failed to send. Error:", str(e))

                    subjects="Welcome to School Management System - Your Login Credentials"
                    body=f"Dear {name_list[i]},\n\nWe are pleased to inform you that your account for the Vivekandand Vidya Bhavan Management System has been successfully created. This platform will allow you to access important information about your classes, assignments, grades, and more.\n\nPlease find your login credentials below:\n\nUsername: {email_list[i]}\nPassword: {password_list[i]}\n\nIf you experience any issues or have any questions, please contact support at vvb.admin@gmail.com or +91 9619148774.\n\nThis message is generated automatically. Please do not reply to this email.\n\nThank you,\n\nVivekandand Vidya Bhavan Management System"

                    # Usage example:
                    send_email(subject=subjects, message=body,recipient_email=email_list[i], sender_email="vikas.kahar.4471804@ves.ac.in", sender_password="VIKAS@4471804")

                #commit the changes
                con.commit()

                end_time=time.time()
                total_time=end_time-start_time
                print(total_time)
                '''def run_task():
                    gif_path = "image/animat_bus.gif"
                    gif = Image.open(gif_path)

                    frames = [ctk.CTkImage(light_image=frame, dark_image=frame, size=(65, 65))
                          for frame in ImageSequence.Iterator(gif)]

                    def update_frame(index):
                        frame = frames[index % len(frames)]
                        self.my_label.configure(image=frame)
                        self.loading_screen.after(100, update_frame, (index + 1) % len(frames))

                    self.loading_screen.after(0, update_frame, 0)

                    # Simulate a long task
                    time.sleep(5)
                    self.loading_screen.after(0, self.loading_screen.destroy)
                    self.loading_screen.after(0, lambda: messagebox.showinfo("Email", "Email sent successfully"))

                Thread(target=run_task).start()
                self.loading_screen.mainloop()'''

                messagebox.showinfo("Email", "Email sent successfully")

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
      
        #======inside widgets==========#  
        # self.std_div_select_func(self.student_report_page_frame) 

        self.choose_standard_label = ctk.CTkLabel(self.student_report_page_frame, text = "Select Standard :", font = ("Consolas", 20), text_color="green")
        self.choose_standard_label.place(x = 30, y = 60)

        self.fetch_std_label = ctk.CTkLabel(self.student_report_page_frame, text = "", font = ("Consolas", 20), text_color="green")
        self.fetch_std_label.place(x = 240, y = 60)

        self.choose_division_label = ctk.CTkLabel(self.student_report_page_frame, text = "Select Division :", font = ("Consolas", 20), text_color="green")
        self.choose_division_label.place(x = 30, y =100)

        self.fetch_div_label = ctk.CTkLabel(self.student_report_page_frame, text = "", font = ("Consolas", 20), text_color="green")
        self.fetch_div_label.place(x = 240, y =100)
        
        self.select_button = ctk.CTkButton(self.student_report_page_frame, text = "Select", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=search_student_class_div, border_color="green", border_width=2)
        self.select_button.place(x = 470, y = 95)

        self.total_student_label = ctk.CTkLabel(self.student_report_page_frame, text = "Total Student = ", font = ("Consolas", 20), text_color="black")
        self.total_student_label.place(x = 250, y = 135)

        self.total_student_count_label = ctk.CTkLabel(self.student_report_page_frame, text = "0", font = ("Consolas", 20), text_color="black")
        self.total_student_count_label.place(x = 425, y = 135)

        #===button======#
        self.approve_button = ctk.CTkButton(self.student_report_page_frame, text = "Approve", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=approve_student_func)
        self.approve_button.place(x = 20, y = 640)

        self.reject_button = ctk.CTkButton(self.student_report_page_frame, text = "Reject", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=reject_student_func)
        self.reject_button.place(x = 200, y = 640)

        self.update_button = ctk.CTkButton(self.student_report_page_frame, text = "Update", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=update_student_tree)
        self.update_button.place(x = 380, y = 640)

        self.generate_id_button = ctk.CTkButton(self.student_report_page_frame, text = "Generate ID", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=generate_id)
        self.generate_id_button.place(x = 560, y = 640)

        self.generate_id_card_button = ctk.CTkButton(self.student_report_page_frame, text = "Generate ID Card", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=on_tree_view_selection)
        self.generate_id_card_button.place(x = 740, y = 640)

        self.send_email_button = ctk.CTkButton(self.student_report_page_frame, text = "Send Email", width = 140, height = 40, font = ("Consolas", 20), text_color="black", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", border_color="green", border_width=2,command=send_email)
        self.send_email_button.place(x= 920, y = 640)
        
        #=======treeview setting========#
        #add some style
        style = ttk.Style()

        #pick a theme
        style.theme_use("alt")

        #configure the tree view color
        style.configure("Treeview", 
                        background = "#EEF0E5",
                        rowheight = 25,
                        fieldbackground = "#F3FBF1", font = ("Consolas", 14))
        
        style.configure("mystyle.Treeview", font=('Consolas', 15))

        #configure the selected color
        style.configure("Treeview", background = [("selected", "#347083")])

        #increse the font size of heading
        style.configure("Treeview.Heading", font=("Consolas", 18))

        self.data_frame = tk.Frame(self.student_report_page_frame, bg = "lightgrey", borderwidth=0, relief="solid")
        self.data_frame.pack_propagate(False)
        self.data_frame.place(x = 20, y = 230, height = 550, width = 1320)

        #create a scrollbar
        y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
        x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

        y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

        #create a treeview
        self.add_student_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
        self.add_student_tree.pack(fill = "both", expand= True)
        # self.add_student_tree.bind("<<TreeviewSelect>>", on_tree_view_selection)

        #configure the scrollbar
        x_scroll.config(command = self.add_student_tree.xview)
        y_scroll.config(command = self.add_student_tree.yview)

        #define our columns
        self.add_student_tree["columns"] = ("Sr No", "Student ID", "Name", "Gender", "Mobile", "Date of Birth", "Email", "City", "Pincode", "Selection Status")

        #format column
        self.add_student_tree.column("Sr No", anchor="center", width = 100, minwidth=100)
        self.add_student_tree.column("Student ID", anchor="center", width = 150, minwidth=150)
        self.add_student_tree.column("Name", anchor="center", width = 300, minwidth=300)
        self.add_student_tree.column("Gender", anchor="center", width = 300, minwidth = 300)
        self.add_student_tree.column("Mobile", anchor="center", width = 300, minwidth = 300)
        self.add_student_tree.column("Date of Birth", anchor="center", width = 300, minwidth = 300)
        self.add_student_tree.column("Email", anchor="center", width = 300, minwidth = 300)
        # self.add_student_tree.column("Address", anchor="center", width = 300, minwidth = 300)
        self.add_student_tree.column("City", anchor="center", width = 300, minwidth = 300)
        self.add_student_tree.column("Pincode", anchor="center", width = 300, minwidth = 300)
        self.add_student_tree.column("Selection Status", anchor="center", width = 300, minwidth = 300)
        
        #create a heading
        self.add_student_tree.heading("Sr No", text = "Sr No", anchor = "center")
        self.add_student_tree.heading("Student ID", text = "Student ID", anchor = "center")
        self.add_student_tree.heading("Name", text = "Name", anchor = "center")
        self.add_student_tree.heading("Gender", text = "Gender", anchor = "center")
        self.add_student_tree.heading("Mobile", text = "Mobile", anchor = "center")
        self.add_student_tree.heading("Date of Birth", text = "Date of Birth", anchor = "center")
        self.add_student_tree.heading("Email", text = "Email", anchor = "center")
        # self.add_student_tree.heading("Address", text = "Address", anchor = "center")
        self.add_student_tree.heading("City", text = "City", anchor = "center")
        self.add_student_tree.heading("Pincode", text = "Pincode", anchor = "center")
        self.add_student_tree.heading("Selection Status", text = "Selection Status", anchor = "center")

        #Create striped to our tages
        self.add_student_tree.tag_configure("oddrow", background="white")
        self.add_student_tree.tag_configure("evenrow", background="lightblue")

        #======calling the show student record automatically======#
        show_student_record_auto()        

        self.student_report_page_frame.place(x=0,y=0)

    def student_attendance_frame(self):
        self.student_attendance_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.student_attendance_page_frame, text="Attendance")

        #=======functions============#
        
        def show_record_auto():
            std = self.standard_entry.cget("text")
            div = self.division_entry.cget("text")
            
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                cur.execute("select srno, concat(first_name, ' ' , last_name) as name from student where std_name = %s and div_name = %s group by srno", (std, div))

                records = cur.fetchall()
                self.count = 0
                #show record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_attendance_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], "N/A", date.today()), tags=("evenrow",))
                    else:
                        self.add_attendance_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], "N/A", date.today()), tags=("oddrow",))

                    self.count += 1

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        
        #========select record from treeview===========#
        def select_record(e):
            # #clear the option menu
            # self.attendance_var.set(value = "")

            #grab record number
            selected = self.add_attendance_tree.focus()

            if selected:
                #grab record values
                values = self.add_attendance_tree.item(selected, "values")

                self.attendance_var.set(values[2])
        
        #======update attendance==========#
        def update():
            global values
            #clear the treeview
            selected = self.add_attendance_tree.focus()

            if selected:
                values = self.add_attendance_tree.item(selected, "values")
                attendance_status = self.attendance_var.get()

                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    # for item in self.add_attendance_tree.get_children():
                    update_query = "update attendance set attendance_status = %s where student_no = %s and date = %s"
                    cur.execute(update_query, (attendance_status, values[0], values[3]))
            
                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error ", e)


                # #Update the values
                records = self.add_attendance_tree.item(selected, values = (values[0],values[1], self.attendance_var.get(),date.today()))

                self.attendance_var.set("")

        #======save attendance==========#
        def save_attendance():
            empty_data = list()
            values = self.add_attendance_tree.get_children()
            for i in values:
                data = self.add_attendance_tree.item(i, "values")
                empty_data.append(data)

            placeholder = ",".join(["%s"] * len(data))

            #====date=======#
            date = datetime.now()
            month = date.strftime("%B")
            day = date.strftime("%d")
            year = date.strftime("%Y")
                
            current_date = f"{month} {day}, {year}"
            
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                # for item in self.add_attendance_tree.get_children():
                insert_query = f"insert into attendance(student_no, name, attendance_status, date) values({placeholder})" 
                insert_values = empty_data
                
                cur.executemany(insert_query, insert_values)
        
                #commit the changes
                con.commit()

                messagebox.showinfo("Attendance", f"Class Attendance Saved Successfully for {current_date}")

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
                # messagebox.showwarning("Attendance Warning", f"Attendance for {current_date} already exists.")

        #============================================#
        self.standard_label = ctk.CTkLabel(self.student_attendance_page_frame, text = "Select Standard :", font = ("Consolas", 20), text_color="green")
        self.standard_label.place(x = 30, y = 60)

        self.standard_entry = ctk.CTkLabel(self.student_attendance_page_frame, text = "5th std", font = ("Consolas", 20), text_color="green")
        self.standard_entry.place(x = 240, y = 60)

        self.division_label = ctk.CTkLabel(self.student_attendance_page_frame, text = "Select Division :", font = ("Consolas", 20), text_color="green")
        self.division_label.place(x = 30, y = 100)

        self.division_entry = ctk.CTkLabel(self.student_attendance_page_frame, text = "A", font = ("Consolas", 20), text_color="green")
        self.division_entry.place(x = 240, y = 100)

        self.attendance_label = ctk.CTkLabel(self.student_attendance_page_frame, text = "Take Attendance :", font = ("Consolas", 20), text_color="green")
        self.attendance_label.place(x = 30, y = 140)

        self.attendance_values = ["Absent", "Present", "Leave"]
        self.attendance_var = tk.StringVar(value = "N/A")
        self.attendance_option = ctk.CTkOptionMenu(self.student_attendance_page_frame, width = 200, height = 30, corner_radius=2, values=self.attendance_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=self.attendance_var)
        self.attendance_option.place(x = 240, y = 140)

        self.select_button = ctk.CTkButton(self.student_attendance_page_frame, text = "Select", width = 120, height = 40, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=update, border_color="green", border_width=2)
        self.select_button.place(x = 240, y = 180)

        #=======treeview setting========#
        #add some style
        style = ttk.Style()

        #pick a theme
        style.theme_use("alt")

        #configure the tree view color
        style.configure("Treeview", 
                        background = "#EEF0E5",
                        rowheight = 25,
                        fieldbackground = "#F3FBF1", font = ("Consolas", 14))
            
        style.configure("mystyle.Treeview", font=('Consolas', 15))

        #configure the selected color
        style.configure("Treeview", background = [("selected", "#347083")])

        #increse the font size of heading
        style.configure("Treeview.Heading", font=("Consolas", 18))

        self.data_frame = tk.Frame(self.student_attendance_page_frame, bg = "lightgrey", borderwidth=0, relief="solid")
        self.data_frame.pack_propagate(False)
        self.data_frame.place(x = 20, y = 300, height = 500, width = 750)

        #create a scrollbar
        y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
        x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

        y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

        #create a treeview
        self.add_attendance_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
        self.add_attendance_tree.pack(fill = "both", expand= True)
        self.add_attendance_tree.bind("<<TreeviewSelect>>", select_record)

        #configure the scrollbar
        x_scroll.config(command = self.add_attendance_tree.xview)
        y_scroll.config(command = self.add_attendance_tree.yview)

        #define our columns
        self.add_attendance_tree["columns"] = ("Sr No","Name", "Attendance", "Date")

        #format column
        self.add_attendance_tree.column("Sr No", anchor="center", width = 100, minwidth=100)
        self.add_attendance_tree.column("Name", anchor="center", width = 300, minwidth=300)
        self.add_attendance_tree.column("Attendance", anchor="center", width = 300, minwidth=300)
        self.add_attendance_tree.column("Date", anchor="center", width = 200, minwidth=200)
            
        #create a heading
        self.add_attendance_tree.heading("Sr No", text = "Sr No", anchor = "center")
        self.add_attendance_tree.heading("Name", text = "Name", anchor = "center")
        self.add_attendance_tree.heading("Attendance", text = "Attendance", anchor = "center")
        self.add_attendance_tree.heading("Date", text = "Date", anchor = "center")
            
        #Create striped to our tages
        self.add_attendance_tree.tag_configure("oddrow", background="white")
        self.add_attendance_tree.tag_configure("evenrow", background="lightblue")

        #========calendar open=========#
            
        self.atd_calendar_frame = ctk.CTkFrame(self.student_attendance_page_frame, width = 450, height=325, corner_radius=0,  border_width=2, border_color="green", fg_color="white")

        self.atd_calendar = tkcalendar.Calendar(self.atd_calendar_frame, date_pattern = "yyyy-mm-dd" ,background = "#388E3C")
        self.atd_calendar.pack(fill = "both", expand = True)
        # self.atd_calendar.bind("<<CalendarSelected>>", lambda e : grab_date(self.atd_calendar))

        self.atd_calendar_frame.place(x = 622, y = 240)
        self.atd_calendar_frame.pack_propagate(False)

        self.add_attendance_button = ctk.CTkButton(self.student_attendance_page_frame, text = "Add Attendance", width = 450, height = 70, font = ("Consolas", 30), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command = save_attendance, border_color="green", border_width=2)
        self.add_attendance_button.place(x = 622, y = 570)

        show_record_auto()
        
        self.student_attendance_page_frame.place(x=0,y=0)

    def student_attendance_report_frame(self):
        self.attendance_report_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.attendance_report_page_frame,text="Attendance Reports")

        def fetch_std_record():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                cur.execute("select div_name from division group by div_name")

                records = cur.fetchall()

                div_list = []
                for record in records:
                    div_list.append(record[0])
                
                #======configure the option menu for standard values
                self.choose_division_values= div_list
                self.choose_division_option.configure(values = self.choose_division_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

            

        def grab_date(e):
            global current_date
            current_date = self.calendar.get_date()

        def attendance_report_func():
            std = self.selected_standard_label.cget("text")
            div = div_var.get()

            #=======treeview setting========#
            #add some style
            style = ttk.Style()

            #pick a theme
            style.theme_use("alt")

            #configure the tree view color
            style.configure("Treeview", 
                            background = "#EEF0E5",
                            rowheight = 25,
                            fieldbackground = "#F3FBF1", font = ("Consolas", 14))
                
            style.configure("mystyle.Treeview", font=('Consolas', 15))

            #configure the selected color
            style.configure("Treeview", background = [("selected", "#347083")])

            #increse the font size of heading
            style.configure("Treeview.Heading", font=("Consolas", 18))

            self.data_frame = tk.Frame(self.attendance_report_page_frame, bg = "lightgrey", borderwidth=0, relief="solid")
            self.data_frame.pack_propagate(False)
            self.data_frame.place(x = 20, y = 400, height = 300, width = 1000)

            #create a scrollbar
            y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
            x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

            y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
            x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

            #create a treeview
            self.add_attendance_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
            self.add_attendance_tree.pack(fill = "both", expand= True)
            
            #configure the scrollbar
            x_scroll.config(command = self.add_attendance_tree.xview)
            y_scroll.config(command = self.add_attendance_tree.yview)

            #define our columns
            self.add_attendance_tree["columns"] = ("Sr No","Name", "Attendance", "Date")

            #format column
            self.add_attendance_tree.column("Sr No", anchor="center", width = 100, minwidth=100)
            self.add_attendance_tree.column("Name", anchor="center", width = 300, minwidth=300)
            self.add_attendance_tree.column("Attendance", anchor="center", width = 300, minwidth=300)
            self.add_attendance_tree.column("Date", anchor="center", width = 200, minwidth=200)
                
            #create a heading
            self.add_attendance_tree.heading("Sr No", text = "Sr No", anchor = "center")
            self.add_attendance_tree.heading("Name", text = "Name", anchor = "center")
            self.add_attendance_tree.heading("Attendance", text = "Attendance", anchor = "center")
            self.add_attendance_tree.heading("Date", text = "Date", anchor = "center")
                
            #Create striped to our tages
            self.add_attendance_tree.tag_configure("oddrow", background="white")
            self.add_attendance_tree.tag_configure("evenrow", background="lightblue")

            #=======show record in treeview============#
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                cur.execute("select student_no, name, attendance_status, date from attendance a, student s where s.srno = a.student_no and s.std_name = %s and s.div_name = %s and a.date = %s", (std, div, current_date))

                records = cur.fetchall()
                self.count = 0
                #show record in treeview
                for record in records:
                    if self.count %2 == 0:
                        self.add_attendance_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2], record[3]), tags=("evenrow",))
                    else:
                        self.add_attendance_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2], record[3]), tags=("oddrow",))

                    self.count += 1

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #======other widgets=====#
        self.choose_standard_label = ctk.CTkLabel(self.attendance_report_page_frame, text = "Select Standard :", font = ("Consolas", 20), text_color="green")
        self.choose_standard_label.place(x = 30, y = 60)

        self.selected_standard_label = ctk.CTkLabel(self.attendance_report_page_frame, text = "5th std", font = ("Consolas", 20), text_color="green")
        self.selected_standard_label.place(x = 240, y = 60)

        self.choose_division_label = ctk.CTkLabel(self.attendance_report_page_frame, text = "Select Division :", font = ("Consolas", 20), text_color="green")
        self.choose_division_label.place(x = 30, y =100)

        self.choose_division_values = []
        div_var = tk.StringVar(value = "")
        self.choose_division_option = ctk.CTkOptionMenu(self.attendance_report_page_frame, width = 200, height = 30, corner_radius=2, values=self.choose_division_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=div_var)
        self.choose_division_option.place(x = 240, y = 100)

        self.select_date_label = ctk.CTkLabel(self.attendance_report_page_frame, text = "Select Date :", font = ("Consolas", 20), text_color="green")
        self.select_date_label.place(x = 75, y = 150)

        self.calendar_frame = ctk.CTkFrame(self.attendance_report_page_frame, width = 300, height=200, corner_radius=0,  border_width=0, border_color="green", fg_color="white")

        self.calendar = tkcalendar.Calendar(self.calendar_frame, date_pattern = "yyyy-mm-dd" ,background = "#388E3C")
        self.calendar.pack(fill = "both", expand = True)
        self.calendar.bind("<<CalendarSelected>>", lambda e : grab_date(self.calendar))

        self.calendar_frame.place(x = 240, y = 150)

        self.select_button = ctk.CTkButton(self.attendance_report_page_frame, text = "Select", width = 120, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command= attendance_report_func, border_color="green", border_width=2)
        self.select_button.place(x = 455, y = 267)

        #=========calling the function============#
        fetch_std_record()

        self.attendance_report_page_frame.place(x=0,y=0)

    def advance_report_frame(self):
        self.advance_report_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.advance_report_page_frame,text="Advance Reports")

        def fetch_std_and_div():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #execute the cursor query
                cur.execute("select d.std_name, d.div_name from staff, teacher_assignments ta, division d where staff.srno = ta.srno and d.div_id = ta.std_div_id and email = 'vikas123@gmail.com'")

                records = cur.fetchall()

                for record in records:
                    self.selected_standard_label.configure(text = f"{record[0]}")
                    self.select_division_option.configure(text = f"{record[1]}")

                #execute the cursor query
                cur.execute("select srno from student where std_name = %s and div_name = %s", (record[0], record[1]))

                roll_records = cur.fetchall()

                rollno_list = []
                for rollno in roll_records:
                    rollno_list.append(str(rollno[0]))
                
                #======configure the option menu for standard values
                self.choose_student_values = rollno_list
                self.choose_student_option.configure(values = self.choose_student_values)

                #commit the changes
                con.commit()

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)

        #=======functions=======#
        def report_sumary_frame():
            #======checking the condition==========#
            rollno = rollno_var.get()
            std = self.selected_standard_label.cget("text")
            div = self.select_division_option.cget("text")

            
            def fetch_student_summary():
                if std == "" and div == "" or rollno == "":
                    messagebox.showerror("Error", "Please select a roll number.")
                else:
                    try:
                        con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                        #create a cursor instance
                        cur = con.cursor()

                        #execute the cursor query
                        cur.execute("select srno, concat(first_name, ' ', last_name) as name,  email, mobile, dob, address, city, pincode, image_path from student where srno = %s and std_name = %s and div_name = %s", (rollno, std, div))

                        records = cur.fetchall()

                        for record in records:
                            self.report_frame_label.configure(text = f"Student Name: {record[1]}")
                            self.student_rollno.configure(text = record[0])
                            self.student_email.configure(text = record[2])
                            self.student_mobile.configure(text = record[3])
                            self.student_birthdate.configure(text = record[4])
                            self.student_address.configure(text = record[5], wraplength = 300)
                            self.student_city.configure(text = record[6])
                            self.student_pincode.configure(text = record[7])
                            image_path = record[8]

                        try:
                            image = Image.open(image_path)

                        except FileNotFoundError:
                            print(f"Error: Could not find image at path: {image_path}")

                        #====configure the image===========#
                            
                        #base name of the image
                        image_file_name = os.path.basename(image_path)

                        #save the image
                        image.save(image_file_name)
                            
                        #open image in form of ctk.CTkImage
                        imageo = ctk.CTkImage(light_image=image, dark_image=image, size = (127, 147))

                        #configure the right side frame label
                        self.student_photo_label.configure(image = imageo)
                        self.student_photo_label.image = imageo

                        #commit the changes
                        con.commit()

                        #close the connection
                        con.close()

                    except Exception as e:
                        print("Error ", e)

            #===========================================#
            self.report_frame = ctk.CTkFrame(self.advance_report_page_frame, width = 700, height=450, corner_radius=2,  border_width=2, border_color="green", fg_color="white")

            self.report_frame_label = ctk.CTkLabel(self.report_frame, width = 700, height = 40, text = "Student Name: ", font = ("Consolas", 25), fg_color="green", text_color="white")
            self.report_frame_label.place(x = 0, y = 0)

            #======other entries=======#
            self.rollno = ctk.CTkLabel(self.report_frame, text = "Roll No: ", font = ("Consolas", 20), text_color="green")
            self.rollno.place(x = 45, y = 50)

            self.student_rollno = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_rollno.place(x = 150, y = 50)

            self.email = ctk.CTkLabel(self.report_frame, text = "Email: ", font = ("Consolas", 20), text_color="green")
            self.email.place(x = 67, y = 90)

            self.student_email = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_email.place(x = 150, y = 90)

            self.mobile = ctk.CTkLabel(self.report_frame, text = "Mobile: ", font = ("Consolas", 20), text_color="green")
            self.mobile.place(x = 57, y = 130)

            self.student_mobile = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_mobile.place(x = 150, y = 130)

            self.birthdate = ctk.CTkLabel(self.report_frame, text = "Birth Date: ", font = ("Consolas", 20), text_color="green")
            self.birthdate.place(x = 10, y = 170)

            self.student_birthdate = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_birthdate.place(x = 150, y = 170)

            self.address = ctk.CTkLabel(self.report_frame, text = "Address: ", font = ("Consolas", 20), text_color="green")
            self.address.place(x = 45, y = 210)

            self.student_address = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_address.place(x = 150, y = 210)

            self.city = ctk.CTkLabel(self.report_frame, text = "City: ", font = ("Consolas", 20), text_color="green")
            self.city.place(x = 78, y = 290)

            self.student_city = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_city.place(x = 150, y = 290)

            self.pincode = ctk.CTkLabel(self.report_frame, text = "Pincode: ", font = ("Consolas", 20), text_color="green")
            self.pincode.place(x = 45, y = 330)

            self.student_pincode = ctk.CTkLabel(self.report_frame, text = "", font = ("Consolas", 20), text_color="green")
            self.student_pincode.place(x = 150, y = 330)

            self.student_photo_frame = ctk.CTkFrame(self.report_frame, width = 130, height=150, corner_radius=0,  border_width=3, border_color="black", fg_color="white")
            self.student_photo_frame.place(x = 540, y = 60)

            self.student_photo_label = ctk.CTkLabel(self.student_photo_frame, text = "", fg_color="grey", width = 127, height=147)
            self.student_photo_label.place(x = 1, y = 1)

            #=======calling the function============#
            fetch_student_summary()

            self.report_frame.place(x = 200, y = 200)

        self.choose_standard_label = ctk.CTkLabel(self.advance_report_page_frame, text = "Select Standard :", font = ("Consolas", 20), text_color="green")
        self.choose_standard_label.place(x = 30, y = 60)

        self.selected_standard_label = ctk.CTkLabel(self.advance_report_page_frame, text = "", font = ("Consolas", 20), text_color="green")
        self.selected_standard_label.place(x = 240, y = 60)

        self.choose_division_label = ctk.CTkLabel(self.advance_report_page_frame, text = "Select Division :", font = ("Consolas", 20), text_color="green")
        self.choose_division_label.place(x = 30, y =100)

        self.select_division_option = ctk.CTkLabel(self.advance_report_page_frame, text = "", font = ("Consolas", 20), text_color="green")
        self.select_division_option.place(x = 240, y = 100)

        self.choose_student_label = ctk.CTkLabel(self.advance_report_page_frame, text = "Select Student :", font = ("Consolas", 20), text_color="green")
        self.choose_student_label.place(x = 41, y =140)

        self.choose_student_values = []
        rollno_var = tk.StringVar(value = "")
        self.choose_student_option = ctk.CTkOptionMenu(self.advance_report_page_frame, width = 200, height = 30, corner_radius=2, values=self.choose_student_values, fg_color="#D8D9DA", text_color="black", dropdown_font=("Consolas", 18), font=("Consolas", 18), variable=rollno_var)
        self.choose_student_option.place(x = 240, y = 140)

        self.select_button = ctk.CTkButton(self.advance_report_page_frame, text = "Select", width = 120, height = 35, font = ("Consolas", 20), text_color="green", fg_color="white", corner_radius=2, hover_color="white", cursor = "hand2", command=report_sumary_frame, border_color="green", border_width=2)
        self.select_button.place(x = 455, y = 140)

        #==========calling the function==========#

        fetch_std_and_div()

        self.advance_report_page_frame.place(x=0,y=0)

    def advance_att_report_frame(self):
        self.advance_att_report_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=600, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.advance_att_report_page_frame,text="Advance Att Reports")
        self.advance_att_report_page_frame.place(x=0,y=0)

    def student_complain_frame(self):
        self.complain_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.complain_page_frame,text="Complain")

        def show_complain_record():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                #fetch the detail of complain
                cur.execute("select rollno, student_name, subject, message, reply,complain_id from complain c, student s where s.srno = c.rollno and s.email = 'vikaskahar25077@gmail.com'")

                complain_record = cur.fetchall()

                #===showing the data in treeview=====#
                self.count = 0
                for fetch_record in complain_record:
                    if self.count %2 == 0:
                        self.complain_tree.insert(parent = "", index = tk.END, iid = self.count, values=(fetch_record[0], fetch_record[1], fetch_record[2], fetch_record[3], fetch_record[4]), tags=("evenrow",))
                    else:
                        self.complain_tree.insert(parent = "", index = tk.END, iid = self.count, values=(fetch_record[0], fetch_record[1], fetch_record[2], fetch_record[3], fetch_record[4]), tags=("oddrow",))
                    self.count += 1

                #commit the changes
                con.commit()

                self.complain_count_label.configure(text = len(complain_record))

                #close the connection
                con.close()

            except Exception as e:
                print("Error ", e)
        
        def complain_reply_func():
            selected = self.complain_tree.focus()
            selected_values = self.complain_tree.item(selected, "values")
            
            if selected:
                #====open reply window ==========#
                reply_window = ctk.CTkToplevel(fg_color="white")
                reply_window.title("School Management System")
                reply_window.geometry("700x400+750+300")

                #======function======#
                def update_reply_msg():
                    answer = self.complain_answer_textbox.get("0.0", tk.END)
                    try:
                        con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                        #create a cursor instance
                        cur = con.cursor()

                        cur.execute("select complain_id, edate from complain where rollno = %s and student_name = %s and subject = %s and message = %s and reply = %s", (selected_values[0], selected_values[1], selected_values[2], selected_values[3], selected_values[4]))

                        records = cur.fetchall()
                        
                        #====update the database==========#
                        for record in records:
                            #fetch the complain record detail to see status
                            cur.execute("update complain set reply = %s where complain_id = %s and edate = %s", (answer, record[0], record[1]))

                        #commit the changes
                        con.commit()


                        #close the connection
                        con.close()

                    except Exception as e:
                        print("Error :", e)

                    #====update the values==========#
                    self.complain_tree.item(selected, values = (self.rollno_entry.cget("text"), self.name_entry.cget("text"), self.subject_entry.cget("text"), self.complain_entry.cget("text"), self.complain_answer_textbox.get("0.0", tk.END)))
                
                def destroy_reply_window(e):
                    reply_window.destroy()

                #===making heading label===========#
                self.reply_head_label =  ctk.CTkLabel(reply_window, text = "Reply Complain", font = ("Consolas", 20), text_color="white", fg_color="green", width = 700, height = 40)
                self.reply_head_label.place(x = 0, y = 0)

                self.rollno_label = ctk.CTkLabel(reply_window, text = "Roll No: ", font = ("Consolas", 20), text_color="green")
                self.rollno_label.place(x = 20, y = 50)

                self.rollno_entry = ctk.CTkLabel(reply_window, text = selected_values[0], font = ("Consolas", 20), text_color="green")
                self.rollno_entry.place(x = 125, y = 50)

                self.name_label = ctk.CTkLabel(reply_window, text = "Name: ", font = ("Consolas", 20), text_color="green")
                self.name_label.place(x = 55, y = 100)

                self.name_entry = ctk.CTkLabel(reply_window, text = selected_values[1], font = ("Consolas", 20), text_color="green")
                self.name_entry.place(x = 125, y = 100)

                self.subject_label = ctk.CTkLabel(reply_window, text = "Subject: ", font = ("Consolas", 20), text_color="green")
                self.subject_label.place(x = 22, y = 150)

                self.subject_entry = ctk.CTkLabel(reply_window, text = selected_values[2], font = ("Consolas", 20), text_color="green")
                self.subject_entry.place(x = 125, y = 150)

                self.complain_label = ctk.CTkLabel(reply_window, text = "Complain: ", font = ("Consolas", 20), text_color="green")
                self.complain_label.place(x = 10, y = 200)

                self.complain_entry = ctk.CTkLabel(reply_window, text = selected_values[3], font = ("Consolas", 20), text_color="green")
                self.complain_entry.place(x = 125, y = 200)

                self.complain_answer_label = ctk.CTkLabel(reply_window, text = "Answer: ", font = ("Consolas", 20), text_color="green")
                self.complain_answer_label.place(x = 32, y = 250)

                self.complain_answer_textbox = ctk.CTkTextbox(reply_window, height = 80, corner_radius=2, border_width=2, border_color="grey", scrollbar_button_hover_color="green", font = ("Consolas", 20), wrap = "word")
                self.complain_answer_textbox.place(x = 125, y = 250)
                
                self.send_button = ctk.CTkButton(reply_window, text = "Send", width = 130, height = 35, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=update_reply_msg)
                self.send_button.place(x = 125, y = 340)
                self.send_button.bind("<Button-1>", destroy_reply_window)

                reply_window.grab_set()
            
        #=======treeview setting========#
        #add some style
        style = ttk.Style()

        #pick a theme
        style.theme_use("alt")

        #configure the tree view color
        style.configure("Treeview", 
                        background = "#EEF0E5",
                        rowheight = 25,
                        fieldbackground = "#F3FBF1", font = ("Consolas", 14))
                
        style.configure("mystyle.Treeview", font=('Consolas', 15))

        #configure the selected color
        style.configure("Treeview", background = [("selected", "#347083")])

        #increse the font size of heading
        style.configure("Treeview.Heading", font=("Consolas", 18))

        self.data_frame = tk.Frame(self.complain_page_frame, bg = "lightgrey", borderwidth=0, relief="solid")
        self.data_frame.pack_propagate(False)
        self.data_frame.place(x = 25, y = 170 , height = 200, width = 1300)

        #create a scrollbar
        y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
        x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

        y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
        x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

        #create a treeview
        self.complain_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
        self.complain_tree.pack(fill = "both", expand= True)

        #configure the scrollbar
        x_scroll.config(command = self.complain_tree.xview)
        y_scroll.config(command = self.complain_tree.yview)

        #define our columns
        self.complain_tree["columns"] = ("Roll No", "Student Name", "Subject", "Complain", "Reply")

        #format column
        self.complain_tree.column("Roll No", anchor="center", width = 150, minwidth=150)
        self.complain_tree.column("Student Name", anchor="center", width = 300, minwidth=300)
        self.complain_tree.column("Subject", anchor="center", width = 400, minwidth = 400)
        self.complain_tree.column("Complain", anchor="center", width = 400, minwidth = 400)
        self.complain_tree.column("Reply", anchor="center", width = 400, minwidth = 400)
                
        #create a heading
        self.complain_tree.heading("Roll No", text = "Roll No", anchor = "center")
        self.complain_tree.heading("Student Name", text = "Student Name", anchor = "center")
        self.complain_tree.heading("Subject", text = "Subject", anchor = "center")
        self.complain_tree.heading("Complain", text = "Complain", anchor = "center")
        self.complain_tree.heading("Reply", text = "Reply", anchor = "center")
                
        #Create striped to our tages
        self.complain_tree.tag_configure("oddrow", background="white")
        self.complain_tree.tag_configure("evenrow", background="lightblue") 

        self.total_complain_label = ctk.CTkLabel(self.complain_page_frame, text = "Total Complain = ", font = ("Consolas", 20), text_color="green")
        self.total_complain_label.place(x = 20, y = 60)

        self.complain_count_label = ctk.CTkLabel(self.complain_page_frame, text = "0", font = ("Consolas", 20), text_color="green")
        self.complain_count_label.place(x = 210, y = 60)

        self.reply_button = ctk.CTkButton(self.complain_page_frame, text = "Reply", width = 130, height = 35, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=complain_reply_func)
        self.reply_button.place(x = 25, y = 310)

        #=======calling the function==========#
        show_complain_record()

        self.complain_page_frame.place(x=0,y=0)

    def student_leave_frame(self):
        self.leave_page_frame = ctk.CTkFrame(self.rightside_frame, width = 1092, height=700, corner_radius=0,  border_width=1, border_color="green", fg_color="white")
        ChangeLabel(self.leave_page_frame,text="Leave")

        #======show record of leave===========#
        def student_new_leave_frame():
            #=====inside frame======#
            self.new_leave_frame = ctk.CTkFrame(self.leave_page_frame, width = 1072, height=270, corner_radius=0,  border_width=0, border_color="green", fg_color="white")
        
            #====================function====================#
            def show_new_leave_record():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #fetch the leave record detail to see status
                    cur.execute("select rollno, student_name, message, no_days, status from student_leave where status = 'Pending'")

                    records = cur.fetchall()
                    total_new_leave_count = len(records)

                    self.count = 0
                    #show record in treeview
                    for record in records:
                        if self.count %2 == 0:
                            self.new_leave_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2], record[3], record[4]), tags=("evenrow",))
                        else:
                            self.new_leave_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2], record[3], record[4]), tags=("oddrow",))
                        self.count += 1

                    #=====configure the count label============#
                    self.total_leave_label.configure(text = f"Total New Leave = {total_new_leave_count}")
                    
                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error :", e)

            #=====approve new record ============#
            def approve_new_record():
                selected = self.new_leave_tree.selection()
                selected_values = self.new_leave_tree.item(selected, "values")
                # print(selected_values)

                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #fetch the leave record detail to see status
                    cur.execute("select leave_id, edate from student_leave where rollno = %s and student_name = %s and message = %s and no_days = %s and status = %s", selected_values)

                    pending_record = cur.fetchall()
                
                    for record in pending_record:
                        # #update the leave status
                        cur.execute("update student_leave set status = 'Approve' where leave_id = %s and edate = %s", (record[0], record[1]))

                    # commit the changes
                    con.commit()

                    destroy_new_leave_frame()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error :", e)
            
            #=========reject new record===============#
            def reject_new_record():
                reject_selected = self.new_leave_tree.selection()
                reject_selected_values = self.new_leave_tree.item(reject_selected, "values")
     
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    # #fetch the leave record detail to see status
                    cur.execute("select leave_id, edate from student_leave where rollno = %s and student_name = %s and message = %s and no_days = %s and status = %s", reject_selected_values)

                    pending_record = cur.fetchall()
   
                    for record in pending_record:
                        # #update the leave status
                        cur.execute("update student_leave set status = 'Reject' where leave_id = %s and edate = %s", (record[0], record[1]))

                    #commit the changes
                    con.commit()

                    destroy_new_leave_frame()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error :", e)

            #=====destroy the frame============#
            def destroy_new_leave_frame():
                self.new_leave_frame.destroy()

            #=======treeview setting========#
            #add some style
            style = ttk.Style()

            #pick a theme
            style.theme_use("alt")

            #configure the tree view color
            style.configure("Treeview", 
                                background = "#EEF0E5",
                                rowheight = 25,
                                fieldbackground = "#F3FBF1", font = ("Consolas", 14))
                
            style.configure("mystyle.Treeview", font=('Consolas', 15))

            #configure the selected color
            style.configure("Treeview", background = [("selected", "#347083")])

            #increse the font size of heading
            style.configure("Treeview.Heading", font=("Consolas", 18))

            self.data_frame = tk.Frame(self.new_leave_frame, bg = "lightgrey", borderwidth=0, relief="solid")
            self.data_frame.pack_propagate(False)
            self.data_frame.place(x = 10, y = 5, height = 200, width = 1320)

            #create a scrollbar
            y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
            x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

            y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
            x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

            #create a treeview
            self.new_leave_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
            self.new_leave_tree.pack(fill = "both", expand= True)

            #configure the scrollbar
            x_scroll.config(command = self.new_leave_tree.xview)
            y_scroll.config(command = self.new_leave_tree.yview)

            #define our columns
            self.new_leave_tree["columns"] = ("Roll No", "Student Name", "Subject", "Days","Status")

            #format column
            self.new_leave_tree.column("Roll No", anchor="center", width = 50, minwidth=50)
            self.new_leave_tree.column("Student Name", anchor="center", width = 150, minwidth=150)
            self.new_leave_tree.column("Subject", anchor="center", width = 300, minwidth = 300)
            self.new_leave_tree.column("Days", anchor="center", width = 50, minwidth = 50)
            self.new_leave_tree.column("Status", anchor="center", width = 100, minwidth = 100)
                
            #create a heading
            self.new_leave_tree.heading("Roll No", text = "Roll No", anchor = "center")
            self.new_leave_tree.heading("Student Name", text = "Student Name", anchor = "center")
            self.new_leave_tree.heading("Subject", text = "Subject", anchor = "center")
            self.new_leave_tree.heading("Days", text = "Days", anchor = "center")
            self.new_leave_tree.heading("Status", text = "Status", anchor = "center")
                
            #Create striped to our tages
            self.new_leave_tree.tag_configure("oddrow", background="white")
            self.new_leave_tree.tag_configure("evenrow", background="lightblue")

            self.approve_button = ctk.CTkButton(self.new_leave_frame, text = "Approve", width = 100, height = 35, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=approve_new_record)
            self.approve_button.place(x=10,y=180)

            self.reject_button = ctk.CTkButton(self.new_leave_frame, text = "Reject", width = 100, height = 35, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=reject_new_record)
            self.reject_button.place(x=120,y=180)

            #=======calling the function==========#
            show_new_leave_record()

            self.new_leave_frame.place(x =10, y = 170)

        def student_approve_leave_frame():
            #=====inside frame======#
            self.approve_leave_frame = ctk.CTkFrame(self.leave_page_frame, width = 1072, height=270, corner_radius=0,  border_width=0, border_color="green", fg_color="white")

            #====================function====================#
            def show_approve_leave_record():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #fetch the leave record detail to see status
                    cur.execute("select rollno, student_name, message, no_days, status from student_leave where status = 'Approve'")

                    records = cur.fetchall()
                    total_approve_leave_count = len(records)

                    self.count = 0
                    #show record in treeview
                    for record in records:
                        if self.count %2 == 0:
                            self.approve_leave_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2], record[3], record[4]), tags=("evenrow",))
                        else:
                            self.approve_leave_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2], record[3], record[4]), tags=("oddrow",))
                        self.count += 1

                    #=====configure the count label============#
                    self.total_leave_label.configure(text = f"Total Approve Leave = {total_approve_leave_count}")
                    
                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error :", e)

            #=========reject new record===============#
            def reject_approve_record():
                reject_selected = self.approve_leave_tree.selection()
                reject_selected_values = self.approve_leave_tree.item(reject_selected, "values")

                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    # #fetch the leave record detail to see status
                    cur.execute("select leave_id, edate from student_leave where rollno = %s and student_name = %s and message = %s and no_days = %s and status = %s", reject_selected_values)

                    pending_record = cur.fetchall()
                    for record in pending_record:
                        # #update the leave status
                        cur.execute("update student_leave set status = 'Reject' where leave_id = %s and edate = %s", (record[0], record[1]))

                    #commit the changes
                    con.commit()

                    destroy_approve_leave_frame()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error :", e)

            #=====destroy the frame============#
            def destroy_approve_leave_frame():
                self.approve_leave_frame.destroy()
            
            #=======treeview setting========#
            #add some style
            style = ttk.Style()

            #pick a theme
            style.theme_use("alt")

            #configure the tree view color
            style.configure("Treeview", 
                            background = "#EEF0E5",
                            rowheight = 25,
                            fieldbackground = "#F3FBF1", font = ("Consolas", 14))
            
            style.configure("mystyle.Treeview", font=('Consolas', 15))

            #configure the selected color
            style.configure("Treeview", background = [("selected", "#347083")])

            #increse the font size of heading
            style.configure("Treeview.Heading", font=("Consolas", 18))

            self.data_frame = tk.Frame(self.approve_leave_frame, bg = "lightgrey", borderwidth=0, relief="solid")
            self.data_frame.pack_propagate(False)
            self.data_frame.place(x = 10, y = 5, height = 200, width = 1320)

            #create a scrollbar
            y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
            x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

            y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
            x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

            #create a treeview
            self.approve_leave_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
            self.approve_leave_tree.pack(fill = "both", expand= True)

            #configure the scrollbar
            x_scroll.config(command = self.approve_leave_tree.xview)
            y_scroll.config(command = self.approve_leave_tree.yview)

            #define our columns
            self.approve_leave_tree["columns"] = ("Roll No", "Student Name", "Subject", "Days", "Status")

            #format column
            self.approve_leave_tree.column("Roll No", anchor="center", width = 50, minwidth=50)
            self.approve_leave_tree.column("Student Name", anchor="center", width = 150, minwidth=150)
            self.approve_leave_tree.column("Subject", anchor="center", width = 300, minwidth = 300)
            self.approve_leave_tree.column("Days", anchor="center", width = 50, minwidth = 50)
            self.approve_leave_tree.column("Status", anchor="center", width = 100, minwidth = 100)
            
            #create a heading
            self.approve_leave_tree.heading("Roll No", text = "Roll No", anchor = "center")
            self.approve_leave_tree.heading("Student Name", text = "Student Name", anchor = "center")
            self.approve_leave_tree.heading("Subject", text = "Subject", anchor = "center")
            self.approve_leave_tree.heading("Days", text = "Days", anchor = "center")
            self.approve_leave_tree.heading("Status", text = "Status", anchor = "center")
            
            #Create striped to our tages
            self.approve_leave_tree.tag_configure("oddrow", background="white")
            self.approve_leave_tree.tag_configure("evenrow", background="lightblue")

            self.reject_button = ctk.CTkButton(self.approve_leave_frame, text = "Reject", width = 100, height = 35, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=reject_approve_record)
            self.reject_button.place(x=10,y=180)
            
            #======calling the function===============#
            show_approve_leave_record()

            self.approve_leave_frame.place(x =10, y = 170)

        def student_reject_leave_frame():
            #=====inside frame======#
            self.reject_leave_frame = ctk.CTkFrame(self.leave_page_frame, width = 1072, height=270, corner_radius=0,  border_width=0, border_color="green", fg_color="white")

            def show_reject_leave_record():
                try:
                    con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                    #create a cursor instance
                    cur = con.cursor()

                    #fetch the leave record detail to see status
                    cur.execute("select rollno, student_name, message, no_days, status from student_leave where status = 'Reject'")

                    records = cur.fetchall()
                    total_reject_leave_count = len(records)

                    self.count = 0
                    #show record in treeview
                    for record in records:
                        if self.count %2 == 0:
                            self.reject_leave_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2], record[3], record[4]), tags=("evenrow",))
                        else:
                            self.reject_leave_tree.insert(parent = "", index = tk.END, iid = self.count, values=(record[0], record[1], record[2], record[3], record[4]), tags=("oddrow",))
                        self.count += 1

                    self.total_leave_label.configure(text = f"Total Reject Leave = {total_reject_leave_count}")
                    
                    #commit the changes
                    con.commit()

                    #close the connection
                    con.close()

                except Exception as e:
                    print("Error :", e)
            
            #=======treeview setting========#
            #add some style
            style = ttk.Style()

            #pick a theme
            style.theme_use("alt")

            #configure the tree view color
            style.configure("Treeview", 
                            background = "#EEF0E5",
                            rowheight = 25,
                            fieldbackground = "#F3FBF1", font = ("Consolas", 14))
            
            style.configure("mystyle.Treeview", font=('Consolas', 15))

            #configure the selected color
            style.configure("Treeview", background = [("selected", "#347083")])

            #increse the font size of heading
            style.configure("Treeview.Heading", font=("Consolas", 18))

            self.data_frame = tk.Frame(self.reject_leave_frame, bg = "lightgrey", borderwidth=0, relief="solid")
            self.data_frame.pack_propagate(False)
            self.data_frame.place(x = 10, y = 5, height = 200, width = 1320)

            #create a scrollbar
            y_scroll = tk.Scrollbar(self.data_frame, orient="vertical")
            x_scroll = tk.Scrollbar(self.data_frame, orient="horizontal")

            y_scroll.pack(side = tk.RIGHT, fill = tk.Y)
            x_scroll.pack(side = tk.BOTTOM, fill = tk.X)

            #create a treeview
            self.reject_leave_tree = ttk.Treeview(self.data_frame, show = "headings",selectmode="extended", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, style="mystyle.Treeview")
            self.reject_leave_tree.pack(fill = "both", expand= True)

            #configure the scrollbar
            x_scroll.config(command = self.reject_leave_tree.xview)
            y_scroll.config(command = self.reject_leave_tree.yview)

            #define our columns
            self.reject_leave_tree["columns"] = ("Roll No", "Student Name", "Subject", "Days", "Status")

            #format column
            self.reject_leave_tree.column("Roll No", anchor="center", width = 50, minwidth=50)
            self.reject_leave_tree.column("Student Name", anchor="center", width = 150, minwidth=150)
            self.reject_leave_tree.column("Subject", anchor="center", width = 300, minwidth = 300)
            self.reject_leave_tree.column("Days", anchor="center", width = 50, minwidth = 50)
            self.reject_leave_tree.column("Status", anchor="center", width = 100, minwidth = 100)
            
            #create a heading
            self.reject_leave_tree.heading("Roll No", text = "Roll No", anchor = "center")
            self.reject_leave_tree.heading("Student Name", text = "Student Name", anchor = "center")
            self.reject_leave_tree.heading("Subject", text = "Subject", anchor = "center")
            self.reject_leave_tree.heading("Days", text = "Days", anchor = "center")
            self.reject_leave_tree.heading("Status", text = "Status", anchor = "center")
            
            #Create striped to our tages
            self.reject_leave_tree.tag_configure("oddrow", background="white")
            self.reject_leave_tree.tag_configure("evenrow", background="lightblue")

            #=========calling the function===========#
            show_reject_leave_record()

            self.reject_leave_frame.place(x =10, y = 170)

        #=======other widgets==========#
        self.new_leave_report_button = ctk.CTkButton(self.leave_page_frame, text = "New Leave Report", width = 250, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=student_new_leave_frame)
        self.new_leave_report_button.place(x=10,y=80) 

        self.approve_leave_button = ctk.CTkButton(self.leave_page_frame, text = "Approve Leave", width = 250, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=student_approve_leave_frame)
        self.approve_leave_button.place(x=270,y=80)

        self.reject_leave_report_button = ctk.CTkButton(self.leave_page_frame, text = "Reject Leave", width = 250, height = 40, font = ("Consolas", 20), text_color="white", fg_color="green", corner_radius=2, hover_color="green", cursor = "hand2", command=student_reject_leave_frame)
        self.reject_leave_report_button.place(x=530,y=80)

        self.total_leave_label = ctk.CTkLabel(self.leave_page_frame, text = "Total Reject Leave = 0", font = ("Consolas", 18), text_color="green")
        self.total_leave_label.place(x = 15, y = 140)
      
        #=======calling the function===========#
        student_new_leave_frame()

        self.leave_page_frame.place(x=0,y=0)

class AnnouncementWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="white")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        #========heading frame=================#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        self.notices_label = ctk.CTkLabel(self, text = "Notices", text_color="black", font = ("MS Reference Sans Serif", 30))
        self.notices_label.place(x = 700, y = 150)

        #==========fetch notice==========#
        def fetch_notices():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                cur.execute("select announcement_subject from announcement where type = 'Notice' limit 8")
                results = cur.fetchall()
                return results

                #close the connection
                con.close()

            except Exception as e:
                print("Error :", e)

        #=======notice frame=========#
        self.notice_frame = ctk.CTkFrame(self, width = 840, height = 500, fg_color="#C8DAD3", corner_radius=10)

        # #=======all notices label============#
        self.whatnew_label = ctk.CTkLabel(self.notice_frame, text = "What's New", text_color="black", font = ("MS Reference Sans Serif", 27))
        self.whatnew_label.place(x = 10, y = 20)

        #=====line label===========#
        self.underline1_label = tk.Label(self.notice_frame,bg="black")
        self.underline1_label.place(x = 10, y = 90, width = 1020, height=1)

        #======subject and title==========#
        notice = fetch_notices()
        subject_list = []
        for note in notice:
            subject_list.append(note[0])

        #=====right arrow image=======#
        self.right_arrow_image = ctk.CTkImage(light_image=Image.open("image/turn-right.png"), dark_image=Image.open("image/turn-right.png"), size = (20, 20))

        for i in range(0, len(subject_list)):
            self.dot_label = ctk.CTkLabel(self.notice_frame, text = "", image = self.right_arrow_image)
            self.dot_label.place(x = 10, y = 90 + (i * 40))

            self.subject_label = ctk.CTkLabel(self.notice_frame, text = f"{subject_list[i]}", text_color="darkblue", font = ("MS Reference Sans Serif", 18))
            self.subject_label.place(x = 40, y = 90 + (i * 40))

        self.notice_frame.place(x = 80 , y = 250)
        #=============================#

        #=======event frame=========#
        self.event_frame = ctk.CTkFrame(self, width = 500, height = 500, fg_color="#C8DAD3", corner_radius=10)

        # #=======all notices label============#
        self.event_label = ctk.CTkLabel(self.event_frame, text = "Event", text_color="black", font = ("MS Reference Sans Serif", 27))
        self.event_label.place(x = 10, y = 20)

        #==========fetch the event record=======#
        def fetch_event():
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "software")

                #create a cursor instance
                cur = con.cursor()

                cur.execute("select announcement_subject, event_date, event_time, event_venue from announcement where type = 'Event' limit 4")
                results = cur.fetchall()
                return results

                #close the connection
                con.close()

            except Exception as e:
                print("Error :", e)

        #=====line label===========#
        self.underline2_label = tk.Label(self.event_frame,bg="black")
        self.underline2_label.place(x = 10, y = 90, width = 600, height=1)

        #=======records==========#
        event_records = fetch_event()
        event_subject_list = []
        event_date_list = []
        event_time_list = []
        event_venue_list = []
        for event in event_records:
            month = event[1].strftime("%B")
            day = event[1].day
            year = event[1].year
            final_date = f"{month} {day}, {year}"
            event_subject_list.append(event[0])
            event_date_list.append(final_date)
            event_time_list.append(event[2])
            event_venue_list.append(event[3])

        #=====right arrow image=======#
        self.right_arrow_image = ctk.CTkImage(light_image=Image.open("image/turn-right.png"), dark_image=Image.open("image/turn-right.png"), size = (20, 20))

        for i in range(0, len(subject_list)):
            self.dot_label = ctk.CTkLabel(self.event_frame, text = "", image = self.right_arrow_image)
            self.dot_label.place(x = 10, y = 90 + (i * 80))

            self.event_subject_label = ctk.CTkLabel(self.event_frame, text = f"{event_subject_list[i]}", text_color="darkblue", font = ("MS Reference Sans Serif", 18))
            self.event_subject_label.place(x = 40, y = 90 + (i * 80))

            self.event_date_label = ctk.CTkLabel(self.event_frame, text = f"{event_date_list[i]} | {event_time_list[i]} | {event_venue_list[i]}", text_color="black", font = ("MS Reference Sans Serif", 15))
            self.event_date_label.place(x = 40, y = 120 + (i * 80))

        self.event_frame.place(x = 950 , y = 250)

class FacilityWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="white")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        #=====infrastructure label===========#
        self.faciltiy_label = ctk.CTkLabel(self, text = "School Infrastructure", font = ("Consolas",25), text_color="red")
        self.faciltiy_label.place(x = 600, y = 120)

        def facility_photos(image_path, label_text, x, y):
            self.facility_frame = ctk.CTkFrame(self, width = 350, height = 310, fg_color="#D8D9DA", corner_radius=6, border_width=0, border_color="green")

            self.image = ctk.CTkImage(light_image=Image.open(f"{image_path}"), dark_image=Image.open(f"{image_path}"), size = (330, 250))

            self.image_label = ctk.CTkLabel(self.facility_frame, text = "", image = self.image, fg_color="transparent")
            self.image_label.place(x = 10, y = 10)

            self.facility_name_label = ctk.CTkLabel(self.facility_frame, text = f"{label_text}", font = ("Consolas",20), text_color="black")
            self.facility_name_label.place(x = 10, y = 270)

            self.facility_frame.place(x = x, y = y)

        #====1st frame========#
        facility_photos(image_path="image/school-building.png", label_text="School building", x = 20, y = 200)

        #====2nd frame========#
        facility_photos(image_path="image/classroom.png", label_text="School classroom", x = 400, y = 400)

        #====3rd frame========#
        facility_photos(image_path="image/ground.png", label_text="Multi Surface Sports Ground", x = 780, y = 200)

        #====4th frame========#
        facility_photos(image_path="image/science lab.png", label_text="Science lab", x = 1160, y = 400)

class RulesRegulationsWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="white")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        self.guideline_label = ctk.CTkLabel(self, text = "Guidelines", width = 670, height =45, font = ("Consolas",25), text_color="white", fg_color="red", anchor = "center")
        self.guideline_label.place(x = 350, y = 100)

        self.underline_label = tk.Label(self,bg="black")
        self.underline_label.place(x = 438, y = 180, width = 836, height=4)

        #=========function===========#
        def open_new_frame(page):
            for widgets in self.guideline_frame.winfo_children():
                widgets.pack_forget()
                self.update()
            page()
        
        #=======create a frame=========#
        self.guideline_frame = ctk.CTkFrame(self, width = 670, height = 600, fg_color="white", corner_radius=2, border_width=2, border_color="green")

        def display_frame(parent, frame_color,title, image_relative_path, button_text, button_color, page_name, x, y):

            #=======about us buttons=======#
            self.about_us_frame = ctk.CTkFrame(parent, width = 300, height = 150, fg_color=f"{frame_color}", corner_radius=4, border_width=0)

            self.about_us_label = ctk.CTkLabel(self.about_us_frame, text = f"{title}",font = ("Consolas",20), text_color="white")
            self.about_us_label.place(x = 10, y = 50)

            self.about_us_image = ctk.CTkImage(light_image=Image.open(f"{image_relative_path}"), dark_image=Image.open(f"{image_relative_path}"), size = (50, 50))
            
            self.image_label = ctk.CTkLabel(self.about_us_frame, text = "", image = self.about_us_image, fg_color="transparent")
            self.image_label.place(x = 220, y = 40)

            self.more_info_button = ctk.CTkButton(self.about_us_frame, width = 299, height= 35, text = f"{button_text} ➡️",font = ("Consolas", 18), fg_color=f"{button_color}", text_color="white", hover="disabled", corner_radius=0, cursor = "hand2", command = lambda : open_new_frame(page = page_name))
            self.more_info_button.place(x = 0, y = 116)

            self.about_us_frame.place(x= x, y = y)

        #==========pages=============3
        def about_us():
            about_us_frame = ctk.CTkFrame(self.guideline_frame, fg_color="#DCF2F1", corner_radius=0, border_width=2, border_color="black", width = 670, height = 600)

            with open(f"text/about_us.txt", "r") as about_file:
                content = about_file.read()
                wrapped_content = textwrap.fill(text=content, width=50)
                # print(wrapped_content)

            self.about_label = ctk.CTkLabel(about_us_frame, text = "About Us", width = 670, height = 45, font = ("Consolas",25), text_color="white", fg_color="red", anchor = "center")
            self.about_label.place(x = 0, y = 0)

            self.cancel_button = ctk.CTkButton(about_us_frame, text = "X", font = ("Consolas", 25), fg_color="red", text_color="white", hover="disabled", bg_color="red", width = 0, height = 0 , command=lambda : about_us_frame.destroy())
            self.cancel_button.place(x = 600, y = 5)

            #=======text label==========#
            text = ctk.CTkLabel(about_us_frame, text = f"{wrapped_content}",font = ("Consolas",18), text_color="black", anchor="w")
            text.place(x = 120, y = 50)

            about_us_frame.place(x = 0, y = 0)

        #===========discipline_page===========#
        def discipline():
            discipline_frame = ctk.CTkFrame(self.guideline_frame, fg_color="#DCF2F1", corner_radius=0, border_width=2, border_color="black", width = 670, height = 600)

            with open(f"text/discipine.txt", "r") as about_file:
                content = about_file.read()
                wrapped_content = textwrap.fill(text=content, width=50)
                # print(wrapped_content)

            self.discipline_label = ctk.CTkLabel(discipline_frame, text = "Discipline", width = 750, height = 45, font = ("Consolas",25), text_color="white", fg_color="red", anchor = "center")
            self.discipline_label.place(x = 0, y = 0)

            self.cancel_button = ctk.CTkButton(discipline_frame, text = "X", font = ("Consolas", 25), fg_color="red", text_color="white", hover="disabled", bg_color="red", width = 0, height = 0 , command=lambda : discipline_frame.destroy())
            self.cancel_button.place(x = 600, y = 5)

            #=======text label==========#
            text = ctk.CTkLabel(discipline_frame, text = f"{wrapped_content}",font = ("Consolas",18), text_color="black", anchor="w")
            text.place(x = 120, y = 50)

            discipline_frame.place(x = 0, y = 0)

        #===========about us frame===========#
        display_frame(parent = self.guideline_frame,frame_color="#135D66",title="About Us", image_relative_path="image/about us icon.png",button_text="More Info",button_color="#2D9596", page_name=about_us, x = 20, y = 10)

        #===========discipline frame===========#
        display_frame(parent = self.guideline_frame, frame_color="#388E3C", title="General Rules\n(Discipline)", image_relative_path="image/discipline.png", button_text="More Info",button_color="#217756", page_name=discipline, x = 350, y = 10)

        #===========absence frame===========#
        display_frame(parent = self.guideline_frame, frame_color="#FF204E", title="General Rules\n(Attendance)", image_relative_path="image/present.png", button_text="More Info",button_color="#D80032", page_name=None, x = 20, y = 180)

        #===========fee rules frame===========#
        display_frame(parent = self.guideline_frame, frame_color="#FEB139", title="General Rules\n(Fee Rules)", image_relative_path="image/fees.png", button_text="More Info",button_color="#F2921D", page_name=None, x = 350, y = 180)

        #===========examination frame===========#
        display_frame(parent = self.guideline_frame, frame_color="#A61F69", title="General Rules\n(Examinations)", image_relative_path="image/exam.png", button_text="More Info",button_color="#810955", page_name=None, x = 20, y = 350)

        #===========uniform frame===========#
        display_frame(parent = self.guideline_frame, frame_color="#9A3B3B", title="General Rules\n(Uniform & Shoes)", image_relative_path="image/uniform.png", button_text="More Info",button_color="#7C0A02", page_name=None, x = 350, y = 350)

        self.guideline_frame.place(x = 350, y = 200)
        #========rules and regulation window==========#

class ContactUsWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="white")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        #======calling heading label class =======#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        self.contact_label = ctk.CTkLabel(self, text = "Connect With Us", width = 670, height =45, font = ("Consolas",25), text_color="white", fg_color="red", anchor = "center")
        self.contact_label.place(x = 350, y = 100)

        self.contact_label = tk.Label(self,bg="black")
        self.contact_label.place(x = 438, y = 180, width = 836, height=4)

        #=======create a frame=========#
        self.contact_frame = ctk.CTkFrame(self, width = 670, height = 620, fg_color="white", corner_radius=2, border_width=2, border_color="green")

        def image_label(image_path, label, image_y, label_y):
            self.contact_us_image = ctk.CTkImage(light_image=Image.open(f"{image_path}"), dark_image=Image.open(f"{image_path}"), size = (40, 40))
                
            self.image_label = ctk.CTkLabel(self.contact_frame, text = "", image = self.contact_us_image, fg_color="transparent")
            self.image_label.place(x = 20, y = image_y)

            #========label===========#
            self.label = ctk.CTkLabel(self.contact_frame, text = label, font = ("Consolas", 17), anchor="w")
            self.label.place(x = 80, y = label_y)
        
        #=========address icon===========#
        self.address_label = "Vivekanand Vidya Bhavan English High School, Aadarsh\n Society,Chembur, Mumbai 400071, India"
        image_label(image_path="image/address.png", label =self.address_label, image_y=43, label_y=45)

        #========contact icon=========#
        self.phone_label = "+91 9619148774 / 7021151536"
        image_label(image_path="image/phone.png", label =self.phone_label, image_y=103, label_y=107)

        #========mail icon=========#
        self.mail_label = "vvb.admin@gmail.com"
        image_label(image_path="image/email.png", label =self.mail_label, image_y=163, label_y=169)

        #===========map frame============#
        self.map_frame1 = tk.LabelFrame(self.contact_frame, width=670, height=370, highlightthickness=0)

        self.map_widget = tkintermapview.TkinterMapView(self.map_frame1, width = 850, height=480, corner_radius=0)

        #=========set cordinates=======#
        self.map_widget.set_position(19.0481, 72.8900, text = "Vivekanand Vidya Bhavan")

        #===========set zoom level===========#
        # self.map_widget.set_zoom(10)

        #=======set marker===============#
        self.map_widget.set_marker(19.0481, 72.8900, text = "Vivekanand Vidya Bhavan")

        self.map_widget.pack(fill = "both")

        self.map_frame1.place(x = 0, y = 290)

        self.contact_frame.place(x = 350, y = 190)
                
class AskAQuestionWindow(ctk.CTkToplevel):
    def __init__(self):
        super().__init__(fg_color="white")
        self.geometry("1536x864-10-7")
        self.title("School Management System")

        #========heading frame=================#
        self.heading_frame = HeadingFrame(self)
        self.heading_frame.place(x = 5, y = 5)

        #=======create a frame for asking a question=========#
        self.main_frame = ctk.CTkFrame(self, width = 700, height = 600, fg_color="#3c3c50", corner_radius=2, border_width=2, border_color="green")

        self.gif_frames = []
        self.frames_delay = 0

        '''def ready_gif():
            global gif_file, frames_delay
            gif_file = Image.open("image/animat_bus.gif")
            print(gif_file.n_frames)

            for r in range(0, gif_file.n_frames):
                gif_file.seek(r)     #save all frames
                self.gif_frames.append(gif_file.copy())         #save all frames in a list

            self.frames_delay = gif_file.info["duration"]    #saving frequncy (gif_file.info)
            play_gif()

        self.frames_count = 0
        def play_gif():

            #increment the frame
            self.frames_count += 1     

            if self.frames_count == gif_file.n_frames:
                self.frames_count = 0                   #reset frame start from 0

            #====ignore warnings===========#
            warnings.filterwarnings("ignore", category=UserWarning)
            
            #changes the frames
            current_frame = ImageTk.PhotoImage(self.gif_frames[self.frames_count])    

            self.gif_label.configure(image = current_frame)     #now play gif in label

            root.after(self.frames_delay, play_gif)'''

        def fetch_answer():
            start_time = time.perf_counter()
            user_query = self.prompt_box.get("1.0", tk.END)

            #===========answer scrollable frame=========#
            answer_frame = ctk.CTkScrollableFrame(self.main_frame, width = 490, height = 400, fg_color="black")
            answer_frame.place(x = 87, y = 140)

            #========URL============#
            url = "https://chatgpt-api8.p.rapidapi.com/"

            #========Fetch the content and answer the question=========#
            payload = [
            {
                "content": "Hello! I'm an AI assistant bot based on ChatGPT 3. How may I help you?",
                "role": "system"
            },
            {
                "content": f"{user_query}",
                "role": "user"
            }
            ]
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "3b7d77ed76msh22d3ce03e1655e5p19e0a1jsn4f01b3ff110d",
                "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
            }

            #===========response from api=============#
            response = requests.post(url, json=payload, headers=headers)

            #==============check for successfull response===========#
            if response.status_code == 200:
                result = response.json()
                # query_answer = result["text"]
                print(f"API response time (seconds): {time.perf_counter() - start_time:.2f}")
            else:
                print(f"API error : {response.status_code}")
                
            # #======clear previous content in my frame===========#
            for widget in answer_frame.winfo_children():
                widget.destroy()

            #=========display the answer===========#
            my_label = ctk.CTkLabel(answer_frame, text = "", font = ("Consolas", 20),wraplength = 500, text_color="black", anchor = "nw")
            my_label.pack(padx = 10, pady = 10)

            self.prompt_box.delete("0.0", tk.END)

        #=======prompt entry box===========#
        self.search_image = ctk.CTkImage(light_image=Image.open("image/search_21743.png"), dark_image=Image.open("image/search_21743.png"), size = (64, 66))

        self.search_label = ctk.CTkLabel(self.main_frame, text = "", image = self.search_image, fg_color="transparent")
        self.search_label.place(x = 47, y = 12)

        self.prompt_box = ctk.CTkTextbox(self.main_frame, width =500, height=50, corner_radius=2, border_width=2, border_color="grey", font = ("Consolas", 20), border_spacing=10, activate_scrollbars=False)
        self.prompt_box.place(x = 100, y = 20)
    
        self.button_image = ctk.CTkImage(light_image=Image.open("image/playbutton_78507.png"), dark_image=Image.open("image/playbutton_78507.png"), size = (45, 45))
        self.enter_button = ctk.CTkButton(self.main_frame, width = 0, height= 0, text = "", image = self.button_image, fg_color="transparent", bg_color="transparent", hover="disabled", cursor = "hand2", command = fetch_answer)
        self.enter_button.place(x = 600, y = 18)

        self.gif_label = ctk.CTkLabel(self.main_frame, text = "")
        self.gif_label.place(x= 40, y = 150)

        # threading.Thread(target=ready_gif).start()
        # answer_func()
        self.main_frame.place(x = 300, y = 100)

if __name__== "__main__":
    root = App()
    root.home_page()  
    root.mainloop() 
