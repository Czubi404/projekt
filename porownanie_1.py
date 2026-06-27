import pandas as pd

df1 = pd.read_csv(r'C:\Users\jaski\Desktop\wyszukiwanie\dane_1.csv')     
df2 = pd.read_csv(r'C:\Users\jaski\Desktop\wyszukiwanie\dane_2.csv')
                                    # Wczytanie obu plików CSV do DataFrame'ów
print(df1.head())                   # Wyświetlenie pierwszych 5 wierszy ramki danych
print(df2.head())

df1["Nazwisko"] = df1["Nazwisko"].str.upper()           # Zamiana liter na duże w kolumnach "Nazwisko" i "Imię"
df1["Imię"] = df1["Imię"].str.upper()   
df2["Nazwisko"] = df2["Nazwisko"].str.upper()          
df2["Imię"] = df2["Imię"].str.upper()  


df_polaczone = pd.merge(df1, df2, on='Nazwa', suffixes=('_plik1', '_plik2'))
                                    # Połączenie plików na podstawie wspólnego identyfikatora 'Nazwa'
                                    # Kolumny o tych samych nazwach dostaną przyrostki _plik1 i _plik2

roznice = df_polaczone[df_polaczone['Nazwisko_plik1'] != df_polaczone['Nazwisko_plik2']]
                                    # Znalezienie wierszy, w których wartości w kolumnie 'Nazwisko' różnią się między plikami
print(roznice)                      # Wyświetlenie wyniku

roznice.to_csv('roznice.csv', index=False)  
                                    # Zapisanie różnic do pliku CSV