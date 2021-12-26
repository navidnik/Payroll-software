import tkinter as tk
from tkinter.constants import ANCHOR, CENTER, COMMAND, E, LEFT, N, NE, RIGHT, S, TRUE, X, Y
from PIL import Image,ImageTk
import sys
import os.path
import json

file = sys.argv[0]
foldername =os.path.dirname(file)

GreetFont = ("b nazanin", 17)
PresentFont = ("b nazanin", 25)
simpleFont = ("b nazanin", 12)

class Salary(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,*kwargs)
        tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self, "نرم افزار حقوق و دستمزد")
        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_columnconfigure(0,weight = 1)
        container.grid_rowconfigure(0, weight = 1)
        self.frames = {}
        for F in (StartPage,DefinitionPage,CamputingPage,PersonList,SalaryPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0 , column = 0 , sticky = 'nsew')
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        imageAdd = Image.open(foldername+"/BTNimages/defbtn.png")
        resizedImageAdd = imageAdd.resize((200,200))
        addPhoto = ImageTk.PhotoImage(resizedImageAdd)
        imageCam = Image.open(foldername+"/BTNimages/par.png")
        resizedImageCam = imageCam.resize((200,200))
        camPhoto = ImageTk.PhotoImage(resizedImageCam)
        imagePersons = Image.open(foldername+"/BTNimages/personslist.png")
        resizedImagePersons = imagePersons.resize((200,200))
        personsPhoto = ImageTk.PhotoImage(resizedImagePersons)
        salaryimage = Image.open(foldername+"/BTNimages/salarylist.png")
        resizedsalaryimage = salaryimage.resize((200,200))
        salaryphoto = ImageTk.PhotoImage(resizedsalaryimage)
        def onEnter(e):
            e.widget['background'] = "#fa9d8e"
        def onLeave(e):
            e.widget['background'] = '#7c3766'
        
        tk.Frame.__init__(self,parent)
        PresentLabel = tk.Label(self, text = 'نرم افزار محاسبه حقوق و دستمزد', font=PresentFont,bg='#8f9183',fg='#150f0f')
        developerLabel = tk.Label(self, text = 'طراحی و پیاده سازی توسط : نوید نیک یار', font=PresentFont,bg='#8f9183',fg='#fa9d8e')
        GreetingLabel = tk.Label(self, text = 'لطفا از گزینه های زیر یک مورد را انتخاب کنید', font=GreetFont,bg='#8f9183',fg='#150f0f')
        defBtn = tk.Button(self, text = 'تعریف پرسنل',bg='#7c3766', image=addPhoto,command = lambda: controller.show_frame(DefinitionPage))
        defBtn.image = addPhoto
        camBtn = tk.Button(self, text = 'محاسبه حقوق افراد',bg='#7c3766',image =camPhoto, command = lambda: controller.show_frame(CamputingPage))
        camBtn.image = camPhoto
        personsBtn = tk.Button(self,bg='#7c3766',image =personsPhoto, command = lambda: controller.show_frame(PersonList))
        personsBtn.image = personsPhoto
        salaryBtn = tk.Button(self, text = 'لیست حقوق ها',bg='#7c3766', image=salaryphoto,command = lambda: controller.show_frame(SalaryPage))
        salaryBtn.image = salaryphoto
        PresentLabel.grid(row = 0,column = 0 ,columnspan=5, pady = 20, padx=20)
        developerLabel.grid(row = 3,column = 0 ,columnspan=5, pady = 20, padx=20)
        GreetingLabel.grid(row = 1,column = 0 ,columnspan=5, pady = 20, padx=20)
        defBtn.grid(row = 2,column = 1 , pady = 20, padx=20)
        camBtn.grid(row = 2,column = 2 , pady = 20, padx=20)
        personsBtn.grid(row = 2, column = 3, padx = 20,pady = 20)
        salaryBtn.grid(row = 2, column = 4, padx = 20,pady = 20) 
        StartPage.config(self,bg='#8f9183')
        for i in range(7):
            self.grid_columnconfigure(i,weight = 1)
        defBtn.bind("<Enter>",onEnter)
        defBtn.bind("<Leave>",onLeave)
        camBtn.bind("<Enter>",onEnter)
        camBtn.bind("<Leave>",onLeave)
        personsBtn.bind("<Enter>",onEnter)
        personsBtn.bind("<Leave>",onLeave)
        salaryBtn.bind("<Enter>",onEnter)
        salaryBtn.bind("<Leave>",onLeave)

class SalaryPage(tk.Frame):

    def __init__(self,parent,controller):

        homeImg = Image.open(foldername+"/BTNimages/home.png")
        resizedhomeImg = homeImg.resize((50,50))
        homePhoto = ImageTk.PhotoImage(resizedhomeImg)

        tk.Frame.__init__(self,parent)
        mainLabel = tk.Label(self, text = 'لیست حقوق', font=PresentFont,bg='#8f9183',fg='#150f0f')
        numLabel = tk.Label(self, text = 'ردیف',font = simpleFont,bg='#8f9183',fg='#150f0f')
        nameLabel = tk.Label(self,text = ':نام',font = simpleFont,bg='#8f9183',fg='#150f0f')
        lnameLabel = tk.Label(self,text = ':نام خانوادگی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        pcodeLabel = tk.Label(self,text = ':کد پرسنلی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        kindLabel = tk.Label(self,text = ':نوع قرارداد',font = simpleFont,bg='#8f9183',fg='#150f0f')
        hsalaryLabel = tk.Label(self,text = ':ساعت کارکرد',font = simpleFont,bg='#8f9183',fg='#150f0f')
        msalaryLabel = tk.Label(self,text = ':حقوق پایه ',font = simpleFont,bg='#8f9183',fg='#150f0f')
        bonsalaryLabel = tk.Label(self,text = ':مزایا و بن ',font = simpleFont,bg='#8f9183',fg='#150f0f')
        misalaryLabel = tk.Label(self,text = ':کسری ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        asalaryLabel = tk.Label(self,text = ':اضافه ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        monthLabel = tk.Label(self,text = ':ماه',font = simpleFont,bg='#8f9183',fg='#150f0f')
        salaryLabel = tk.Label(self,text = ':مبلغ حقوق',font = simpleFont,bg='#8f9183',fg='#150f0f')
        homeBtn = tk.Button(self, text = 'خانه',bg='#7c3766',image = homePhoto, fg='#150f0f', command = lambda: controller.show_frame(StartPage))
        homeBtn.image = homePhoto
        homeBtn.grid(row = 1, column = 11)
        mainLabel.grid(row = 0, column = 0, columnspan = 12)
        numLabel.grid(row = 2,column=11,padx = 10, pady=10)
        nameLabel.grid(row = 2, column = 10, padx=10,pady=10)
        lnameLabel.grid(row = 2, column = 9, padx=10,pady=10)
        pcodeLabel.grid(row = 2, column = 8, padx=10,pady=10)
        kindLabel.grid(row = 2, column = 7, padx=10,pady=10)
        hsalaryLabel.grid(row = 2, column = 6, padx=10,pady=10)
        msalaryLabel.grid(row = 2, column = 5, padx=10,pady=10)
        bonsalaryLabel.grid(row = 2, column = 4, padx=10,pady=10)
        misalaryLabel.grid(row = 2, column =3 , padx=10,pady=10)
        asalaryLabel.grid(row = 2, column =2 , padx=10,pady=10)
        monthLabel.grid(row = 2, column =1 , padx=10,pady=10)
        salaryLabel.grid(row = 2, column =0 , padx=10,pady=10)

        with open(foldername+"/data.json","r") as f:
            data = json.load(f)
            peoples = data["Salary"]

        for i in range(len(peoples)):
            numValueLabel = tk.Label(self, text = i+1,font = simpleFont,bg='#8f9183',fg='#150f0f')
            numValueLabel.grid(row = i+3 , column=11, padx=10, pady=10)
            nameValueLabel = tk.Label(self,text = peoples[i]["Fname"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            nameValueLabel.grid(row = i+3 , column = 10, padx=10,pady=10)
            lnameValueLabel = tk.Label(self,text = peoples[i]["Lname"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            lnameValueLabel.grid(row = i+3, column = 9, padx=10,pady=10)
            pcodeValueLabel = tk.Label(self,text = peoples[i]["Pcode"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            pcodeValueLabel.grid(row = i+3, column = 8, padx=10,pady=10)
            kindValueLabel = tk.Label(self,text = peoples[i]["Type"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            kindValueLabel.grid(row = i+3, column = 7, padx=10,pady=10)
            hsalaryValueLabel = tk.Label(self,text = peoples[i]["Hsalary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            hsalaryValueLabel.grid(row = i+3, column = 6 , padx=10,pady=10)
            msalaryValueLabel = tk.Label(self,text = peoples[i]["Msalary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            msalaryValueLabel.grid(row = i+3, column = 5 , padx=10,pady=10)
            bonsalaryValueLabel = tk.Label(self,text = peoples[i]["Bonus"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            bonsalaryValueLabel.grid(row = i+3, column = 4 , padx=10,pady=10)
            misalaryValueLabel = tk.Label(self,text = peoples[i]["Misalary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            misalaryValueLabel.grid(row = i+3, column = 3 , padx=10,pady=10)
            asalaryValueLabel = tk.Label(self,text = peoples[i]["Asalary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            asalaryValueLabel.grid(row = i+3,column = 2,padx = 20, pady = 20)
            monthValueLabel = tk.Label(self,text = peoples[i]["Month"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            monthValueLabel.grid(row = i+3,column = 1,padx = 20, pady = 20)
            salaryValueLabel = tk.Label(self,text = peoples[i]["Salary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            salaryValueLabel.grid(row = i+3,column = 0,padx = 20, pady = 20)

        PersonList.config(self,bg='#8f9183')

        for i in range(15):
            self.grid_columnconfigure(i,weight = 1)

class PersonList(tk.Frame):
    def __init__(self,parent,controller):

        homeImg = Image.open(foldername+"/BTNimages/home.png")
        resizedhomeImg = homeImg.resize((50,50))
        homePhoto = ImageTk.PhotoImage(resizedhomeImg)

        tk.Frame.__init__(self,parent)
        mainLabel = tk.Label(self, text = 'لیست افراد', font=PresentFont,bg='#8f9183',fg='#150f0f')
        numLabel = tk.Label(self, text = 'ردیف',font = simpleFont,bg='#8f9183',fg='#150f0f')
        nameLabel = tk.Label(self,text = ':نام',font = simpleFont,bg='#8f9183',fg='#150f0f')
        lnameLabel = tk.Label(self,text = ':نام خانوادگی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        mcodeLabel = tk.Label(self,text = ':کد ملی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        pcodeLabel = tk.Label(self,text = ':کد پرسنلی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        eduLabel = tk.Label(self,text = ':مدرک تحصیلی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        telLabel = tk.Label(self,text = ':تلفن ثابت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        mobLabel = tk.Label(self,text = ':تلفن همراه',font = simpleFont,bg='#8f9183',fg='#150f0f')
        addLabel = tk.Label(self,text = ':آدرس',font = simpleFont,bg='#8f9183',fg='#150f0f')
        kindLabel = tk.Label(self,text = ':نوع قرارداد',font = simpleFont,bg='#8f9183',fg='#150f0f')
        hsalaryLabel = tk.Label(self,text = ':حقوق هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        msalaryLabel = tk.Label(self,text = ':حقوق پایه ',font = simpleFont,bg='#8f9183',fg='#150f0f')
        bonsalaryLabel = tk.Label(self,text = ':مزایا و بن ',font = simpleFont,bg='#8f9183',fg='#150f0f')
        misalaryLabel = tk.Label(self,text = ':کسر هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        asalaryLabel = tk.Label(self,text = ':اضافه هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        homeBtn = tk.Button(self, text = 'خانه',bg='#7c3766',image = homePhoto, fg='#150f0f', command = lambda: controller.show_frame(StartPage))
        homeBtn.image = homePhoto
        homeBtn.grid(row = 1, column = 14, columnspan = 15)
        mainLabel.grid(row = 0, column = 0, columnspan = 15)
        numLabel.grid(row = 2,column=14,padx = 10, pady=10)
        nameLabel.grid(row = 2, column = 13, padx=10,pady=10)
        lnameLabel.grid(row = 2, column = 12, padx=10,pady=10)
        mcodeLabel.grid(row = 2, column = 11, padx=10,pady=10)
        pcodeLabel.grid(row = 2, column = 10, padx=10,pady=10)
        eduLabel.grid(row = 2, column = 9, padx=10,pady=10)
        telLabel.grid(row = 2, column = 8, padx=10,pady=10)
        mobLabel.grid(row = 2, column = 7, padx=10,pady=10)
        addLabel.grid(row = 2, column = 6, padx=10,pady=10)
        kindLabel.grid(row = 2, column = 5, padx=10,pady=10)
        hsalaryLabel.grid(row = 2, column = 4, padx=10,pady=10)
        msalaryLabel.grid(row = 2, column = 3, padx=10,pady=10)
        bonsalaryLabel.grid(row = 2, column = 2, padx=10,pady=10)
        misalaryLabel.grid(row = 2, column =1 , padx=10,pady=10)
        asalaryLabel.grid(row = 2, column =0 , padx=10,pady=10)

        with open(foldername+"/data.json","r") as f:
            data = json.load(f)
            peoples = data["people"]
            
        for i in range(len(peoples)):
            numValueLabel = tk.Label(self, text = i+1,font = simpleFont,bg='#8f9183',fg='#150f0f')
            numValueLabel.grid(row = i+3 , column=14, padx=10, pady=10)
            nameValueLabel = tk.Label(self,text = peoples[i]["Fname"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            nameValueLabel.grid(row = i+3 , column = 13, padx=10,pady=10)
            lnameValueLabel = tk.Label(self,text = peoples[i]["Lname"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            lnameValueLabel.grid(row = i+3, column = 12, padx=10,pady=10)
            mcodeValueLabel = tk.Label(self,text = peoples[i]["Mcode"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            mcodeValueLabel.grid(row = i+3, column = 11, padx=10,pady=10)
            pcodeValueLabel = tk.Label(self,text = peoples[i]["Pcode"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            pcodeValueLabel.grid(row = i+3, column = 10, padx=10,pady=10)
            eduValueLabel = tk.Label(self,text = peoples[i]["Education"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            eduValueLabel.grid(row = i+3, column = 9, padx=10,pady=10)
            telValueLabel = tk.Label(self,text = peoples[i]["Tel"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            telValueLabel.grid(row = i+3, column = 8, padx=10,pady=10)
            mobValueLabel = tk.Label(self,text = peoples[i]["Mobile"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            mobValueLabel.grid(row = i+3, column = 7, padx=10,pady=10)
            addValueLabel = tk.Label(self,text = peoples[i]["Address"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            addValueLabel.grid(row = i+3, column = 6, padx=10,pady=10)
            kindValueLabel = tk.Label(self,text = peoples[i]["Type"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            kindValueLabel.grid(row = i+3, column = 5, padx=10,pady=10)
            hsalaryValueLabel = tk.Label(self,text = peoples[i]["Hsalary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            hsalaryValueLabel.grid(row = i+3, column = 4 , padx=10,pady=10)
            msalaryValueLabel = tk.Label(self,text = peoples[i]["Msalary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            msalaryValueLabel.grid(row = i+3, column = 3 , padx=10,pady=10)
            bonsalaryValueLabel = tk.Label(self,text = peoples[i]["Bonus"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            bonsalaryValueLabel.grid(row = i+3, column = 2 , padx=10,pady=10)
            misalaryValueLabel = tk.Label(self,text = peoples[i]["Misalary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            misalaryValueLabel.grid(row = i+3, column = 1 , padx=10,pady=10)
            asalaryValueLabel = tk.Label(self,text = peoples[i]["Asalary"],font = simpleFont,bg='#8f9183',fg='#150f0f')
            asalaryValueLabel.grid(row = i+3,column = 0,padx = 20, pady = 20)

        PersonList.config(self,bg='#8f9183')

        for i in range(15):
            self.grid_columnconfigure(i,weight = 1)

class DefinitionPage(tk.Frame):
    def __init__(self,parent,controller):

        def onEnter(e):
            e.widget['background'] = "#fa9d8e"
        def onLeave(e):
            e.widget['background'] = '#7c3766'

        class Person:

            def __init__(self,Fname,Lname,Mcode,Pcode,Education,Tel,Mobile,Address,Type,Hsalary,Msalary,Bonus,MiSalary,Asalary):
                self.Fname = Fname
                self.Lname = Lname
                self.Mcode = Mcode
                self.Pcode = Pcode
                self.Education = Education
                self.Tel = Tel
                self.Mobile = Mobile
                self.Address = Address
                self.Type = Type
                self.Hsalary = Hsalary
                self.Msalary = Msalary
                self.Bonus = Bonus
                self.Misalary = MiSalary
                self.Asalary = Asalary

            def savePerson(self,filename):
                person_Dict = {"Fname":self.Fname,"Lname":self.Lname,"Mcode":self.Mcode,"Pcode":self.Pcode,"Education":self.Education,
                               "Tel":self.Tel,"Mobile":self.Mobile,"Address":self.Address,"Type":self.Type,"Hsalary":self.Hsalary,
                               "Msalary": self.Msalary,"Bonus":self.Bonus,"Misalary":self.Misalary,"Asalary":self.Asalary}
                with open(filename,"r") as f:
                    data = json.load(f)
                data["people"].append(person_Dict)
                with open(filename,"w") as f:
                    json.dump(data,f,indent = 2)

        def kinda():
            s = kind.get()
            if s == 'ساعتی':
                hsalaryLabel.grid(row = 5, column = 7 , padx=10,pady=10)
                hsalaryEntry.grid(row = 5, column = 6 , padx=10,pady=10)
                submitBtn.grid(row = 7, column = 5, padx=10, pady=10)
                msalaryEntry.grid_remove()
                msalaryEntry.insert(0,"ندارد")
                msalaryLabel.grid_remove()
                bonsalaryLabel.grid_remove()
                bonsalaryEntry.insert(0,"ندارد")
                bonsalaryEntry.grid_remove()
                hsalaryEntry.delete(0,"end")
            elif s == 'ماهانه':
                hsalaryLabel.grid_remove()
                hsalaryEntry.grid_remove()
                hsalaryEntry.insert(0,"ندارد")
                msalaryEntry.delete(0,"end")
                bonsalaryEntry.delete(0,"end")
                msalaryLabel.grid(row = 5, column = 7 , padx=10,pady=10)
                msalaryEntry.grid(row = 5, column = 6 , padx=10,pady=10)
                bonsalaryLabel.grid(row = 5, column = 5 , padx=10,pady=10)
                bonsalaryEntry.grid(row = 5, column = 4 , padx=10,pady=10)
                submitBtn.grid(row = 7, column = 5, padx=10, pady=10)

        def submit():
            if nameEntry.get() == "" or lnameEntry.get() == "" or hsalaryEntry.get() == "" or msalaryEntry.get()=="" or bonsalaryEntry.get() == "" or misalaryEntry.get() == "" or asalaryEntry.get() == "" :
                errorLabel.grid(row = 7, column = 0,columnspan=8 ,pady=10,padx= 10,)
            else:
                person = Person(nameEntry.get(),lnameEntry.get(),mcodeEntry.get(),pcodeEntry.get(),eduEntry.get(),telEntry.get(),
                                mobEntry.get(),addEntry.get(),kind.get(),hsalaryEntry.get(),msalaryEntry.get(),bonsalaryEntry.get(),
                                misalaryEntry.get(),asalaryEntry.get())
                person.savePerson(foldername+"/data.json")
                errorLabel.config(text = "کارمند با موفقیت ذخیره شد")
                errorLabel.grid(row = 7, column = 0,columnspan=8 ,pady=10,padx= 10,) 
                nameEntry.delete(0,"end")
                lnameEntry.delete(0,"end")
                mcodeEntry.delete(0,"end")
                pcodeEntry.delete(0,"end")
                eduEntry.delete(0,"end")
                telEntry.delete(0,"end")
                mobEntry.delete(0,"end")
                addEntry.delete(0,"end")
                misalaryEntry.delete(0,"end")
                hsalaryEntry.delete(0,"end")
                msalaryEntry.delete(0,"end")
                asalaryEntry.delete(0,"end")
                bonsalaryEntry.delete(0,"end")
                
        kind = tk.StringVar()
        tk.Frame.__init__(self,parent)
        imageSub = Image.open(foldername+"/BTNimages/submit.png")
        resizedImageSub = imageSub.resize((50,50))
        subPhoto = ImageTk.PhotoImage(resizedImageSub)
        homeImg = Image.open(foldername+"/BTNimages/home.png")
        resizedhomeImg = homeImg.resize((50,50))
        homePhoto = ImageTk.PhotoImage(resizedhomeImg)
        errorLabel = tk.Label(self, text = '.لطفا موارد ستاره دار را کامل کنید', font = PresentFont,bg='#8f9183',fg='#150f0f')
        titleLabel = tk.Label(self, text = 'تعریف پرسنل', font = PresentFont,bg='#8f9183',fg='#150f0f')
        nameLabel = tk.Label(self,text = ':*نام',font = simpleFont,bg='#8f9183',fg='#150f0f')
        lnameLabel = tk.Label(self,text = ':*نام خانوادگی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        mcodeLabel = tk.Label(self,text = ':کد ملی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        pcodeLabel = tk.Label(self,text = ':کد پرسنلی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        eduLabel = tk.Label(self,text = ':مدرک تحصیلی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        telLabel = tk.Label(self,text = ':تلفن ثابت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        mobLabel = tk.Label(self,text = ':تلفن همراه',font = simpleFont,bg='#8f9183',fg='#150f0f')
        addLabel = tk.Label(self,text = ':آدرس',font = simpleFont,bg='#8f9183',fg='#150f0f')
        kindLabel = tk.Label(self,text = ':نوع قرارداد',font = simpleFont,bg='#8f9183',fg='#150f0f')
        hsalaryLabel = tk.Label(self,text = ':*حقوق هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        msalaryLabel = tk.Label(self,text = ':*حقوق پایه ',font = simpleFont,bg='#8f9183',fg='#150f0f')
        bonsalaryLabel = tk.Label(self,text = ':*مزایا و بن ',font = simpleFont,bg='#8f9183',fg='#150f0f')
        misalaryLabel = tk.Label(self,text = ':*کسر هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        asalaryLabel = tk.Label(self,text = ':*اضافه هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        nameEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        lnameEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        mcodeEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        pcodeEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        eduEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        telEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        mobEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        addEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        misalaryEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        hsalaryEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        msalaryEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        asalaryEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        bonsalaryEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        hourRadio = tk.Radiobutton(self, text='ساعتی', pady=10, variable=kind,value='ساعتی',bg='#8f9183', command=kinda)
        monthRadio = tk.Radiobutton(self, text='ماهانه', pady=10, variable=kind,value='ماهانه',bg='#8f9183', command=kinda)
        submitBtn = tk.Button(self, text = 'ثبت',bg='#7c3766',image = subPhoto, fg='#150f0f', command=submit)
        homeBtn = tk.Button(self, text = 'خانه',bg='#7c3766',image = homePhoto, fg='#150f0f', command = lambda: controller.show_frame(StartPage))
        homeBtn.image = homePhoto
        submitBtn.image = subPhoto
        titleLabel.grid(row = 0, column = 0,columnspan=8 ,pady=10,padx= 10,)
        nameLabel.grid(row = 2, column = 7, padx=10,pady=10)
        nameEntry.grid(row = 2, column = 6, padx=10,pady=10)
        lnameLabel.grid(row = 2, column = 5, padx=10,pady=10)
        lnameEntry.grid(row = 2, column = 4, padx=10,pady=10)
        mcodeLabel.grid(row = 2, column = 3, padx=10,pady=10)
        mcodeEntry.grid(row = 2, column = 2, padx=10,pady=10)
        pcodeLabel.grid(row = 2, column = 1, padx=10,pady=10)
        pcodeEntry.grid(row = 2, column = 0, padx=10,pady=10)
        eduLabel.grid(row = 3, column = 7, padx=10,pady=10)
        eduEntry.grid(row = 3, column = 6, padx=10,pady=10)
        telLabel.grid(row = 3, column = 5, padx=10,pady=10)
        telEntry.grid(row = 3, column = 4, padx=10,pady=10)
        mobLabel.grid(row = 3, column = 3, padx=10,pady=10)
        mobEntry.grid(row = 3, column = 2, padx=10,pady=10)
        addLabel.grid(row = 3, column = 1, padx=10,pady=10)
        addEntry.grid(row = 3, column = 0, padx=10,pady=10)
        kindLabel.grid(row = 4, column = 7, padx=10,pady=10)
        hourRadio.grid(row = 4, column = 6, padx=10,pady=10)
        monthRadio.grid(row = 4, column = 5, padx=10, columnspan=2)
        misalaryLabel.grid(row = 6, column =7 , padx=10,pady=10)
        misalaryEntry.grid(row = 6, column = 6 , padx=10,pady=10)
        asalaryLabel.grid(row = 6, column =5 , padx=10,pady=10)
        asalaryEntry.grid(row = 6, column = 4 , padx=10,pady=10)
        homeBtn.grid(row = 7, column = 6, padx=10, pady=10)
        for i in range(8):
            self.grid_columnconfigure(i,weight = 1)

        DefinitionPage.config(self,bg='#8f9183')

        submitBtn.bind("<Enter>",onEnter)
        submitBtn.bind("<Leave>",onLeave)
        homeBtn.bind("<Enter>",onEnter)
        homeBtn.bind("<Leave>",onLeave)

class CamputingPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        def onEnter(e):
            e.widget['background'] = "#fa9d8e"
        def onLeave(e):
            e.widget['background'] = '#7c3766'

        camImg = Image.open(foldername+"/BTNimages/par.png")
        resizedcamImg = camImg.resize((50,50))
        camPhoto = ImageTk.PhotoImage(resizedcamImg)

        homeImg = Image.open(foldername+"/BTNimages/home.png")
        resizedhomeImg = homeImg.resize((50,50))
        homePhoto = ImageTk.PhotoImage(resizedhomeImg)

        searchImg = Image.open(foldername+"/BTNimages/search.png")
        resizedsearchImg = searchImg.resize((25,25))
        searchPhoto = ImageTk.PhotoImage(resizedsearchImg)

        saveImg = Image.open(foldername+"/BTNimages/save.png")
        resizedsaveImg = saveImg.resize((25,25))
        savePhoto = ImageTk.PhotoImage(resizedsaveImg)

        

        class Salary:
            def __init__(self,Fname,Lname,Pcode,Type,Hsalary,Msalary,Bonus,MiSalary,Asalary,Month,Salary):
                self.Fname = Fname
                self.Lname = Lname
                self.Pcode = Pcode
                self.Type = Type
                self.Hsalary = Hsalary
                self.Msalary = Msalary
                self.Bonus = Bonus
                self.Misalary = MiSalary
                self.Asalary = Asalary
                self.Month = Month
                self.Salary = Salary

            def saveSalary(self,filename):
                person_Dict = {"Fname":self.Fname,"Lname":self.Lname,"Pcode":self.Pcode,"Type":self.Type,"Hsalary":self.Hsalary,
                               "Msalary": self.Msalary,"Bonus":self.Bonus,"Misalary":self.Misalary,"Asalary":self.Asalary,
                               "Month":self.Month,"Salary":self.Salary}
                with open(filename,"r") as f:
                    data = json.load(f)
                    data["Salary"].append(person_Dict)
                with open(filename,"w") as f:
                    json.dump(data,f,indent = 2)

        def search():
            with open(foldername+"/data.json","r") as f:
                data = json.load(f)
                peoples = data["people"]
            for i in range(len(peoples)):
                if peoples[i]["Pcode"] == cSearchEntry.get():
                    x = i
                    break
            def submit():
                salary = Salary(peoples[x]["Fname"],peoples[x]["Lname"],peoples[x]["Pcode"],peoples[x]["Type"],campHourEntry.get(),
                                peoples[x]["Msalary"],peoples[x]["Bonus"],miHourEntry.get(),addHourEntry.get(),kind.get(),
                                campute())
                salary.saveSalary(foldername+"/data.json")
                campHourEntry.delete(0,"end")
                miHourEntry.delete(0,"end")
                addHourEntry.delete(0,"end")

            def campute():
                errorSalaryLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
                errorSalaryLabel.grid(row = 11, column = 3,columnspan=2, padx = 10, pady = 10)
                camputedSalaryLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
                camputedSalaryLabel.grid(row = 11, column = 6, padx = 10, pady = 10)
                if peoples[x]["Type"] == "ساعتی":
                    try:
                        camputed = (int(peoples[x]["Hsalary"])*eval(campHourEntry.get()))+(int(peoples[x]["Asalary"])*eval(addHourEntry.get()))-(int(peoples[x]["Misalary"])*eval(miHourEntry.get()))
                        saveBtn.grid(row = 10, column = 0,rowspan = 3, columnspan = 2, padx = 10, pady = 10)
                        camputedSalaryLabel.config(text = camputed)
                        return camputed
                    except:                        
                        errorSalaryLabel.config(text = "لطفا همه مقادیر را وارد کنید")     
                elif peoples[x]["Type"] == "ماهانه":
                    campHourEntry.insert(0,"ندارد")
                    try:
                        camputed = (int(peoples[x]["Msalary"]))+(int(peoples[x]["Asalary"])*eval(addHourEntry.get()))-(int(peoples[x]["Misalary"])*eval(miHourEntry.get()))
                        camputedSalaryLabel.config(text = camputed)
                        saveBtn.grid(row = 10, column = 0,rowspan = 3, columnspan = 2, padx = 10, pady = 10)
                        return camputed
                    except:
                        errorSalaryLabel.config(text = "لطفا همه مقادیر را وارد کنید")
                        
            
            nameLabel.grid(row = 4, column = 7, padx=10,pady=10)
            nameValueLabel.config(text=peoples[x]["Fname"])
            nameValueLabel.grid(row = 4, column = 6, padx=10,pady=10)
            lnameLabel.grid(row = 4, column = 5, padx=10,pady=10)
            lnameValueLabel.config(text=peoples[x]["Lname"])
            lnameValueLabel.grid(row = 4, column = 4, padx=10,pady=10)
            mcodeLabel.grid(row = 4, column = 3, padx=10,pady=10)
            mcodeValueLabel.config(text = peoples[x]["Mcode"])
            mcodeValueLabel.grid(row = 4, column = 2, padx=10,pady=10)
            pcodeLabel.grid(row = 4, column = 1, padx=10,pady=10)
            pcodeValueLabel.config(text=peoples[x]["Pcode"])
            pcodeValueLabel.grid(row = 4, column = 0, padx=10,pady=10)
            eduLabel.grid(row = 5, column = 7, padx=10,pady=10)
            eduValueLabel.config(text=peoples[x]["Education"])
            eduValueLabel.grid(row = 5, column = 6, padx=10,pady=10)
            telLabel.grid(row = 5, column = 5, padx=10,pady=10)
            telValueLabel.config(text=peoples[x]["Tel"])
            telValueLabel.grid(row = 5, column = 4, padx=10,pady=10)
            mobLabel.grid(row = 5, column = 3, padx=10,pady=10)
            mobValueLabel.config(text=peoples[x]["Mobile"])
            mobValueLabel.grid(row = 5, column = 2, padx=10,pady=10)
            addLabel.grid(row = 5, column = 1, padx=10,pady=10)
            addValueLabel.config(text=peoples[x]["Address"])
            addValueLabel.grid(row = 5, column = 0, padx=10,pady=10)
            kindLabel.grid(row = 6, column = 7, padx=10,pady=10)
            kindValueLabel.config(text=peoples[x]["Type"])
            kindValueLabel.grid(row = 6, column = 6, padx=10,pady=10)
            misalaryLabel.grid(row = 6, column =5 , padx=10,pady=10)
            misalaryValueLabel.config(text = peoples[x]["Misalary"])
            misalaryValueLabel.grid(row = 6, column = 4 , padx=10,pady=10)
            asalaryLabel.grid(row = 6, column =3 , padx=10,pady=10)
            asalaryValueLabel.config(text = peoples[x]["Asalary"])
            asalaryValueLabel.grid(row = 6,column = 2,padx = 20, pady = 20)
            hsalaryLabel.grid(row = 6, column = 1 , padx=10,pady=10)
            hsalaryValueLabel.config(text = peoples[x]["Hsalary"])
            hsalaryValueLabel.grid(row = 6, column = 0 , padx=10,pady=10)
            msalaryLabel.grid(row = 7, column = 7 , padx=10,pady=10)
            msalaryValueLabel.config(text = peoples[x]["Msalary"])
            msalaryValueLabel.grid(row = 7, column = 6 , padx=10,pady=10)
            bonsalaryLabel.grid(row = 7, column = 5 , padx=10,pady=10)
            bonsalaryValueLabel.config(text = peoples[x]["Bonus"])
            bonsalaryValueLabel.grid(row = 7, column = 4 , padx=10,pady=10)
            kind = tk.StringVar()
            campHourLabel = tk.Label(self, text = 'ساعت کارکرد',font = simpleFont,bg='#8f9183',fg='#150f0f')
            campHourLabel.grid(row = 8 , column = 7, padx = 10, pady = 10)
            campHourEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
            campHourEntry.grid(row = 8, column = 6, padx=10,pady=10)
            miHourLabel = tk.Label(self, text = 'ساعت کسر',font = simpleFont,bg='#8f9183',fg='#150f0f')
            miHourLabel.grid(row = 8 , column = 5, padx = 10, pady = 10)
            miHourEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
            miHourEntry.grid(row = 8, column = 4, padx=10,pady=10)
            addHourLabel = tk.Label(self, text = 'ساعت اضافه',font = simpleFont,bg='#8f9183',fg='#150f0f')
            addHourLabel.grid(row = 8 , column = 3, padx = 10, pady = 10)
            addHourEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
            addHourEntry.grid(row = 8, column = 2, padx=10,pady=10)
            camBtn = tk.Button(self, text = 'محاسبه',bg='#7c3766',image=camPhoto, command=campute)
            camBtn.image = camPhoto
            saveBtn = tk.Button(self,text = 'ثبت',image= savePhoto,bg='#7c3766',command=submit)
            saveBtn.image = savePhoto
            camBtn.grid(row = 8, column = 0,rowspan = 3, columnspan = 2, padx = 10, pady = 10)
            farvardin = tk.Radiobutton(self, text='فروردین', pady=10, variable=kind,value='فروردین',bg='#8f9183')
            farvardin.grid(row = 9, column = 7 , padx = 1, pady = 10)
            ordibehesht = tk.Radiobutton(self, text='اردیبهشت', pady=10, variable=kind,value='اردیبهشت',bg='#8f9183')
            ordibehesht.grid(row = 9, column = 6 , padx = 1, pady = 10)
            khordad = tk.Radiobutton(self, text='خرداد', pady=10, variable=kind,value='خرداد',bg='#8f9183')
            khordad.grid(row = 9, column = 5 , padx = 1, pady = 10)
            tir = tk.Radiobutton(self, text='تیر', pady=10, variable=kind,value='تیر',bg='#8f9183')
            tir.grid(row = 9, column = 4 , padx = 1, pady = 10)
            mordad = tk.Radiobutton(self, text='مرداد', pady=10, variable=kind,value='مرداد',bg='#8f9183')
            mordad.grid(row = 9, column = 3 , padx = 1, pady = 10)
            shahrivar = tk.Radiobutton(self, text='شهریور', pady=10, variable=kind,value='شهریور',bg='#8f9183')
            shahrivar.grid(row = 9, column = 2 , padx = 1, pady = 10)
            mehr = tk.Radiobutton(self, text='مهر', pady=10, variable=kind,value='مهر',bg='#8f9183')
            mehr.grid(row = 10, column = 7 , padx = 1, pady = 10)
            aban = tk.Radiobutton(self, text='آبان', pady=10, variable=kind,value='آبان',bg='#8f9183')
            aban.grid(row = 10, column = 6 , padx = 1, pady = 10)
            azar = tk.Radiobutton(self, text='آذر', pady=10, variable=kind,value='آذر',bg='#8f9183')
            azar.grid(row = 10, column = 5 , padx = 1, pady = 10)
            dey = tk.Radiobutton(self, text='دی', pady=10, variable=kind,value='دی',bg='#8f9183')
            dey.grid(row = 10, column = 4 , padx = 1, pady = 10)
            bahman = tk.Radiobutton(self, text='بهمن', pady=10, variable=kind,value='بهمن',bg='#8f9183')
            bahman.grid(row = 10, column = 3 , padx = 1, pady = 10)
            esfand = tk.Radiobutton(self, text='اسفند', pady=10, variable=kind,value='اسفند',bg='#8f9183')
            esfand.grid(row = 10, column = 2 , padx = 1, pady = 10)
            camSalaryLabel = tk.Label(self, text = 'حقوق محاسبه شده',font = simpleFont,bg='#8f9183',fg='#150f0f')
            camSalaryLabel.grid(row = 11, column = 7, pady = 10, padx = 10)
            camBtn.bind("<Enter>",onEnter)
            camBtn.bind("<Leave>",onLeave)
            saveBtn.bind("<Enter>",onEnter)
            saveBtn.bind("<Leave>",onLeave)
        
        bonsalaryValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        msalaryValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        hsalaryValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        asalaryValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        misalaryValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        kindValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        addValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        mobValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        telValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        eduValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        pcodeValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        lnameValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        nameValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        mcodeValueLabel = tk.Label(self,font = simpleFont,bg='#8f9183',fg='#150f0f')
        titleLabel = tk.Label(self,text = 'محاسبه حقوق پرسنل', font = PresentFont,bg='#8f9183',fg='#150f0f')
        titleLabel.grid(row = 0,column = 0,columnspan=8, pady = 20,padx = 20)
        backBtn = tk.Button(self, text = 'بازگشت به صفحه اصلی',fg='#150f0f',bg='#7c3766',image = homePhoto, command = lambda: controller.show_frame(StartPage))
        backBtn.image = homePhoto
        backBtn.grid(row = 1, column = 7, pady=20, padx= 20)
        cSearchLabel = tk.Label(self, text = ': کد پرسنلی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        cSearchEntry = tk.Entry(self,fg='#150f0f',bg='#fa9d8e', font = simpleFont, justify=RIGHT)
        searchBtn = tk.Button(self, text ='جستجو',fg='#150f0f',image = searchPhoto,bg='#7c3766', command = search)
        searchBtn.image = searchPhoto
        nameLabel = tk.Label(self,text = ':نام',font = simpleFont,bg='#8f9183',fg='#150f0f')
        lnameLabel = tk.Label(self,text = ':نام خانوادگی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        mcodeLabel = tk.Label(self,text = ':کد ملی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        pcodeLabel = tk.Label(self,text = ':کد پرسنلی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        eduLabel = tk.Label(self,text = ':مدرک تحصیلی',font = simpleFont,bg='#8f9183',fg='#150f0f')
        telLabel = tk.Label(self,text = ':تلفن ثابت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        mobLabel = tk.Label(self,text = ':تلفن همراه',font = simpleFont,bg='#8f9183',fg='#150f0f')
        addLabel = tk.Label(self,text = ':آدرس',font = simpleFont,bg='#8f9183',fg='#150f0f')
        kindLabel = tk.Label(self,text = ':نوع قرارداد',font = simpleFont,bg='#8f9183',fg='#150f0f')
        hsalaryLabel = tk.Label(self,text = ':حقوق هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        msalaryLabel = tk.Label(self,text = ':حقوق پایه ',font = simpleFont,bg='#8f9183',fg='#150f0f')
        bonsalaryLabel = tk.Label(self,text = ':مزایا و بن ',font = simpleFont,bg='#8f9183',fg='#150f0f')
        misalaryLabel = tk.Label(self,text = ':کسر هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        asalaryLabel = tk.Label(self,text = ':اضافه هر ساعت',font = simpleFont,bg='#8f9183',fg='#150f0f')
        cSearchLabel.grid(row = 3, column = 7, padx = 20 , pady = 20)
        cSearchEntry.grid(row = 3 , column = 6, padx = 20 , pady = 20)
        searchBtn.grid(row = 3,column = 5,padx=20,pady=20)
        CamputingPage.config(self,bg='#8f9183')
        for i in range(8):
            self.grid_columnconfigure(i,weight = 1)

        backBtn.bind("<Enter>",onEnter)
        backBtn.bind("<Leave>",onLeave)
        searchBtn.bind("<Enter>",onEnter)
        searchBtn.bind("<Leave>",onLeave)
        

app = Salary()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.state('zoomed')
app.mainloop()
