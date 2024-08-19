# Taş, Kağıt, Makas Oyunu

Bu proje, Python kullanarak geliştirilmiş klasik **Taş, Kağıt, Makas** oyununu içermektedir. Oyun, bir kullanıcı ile bilgisayar arasında oynanır. Oyun, bir oyuncunun iki tur kazanmasıyla sona erer. Her oyundan sonra, hem kullanıcıya hem de bilgisayara başka bir oyun oynamak isteyip istemedikleri sorulur.

## Proje Özeti

Oyun şu kurallara uyar:
- Taş, Makas'ı yener.
- Makas, Kağıt'ı yener.
- Kağıt, Taş'ı yener.

İlk iki turu kazanan oyuncu oyunu kazanır.

## Özellikler

- **Birden Fazla Tur**: Oyun, bir oyuncu iki tur kazanana kadar devam eder.
- **Kullanıcı Girdisi Doğrulama**: Kullanıcının geçerli bir seçenek (Taş, Kağıt, Makas) girmesi sağlanır.
- **Bilgisayar Seçimi**: Bilgisayarın seçimi rastgele olarak belirlenir.
- **Devam Etme İsteği**: Her oyundan sonra kullanıcı ve bilgisayara oyuna devam etmek isteyip istemedikleri sorulur.
- **Oyun Sonuçları**: Her turun sonucu ve genel oyun sonucu ekrana yazdırılır.

## Çalıştırma

1. **Depoyu Klonlayın**
    ```bash
    git clone https://github.com/kullaniciadiniz/tas-kagit-makas.git
    cd tas-kagit-makas
    ```

2. **Oyunu Çalıştırın**
    Python'un yüklü olduğundan emin olun (Python 3.6 veya daha yeni bir sürüm önerilir). Oyun script'ini Python ile çalıştırın:
    ```bash
    python tas_kagit_makas_beyza_avci.py
    ```

## Teknik Detaylar

- **Programlama Dili**: Python
- **Random Modülü**: Bilgisayarın rastgele seçimler yapması için kullanılır.
- **Girdi İşleme**: Kullanıcı girdisi işlenir ve geçerli seçeneklerden biri olup olmadığı doğrulanır.
- **Oyun Mantığı**: Tur başına kazananı belirlemek ve puanları güncellemek için koşullu ifadeler kullanılır.

## Kod Yapısı

- **Fonksiyon**: `tas_kagit_makas_beyza_avci()`
  - Karşılama mesajı ve oyun kurallarını gösterir.
  - Oyun değişkenlerini (oyun sayısı, oyuncu ve bilgisayar puanları) başlatır.
  - Tur tur oyun oynama işlemini gerçekleştiren ana döngüyü içerir.
  - Her oyundan sonra devam etme isteğini kullanıcıya ve bilgisayara sorar.
  - Puanlara göre oyun kazananını belirler ve sonucu ekrana yazar.

## Örnek Kullanım

```python
import random

def tas_kagit_makas_beyza_avci():
    # Oyun kodu burada
    ...
