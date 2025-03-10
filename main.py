uczestniczki = {
    "Aneta": 52,
    "Marta": 28,
    "Ewelina": 30,
    "Ewa": 30,
    "Natalia": 35,
    "Waleria": 28,
    "Josephine": 28,
    "Klaudia_N": 23,
    "Edyta": 37,
    "Monika": 30,
    "Wiktoria": 26,
    "Klaudia_K": 34
}

pierwsza_uczestniczka = input("Wybierz pierwszą uczestniczkę: ")
druga_uczestniczka = input("Wybierz drugą uczestniczkę: ")


def roznica_wieku(imie1, imie2):
    if imie1 in uczestniczki and imie2 in uczestniczki:
        wiek1 = uczestniczki[imie1]
        wiek2 = uczestniczki[imie2]
        roznica = abs(wiek1 - wiek2)
        return f"Różnica wieku między {imie1} a {imie2} wynosi {roznica} lat."
    else:
        return "Podano nieprawidłowe imię!"


print(roznica_wieku(pierwsza_uczestniczka, druga_uczestniczka))