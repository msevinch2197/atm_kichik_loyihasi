plastik_parol = 2020
plastik_balans = 200_000
foiz = 0.01

sorov = int(input("Karta parolini kiriting: "))

if sorov == plastik_parol:
    while True:
        print("\nSo'rovni tanlang: ")
        print("1 - Balansni ko'rish")
        print("2 - Naqd pul olish")
        print("0 - Chiqish")

        tanlov = int(input("Tanlovingiz: "))

        if tanlov == 1:
            print(f"Balansingiz: {plastik_balans}")

        elif tanlov == 2:
            print("\nSummani tanlang: ")
            print("1 - 50_000")
            print("2 - 100_000")
            print("3 - 200_000")
            print("4 - 500_000")
            print("5 - Boshqa summa")


            tanlov_summa = int(input("Tanlovingiz: "))

            if tanlov_summa == 1:
                summa = 50_000
            elif tanlov == 2:
                summa = 100_000
            elif tanlov_summa == 3:
                summa = 200_000
            elif tanlov_summa == 4:
                summa = 500_000
            elif tanlov_summa == 5:
                summa = int(input("Summani kiriting: "))
            else:
                print("Noto'g'ri tanlov!")
                continue

            kam = int(summa * foiz)
            plastik_balans -= kam
            print(f"Bizning kamissiyamiz: {kam}")


            if summa <= plastik_balans:
                plastik_balans -= summa
                print("Pul muvaffaqiyatli yechildi.")
                print("Qolgan balans: ", plastik_balans)

            else:
                print("Balans yetarli emas!")

        elif tanlov == 0:
            print("Bankomatdan chiqildi.")
            break

        else:
            print("Noto'g'ri tanlov!")

else:
    print("Parol xato!")





























