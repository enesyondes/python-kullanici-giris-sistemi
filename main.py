from tkinter.tix import Select
import webbrowser
from tkinter import *
import time
import sqlite3


pencere =Tk()
pencere.geometry("1200x600")
pencere.configure(background='black')

başlık = Label(text="HOŞGELDİNİZ",fg = "blue",font=("open sans","30","underline"),
                                                    background = ("black"))
başlık.place(x=100,y=100)


isim = Entry(text="kullanıcı adı:",font="Verdana 15 bold")
isim.place(x=250,y=200)


boşlukadı = Label(text = "KULLANICI ADI:",
                  fg = "red",font=("open sans", "15",
                  "normal"),background="black")
boşlukadı.place(x=100,y=200)


şfre = Entry(text="ŞİFRE:",font="Verdana 15 bold",show="*")
şfre.place(x=250,y=250)

şifreadı = Label(text = "PAROLA:",
                 fg = "red",font=("open sans","15",
                                  "normal"),background="black" )
şifreadı.place(x=100,y=250)


con = sqlite3.connect("bilgiler.db")
cursor = con.cursor()

def tablo():
        cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler (ad TEXT,soyad TEXT,kullanıcıadı TEXT,parola TEXT)")
        con.commit()

tablo()





cursor.execute("SELECT kullanıcıadı FROM bilgiler;")
defkullanıcı = cursor.fetchall()




cursor.execute("SELECT parola FROM bilgiler;")
defparola = cursor.fetchall()




denemehakkı = 3
zaman = 0
                 
cevap = Label(pencere,text= "",font=("Verdana 13 bold"),background="black",fg ="red")
cevap.place(x=250,y=350)

def kalan():
        if denemehakkı == 3:
                cevap.config(text = "Hatalı giriş kalan hakkınız 2")
        elif denemehakkı == 2:
                 cevap.config(text = "Hatalı giriş kalan hakkınız 1")
        elif denemehakkı == 1:
                 cevap.config(text = "Hatalı giriş kalan hakkınız 0")

def sistem():


        cevap = Label(pencere,text= "",font=("Verdana 13 bold"),background="black",fg ="red")
        cevap.place(x=250,y=350)

        global denemehakkı, zaman

        if denemehakkı > 0 :
                 kalan()


        elif denemehakkı <= 0 :
                if time.time()-zaman >= 30:
                        denemehakkı = 3

                else:
                  cevap.config(text = "Askıya alındı 30 saniye bekleyiniz!!")
                  return False




        kullan = isim.get()     #input olarak aldığımız bilgi
        şifre = şfre.get()      #input olarak aldığımız şifre
        

        for i in defkullanıcı:
                for j in defparola:
                        i = str(i).strip("'(),")
                        j = str(j).strip("'(),")
                        
                        if(kullan == i) and (şifre == j):
                                silme()
                                cevap.config(text = "HOŞGELDİNİZ "+kullan+"  ")

                        else:
                                denemehakkı -= 1
                                
                                if denemehakkı == 0:
                                        zaman = time.time()
                                        cevap.config(text = "Bilgiler yanlış! Kalan deneme: %d" %denemehakkı)


def silme(): 
        başlık.config(text = "GİRİŞ BAŞARILI")
        btn.destroy()
        şifreadı.destroy()
        şfre.destroy()
        boşlukadı.destroy()
        isim.destroy()
        kayıttuş.destroy()
        cevap.destroy()

def kayıtolma():

        def kaydol():
                ism = isimgir.get()
                soyism = soyisim.get()
                is_im = kuladı.get()
                par_ol = parol.get()

                if ism == "" or soyism == "" or is_im == "" or par_ol == "":
                        uyarı = Label(text = "Lütfen boş bırakmayınız!!",font=("Verdana 13 bold"),background="black",fg ="red")
                        uyarı.place(x=200,y=400)

                else:
                        tablo()
                        sql = "INSERT INTO bilgiler (ad, soyad, kullanıcıadı, parola) VALUES(?,?,?,?)"
                        cursor.execute(sql,(ism, soyism, is_im, par_ol))
                        con.commit()

                        cevap.config(text = "BAŞARIYLA KAYDEDİLDİ HOŞGELDİNİZ")
                        cevap.place(x=200,y=400)




        #kayıt bilgiler#

        başlık.config(text = "BİLGİLERİ DOLDURUNUZ")
        btn.destroy()
        şifreadı.destroy()
        şfre.destroy()
        boşlukadı.destroy()
        isim.destroy()
        kayıttuş.destroy()

        kayıtet = Button(text="KAYIT OL",command=kaydol)
        kayıtet.place(x=400,y=500)

        isimgir = Entry(font="Verdana 15 bold")
        isimgir.place(x=250,y=200)

        soyisim = Entry(font="Verdana 15 bold")
        soyisim.place(x=250,y=250)

        kuladı = Entry(font="Verdana 15 bold")
        kuladı.place(x=250,y=300)

        parol = Entry(font="Verdana 15 bold")
        parol.place(x=250,y=350)




        #kayıt başlıkları#

        name = Label(text = "İSİM:",
                  fg = "red",font=("open sans", "15",
                  "normal"),background="black")
        name.place(x=100,y=200)

        soygir = Label(text = "SOYİSİM:",fg = "red",font=("open sans", "15",
                  "normal"),background="black")
        soygir.place(x=100,y=250)

        kuladgir = Label(text="KULLANICI ADI:",fg = "red",font=("open sans", "15",
                  "normal"),background="black")
        kuladgir.place(x=100,y=300)

        parolgir = Label(text="PAROLA:",fg = "red",font=("open sans", "15",
                  "normal"),background="black")
        parolgir.place(x=100,y=350)

cursor.execute("SELECT kullanıcıadı from bilgiler")
a = cursor.fetchall()

cursor.execute("SELECT parola from bilgiler")
b = cursor.fetchall()
 
print(a)
print(b)

def veri_al():
        cursor.execute("SELECT * FROM kullanıcıadı")
        data = cursor.fetchall()
        for i_ in data:
                print(i_)


kayıttuş = Button(text="KAYIT OL",command=kayıtolma)
kayıttuş.place(x=400,y=300)



btn = Button(text="GİRİŞ", command=sistem)
btn.place(x=300,y=300)

pencere.mainloop()