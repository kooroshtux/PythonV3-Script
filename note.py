print ("Entrer votre note: ")
note=float(input()) or int(input())

if note < 10:
    print ("Vous avez échoué votre exam")
elif note == 10 or note > 10:
    print ("Vous avez validé votre exam :)")
else:
    print ("Vous avez entré aucune note")


 
