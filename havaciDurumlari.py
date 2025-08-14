import requests


API_ANAHTARI = "f1a8491ecb5e988ee2da123f13f43cef"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def hava_durumunu_getir(sehir):
   
    complete_url = f"{BASE_URL}appid={API_ANAHTARI}&q={sehir}&lang=tr&units=metric"

    try:
       
        response = requests.get(complete_url)
        response.raise_for_status()  

        veri = response.json()

       
        if veri["cod"] != "404":
            ana_veri = veri["main"]
            sicaklik = ana_veri["temp"]
            hissedilen_sicaklik = ana_veri["feels_like"]
            nem = ana_veri["humidity"]
            hava_durumu = veri["weather"][0]["description"]
            ruzgar_hizi = veri["wind"]["speed"]

            print(f"\nŞehir: {sehir}")
            print(f"Sıcaklık: {sicaklik}°C")
            print(f"Hissedilen Sıcaklık: {hissedilen_sicaklik}°C")
            print(f"Nem Oranı: {nem}%")
            print(f"Hava Durumu: {hava_durumu.capitalize()}")
            print(f"Rüzgar Hızı: {ruzgar_hizi} m/s")

        else:
            print("Şehir bulunamadı.")
    
    except requests.exceptions.RequestException as e:
        print(f"Bir hata oluştu: {e}")


if __name__ == "__main__":
    print("Hava Durumu Uygulamasına Hoş Geldiniz!")
    
    while True:
        sehir_adi = input("\nHava durumunu öğrenmek istediğiniz şehir adını girin (Çıkmak için 'q'): ").strip()
        
        if sehir_adi.lower() == 'q':
            print("Uygulamadan çıkılıyor...")
            break
        
        hava_durumunu_getir(sehir_adi)