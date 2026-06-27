import pandas as pd
#from Levenshtein import distance
from rapidfuzz import fuzz

print("Podaj szukane nazwisko:  ")                          # Wczytanie szukanego nazwiska
szukane_nazwisko = input().upper()
print("szukane nazwisko: ", szukane_nazwisko)

df = pd.read_csv('dane.csv')                                # Wczytanie pliku CSV do obiektu DataFrame
df["Nazwisko"] = df["Nazwisko"].str.upper()                 # Zamiana liter na duże w kolumnie "Nazwisko"
df["Imię"] = df["Imię"].str.upper()                         # Zamiana liter na duże w kolumnie "Imię"

print(df.head())                                            # Domyślnie zwraca 5 pierwszych wierszy
#print(df.tail(2))                                           # Zwraca 2 ostatnie wiersze


if szukane_nazwisko in df["Nazwisko"].values:               # Szuka nazwiska w kolumnie "Nazwisko" i zwraca True lub False
      print("Znaleziono nazwisko: ", szukane_nazwisko)     
      print(df.loc[df.Nazwisko == szukane_nazwisko])        # Wyświetla rząd z szukanym nazwiskiem
else:
     print("Nie znaleziono nazwiska: ", szukane_nazwisko)
     if szukane_nazwisko in df["Imię"].values:              # Szuka nazwiska w kolumnie "Nazwisko" i zwraca True lub False
         print("Znaleziono nazwisko w kolumnie Imię: \n", df.loc[df.Imię == szukane_nazwisko])     
                                                            # Wyświetla rząd z szukanym nazwiskiem wpisanym w kolumnie imię
     else:
         print("Nie znaleziono nazwiska w kolumnie Imię: ", szukane_nazwisko)
     print("Minimalne podobieństwo procentowe to 60%")
     for i in df["Nazwisko"].values:
         if fuzz.ratio(szukane_nazwisko, i)   > 60:             # Oblicza procentowe podobieństwo szukanego nazwiska do nazwisk w kolumnie "Nazwisko"
             print("Znaleziono podobne nazwisko: ", i)          # Wyświetla podobne nazwisko
             print(df.loc[df.Nazwisko == i])                    # Wyświetla rząd z podobnym nazwiskiem
     
     

 

# df.to_csv("nowy_plik.csv", index=False)     # Utworzenie nowego pliku CSV z danymi z DataFrame
# df.to_excel("nowy_plik.xlsx", index=False)
# Obliczanie podobieństwa procentowego (0 - 100)



