from menuHandler import TakeInput
import time

while True:
    print("Veuillez choisir une action à réaliser :")
    print(
        "1. Afficher les mots les moins importants \n"
        "2. Afficher le mot le plus important \n"
        "3. Afficher le mot le plus répété \n"   
        "4. Afficher les présidents qui ont parlé du mot que vous choisirez \n"
        "5. Afficher le président qui a le plus parlé du mot que vous choisirez \n"
        "6. Afficher quel président a dit en premier le mot que vous choisirez \n"
        "7. Afficher les mots que tous les présidents ont dit \n"
        "8. Afficher la matrice TFIDF \n"
        "9. Arrêter le programme :("
    )

    userinput = int(input("Saisissez votre choix : "))
    if userinput == 9:
        break
    TakeInput(userinput)
    time.sleep(5)
print("Bye Bye, à la revoyure les coupains !")


