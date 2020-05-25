# tugamaydigan tsikl yasash lekin ehtiyot bolish kerak agar while True: va keyingi qatorga print yozilsa komp qotib qolishi ham mumkin
# while True:
#     pass

# 0dan 10gachan sanaydigan tsikl yasash va print yordamida uni terminalga chiqarish
for sanash in range(0, 10):
    print(sanash)

# if operatori shartni tekshirish uchun ishlatiladi: agar shart to'g'ri bo'lsa, birinchi ifodalar bloki bajariladi (bu blok "if — blok" deb nomlanadi), aks xolda keyingi ifodalar bloki bajariladi (bu blok "else — blok" deb nomlanadi). "else" blokining bo'lishi majburiy emas.
number = 23
guess = int(input("Butun son kiriting : "))

if guess == number:

    print("Tabriklayman, siz topdingiz,")
    # Bu yerda yangi blok boshlanadi

    print("(ammo xech qanday sovg'a yutmadingiz!)")
    # Bu yerda yangi blok tugaydi

elif guess not in number:

    print("Yo'q, o'ylangan son kiritilgan sondan kattaroq.")
    # Yana bir blok

    # Blok ichida nima xoxlasangiz bajarishingiz mumkin ...

else:

    print("Yo'q, o'ylangan son kiritilgan sondan kichikroq.")

    # Bu blokka tushish uchun kiritilgan guess soni oldindan o'ylangan

    #number sonidan katta bo'lishi kerak
    print("Tamom.")
    # Bu oxirgi ifoda doimo yuqoridagi ifodalardan so'ng bajariladi.

