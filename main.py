import random as r
from tkinter import *

# inicjalizacja okna i startowych zmiennych
root = Tk()
root.title("Kolko i krzyzyk")
move = 0

plansza = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# sprawdza, czy plansza nie jest pelna
def czyRuch(plansza):
    for i in range(3):
        for j in range(3):
            if (plansza[i][j] == "_"):
                return True
    return False


# nadaje wartości danym sytuacja -> wygrana komputera = 10, gracza = -10, remis = 0
def wartosci(plansza):
    # sprawdzenie wierszy
    for i in range(3):
        if (plansza[i][0] == plansza[i][1] == plansza[i][2] == 'O'):
            return 10

        elif (plansza[i][0] == plansza[i][1] == plansza[i][2] == 'X'):

            return -10
    # sprawdzenie kolumn
    for i in range(3):
        if (plansza[0][i] == plansza[1][i] == plansza[2][i] == 'O'):
            return 10

        elif (plansza[0][i] == plansza[1][i] == plansza[2][i] == 'X'):
            return -10
    # sprawdzenie przekątnych
    if (plansza[0][0] == plansza[1][1] == plansza[2][2] == 'O'):
        return 10

    elif (plansza[0][0] == plansza[1][1] == plansza[2][2] == 'X'):
        return -10

    if (plansza[2][0] == plansza[1][1] == plansza[0][2] == 'O'):
        return 10

    elif (plansza[2][0] == plansza[1][1] == plansza[0][2] == 'X'):
        return -10
    return 0


# algorytm minimax
def min_max(plan, czyMax):
    # zarządzanie wartościami
    score = wartosci(plan)
    if score == 10:
        return score
    if score == -10:
        return score
    if not czyRuch(plan):
        return 0
    # dla komputera => szukanie najlepszej sytuacji
    if czyMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if plan[i][j] == "_":
                    plan[i][j] = "O"
                    best = max(best, min_max(plan, not czyMax))
                    plan[i][j] = "_"
        return best
    # dla gracza => szukanie najgorszej sytuacji
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if plan[i][j] == "_":
                    plan[i][j] = "X"
                    best = min(best, min_max(plan, not czyMax))
                    plan[i][j] = "_"
        return best


# funkcja znajdująca najlepszy ruch dla komputera korzystając z min_max
def naj_ruch(plansza):
    plan = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    for i in range(3):
        for j in range(3):
            if plansza[i][j].cget('text') == "":
                plan[i][j] = "_"
            else:
                plan[i][j] = plansza[i][j].cget('text')
    naj_war = -1000
    najlepszy_ruch = (-1, -1)
    for k in range(3):
        for l in range(3):
            if plan[k][l] == "_":
                plan[k][l] = "O"
                wartosc = min_max(plan, False)
                plan[k][l] = "_"
                if wartosc > naj_war:
                    najlepszy_ruch = (k, l)
                    naj_war = wartosc
    return najlepszy_ruch


# funkcja losowo wybierająca wolne miejsce (może być użyta jako poziom łatwy)
def wybierz_miejsce(plansza):
    tab = []
    for i in range(3):
        for j in range(3):
            if plansza[i][j].cget('state') != 'disabled':
                tab.append([i, j])
    z = r.choice(tab)
    return z


# wyświetlanie komunikatu w oknie
def wyswietl_komunikat(tekst):
    text_label = Label(root, text=tekst)
    text_label.grid(row=3, column=0, columnspan=3)


# sprawdzanie stanu gry => analogicznie do przypisywania wartości
def sprawdz_stan(plansza):
    # wiersze
    for i in range(3):
        if (plansza[i][0].cget('text') == plansza[i][1].cget('text') == plansza[i][2].cget('text') == 'O'):
            wyswietl_komunikat("Gracz z kolkami wygral!")

        elif (plansza[i][0].cget('text') == plansza[i][1].cget('text') == plansza[i][2].cget('text') == 'X'):

            wyswietl_komunikat("Gracz z krzyzykami wygral!")
    # kolumny
    for i in range(3):
        if (plansza[0][i].cget('text') == plansza[1][i].cget('text') == plansza[2][i].cget('text') == 'O'):
            wyswietl_komunikat("Gracz z kolkami wygral!")

        elif (plansza[0][i].cget('text') == plansza[1][i].cget('text') == plansza[2][i].cget('text') == 'X'):
            wyswietl_komunikat("Gracz z krzyzykami wygral!")
    # przekątne
    if (plansza[0][0].cget('text') == plansza[1][1].cget('text') == plansza[2][2].cget('text') == 'O'):
        wyswietl_komunikat("Gracz z kolkami wygral!")

    elif (plansza[0][0].cget('text') == plansza[1][1].cget('text') == plansza[2][2].cget('text') == 'X'):
        wyswietl_komunikat("Gracz z krzyzykami wygral!")

    if (plansza[2][0].cget('text') == plansza[1][1].cget('text') == plansza[0][2].cget('text') == 'O'):
        wyswietl_komunikat("Gracz z kolkami wygral!")

    elif (plansza[2][0].cget('text') == plansza[1][1].cget('text') == plansza[0][2].cget('text') == 'X'):
        wyswietl_komunikat("Gracz z krzyzykami wygral!")


# po wciśnięciu przycisku
def clicked(r, c):
    global move
    # jeśli ruch gracza zmiana tam gdzie nacisnął
    if move % 2 == 0:
        plansza[r][c].configure(text='X', state='disabled')
        sprawdz_stan(plansza)
    # warunek remisu
    if move == 8:
        wyswietl_komunikat("Remis")
    move += 1
    # jeśli runda komputera => znajduje najlepszy ruch
    if (move % 2 == 1) and (move != 9):
        n = naj_ruch(plansza)
        # level łatwy n= wybierz_miejsce(plansza)
        plansza[n[0]][n[1]].configure(text='O', state='disabled')
        sprawdz_stan(plansza)
        move += 1


# inicjalizacja planszy
for i in range(3):
    for j in range(3):
        plansza[i][j] = Button(
            height=4, width=8,
            command=lambda r=i, c=j: clicked(r, c))
        plansza[i][j].grid(row=i, column=j)
root.mainloop()
