#Developer:
from Tkinter import *
import ttk
import os
import tkFont
import tkMessageBox
import ScrolledText
import time
import subprocess

#ventana
v0=Tk()
v0.title("Area de Texto GPIO")
v0.geometry("700x400+0+0")


#Imagenes
immgON=PhotoImage(file="/home/elvis/on.gif")
immgOff=PhotoImage(file="/home/elvis/off.gif")

#Fuente
textt=tkFont.Font(family="Helvatica",size=12)


def cargar():
    ck=int(check.get())
    if (ck == 1):
                os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio readall" > cargar.txt')
                valor=subprocess.check_output("cat /home/elvis/cargar.txt",shell=True)
                area=ScrolledText.ScrolledText(v0,width=80,height=20)
                area.place(x=10,y=50)
                area.insert(INSERT,valor)
    if (ck == 0):
                area=ScrolledText.ScrolledText(v0,width=80,height=20)
                area.place(x=10,y=50)
                area.delete("1.0",END)

def cargar2():
    rd=int(radio.get())
    if (rd == 1):
                os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio readall" > cargar.txt')
                valor=subprocess.check_output("cat /home/elvis/cargar.txt",shell=True)
                area=ScrolledText.ScrolledText(v0,width=80,height=20)
                area.place(x=10,y=50)
                area.insert(INSERT,valor)
    if (rd == 2):
                area=ScrolledText.ScrolledText(v0,width=80,height=20)
                area.place(x=10,y=50)
                area.delete("1.0",END)

def cargar3():
    c=(combo.get())
    if (c == "Cargar"):
                os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio readall" > cargar.txt')
                valor=subprocess.check_output("cat /home/elvis/cargar.txt",shell=True)
                area=ScrolledText.ScrolledText(v0,width=80,height=20)
                area.place(x=10,y=50)
                area.insert(INSERT,valor)
    if (c == "Limpiar"):
                area=ScrolledText.ScrolledText(v0,width=80,height=20)
                area.place(x=10,y=50)
                area.delete("1.0",END)


def dialogo17():
    v17=Toplevel()
    v17.title("Control GPIO-17")
    v17.geometry("600x300+180+50")

        
    def limpiar():
                horaini17.set("")
                minini17.set("")
                minf17.set("")
                horaf17.set("")
                
    def registrar():
            print "Registrado"
            hi17=horaini17.get()
            mi17=minini17.get()
            hf17=horaf17.get()
            mf17=minf17.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on17r.sh"
            path2="/home/elvis/off17r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_17")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_17")

            #cadena
            cadena=(str(mi17)+''+str(tab)+''+str(hi17)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf17)+''+str(tab)+''+str(hf17)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_17","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_17","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_17")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_17")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini17=StringVar()
    horaini17=StringVar()
    minf17=StringVar()
    horaf17=StringVar()

    label_horaini17=Label(v17,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini17=Entry(v17,textvariable=horaini17,font=text2).place(x=130,y=10)
    label_horaini17=Label(v17,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini17=Entry(v17,textvariable=minini17,font=text2).place(x=130,y=50)
    label_horaf17=Label(v17,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini17=Entry(v17,textvariable=horaf17,font=text2).place(x=130,y=90)
    label_mif17=Label(v17,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini17=Entry(v17,textvariable=minf17,font=text2).place(x=130,y=130)
    btn_guardar17=Button(v17,text="Registrar",command=registrar).place(x=185,y=160)

    def actualizar():
            os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio read 0" > estado17.txt')                     
            pf=open("/home/elvis/estado17.txt","r")
            for linea in pf:
                campo=linea.split("\n")
                campof=campo[0]
                if (campof=="1"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v17,text="1",font=text1).place(x=340,y=50)
                                    btn_on20=Button(v17,image=immgON).place(x=400,y=30)
                                    v17.after(1000,actualizar)
                                    
                if (campof=="0"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v17,text="0",font=text1).place(x=340,y=50)
                                    btn_off20=Button(v17,image=immgOff).place(x=400,y=30)
                                    v17.after(1000,actualizar)
                                    
    actualizar()

    
    def on17r():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on17r.sh")

    def off17r():
        print "APAGADO"
        os.system("sudo /./home/elvis/off17r.sh")
    
    #boton
    btn_on=Button(v17,text="ON",command=on17r).place(x=380,y=150)
    btn_off=Button(v17,text="OFF",command=off17r).place(x=450,y=150)

    def aplicar_check():
                    print "APLICADO"
                    c=float(check.get())
                    if (c==1):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on17.sh"')
                     
                    if (c==0):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off17.sh"')
  
    global check
    check = IntVar()
    #Objeto Check
    check_obj=ttk.Checkbutton(v17,text="ON/OFF",variable=check)
    check_obj.place(x=40,y=200)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v17,text="Aplicar",command=aplicar_check).place(x=38,y=230)


    def aplicar():
            rf=float(radio.get())
            if (rf==1):
                       print "uno"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on17.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
            if (rf==2):
                       print "dos"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off17.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')

    #Declarar variable
    global radio
    radio = IntVar()
    #Objeto Radio
    r1=Radiobutton(v17,text="ON",variable=radio,value=1).place(x=200,y=200)
    r2=Radiobutton(v17,text="OFF",variable=radio,value=2).place(x=200,y=250)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v17,text="Aplicar",command=aplicar).place(x=280,y=220)


    def cargar3():
        c=(combo.get())
        if (c == "Encendido"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on17.sh"')
        if (c == "Apagado"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off17.sh"')

    global combo
    combo=StringVar()
    combo=ttk.Combobox(v17,state="read only",value=["Encendido","Apagado"])
    combo.place(x=350,y=5)
    btn_cargar=Button(v17,text=">",command=cargar3).place(x=530,y=5)


    v17.mainloop()

                
def dialogo27():
    v27=Toplevel()
    v27.title("Control GPIO-27")
    v27.geometry("600x300+180+50")

        
    def limpiar():
                horaini27.set("")
                minini27.set("")
                minf27.set("")
                horaf27.set("")
                
    def registrar():
            print "Registrado"
            hi27=horaini27.get()
            mi27=minini27.get()
            hf27=horaf27.get()
            mf27=minf27.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on27r.sh"
            path2="/home/elvis/off27r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_27")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_27")

            #cadena
            cadena=(str(mi27)+''+str(tab)+''+str(hi27)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf27)+''+str(tab)+''+str(hf27)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_27","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_27","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_27")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_27")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini27=StringVar()
    horaini27=StringVar()
    minf27=StringVar()
    horaf27=StringVar()

    label_horaini27=Label(v27,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini27=Entry(v27,textvariable=horaini27,font=text2).place(x=130,y=10)
    label_horaini27=Label(v27,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini27=Entry(v27,textvariable=minini27,font=text2).place(x=130,y=50)
    label_horaf27=Label(v27,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini27=Entry(v27,textvariable=horaf27,font=text2).place(x=130,y=90)
    label_mif27=Label(v27,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini27=Entry(v27,textvariable=minf27,font=text2).place(x=130,y=130)
    btn_guardar27=Button(v27,text="Registrar",command=registrar).place(x=185,y=160)

    def actualizar():
            os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio read 2" > estado27.txt')                     
            pf=open("/home/elvis/estado27.txt","r")
            for linea in pf:
                campo=linea.split("\n")
                campof=campo[0]
                if (campof=="1"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v27,text="1",font=text1).place(x=340,y=50)
                                    btn_on20=Button(v27,image=immgON).place(x=400,y=30)
                                    v27.after(1000,actualizar)
                                    
                if (campof=="0"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v27,text="0",font=text1).place(x=340,y=50)
                                    btn_off20=Button(v27,image=immgOff).place(x=400,y=30)
                                    v27.after(1000,actualizar)
                                    
    actualizar()

    
    def on27r():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on27r.sh")

    def off27r():
        print "APAGADO"
        os.system("sudo /./home/elvis/off27r.sh")
    
    #boton
    btn_on=Button(v27,text="ON",command=on27r).place(x=380,y=150)
    btn_off=Button(v27,text="OFF",command=off27r).place(x=450,y=150)

    def aplicar_check():
                    print "APLICADO"
                    c=float(check.get())
                    if (c==1):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on27.sh"')
                     
                    if (c==0):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off27.sh"')
  
    global check
    check = IntVar()
    #Objeto Check
    check_obj=ttk.Checkbutton(v27,text="ON/OFF",variable=check)
    check_obj.place(x=40,y=200)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v27,text="Aplicar",command=aplicar_check).place(x=38,y=230)


    def aplicar2():
            rf2=float(radio2.get())
            if (rf2==1):
                       print "uno"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on27.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
            if (rf2==2):
                       print "dos"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off27.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')

    #Declarar variable
    global radio2
    radio2 = IntVar()
    #Objeto Radio
    r11=Radiobutton(v27,text="ON",variable=radio2,value=1).place(x=200,y=200)
    r22=Radiobutton(v27,text="OFF",variable=radio2,value=2).place(x=200,y=250)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v27,text="Aplicar",command=aplicar2).place(x=280,y=220)


    def cargar3():
        c=(combo2.get())
        if (c == "Encendido"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on27.sh"')
        if (c == "Apagado"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off27.sh"')

    global combo2
    combo2=StringVar()
    combo2=ttk.Combobox(v27,state="read only",value=["Encendido","Apagado"])
    combo2.place(x=350,y=5)
    btn_cargar=Button(v27,text=">",command=cargar3).place(x=530,y=5)


    
    v27.mainloop()
                
def dialogo6():
    v6=Toplevel()
    v6.title("Control GPIO-6")
    v6.geometry("600x300+180+50")


        
    def limpiar():
                horaini6.set("")
                minini6.set("")
                minf6.set("")
                horaf6.set("")
                
    def registrar():
            print "Registrado"
            hi6=horaini6.get()
            mi6=minini6.get()
            hf6=horaf6.get()
            mf6=minf6.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on6r.sh"
            path2="/home/elvis/off6r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_6")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_6")

            #cadena
            cadena=(str(mi6)+''+str(tab)+''+str(hi6)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf6)+''+str(tab)+''+str(hf6)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_6","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_6","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_6")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_6")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini6=StringVar()
    horaini6=StringVar()
    minf6=StringVar()
    horaf6=StringVar()

    label_horaini6=Label(v6,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini6=Entry(v6,textvariable=horaini6,font=text2).place(x=130,y=10)
    label_horaini6=Label(v6,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini6=Entry(v6,textvariable=minini6,font=text2).place(x=130,y=50)
    label_horaf6=Label(v6,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini6=Entry(v6,textvariable=horaf6,font=text2).place(x=130,y=90)
    label_mif6=Label(v6,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini6=Entry(v6,textvariable=minf6,font=text2).place(x=130,y=130)
    btn_guardar6=Button(v6,text="Registrar",command=registrar).place(x=185,y=160)

    def actualizar():
            os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio read 22" > estado6.txt')                     
            pf=open("/home/elvis/estado6.txt","r")
            for linea in pf:
                campo=linea.split("\n")
                campof=campo[0]
                if (campof=="1"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v6,text="1",font=text1).place(x=340,y=50)
                                    btn_on20=Button(v6,image=immgON).place(x=400,y=30)
                                    v6.after(1000,actualizar)
                                    
                if (campof=="0"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v6,text="0",font=text1).place(x=340,y=50)
                                    btn_off20=Button(v6,image=immgOff).place(x=400,y=30)
                                    v6.after(1000,actualizar)
                                    
    actualizar()

    
    def on6r():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on6r.sh")

    def off6r():
        print "APAGADO"
        os.system("sudo /./home/elvis/off6r.sh")
    
    #boton
    btn_on=Button(v6,text="ON",command=on6r).place(x=380,y=150)
    btn_off=Button(v6,text="OFF",command=off6r).place(x=450,y=150)

    def aplicar_check():
                    print "APLICADO"
                    c=float(check.get())
                    if (c==1):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on6.sh"')
                     
                    if (c==0):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off6.sh"')
  
    global check
    check = IntVar()
    #Objeto Check
    check_obj=ttk.Checkbutton(v6,text="ON/OFF",variable=check)
    check_obj.place(x=40,y=200)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v6,text="Aplicar",command=aplicar_check).place(x=38,y=230)


    def aplicar2():
            rf2=float(radio2.get())
            if (rf2==1):
                       print "uno"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on6.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
            if (rf2==2):
                       print "dos"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off6.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')

    #Declarar variable
    global radio2
    radio2 = IntVar()
    #Objeto Radio
    r11=Radiobutton(v6,text="ON",variable=radio2,value=1).place(x=200,y=200)
    r22=Radiobutton(v6,text="OFF",variable=radio2,value=2).place(x=200,y=250)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v6,text="Aplicar",command=aplicar2).place(x=280,y=220)


    def cargar3():
        c=(combo2.get())
        if (c == "Encendido"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on6.sh"')
        if (c == "Apagado"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off6.sh"')

    global combo2
    combo2=StringVar()
    combo2=ttk.Combobox(v6,state="read only",value=["Encendido","Apagado"])
    combo2.place(x=350,y=5)
    btn_cargar=Button(v6,text=">",command=cargar3).place(x=530,y=5)





    v6.mainloop()

def dialogo21():
    v21=Toplevel()
    v21.title("Control GPIO-21")
    v21.geometry("600x300+180+50")



        
    def limpiar():
                horaini21.set("")
                minini21.set("")
                minf21.set("")
                horaf21.set("")
                
    def registrar():
            print "Registrado"
            hi21=horaini21.get()
            mi21=minini21.get()
            hf21=horaf21.get()
            mf21=minf21.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on21r.sh"
            path2="/home/elvis/off21r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_21")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_21")

            #cadena
            cadena=(str(mi21)+''+str(tab)+''+str(hi21)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf21)+''+str(tab)+''+str(hf21)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_21","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_21","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_21")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_21")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini21=StringVar()
    horaini21=StringVar()
    minf21=StringVar()
    horaf21=StringVar()

    label_horaini21=Label(v21,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini21=Entry(v21,textvariable=horaini21,font=text2).place(x=130,y=10)
    label_horaini21=Label(v21,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini21=Entry(v21,textvariable=minini21,font=text2).place(x=130,y=50)
    label_horaf21=Label(v21,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini21=Entry(v21,textvariable=horaf21,font=text2).place(x=130,y=90)
    label_mif21=Label(v21,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini21=Entry(v21,textvariable=minf21,font=text2).place(x=130,y=130)
    btn_guardar21=Button(v21,text="Registrar",command=registrar).place(x=185,y=160)

    def actualizar():
            os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio read 29" > estado21.txt')                     
            pf=open("/home/elvis/estado21.txt","r")
            for linea in pf:
                campo=linea.split("\n")
                campof=campo[0]
                if (campof=="1"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v21,text="1",font=text1).place(x=340,y=50)
                                    btn_on20=Button(v21,image=immgON).place(x=400,y=30)
                                    v21.after(1000,actualizar)
                                    
                if (campof=="0"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v21,text="0",font=text1).place(x=340,y=50)
                                    btn_off20=Button(v21,image=immgOff).place(x=400,y=30)
                                    v21.after(1000,actualizar)
                                    
    actualizar()

    
    def on21r():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on21r.sh")

    def off21r():
        print "APAGADO"
        os.system("sudo /./home/elvis/off21r.sh")
    
    #boton
    btn_on=Button(v21,text="ON",command=on21r).place(x=380,y=150)
    btn_off=Button(v21,text="OFF",command=off21r).place(x=450,y=150)

    def aplicar_check():
                    print "APLICADO"
                    c=float(check.get())
                    if (c==1):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on21.sh"')
                     
                    if (c==0):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off21.sh"')
  
    global check
    check = IntVar()
    #Objeto Check
    check_obj=ttk.Checkbutton(v21,text="ON/OFF",variable=check)
    check_obj.place(x=40,y=200)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v21,text="Aplicar",command=aplicar_check).place(x=38,y=230)


    def aplicar2():
            rf2=float(radio2.get())
            if (rf2==1):
                       print "uno"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on21.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
            if (rf2==2):
                       print "dos"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off21.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')

    #Declarar variable
    global radio2
    radio2 = IntVar()
    #Objeto Radio
    r11=Radiobutton(v21,text="ON",variable=radio2,value=1).place(x=200,y=200)
    r22=Radiobutton(v21,text="OFF",variable=radio2,value=2).place(x=200,y=250)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v21,text="Aplicar",command=aplicar2).place(x=280,y=220)


    def cargar3():
        c=(combo2.get())
        if (c == "Encendido"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on21.sh"')
        if (c == "Apagado"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off21.sh"')

    global combo2
    combo2=StringVar()
    combo2=ttk.Combobox(v21,state="read only",value=["Encendido","Apagado"])
    combo2.place(x=350,y=5)
    btn_cargar=Button(v21,text=">",command=cargar3).place(x=530,y=5)




    v21.mainloop()

def dialogo26():
    v26=Toplevel()
    v26.title("Control GPIO-26")
    v26.geometry("600x300+180+50")



        
    def limpiar():
                horaini26.set("")
                minini26.set("")
                minf26.set("")
                horaf26.set("")
                
    def registrar():
            print "Registrado"
            hi26=horaini26.get()
            mi26=minini26.get()
            hf26=horaf26.get()
            mf26=minf26.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on26r.sh"
            path2="/home/elvis/off26r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_26")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_26")

            #cadena
            cadena=(str(mi26)+''+str(tab)+''+str(hi26)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf26)+''+str(tab)+''+str(hf26)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_26","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_26","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_26")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_26")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini26=StringVar()
    horaini26=StringVar()
    minf26=StringVar()
    horaf26=StringVar()

    label_horaini26=Label(v26,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini26=Entry(v26,textvariable=horaini26,font=text2).place(x=130,y=10)
    label_horaini26=Label(v26,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini26=Entry(v26,textvariable=minini26,font=text2).place(x=130,y=50)
    label_horaf26=Label(v26,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini26=Entry(v26,textvariable=horaf26,font=text2).place(x=130,y=90)
    label_mif26=Label(v26,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini26=Entry(v26,textvariable=minf26,font=text2).place(x=130,y=130)
    btn_guardar26=Button(v26,text="Registrar",command=registrar).place(x=185,y=160)

    def actualizar():
            os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio read 25" > estado26.txt')                     
            pf=open("/home/elvis/estado26.txt","r")
            for linea in pf:
                campo=linea.split("\n")
                campof=campo[0]
                if (campof=="1"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v26,text="1",font=text1).place(x=340,y=50)
                                    btn_on20=Button(v26,image=immgON).place(x=400,y=30)
                                    v26.after(1000,actualizar)
                                    
                if (campof=="0"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v26,text="0",font=text1).place(x=340,y=50)
                                    btn_off20=Button(v26,image=immgOff).place(x=400,y=30)
                                    v26.after(1000,actualizar)
                                    
    actualizar()

    
    def on26r():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on26r.sh")

    def off26r():
        print "APAGADO"
        os.system("sudo /./home/elvis/off26r.sh")
    
    #boton
    btn_on=Button(v26,text="ON",command=on26r).place(x=380,y=150)
    btn_off=Button(v26,text="OFF",command=off26r).place(x=450,y=150)

    def aplicar_check():
                    print "APLICADO"
                    c=float(check.get())
                    if (c==1):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on26.sh"')
                     
                    if (c==0):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off26.sh"')
  
    global check
    check = IntVar()
    #Objeto Check
    check_obj=ttk.Checkbutton(v26,text="ON/OFF",variable=check)
    check_obj.place(x=40,y=200)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v26,text="Aplicar",command=aplicar_check).place(x=38,y=230)


    def aplicar2():
            rf2=float(radio2.get())
            if (rf2==1):
                       print "uno"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on26.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
            if (rf2==2):
                       print "dos"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off26.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')

    #Declarar variable
    global radio2
    radio2 = IntVar()
    #Objeto Radio
    r11=Radiobutton(v26,text="ON",variable=radio2,value=1).place(x=200,y=200)
    r22=Radiobutton(v26,text="OFF",variable=radio2,value=2).place(x=200,y=250)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v26,text="Aplicar",command=aplicar2).place(x=280,y=220)


    def cargar3():
        c=(combo2.get())
        if (c == "Encendido"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on26.sh"')
        if (c == "Apagado"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off26.sh"')

    global combo2
    combo2=StringVar()
    combo2=ttk.Combobox(v26,state="read only",value=["Encendido","Apagado"])
    combo2.place(x=350,y=5)
    btn_cargar=Button(v26,text=">",command=cargar3).place(x=530,y=5)



    
    v26.mainloop()

def dialogo19():
    v19=Toplevel()
    v19.title("Control GPIO-19")
    v19.geometry("600x300+180+50")



  
    def limpiar():
                horaini19.set("")
                minini19.set("")
                minf19.set("")
                horaf19.set("")
                
    def registrar():
            print "Registrado"
            hi19=horaini19.get()
            mi19=minini19.get()
            hf19=horaf19.get()
            mf19=minf19.get()
            tab = " "
            dia="*"
            mes="*"
            ano="*"
            usuario="root"
            path1="/home/elvis/on19r.sh"
            path2="/home/elvis/off19r.sh"

            #ASIGNAR PERMISOS DE ESCRITURA Y EJECUCION
            os.system("sudo chmod -R 777 /etc/cron.d/tarea1_19")
            os.system("sudo chmod -R 777 /etc/cron.d/tarea2_19")

            #cadena
            cadena=(str(mi19)+''+str(tab)+''+str(hi19)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path1))
            cadena2=(str(mf19)+''+str(tab)+''+str(hf19)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ano)+''+str(tab)+''+str(usuario)+''+str(tab)+''+str(path2))
         
            #apertura archivo
            pf=open("/etc/cron.d/tarea1_19","w")
            pf.write(cadena)
            pf.write("\n")
            pf.close()
            time.sleep(0.1)

            pf2=open("/etc/cron.d/tarea2_19","w")
            pf2.write(cadena2)
            pf2.write("\n")
            pf2.close()
            time.sleep(0.1)

            #permiso
            os.system("sudo chmod -R 755 /etc/cron.d/tarea1_19")
            os.system("sudo chmod -R 755 /etc/cron.d/tarea2_19")

            #servicio
            os.system("sudo /etc/init.d/cron restart")

            limpiar()
            tkMessageBox.showinfo("save",message="Tiempo Registrado")

    #variables
    minini19=StringVar()
    horaini19=StringVar()
    minf19=StringVar()
    horaf19=StringVar()

    label_horaini19=Label(v19,text="Hora Inicial:",font=text2).place(x=15,y=10)
    txt_horaini19=Entry(v19,textvariable=horaini19,font=text2).place(x=130,y=10)
    label_horaini19=Label(v19,text="Minuto Inicial:",font=text2).place(x=15,y=50)
    txt_minini19=Entry(v19,textvariable=minini19,font=text2).place(x=130,y=50)
    label_horaf19=Label(v19,text="Hora Final:",font=text2).place(x=15,y=90)
    txt_horaini19=Entry(v19,textvariable=horaf19,font=text2).place(x=130,y=90)
    label_mif19=Label(v19,text="Minuto Final:",font=text2).place(x=15,y=130)
    txt_minini19=Entry(v19,textvariable=minf19,font=text2).place(x=130,y=130)
    btn_guardar19=Button(v19,text="Registrar",command=registrar).place(x=185,y=160)

    def actualizar():
            os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo gpio read 24" > estado19.txt')                     
            pf=open("/home/elvis/estado19.txt","r")
            for linea in pf:
                campo=linea.split("\n")
                campof=campo[0]
                if (campof=="1"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v19,text="1",font=text1).place(x=340,y=50)
                                    btn_on20=Button(v19,image=immgON).place(x=400,y=30)
                                    v19.after(1000,actualizar)
                                    
                if (campof=="0"):
                                    text1=tkFont.Font(family="Helvatica",size=32)
                                    label1=Label(v19,text="0",font=text1).place(x=340,y=50)
                                    btn_off20=Button(v19,image=immgOff).place(x=400,y=30)
                                    v19.after(1000,actualizar)
                                    
    actualizar()

    
    def on19r():
        print "ENCENDIDO"
        os.system("sudo /./home/elvis/on19r.sh")

    def off19r():
        print "APAGADO"
        os.system("sudo /./home/elvis/off19r.sh")
    
    #boton
    btn_on=Button(v19,text="ON",command=on19r).place(x=380,y=150)
    btn_off=Button(v19,text="OFF",command=off19r).place(x=450,y=150)

    def aplicar_check():
                    print "APLICADO"
                    c=float(check.get())
                    if (c==1):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on19.sh"')
                     
                    if (c==0):
                           #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')
                           os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off19.sh"')
  
    global check
    check = IntVar()
    #Objeto Check
    check_obj=ttk.Checkbutton(v19,text="ON/OFF",variable=check)
    check_obj.place(x=40,y=200)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v19,text="Aplicar",command=aplicar_check).place(x=38,y=230)


    def aplicar2():
            rf2=float(radio2.get())
            if (rf2==1):
                       print "uno"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on19.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/on17.sh"')
            if (rf2==2):
                       print "dos"
                       os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off19.sh"')
                       #os.system('sudo sshpass -p "Y0987654321" ssh -l elvis 192.168.0.7 "sudo /./home/elvis/off17.sh"')

    #Declarar variable
    global radio2
    radio2 = IntVar()
    #Objeto Radio
    r11=Radiobutton(v19,text="ON",variable=radio2,value=1).place(x=200,y=200)
    r22=Radiobutton(v19,text="OFF",variable=radio2,value=2).place(x=200,y=250)
    #Etiquetas
    text1=tkFont.Font(family="Helvatica",size=18)
    btn_aplicar=Button(v19,text="Aplicar",command=aplicar2).place(x=280,y=220)


    def cargar3():
        c=(combo2.get())
        if (c == "Encendido"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/on19.sh"')
        if (c == "Apagado"):
                    os.system('sudo sshpass -p "1234" ssh -l uth 45.181.84.101 "sudo /./home/uth/off19.sh"')

    global combo2
    combo2=StringVar()
    combo2=ttk.Combobox(v19,state="read only",value=["Encendido","Apagado"])
    combo2.place(x=350,y=5)
    btn_cargar=Button(v19,text=">",command=cargar3).place(x=530,y=5)






    v19.mainloop()




#variables golbales
global minini17
global horaini17
global minf17
global horaf17

global minini27
global horaini27
global minf27
global horaf27

global minini21
global horaini21
global minf21
global horaf21



global minini6
global horaini6
global minf6
global horaf6


global minini26
global horaini26
global minf26
global horaf26



global minini19
global horaini19 
global minf19
global horaf19




global check
check=IntVar()
check1=ttk.Checkbutton(v0,text="Load",variable=check,command=cargar)
check1.place(x=10,y=10)

global radio
radio=IntVar()
r1=ttk.Radiobutton(v0,text="Cargar",variable=radio,value=1,command=cargar2)
r1.place(x=100,y=10)
r2=ttk.Radiobutton(v0,text="Limpiar",variable=radio,value=2,command=cargar2)
r2.place(x=180,y=10)

global combo
combo=StringVar()
combo=ttk.Combobox(v0,state="read only",value=["Cargar","Limpiar"])
combo.place(x=300,y=10)
btn_cargar=Button(v0,text=">",command=cargar3).place(x=480,y=10)

# Tipo De Fuente
text1=tkFont.Font(family="Helvatica",size=12)
text2=tkFont.Font(family="Arial",size=12)


menubar=Menu(v0)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="GPIO17",command=dialogo17)
filemenu.add_command(label="GPIO27",command=dialogo27)
filemenu.add_command(label="GPIO6",command=dialogo6)
filemenu.add_command(label="GPIO21",command=dialogo21)
filemenu.add_command(label="GPIO26",command=dialogo26)
filemenu.add_command(label="GPIO19",command=dialogo19)
filemenu.add_command(label="Exit",command=v0.destroy)
menubar.add_cascade(label="Control-GPIOS",menu=filemenu)
v0.config(menu=menubar)




v0.mainloop()