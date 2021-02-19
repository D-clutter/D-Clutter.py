from tkinter import *
from PIL import Image,ImageTk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
#First window(interface)
top = Tk()
load=Image.open('D:\\app ic\\was1.jpg')
ren=ImageTk.PhotoImage(load)
img=Label(top,image=ren)
img.place(x=0,y=0)
top.iconbitmap(r'D:\\app ic\\appima.ico')
top.title("Waste Management")
load1=Image.open('D:\\app ic\\nobgapp13.png')
ren1=ImageTk.PhotoImage(load1)
img1=Label(top,image=ren1,bd=0)
img1.place(x=40,y=10)
la=Label(top,text="D-Clutter",font=('helvetica',50),bd=0)
la.place(x=120,y=10)
top.geometry("500x450")
aa=Label(top,text="Username :",font=('bold',20))
aa.place(x=100,y=100)
aa1=Label(top,text="Phone Number :",font=('bold',20))
aa1.place(x=100,y=160)
aa1=Label(top,text="Location :",font=('bold',20))
aa1.place(x=100,y=220)
aa2=Label(top,text="State, District",font=('bold',10))
aa2.place(x=360,y=230)
aa3=Label(top,text="House Details :",font=('bold',20))
aa3.place(x=100,y=280)
uv= StringVar()
pv= IntVar()
uv1= StringVar()
uv2=StringVar()
ue= Entry(top, textvariable=uv)
ue1= Entry(top, textvariable=uv1)
pe= Entry(top, textvariable=pv)
pee=Entry(top, textvariable=uv2)
ue.place(x=249,y=110)
pe.place(x=305,y=170)
ue1.place(x=230,y=230)
pee.place(x=300,y=290)
#Hindi window
def getv2():
    global ren1
    global ren123
    top3 = Toplevel(top)
    top3.iconbitmap(r'D:\\app ic\\appima.ico')
    top3.title("कचरा प्रबंधन")
    load1=Image.open('D:\\app ic\\was1.jpg')
    ren1=ImageTk.PhotoImage(load1)
    img12=Label(top3,image=ren1,bd=0)
    img12.place(x=0,y=0)
    la=Label(top3,text="D-clutter",font=('helvetica',50),bd=0)
    la.place(x=120,y=10)
    top3.geometry("500x450")
    aa=Label(top3,text="उपयोगकर्ता का नाम :",font=('bold',20))
    aa.place(x=100,y=100)
    aa1=Label(top3,text="फ़ोन नंबर :",font=('bold',20))
    aa1.place(x=100,y=160)
    aa1=Label(top3,text="स्थान :",font=('bold',20))
    aa1.place(x=100,y=220)
    aa2=Label(top3,text="राज्य, जिला",font=('bold',10))
    aa2.place(x=310,y=230)
    aa3=Label(top3,text="घर की जानकारी :",font=('bold',20))
    aa3.place(x=100,y=280)
    uv= StringVar()
    pv= IntVar()
    uv1= StringVar()
    uv2=StringVar()
    ue= Entry(top3, textvariable=uv)
    ue1= Entry(top3, textvariable=uv1)
    pe= Entry(top3, textvariable=pv)
    pee=Entry(top3, textvariable=uv2)
    ue.place(x=340,y=110)
    pe.place(x=225,y=170)
    ue1.place(x=180,y=230)
    pee.place(x=300,y=290)
    top.withdraw()
    load123=Image.open('D:\\app ic\\nobgapp13.png')
    ren123=ImageTk.PhotoImage(load123)
    img123=Label(top3,image=ren123,bd=0)
    img123.place(x=40,y=10)
    def getv5():
        top.deiconify()
        top3.destroy()
    gg3=Button(top3,text="पिछला  पेज",command=getv5)
    gg3.place(x=200,y=370)
    def getv4():
        top4=Toplevel(top)
        global ren3
        top4.iconbitmap(r'D:\\app ic\\appima.ico')
        top4.title("Form Filling")
        top4.geometry("1200x786")
        load2=Image.open('D:\\app ic\\wastes.jpg')
        ren3=ImageTk.PhotoImage(load2)
        img2=Label(top4,image=ren3)
        img2.place(x=0,y=0)
        ja=uv.get()
        jaa=pv.get()
        qp=Label(top4,text=f"Hello {ja}  welcome to D-clutter an app focused on reducing  \n waste all over India and thus reducing evironmental harms from improper treatment of such wastes \n Kindly fill informations asked below",font=(19))
        qp.place(x=200,y=50)
        a=Text(top4, width=120, height=70, font=("Arial bold",16))
        a.place(x=0,y=400)
        ala=Label(top4,text=f"Please briefly explain the problem regarding your waste below:-")
        ala.place(x=0,y=370)
        ala1=Label(top4,text=f"Select the type of waste your household normally produces:")
        ala1.place(x=50,y=180)
        def click1():
            print(i.get())
            print(i1.get())
            print(i2.get())
            print(i3.get())
            print(f"Your E-mail is {u3.get()}")
            print(f"Your Full Name is {u1.get()}")
            print(f"Amount of Waste you produce is {u2.get()}")
            print(a.get(1.0, END))
            file=open("details.txt",'a+')
            file.write("******************************************\n")
            are1=f"Full Name:   {u1.get()}\n"
            file.write(are1)
            are2=f"Amount of waste you daily produce:    {u2.get()}\n"
            file.write(are2)
            are3=f"E-mail:    {u3.get()}\n"
            file.write(are3)
            are4=f"Phone Number:    {pe.get()}\n"
            file.write(are4)
            are5=f"Location:   {ue1.get()}\n"
            file.write(are5)
            are8=f"House Details: {pee.get()}\n"
            file.write(are8)
            are6=f"Following is problem in brief :\n {a.get(1.0, END)}\n"
            file.write(are6)
            are7=f"Following is the type of waste that should be handled: \n{i.get()} \n{i1.get()}  \n{i2.get()}   \n{i3.get()} \n"
            file.write(are7)
            file.write("******************************************\n")
            file.close()
 
            #Information on E-mails to D-cluutter
 
            em_us="dclutterofficial@gmail.com"
            em_se="dclutterofficial@gmail.com"
            subj="Info regarding people using D-Clutter" 
 
            #mail format
 
            msg=MIMEMultipart()
            msg['From']=em_us
            msg['To']=em_se
            msg['Subject']=subj
 
            body='Hi there, sending this mail from D-Clutter'
            msg.attach(MIMEText(body,'plain'))
 
            filename='details.txt'
            attachment=open(filename,'rb')
 
            #attaching database
 
            part=MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header("Content Display","attachment; filename="+filename)
 
            #login in official D-Clutter mail
 
            msg.attach(part)
            text=msg.as_string()
            server= smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(em_us,'dclutter@7789')
 
            #sending mail using server
 
            server.sendmail(em_us,em_se,text)
            server.quit()
 
 
            #Information on E-mails to client
 
            em_us1="dclutterofficial@gmail.com"
            em_se1=f"{u3.get()}"
            subj1="Welcome to D-clutter!!!!!" 
 
            #mail format
 
            msg1=MIMEMultipart()
            msg1['From']=em_us1
            msg1['To']=em_se1
            msg1['Subject']=subj1
 
            body1='Thank you for believing in D-Clutter. We promise to always provide our clients with the excellent service that they deserve and would like to take this opportunity to thank you for your patronage.\n D-Clutter is grateful for the pleasure of serving you and hope we met your expectations.\n Looking forward to a cleaner and greener future. '
            msg1.attach(MIMEText(body1,'plain'))
 
 
            #login in official D-Clutter mail
 
            text7=msg1.as_string()
            server= smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(em_us1,'dclutter@7789')
 
            #sendind mail using server
 
            try:
                 server.sendmail(em_us1,em_se1,text7)
            except Exception as e:
                   top6=Toplevel(top)
                   top6.geometry("500x500")
                   q1=Label(top6,text="Invalid E-mail",font=('bold',30))
                   q1.place(x=100,y=150)
            server.quit()
 
        i=IntVar()
        i1=IntVar()
        i2=IntVar()
        i3=IntVar()       
        c=Checkbutton(top4, text="Vegetable peels and other organic stuff",variable=i,onvalue=1,offvalue=0)
        c1=Checkbutton(top4, text="Plastic and other inorganic stuff",variable=i1,onvalue=1,offvalue=0)
        c2=Checkbutton(top4, text="Electronic wastes",variable=i2,onvalue=1,offvalue=0)
        c3=Checkbutton(top4, text="Liquid waste",variable=i3,onvalue=1,offvalue=0)
        c.place(x=50,y=200)
        c1.place(x=50,y=225)
        c2.place(x=50,y=250)
        c3.place(x=50,y=275)
        butt1=Button(top4, text="Submit",command=click1)
        butt1.place(x=400,y=300)
        u1= StringVar()
        u2= IntVar()
        u3= StringVar()
        u1e= Entry(top4, textvariable=u1)
        u2e= Entry(top4, textvariable=u2)
        u3e= Entry(top4, textvariable=u3)
        u1e.place(x=700,y=200)
        u2e.place(x=700,y=250)
        u3e.place(x=700,y=300)
        ab=Label(top4,text="Full Name:")
        ab1=Label(top4,text="Amount of waste u daily produce:")
        ab2=Label(top4,text="Your E-mail:")
        ab.place(x=500,y=200)
        ab1.place(x=500,y=250)
        ab2.place(x=500,y=300)
    gg2=Button(top3,text="दर्ज करें",command=getv4)
    gg2.place(x=209,y=340)
Button(top,text="हिंदी",command=getv2).place(x=210,y=390)
#Form Filling
def getv():
    global ren2
    top1=Toplevel(top)
    top1.iconbitmap(r'D:\\app ic\\appima.ico')
    top1.title("Form Filling")
    top1.geometry("1200x786")
    load2=Image.open('D:\\app ic\\wastes.jpg')
    ren2=ImageTk.PhotoImage(load2)
    img2=Label(top1,image=ren2)
    img2.place(x=0,y=0)
    ja=uv.get()
    jaa=pv.get()
    if(jaa<=1000000000):
        la=Label(top1,text="Invalid Number",font=('helvetica',30))
        la.place(x=120,y=10)
    else:
        qp=Label(top1,text=f"Hello {ja}  welcome to D-clutter an app focused on reducing  \n waste all over India and thus reducing evironmental harms from improper treatment of such wastes \n Kindly fill informations asked below",font=(19))
        qp.place(x=200,y=50)
        a=Text(top1, width=120, height=70, font=("Arial bold",16))
        a.place(x=0,y=400)
        ala=Label(top1,text=f"Please briefly explain the problems regarding your waste below:-")
        ala.place(x=0,y=370)
        ala1=Label(top1,text=f"Select the type of waste your household normally produces:")
        ala1.place(x=50,y=180)
        def click1():
            print(i.get())
            print(i1.get())
            print(i2.get())
            print(i3.get())
            print(f"Your E-mail is {u3.get()}")
            print(f"Your Full Name is {u1.get()}")
            print(f"Amount of waste you produce is {u2.get()}")
            print(a.get(1.0, END))
            file=open("details.txt",'a+')
            file.write("******************************************\n")
            are1=f"Full Name:   {u1.get()}\n"
            file.write(are1)
            are2=f"Amount of waste you daily produce:    {u2.get()}\n"
            file.write(are2)
            are3=f"E-mail:    {u3.get()}\n"
            file.write(are3)
            are4=f"Phone Number:    {pe.get()}\n"
            file.write(are4)
            are5=f"Location:   {ue1.get()}\n"
            file.write(are5)
            are8=f"House Details: {pee.get()}\n"
            file.write(are8)
            are6=f"Following is the problem in brief :\n {a.get(1.0, END)}\n"
            file.write(are6)
            are7=f"Following is the type of waste that should be handled: \n{i.get()} \n{i1.get()}  \n{i2.get()}   \n{i3.get()} \n"
            file.write(are7)
            file.write("******************************************\n")
            file.close()
 
 
            #Information on E-mails to D-cluutter
 
            em_us="dclutterofficial@gmail.com"
            em_se="dclutterofficial@gmail.com"
            subj="Info regarding people using D-Clutter" 
 
            #mail format
 
            msg=MIMEMultipart()
            msg['From']=em_us
            msg['To']=em_se
            msg['Subject']=subj
 
            body='Hi there, sending this mail from D-Clutter'
            msg.attach(MIMEText(body,'plain'))
 
            filename='details.txt'
            attachment=open(filename,'rb')
 
            #attaching database
 
            part=MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header("Content Display","attachment; filename="+filename)
 
            #login in official D-Clutter mail
 
            msg.attach(part)
            text=msg.as_string()
            server= smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(em_us,'dclutter@7789')
 
            #sendind mail using server
 
            server.sendmail(em_us,em_se,text)
            server.quit()
 
 
 
 
 
            #Information on E-mails to client
 
            em_us1="dclutterofficial@gmail.com"
            em_se1=f"{u3.get()}"
            subj1="Welcome to D-clutter!!!!!" 
 
             #mail format
 
            msg1=MIMEMultipart()
            msg1['From']=em_us1
            msg1['To']=em_se1
            msg1['Subject']=subj1
 
            body1='Thank you for believing in D-Clutter. We promise to always provide our clients with the excellent service that they deserve and would like to take this opportunity to thank you for your patronage.\n D-Clutter is grateful for the pleasure of serving you and hope we met your expectations.\n Looking forward to a cleaner and greener future. '
            msg1.attach(MIMEText(body1,'plain'))
 
 
 
 
 
 
            #login in official D-Clutter mail
 
            text7=msg1.as_string()
            server= smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(em_us1,'dclutter@7789')
 
            #sending mail using server
            try:
                 server.sendmail(em_us1,em_se1,text7)
            except Exception as e:
                   top6=Toplevel(top)
                   top6.geometry("500x500")
                   q1=Label(top6,text="Invalid E-mail",font=('bold',30))
                   q1.place(x=100,y=150)
            server.quit()
 
        i=StringVar()
        i1=StringVar()
        i2=StringVar()
        i3=StringVar()       
        c=Checkbutton(top1, text="Vegetable peels and other organic stuff",variable=i,onvalue="Vegetable peels and other organic stuff",offvalue="")
        c1=Checkbutton(top1, text="Plastic and other Inorganic stuff",variable=i1,onvalue="Plastic and other Inorganic stuff",offvalue="")
        c2=Checkbutton(top1, text="Electronic Waste",variable=i2,onvalue="Electronic Waste",offvalue="")
        c3=Checkbutton(top1, text="Liquid Waste",variable=i3,onvalue="Liquid Waste",offvalue="")
        c.place(x=50,y=200)
        c1.place(x=50,y=225)
        c2.place(x=50,y=250)
        c3.place(x=50,y=275)
        butt1=Button(top1, text="Submit",command=click1)
        butt1.place(x=400,y=300)
        u1= StringVar()
        u2= IntVar()
        u3= StringVar()
        u1e= Entry(top1, textvariable=u1)
        u2e= Entry(top1, textvariable=u2)
        u3e= Entry(top1, textvariable=u3)
        u1e.place(x=700,y=200)
        u2e.place(x=700,y=250)
        u3e.place(x=700,y=300)
        ab=Label(top1,text="Full Name:")
        ab1=Label(top1,text="Amount of waste you daily produce:")
        ab2=Label(top1,text="Your E-mail:")
        ab.place(x=500,y=200)
        ab1.place(x=500,y=250)
        ab2.place(x=500,y=300)
#About Page
def about():
    top5=Toplevel(top)
    global ren3
    top5.geometry('600x700')
    load2=Image.open('D:\\app ic\\aboutpic2.png')
    ren3=ImageTk.PhotoImage(load2)
    img2=Label(top5,image=ren3)
    img2.place(x=0,y=0)
 
gg3=Button(top,text='About',command=about)
gg3.place(x=400,y=400)       
gg1=Button(top,text="Submit",command=getv)
gg1.place(x=200,y=340)
top.mainloop()