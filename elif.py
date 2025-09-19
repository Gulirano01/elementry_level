# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 10:51:49 2025

@author: User
"""

# yosh=int(input("Yoshingiz nechada?:"))
# if yosh<=4: print("sizga kirish bepul")
# elif yosh<=13: print("Sizga kirish 12 ming so'm") 
# else: print("Sizga kirish 40 ming so'm")    

# kun=input("Bugun qaysi kun/:")
# if kun.lower()=="shanba" or kun.lower()=="Yakshanba":
#     print("Bugun dam olish kuni")
# else: print("Bugun ish kuni")    

# kun=input("Bugun qaysi kun?")
# harorat=float(input("Harorat necha?"))

# if (kun.lower()=="yakshanba" or kun.lower()=='shanba') and harorat>=30:
#       print("Cho'milgani boramiz!")      

# narx=15000
# choy=1
# non=0
# salat=1 
# kampot=1

# if choy:
#     print("Choy sotib oldi")
#     narx=narx+5000
# if non:
#     print("Non sotib oldi")  
#     narx=narx+2000
# if salat:
#     print("Salat sotib oldi")
#     narx=narx+6000
# if kampot:
#     print("kampot sotib oldi")
#     narx=narx+10000
# print(f"Jami {narx} so'm bo'ldi")     

# menu=['osh', 'qozonkabob','shashlik', 'somsa','norin']
# buyurtmalar=['osh', 'manti', 'goja' ]
# for taom in buyurtmalar:
#     if taom.lower() in menu:
# # ovqat=input("Siz nima ovqat yeysiz?")
# # if ovqat.lower() in menu:
#      print(f"Menyuda {taom.lower()} bor")
# else:
#      print(f"Bizda {taom.lower()} ovqat yo'q")    

# amaliyot
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son=int(input("Juft son kiriting:"))
# if son%2:
#     print("bu juft emas")
# else: print("Rahmat!")  
  
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh=int(input("Yoshingizni kiriting:"))
# if yosh<4 or yosh>60:
#     narx=0;
# elif yosh<18:
#     narx=10000;
# else:
#     narx=20000;
# print(f"sizga {narx} so'm")    

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# x=int(input("Birinchi sonni kiriting:"))
# y=int(input("Ikkinchi sonni kiriting:"))
# if x==y:
#     print("ikkala son teng")
# elif x<y:
#      print(f" {y} {x} dan katta ")
# else:
#      print(f" {x} {y} dan katta")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
#Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar=['olma','shaftoli', 'suv','gilos','bodom', 'shokolad', 'cola', 'non', 'choy', 'salat']
# savat=[]
# for n in range(5):
#     savat.append(input(f"savatga {n+1} mahsulotni qoshing"))
    
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#      print(f"Bizda {mahsulot} bor") 
# else:
#       print(f"bizda bunday {mahsulot} yo'q")     
    
#TUSHUNILMADI UNCHALIK
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. 
# Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# mahsulotlar=['olma','shaftoli', 'suv','gilos','bodom', 'shokolad', 'cola', 'non', 'choy', 'salat']
# savat=[]
# for n in range(5):
#     savat.append(input(f"savatga {n+1} mahsulotni qo'shing"))
    
# bor_mahsulotlar=[]   
# mavjud_emas=[] 
# for mahsulot in savat:
#     bor_mahsulotlar.append(mahsulot)
# else:
#      mavjud_emas.append(mahsulot) 
     
# if mavjud_emas:
#          print(f"do'konimizda quyidagi {mahsulot} yo'q:")   
# for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#         print("siz so'ragan hamma mahsulot bor") 
       

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
#Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar=['nodir', 'botir','obid', 'sardor','sevara']
# foydalanuvchi=input("Yangi login kiriting")
# if foydalanuvchi in foydalanuvchilar:
#     print("Boshqa login kiriting")
# else:
#     print("Xush kelibsiz, foydalanuvchi")

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
# son=int(input("Butun son kiriting:"))
# for bolinuvchi in range(1,10):
#     if not(son%bolinuvchi):
#         print((f"{son} soni {bolinuvchi} ga qoldiqsiz bo'linadi"))

