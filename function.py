import datetime

def palindrome(text :str)->str:
       if(text == text[::-1]):
            return "Bien dit!"
       else:
            return text[::-1]
       

def greeting()->str:
    heure = datetime.datetime.now().hour
    if(6<=heure<12):
       return "Bonjour"
    else:
        if(12<=heure<19):
            return "Bonne après-midi"
        else:
             return "Bonsoir"
            