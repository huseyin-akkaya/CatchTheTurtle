# Catch The Turtle Oyunu (Python)

Python'un yerleşik `turtle` grafik kütüphanesi kullanılarak geliştirilmiş, refleksleri test eden eğlenceli bir yakalama oyunudur.

## Özellikler
* **Zaman Sınırı:** Oyuncunun kaplumbağaları yakalamak için 10 saniyesi vardır (gerçek zamanlı geri sayım).
* **Rastgele Çıkışlar:** Ekranda belirli koordinatlarda rastgele beliren ve kaybolan hedefler.
* **Skor Takibi:** Tıklanan (yakalanan) her kaplumbağa için anlık olarak güncellenen skor sistemi.
* **Olay Yönetimi (Event Handling):** Fare tıklamalarını (`onclick`) anlık algılayarak skoru tetikleyen interaktif yapı.

## Kullanılan Teknolojiler
* Python
* `turtle` (Yerleşik Grafik Kütüphanesi)
* `random` Modülü

## Nasıl Çalıştırılır?

Proje tamamen yerleşik Python kütüphaneleri kullandığı için herhangi bir dış paket kurulumu (`pip install`) gerektirmez. Terminal üzerinden kodun bulunduğu dizine gidip doğrudan çalıştırabilirsiniz:

```bash
python main.py
