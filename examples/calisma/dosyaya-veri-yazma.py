def dosyayaYazma(yazi):
    with open('yazilan-dosya.txt', 'w', newline='\r\n') as dosya:
        dosya.write(yazi)

if __name__ == "__main__":
    dosyayayazilacakveri = input("Dosyaya yazmak istediğiniz veri: ")
    dosyayaYazma(dosyayayazilacakveri)
