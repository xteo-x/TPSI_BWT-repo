Parola = input("inserisci Parola");

Stringa = Parola + "$"
i = 0

while i < len(Stringa):
    rotazioni.append(Stringa[i:]+Stringa[:i])
    i+1
    print(Stringa)

