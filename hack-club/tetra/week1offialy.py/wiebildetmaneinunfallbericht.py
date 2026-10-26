import random
fragenliste=["Schreibt man einen Unfallbericht in Päteritum","Solte man einen Unfallbericht sachlichh schreiben","Solte man Persönliche gefühle in einen Unfallbericht benutzen","solte man die W-Frangen wo,wann, was,wie,warum und wofür in einen Unfallbericht"]
lösungen=["ja","ja","nein","nein"]
fragenlösungen=list(zip(fragenliste,lösungen))
random_index=random.randint(0,len(fragenliste)-1)
random_fragen =fragenliste[random_index]
print(random_fragen)

for word,correct_lösungen in fragenlösungen:
    print("\n"+ word)
    user_input = input ("Your answer : ")
    if user_input.strip()==correct_lösungen:
        print("Richtig")
    else:
        print(f"Falsch. Die Lösung ist :{correct_lösungen}")