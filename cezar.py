veta=input("zadaj vetu na šifrovanie")
posun=input("zadaj o kolko sa ma text posunut")

def cezarova_sifra(veta,posun):
    vysledok=""
    for znak in veta:
        if (97>=ord(znak) and ord(znak)<=122):
            vysledok+=chr((ord(znak)-97+posun)%26+97)
            znak=ord(znak)
            znak1=znak-97
            znak2=znak+posun
            znak3=znak2%26
            znak4=znak3+97
            vysledok=chr(znak4)
    return output

