#23/3/2024 - 4/4/2024
#Chotivit busamongkol
#โปรเเกรมคำนวณภาษีเเบบบุคคลธรรมดา

from tkinter import*
from tkinter import filedialog 
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageTk
import os
import json
from tkinter import messagebox

os.getcwd()
os.chdir('C:\\Users\\chotivit busamongkol\\apptax\\Pictures tax') #รูปicon



window = Tk() #จอ1
window.title("คำนวณภาษีสุดเเมว")
window.iconbitmap ('highschool_CB.ico')
window.geometry("600x400+450+250")



menu_tax = Menu()
window.config(menu = menu_tax)

def Exit1():
    cf = messagebox.askquestion('Exit','ต้องการออกจากโปรเเกรมหรือมั้ย?')  #ปุ่มหรือ menuออกจากเเอพ
    if cf == 'yes':
        window.destroy()

def openfile_data():    #menu อ่านไฟล์ที่เราsaveจากการเก็บข้อมูลเเล้วนำมาเปิด
    openfile =Tk()
    openfile.title("อ่านไฟล์json")
    openfile.configure(bg='#333333')
    openfile.iconbitmap ('highschool_CB.ico')

    def openjson():  #function อ่านไฟล์
        json_file = open("taxjson101.json",'r')
        stuff = json_file.read()

        my_json.insert(END,stuff)
        json_file.close()

    def Exit_off(): #function ปิดการทำงานของmenuอ่านไฟล์
        openfile.destroy()

    my_json =Text(openfile,width=40,height=10)
    my_json.pack(pady=20)

    open_button =Button(openfile,text='เปิดเนื้อหาไฟล์ที่save',command=openjson)
    open_button.pack(pady=20)

    off_button =Button(openfile,text='ปิด',command=Exit_off)
    off_button.pack(pady=20)
   

    openfile.mainloop()

def data_about_tax(): #menuสูตรในการคำนวณภาษี
    global my_img,photo1
    data = Toplevel()
    data.title('สูตรในการคำนวณภาษี')
    data.geometry("900x200") 
    data.iconbitmap ('highschool_CB.ico')
    Label(data,text="สูตรหาเงินได้สุทธิ",font=20).pack()
    my_img = ImageTk.PhotoImage(Image.open('Screenshot 2024-04-04 144844.png'))
    my_label = Label(data, image=my_img).pack()

    Label(data,text ='สูตรในการคำนวณหาภาษีที่ต้องชำระ',font=20).pack()
    photo1 = ImageTk.PhotoImage(Image.open("Screenshot 2024-04-04 144904.png")) 
    labelphoto1 =  Label(data,image=photo1).pack()
   
def language(): #menu
    messagebox.showinfo('ภาษาที่ใช้ในการพัฒนา','Python')

def dev(): #menu
    messagebox.showinfo('developer','Chotivit Busamongkol')

menuabout = Menu()
menuFile = Menu()

menuFile.add_command(label="เปิดดูข้อมูลที่save",command = openfile_data)
menuFile.add_command(label="Exit",command= Exit1)

menuabout.add_command(label="ข้อมูลในการคำนวณภาษี",command=data_about_tax)
menuabout.add_command(label = "ภาษาที่ใช้ในการพัฒนา",command=language)
menuabout.add_command(label="ผู้พัฒนา",command=dev)

menu_tax.add_cascade(label='File',menu = menuFile)
menu_tax.add_cascade(label="About",menu=menuabout)


window.configure(bg='#333333') #สีพื้นหัลง




Label(text='รายได้ทั้งปี+โบนัส',font=20,bg='#333333',fg='#FFFFFF').grid(row=0,sticky=W) #คำถามในช่องนั้นๆ
yincome = IntVar()      #นำค่าที่ได้จากการกรอกในช่องกรอกมาเก็บในyincome
yearincome = Entry(textvariable=yincome) #รับค่า
yearincome.grid(row=0,column=1) #ขนาด

Label(text='ค่าใช้จ่ายทั้งปี',font=20,bg='#333333',fg='#FFFFFF').grid(row=1,sticky=W)
ep =IntVar()
expenses = Entry(textvariable=ep)
expenses.grid(row=1,column=1)

Label(text='ค่าลดหย่อน',font=20,bg='#333333',fg='#FFFFFF').grid(row=2,sticky=W)
Aw = IntVar()
Allowance = Entry(textvariable=Aw)
Allowance.grid(row=2,column=1)

Label(text='เงินได้สุทธิ',font=20,bg='#333333',fg='#0000FF').grid(row=4,sticky=W)
netincome =Entry()
netincome.grid(row=4,column=1)

Label(text='อัตราภาษี',font=20,bg='#333333',fg='#FFFFFF').grid(row=9,sticky=W)
tax = Entry()
tax.grid(row=9,column=1)

Label(text='ภาษีสะสมสูงสุดของลำดับขั้นก่อนหน้า',font=20,bg='#333333',fg='#FFFFFF').grid(row=10,sticky=W)
Maxtaxtext = Entry()
Maxtaxtext.grid(row=10,column=1)

Label(text='เงินได้สุทธิจำนวนสูงสุดของขั้นก่อนหน้า',font=20,bg='#333333',fg='#FFFFFF').grid(row=11,sticky=W)
incomebeforetext = Entry()
incomebeforetext.grid(row=11,column=1)


Label(text='ภาษีที่ท่านต้องชำระ',font=20,bg='#333333',fg='#FF0000').grid(row=12,sticky=W)
Taxall = Entry()
Taxall.grid(row=12,column=1)



lnet = [] #listของnetincome1
ylen =[] # list ของ yearincome
elen = [] #list ของ expenses
Alen = [] #list ของ Allowance
tlen = [] #list ของ อัตราภาษี
maxlen = [] #list ของ ภาษีสะสมสูงสุดของลำดับขั้นก่อนหน้า
iblen = []#list ของ เงินได้สุทธิจำนวนสูงสุดของขั้นก่อนหน้า
taxalllen = []#list ของ ภาษีที่ต้องชำระ

def shownetincome():
    yearincome = yincome.get() #รายได้ทั้งปี
    expenses = ep.get()  #ค่าใช้จ่ายทั้งปี
    Allowance = Aw.get()  #ค่าลดหย่อน
    netincome1 = yearincome-expenses-Allowance #คำนวณเงินสุทธิ
    netincome.insert(0,netincome1)

    lnet.append(netincome1) #นำค่าในnetincome1ที่รับมาไปเก็บในlnet
    ylen.append(yearincome)#นำค่าในyearincomeที่รับมาไปเก็บในylen
    elen.append(expenses)#นำค่าในexpensesที่รับมาไปเก็บในelen
    Alen.append(Allowance)#นำค่าในAllowanceที่รับมาไปเก็บในAlen





def tax01():   
    if sum(lnet) <= 150000: 
        tax_rate =  'อัตราภาษี 0% ได้รับการยกเว้นภาษี'
        tax_percent = 0  #อัตราภาษี
        Maxtax = 0       #ภาษีสะสมสูงสุดของลำดับขั้นก่อนหน้า
        incomebefore = 150000   #เงินได้สุทธิจำนวนสูงสุดของขั้นก่อนหน้า

        tax.insert(0,tax_rate) #showอัตราภาษีที่เป็นtax
        Maxtaxtext.insert(0,Maxtax) #showภาษีสะสมสูงสุดของลำดับขั้นก่อนหน้า
        incomebeforetext.insert(0,incomebefore) #showเงินได้สุทธิจำนวนสูงสุดของขั้นก่อนหน้า
        

    elif sum(lnet) >= 150001 and sum(lnet) <= 300000:
        tax_rate = 'อัตราภาษีอยู่ที่ 5%'
        tax_percent = 0.05
        Maxtax = 0
        incomebefore = 150000 
        
        tax.insert(0,tax_rate)
        Maxtaxtext.insert(0,Maxtax)
        incomebeforetext.insert(0,incomebefore)

    elif sum(lnet) >= 300001 and sum(lnet) <= 500000:
        tax_rate = 'อัตราภาษีอยู่ที่ 10%'
        tax_percent = 0.10
        Maxtax = 7500
        incomebefore = 300000

        tax.insert(0,tax_rate)
        Maxtaxtext.insert(0,Maxtax)
        incomebeforetext.insert(0,incomebefore)
    
    elif sum(lnet) >= 500001 and sum(lnet) <= 750000:
        tax_rate = 'อัตราภาษีอยู่ที่ 15%'
        tax_percent = 0.15
        Maxtax = 27500
        incomebefore = 500000
        
        tax.insert(0,tax_rate)
        Maxtaxtext.insert(0,Maxtax)
        incomebeforetext.insert(0,incomebefore)

    elif sum(lnet) >= 750001 and sum(lnet) <= 1000000:
        tax_rate = 'อัตราภาษีอยู่ที่ 20%'
        tax_percent = 0.20
        Maxtax = 65000
        incomebefore = 750000
        
        tax.insert(0,tax_rate)
        Maxtaxtext.insert(0,Maxtax)
        incomebeforetext.insert(0,incomebefore)

    elif sum(lnet) >= 1000001 and sum(lnet) <= 2000000:
        tax_rate = 'อัตราภาษีอยู่ที่ 25%'
        tax_percent = 0.25
        Maxtax =  115000
        incomebefore = 1000000
        
        tax.insert(0,tax_rate)
        Maxtaxtext.insert(0,Maxtax)
        incomebeforetext.insert(0,incomebefore)

    elif sum(lnet) >= 2000001 and sum(lnet) <= 5000000:
        tax_rate = 'อัตราภาษีอยู่ที่ 30%'
        tax_percent = 0.30
        Maxtax =  365000
        incomebefore = 2000000
        
        tax.insert(0,tax_rate)
        Maxtaxtext.insert(0,Maxtax)
        incomebeforetext.insert(0,incomebefore)

    elif sum(lnet) >= 5000001:
        tax_rate = 'อัตราภาษีอยู่ที่ 35%'
        tax_percent = 0.35
        Maxtax = 1265000
        incomebefore = 5000000
        
        tax.insert(0,tax_rate)
        Maxtaxtext.insert(0,Maxtax)
        incomebeforetext.insert(0,incomebefore)

    tax_all = ((sum(lnet)-incomebefore)*tax_percent)+Maxtax #สูตรในการคำนวณภาษีที่ต้องชำระ
    Taxall.insert(0,tax_all)

    tlen.append(tax_percent) #นำค่าในtax_percentที่ตรงตามเงื่อนไขไปเก็บในtlen
    maxlen.append(Maxtax)#นำค่าในMaxtaxที่ตรงตามเงื่อนไขไปเก็บในtlen
    iblen.append(incomebefore)#นำค่าในincomebeforeที่ตรงตามเงื่อนไขไปเก็บในtlen
    taxalllen.append(tax_all)#นำค่าในtax_allที่ตรงตามเงื่อนไขมาไปเก็บในtlen  เพื่อนำไปตำนวณกาภาษีที่ต้องชำระทั้งหมด
    


    




def delete2(): #function ล้างขอ้มูลที่กรอรในช่อง
    yearincome.delete(0,END)
    expenses.delete(0,END)
    Allowance.delete(0,END)
    netincome.delete(0,END)

    tax.delete(0,END)
    Maxtaxtext.delete(0,END)
    incomebeforetext.delete(0,END)
    Taxall.delete(0,END)




def saveExcel(): #function บันทึกข้อมูล โดยsaveเป็นjson

    taxjson_dict = {
              "yearincome":sum(ylen),
              "expenses":sum(elen),
              'Allowance':sum(Alen),
              'Net income':sum(lnet),
              'Tax rate':sum(tlen),
              'Maxtax':sum(maxlen),
              'Max Net income':sum(iblen),
              'Tax payable (THB)':sum(taxalllen)
        
    }

    with open("taxjson101.json",'w') as json_file:
        data = json.dump(taxjson_dict,json_file, indent=4)

    messagebox.showinfo("คำนวณภาษีสุดเเมว",'บันทึกข้อมูลเรียบร้อย')

    
   


b_4 = Button(text='คำนวณเงินได้สุทธิ',command=shownetincome).grid(row=3,column=1,sticky=W)
b_5 = Button(text='คำนวณภาษีที่ต้องชำระ',command=tax01).grid(row=8,column=1,sticky=W)

b_6 = Button(text='บันทึก',command = saveExcel).grid(row =13,column=1,sticky=W)
b_7 = Button(text='ล้าง',command=delete2).grid(row =13,column=1)


window.mainloop()



