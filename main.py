from googletrans import Translator  # kütüphane eklenir

url = input("kelime giriniz  : ")# genel olarak dil girilebilir
Translate = Translator() # çeviri burada yapılıyor
cevir = Translate.translate(url, dest='en') #burda(dest'istediğimiz dil ') çevrilir
print(cevir.text) # ekrana yazdırılır...

#googletrans
#pip instal googletrans "4.0.0rc1"  sürümü yüklenmeli yoksa sürüm hata veriyor..