import sqlite3

baglanti = sqlite3.connect("galeri.db")

imlec = baglanti.cursor()

def tablo_oluşturma():

    imlec.execute("CREATE TABLE IF NOT EXISTS otomobil (Marka TEXT,MODEL INT,Yakıt_Tipi TEXT,Renk TEXT,Vites_Tipi TEXT,Km INT)")

    baglanti.commit()

def araba_ekleme(marka,model,yakit_tipi,renk,vites_tipi,km):

    imlec.execute("INSERT INTO otomobil VALUES(?,?,?,?,?,?)",(marka,model,yakit_tipi,renk,vites_tipi,km))

    baglanti.commit()


marka = input("Marka giriniz :")
model = int(input("Otomobil kaç model?\n"))
yakit_tipi = input("Yakıt tipini giriniz :")
renk = input("Aracın rengini giriniz :")
vites_tipi = input("Vites Tipini giriniz :")
km = int(input("Otomobil kaç KM'de?\n"))

araba_ekleme(marka,model,yakit_tipi,renk,vites_tipi,km)

baglanti.close()