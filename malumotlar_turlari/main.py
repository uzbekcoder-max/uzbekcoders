# komentariya har doim # belgisidan boshlanadi

# tip str
f_str = "Uzbek coders created in "

# tip int
f_int = 2020

# tip str keyingi qatorga otkazish korsatilgan keyingi qatorga otkazish "\n" yordamida boladi
f_str_2 = " Uzbek coders \nbest \nof \nthe \nbest"

# tip sozlarni bir biriga qoshish "+"<<yordamida ruschada "konkatenatsiya"
f_const = f_str + str(f_int) + f_str_2

# input odamdan javob olishga ishlatiladi
inp = input("!: ")


# operator "if" "else" ingiliz tilini biladiganlar if nimaligini chunadi bilmaydiganlar uchun if bu agar degani
if inp == "uzbek_coders_best":
    # print ni hamma biladi manimcha
    print(f_const)

# else degani bu agar if to'g'ri kelmasa shuni bajar degani
else:
    print('Fuck you')