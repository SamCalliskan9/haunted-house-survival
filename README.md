# haunted-house-survival
Description  “PyGame tabanlı mini survival-horror mekanikleri: karakter hareketi, çarpışma algılama, rastgele paranormal olay tetikleme, ışık daralması, temel AI.”

#  Haunted House Mini Game – Basic Algorithm Version  
**Türkçe & English README**

---

# 🇹🇷 Türkçe Açıklama

##  Proje Hakkında
Bu proje, terk edilmiş ve paranormal olayların yaşandığı bir evde geçen **basit bir oyun mekaniği** örneğidir.  
Amaç: Karakterin karanlık bir evin içinde gezinmesini, odalar arasında geçiş yapmasını ve rastgele tetiklenen paranormal olaylarla karşılaşmasını sağlamak.

Bu proje:
- Temel algoritmalar,
- `if-else` karar yapıları,
- `random` ile olay üretme,
- Fonksiyon kullanımı,
- Basit oyun döngüsü (game loop)

gibi **oyun geliştirmenin temel yapı taşlarını öğretir** ve portföy için uygundur.

---

##  Kullanılan Temel Yapılar

###  Fonksiyonlar (`def`)
Kod parçalarını düzenli çalıştırmak için kullanılır.  
Örneğin: `move_player()`, `random_event()`

###  Karar Yapısı (`if / elif / else`)
Oyuncu seçimlerine göre evin içinde yönlendirir.

###  Rastgele Olaylar (`random`)
Evdeki paranormal olayların tahmin edilemez olmasını sağlar.

###  Döngü (game loop)
Oyun bitene kadar tekrar eder:  
Oyuncu → Komut girer → Oyun cevap verir → Döngü devam eder.

---

##  Oyun Hikâyesi (Kısa)
Karakter, demir çitleri kırılmış, bacası şato kulesini andıran, camları kırık terk edilmiş bir eve girer.  
Evin içinde yürüdükçe **rasgele paranormal olaylar** tetiklenir.

---

##  Çalıştırma

```bash
python haunted_game.py

Dosya Yapısı
haunted-house/
  haunted_game.py   # oyun kodu
  README.md         # proje açıklaması (bu dosya)

##  Gelecek Geliştirmeler

•Gerçek harita sistemi
•Envanter mekaniği
•Ses efektleri
•2D/3D hareket (Pygame / Unity)

🇬🇧 English Description
## About The Project

This project is a simple gameplay mechanic prototype set in an abandoned, eerie house where paranormal activity occurs.
The goal is to let the player navigate the house, move between rooms, and trigger random paranormal events.

This teaches:

•Basic algorithms,
•if-else decision structures,
•Random event generation,
•Functions,
•A simple game loop
Perfect for portfolios and beginners aiming at game development or software roles.

## Core Concepts Used

## Functions (def)
Organizes game mechanics like move_player() or random_event().

## Conditions (if / elif / else)
Directs the player based on commands.

## Randomness (random)
Creates unpredictable paranormal encounters.

## Loop (game loop)
Repeats until the game ends:
Player → Input → Game response → Continue.

## Brief Story
You enter a decayed house with a broken gate, castle-like chimney, shattered windows, and a chilling atmosphere.
As you walk inside, random supernatural events occur.

## Run the Game
python haunted_game.py

 Folder Structure
haunted-house/
  haunted_game.py
  README.md

## Future Improvements

• Real map system
• Inventory and items
• Sound events
• Advanced movement using Pygame/Unity

## License
This project is free to use for educational and portfolio purposes.

