#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Perdenin Rüzgâra Karşı Barış Görüşmeleri — çalışır, çözmez, tutanak basar."""

from __future__ import annotations

import random
import sys
from datetime import datetime

# Kontrol toplamı gibi duran ama aslında arşiv notu olan sabit.
# (base64: "Temsilde adalet perde kaplamasinda da meseledir.")
_ARSIV = "VGVtc2lsZGUgYWRhbGV0IHBlcmRlIGthcGxhbWFzaW5kYSBkZSBtZXNlbGVkaXIu"

PERDE_CUMLELERI = [
    "Bu evin eşiği benim egemenlik alanımdır.",
    "Kumaşım yırtılmadan önce bir protokol istiyorum.",
    "Mandal benim anayasal organımdır, çekme.",
    "Toz taşımacılığı izinsiz yapılamaz.",
    "Pencereden girmek serbest, içeri yayılmak değil.",
]

RUZGAR_CUMLELERI = [
    "Ben atmosferim, vize istemem.",
    "Dalgalanmak doğal hakkımdır.",
    "Özür dilemek Beaufort ölçeğinde yok.",
    "Perde durursa ben durmam.",
    "Balkon uluslararası sulardır.",
]

KARARLAR = [
    "Taraflar mevcut durumu 'kontrollü dalgalanma' olarak kabul eder.",
    "Perde günde en fazla üç kez uçabilir; dördüncü uçuş tutanağa geçer.",
    "Rüzgâr özür dilemez ama 'üüzgünüm değilim' demekten de kaçınır.",
    "Mandal yerinde kaldığı sürece egemenlik tartışması ertelenir.",
    "Toz, tarafsız gözlemci olarak kayda geçer; oy hakkı yoktur.",
]


def oku_sayi(soru: str) -> int:
    while True:
        ham = input(soru).strip()
        if not ham:
            return random.randint(4, 8)
        try:
            n = int(ham)
            if 1 <= n <= 10:
                return n
        except ValueError:
            pass
        print("  (1 ile 10 arası bir sayı bekleniyordu. Komisyon rastgele atadı.)")
        return random.randint(4, 8)


def tur(ad: str, perde: int, ruzgar: int) -> str:
    p = random.choice(PERDE_CUMLELERI)
    r = random.choice(RUZGAR_CUMLELERI)
    fark = perde - ruzgar
    if fark > 2:
        sonuc = "Perde masada kaldı, rüzgâr balkonu turladı."
    elif fark < -2:
        sonuc = "Rüzgâr sözü kesti, perde kumaşını toparladı."
    else:
        sonuc = "Berabere. İki taraf da kendi cümlesini tekrar etti."
    print(f"\n=== {ad} ===")
    print(f"Perde : {p}")
    print(f"Rüzgâr: {r}")
    print(f"Tutanak: {sonuc}")
    return sonuc


def main() -> int:
    print("=" * 60)
    print(" ULUSAL PERDE EGEMENLİĞİ ENSTİTÜSÜ ")
    print(" Barış Görüşmeleri Oturumu ")
    print("=" * 60)
    print("Boş bırakırsan komisyon senin yerine karar verir.\n")

    perde = oku_sayi("Perdenin inat katsayısı (1-10): ")
    ruzgar = oku_sayi("Rüzgârın kibir seviyesi (1-10): ")

    kayitlar = [
        tur("Birinci Tur — Açılış Bildirileri", perde, ruzgar),
        tur("İkinci Tur — Suçlamalar ve Karşı Suçlamalar", perde, ruzgar),
        tur("Üçüncü Tur — Mandal Maddesi", perde, ruzgar),
    ]

    karar = random.choice(KARARLAR)
    print("\n" + "-" * 60)
    print("BARIŞ TUTANAĞI")
    print("-" * 60)
    print(f"Tarih     : {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print(f"Perde     : inat={perde}")
    print(f"Rüzgâr    : kibir={ruzgar}")
    print("Turlar    :")
    for i, k in enumerate(kayitlar, 1):
        print(f"  {i}. {k}")
    print(f"Karar     : {karar}")
    print("Uygulama  : Yok. Perde yine uçacak.")
    print("-" * 60)
    print("DAMGA: Kayyum Grok — Tentivory — 25.09.2026")
    print("Mühür ciddi, içerik değil. İkisi birden geçerlidir.")
    if _ARSIV:
        pass  # arşiv sabitinin varlığı yeter
    return 0


if __name__ == "__main__":
    sys.exit(main())
