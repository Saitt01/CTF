import cryptocode

#Stringa criptata presa da /home/aleks/.local/share/pswm/pswm
encrypted_data = "e9laWoKiJ0OdwK05b3hG7xMD+uIBBwl/v01lBRD+pntORa6Z/Xu/TdN3aG/ksAA0Sz55/kLggw==*xHnWpIqBWc25rrHFGPzyTg==*4Nt/05WUbySGyvDgSlpoUw==*u65Jfe0ml9BFaKEviDCHBQ=="

#Path della wordlist (es. rockyou.txt, quella che ho utilizzato io)
wordlist_path = "INSERISCI QUI"

#Funzione Principale
def brute_force():
    #Apro la wordlist in modalità lettura, utilizzando latin-1 perche nel caso specifico, rockyou ha caratteri speciali
    with open(wordlist_path, "r", encoding="latin-1") as file:
    	#Faccio partire il ciclo
        for i, line in enumerate(file):
            password = line.strip()
            decrypted = cryptocode.decrypt(encrypted_data, password)
            if decrypted:
                print("\nPassword trovata!")
                print(f"Master password: {password}")
                print(f"Contenuto decifrato:\n{decrypted}")
                return
    print("Nessuna password valida trovata.")

if __name__ == "__main__":
    brute_force()
