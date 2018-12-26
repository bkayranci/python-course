import time

class Hoca(object):
    def __init__(self, ad, ogrenciler=list()):
        self.yas = 0
        self.isim = ad
        self.ogrencilerim = ogrenciler

    def yasa(self):
        self.uyan()
        self.kahvaltiyap()
        self.okulagel()
        self.ogrencilerinizisayin()
        self.sinavhazirla()
        self.sinavyap()
        self.sinavbitir()
        self.sinavlarioku()
        print(self.sorusor("gunaydın hocam, sinavları okudunuz mu?"))
        self.sinavlariilanet()
        self.evegit()
        self.uyu()
    
    def ogrencilerinizisayin(self):
        for ogrencim in self.ogrencilerim:
            print(ogrencim.isim)
    
    def sorusor(self, soru):
        if soru == 'gunaydın hocam, sinavları okudunuz mu?':
            return True
        else:
            return False

    def uyan(self):
        print("Günaydın...")

    def kahvaltiyap(self):
        print("..mmm güzel bi kahvaltı")

    def okulagel(self):
        print("okula geldim")

    def sinavhazirla(self):
        print("bu soruyu da sormalıyım")

    def sinavyap(self):
        print("silmek için süre vereceğim")

    def sinavbitir(self):
        print("geçmekte kalmakta bir ekip işidir, geçmekte kalmakta...")

    def sinavlarioku(self):
        for ogrencim in self.ogrencilerim:
            ogrencim.notum = 30
    
    def sinavlariilanet(self):
        for ogrencim in self.ogrencilerim:
            print(ogrencim.isim, ogrencim.notum)

    def evegit(self):
        print("beeeen geldiiiiimmm...")

    def uyu(self, zaman = 2):
        print("zzz...")
        time.sleep(zaman)
        self.yas += 1


class Ogrenci(object):
    def __init__(self, ad):
        self.isim = ad
        self.notum = 0


if __name__ == "__main__":
    turkalp = Ogrenci("turkalp")
    yunus = Hoca("yunus", [turkalp])
    
    while True:
        yunus.yasa()

        if yunus.yas > 2:
            break
        else:
            continue