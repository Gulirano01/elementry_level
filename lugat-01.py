# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 09:30:25 2025

@author: User
"""

# car_0={'model':'ferrari', 'rang':'qizil'}
# # print(car_0['model'])
# # print(car_0['rang'])
# print(f"uning moshinasi {car_0['model']} rusumida")
# car_0['tezlik']='1000'
# car_0['egasi']='olimjon'
# talaba_1={}
# talaba_1['ism']='Lazizbek'
# talaba_1['familya']='Olimjonov'
# print(f" {talaba_1['ism'].title()} keldimi?")
# del talaba_1['ism']

# talaba_2={
#     'ism':'Botir',
#     'familya':'Qodirov',
#     'yosh':'23'
#     }
# print(f"{talaba_2['ism'].title()} keldimi?")
# talaba_3=talaba_2.get('adress','Bunday ism mavjud emas')
# print(talaba_3)
 #Vazifalar
#  otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
#Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# otam={'ism':'Baxtiyor','familya':'Aminov','yosh':'40'}
# ism=otam['ism']
# familya=otam['familya']
# yosh=otam['yosh']
# print(f"Otam {ism.title()} {familya.title()} {yosh} yoshda")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
#kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# taomlar={'ali':'osh',
#          'vali':'manti',
#          'nozim':'shurva',
#          'bahodir':'suzma',
#          'bobur':'mastava'
#          }
# print(f"Alining sevimli taomi {taomlar['ali']}.")
# print(f"Valining sevimli taomi {taomlar['vali']}.")
# print(f"boburning sevimli taomi {taomlar['bobur']}.")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
#(masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# python_lugat={'float':'son', 
#               'string':'harf', 
#               'input':'joyla',
#               'title':'bosh harf',
#               'get':'olish'
#               }



# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. 
#Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# soz=input("Kalit sozni kiriting:").lower()
# print(python_lugat.get(soz, "Bunday soz mavud emas"))

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
# soz=input("Kalit so'zni kiriting:").lower()
# tarjima=python_lugat.get(soz)
# if tarjima==None:
#     print('Bunday soz mavjud emas')
# else:
#     print(f"{soz.title()} teng {tarjima}ga.")    


# talaba_3={'ism':'ali','familya':'Valijonov','adress':'andijon'}
# # print(talaba_3.items())
# for kalit, qiymat in talaba_3.items():
#     print(f"Kalit:{kalit}")
#     print(f"Qiymat:{qiymat} \n")
    
# telefonlar={
#     'ali':'nokia',
#     'vali':'ipone',
#     'ozod':'galaxy'
#     }
# for k,y in telefonlar.items():
#     print(f"{k.title()}ning telefoni {y} \n" )
# print(telefonlar.keys())
# for key in telefonlar.keys():
#     print(key.title())
# print('Do\'kondagi mahsulotlar:')
# for mahsulot in telefonlar:
#     print(mahsulot.title())

# mahsulotlar={
#     'olma':'10000',
#     'olcha':'20000',
#     'uzum':'10000'
#     }

# bozorlik=['olma', 'turp', 'uzum', 'shokolad']

# for buyum in mahsulotlar:
#     if buyum in bozorlik:
#         print(f"{buyum.title()} {mahsulotlar[buyum]} som")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos bozorga {buyum}ni ham olib keling")
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# print('Dugonam bu pulllarni sarfladi:')
# for narx in set (mahsulotlar.values()):
#     print(narx)
    
# toys={"bear", "doll","rabbit",'doll'}
# print(toys)

# Amaliyot

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
#Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
# lugat={
#        'sets':'malumot turi',
#        'del':'ochirish',
#        'values':'qiymat',
#        'keys':'kalit',
#        'if':'agar',
#        'else':'agar',
#        'list':'royxat',
#        'print':'chop etmoq',
#        'reverse':'matnni teskari chiqaradi',
#        'range':'qator'
#        }

# for key, value in sorted(lugat.items()):
#     print(f"{key.title()}-{value}")

# Davlatlar va ularning poytaxtlari lug'atini tuzing. 
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
davlat_poytaxt={
    'uzbekistan':'toshkent',
    'qozogiston':'astana',
    'turkiya':'istanbul',
    'hindiston':'dehli'
    }

# print('Davlatlar:')
# for davlat in sorted(davlat_poytaxt):
#     print(davlat.upper())
# print('Poytaxtlar:')    
# for poytaxt in sorted(davlat_poytaxt.values()):
#     print(poytaxt.title())    

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# country=input("davlatni kiriting:")
# capital=davlat_poytaxt.get(country)
# if capital==None:
#     print(f"Kechirasiz, bizda bunday {country} yo'q")
# else:
#     print(f"{country}ning poytaxti {capital}")
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting)
# menu={
#       'osh':'30000',
#       'mastava':'20000',
#       'chuchvara':'25000',
#       'g\'ja':'20000',
#       'sho\'rva': '35000',
#       'assarti':'40000',
#       'manti':'32000'
#       }
# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")

# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.


# print('4 ta taom buyurtma bering')
# buyurtma=[]
# for n in range(4):
#     buyurtma.append(input(f"{n+1}-taom:").lower())
    
# for buyurtmalar in buyurtma:
#         if buyurtmalar in menu:
#             print(f"{buyurtmalar.title()} {menu[buyurtmalar]} so'm")
#         else:
#             print(f"Bizda bunday {buyurtmalar} yo'q")



# print("Do'stlaringiz ismini kiriting:")
# ismlar=[]
# n=1
# while True:
#     savol=f"{n}-do'stingizni kiriting:"
#     ism=input(savol)
#     ismlar.append(ism)
#     takrorlash=input("Yana ism kiritasizmi(ha/yo'q)")
#     n+=1
#     if takrorlash!='ha':
#         break

# print("Do'stlaringiz yoshini ko'rsatuvchi dastur")
# ismlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingiz ismini kiriting:")
#     yosh=input(f"{ism.title()}ning yoshi nechada?")
#     ismlar[ism]=int(yosh)
    
    
#     takror=input("yana ism kiritasizmi?yes/no")
#     if takror=='no':
#         ishora=False
# for ism,yosh in ismlar.items():
#     print(f"{ism.title()} {yosh}da")        
 
# mashinalar=['lasetti','nexia','porsh', 'nexia']
# while 'nexia' in mashinalar:
#     mashinalar.remove('nexia')
# print(mashinalar)    

# talabalar=['hasan','husan','sherzod','hoshim']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     savol=input(f"{talaba.title()}ning bahosi nechchi?")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba]=int(savol)
# print(baholangan_talabalar)    
    
#Amaliyot
#1. Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# print("Foydalanuvchidan buyurtma qabul qiluvchi dastur")
# mahsulot=[]
# n=1
# ishora=True
# while ishora:
#     buyurtma=input(f"{n}-buyurtmani kiriting:")
#     takror=input("Yana buyurtma berasizmi?ha/yo'q")
#     mahsulot.append(buyurtma)
#     n+=1
#     if takror!='ha':
#         ishora=False
# print(mahsulot)        

#2.e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
#Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# print("mahsulot va uning narxini ko'rsatuvchi dastur")
# mahsulot={}
# n=1
# while True:
#     narsa=input("Xohlagan mahsulotingizni kiriting:")
#     narx=input(f"{narsa}ning narxini kiriting:")
#     mahsulot[narsa]=int(narx)
#     takror=input("Yana mahsulot kiritasizmi?ha/yo'q:")
#     n+=1 
#     if takror!='ha':
#         break
# print(mahsulot)    
    
#3.Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi 
# mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa 
# mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")







