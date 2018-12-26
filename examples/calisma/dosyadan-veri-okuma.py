import csv

def dosyadanOku():
    with open('deneme.csv', 'r') as dosya:
        isimler = csv.DictReader(dosya)
        for i in isimler:
            print(i['isim'], i['soyisim'])
                


if __name__ == "__main__":
    dosyadanOku()
