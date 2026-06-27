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

brakujace_wiersze = df1[~df1['Nazwa'].isin(df2['Nazwa'])] 
                                    # Odfiltrowanie wierszy z df1, w których "Nazwa" nie znajduje się w df2

print(brakujace_wiersze)            #  Wyświetlenie wyniku

brakujace_wiersze.to_csv('brakujace_wiersze.csv', index=False, encoding='utf-8-sig')  
                                    # Zapisanie brakujących wierszy do pliku CSV