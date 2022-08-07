# **Korrektor-Py**

<p align="center">
    <img src="assets/logo.png"></img> <br>
     <img src="https://github.com/AbduazizZiyodov/korrektor-py/actions/workflows/ci.yml/badge.svg?branch=master"></img> 
     <img src="https://static.pepy.tech/personalized-badge/korrektor-py?period=total&units=international_system&left_color=blue&right_color=green&left_text=Yuklab%20olishlar%20soni"></img>
     <br>
    <b>Korrektor-Py</b> - https://korrektor.uz loyihasining API'si uchun ishlab chiqilgan python kutubxona. 
    <br>
</p>

## **Loyiha haqida**

korrektor.uz quyidagi imkoniyatlarni siz uchun taqdim etadi.

- Imlo xatoliklarni tekshirish
- Matnlarni transliteratsiya qilish
- Tasvir fayllardan matnlarni ajratib olish (jpeg, png, gif)
- Hujjatlarni transliteratsiya qilish (docx, xlsx, pptx, epub, html)
- Matnlar bilan ishlashda: raqamni so'zga o'girish, so'zlarni korreksiya qilish, so'zni bo'g'inga ajratish, dublikatlarni o'chirish, matndagi so'zlar chastotasini hisoblash kabi qo'shimcha vositalardan foydalanish imkoniyatini yaratib beradi.

Ilovadan foydalanish mutlaqo tekin va dasturchilar uchun ham turli yechimlar mavjud.

Python dasturchilar uchun turli yechimlardan biri ushbu kutubxona hisoblanadi. Yuqorida keltirilgan barcha imkoniyatlardan python dasturlash tili orqali bahramand bo'lishingiz mumkin.

## **O'rnatish**

- `pip` yordamida:

  ```bash
  pip3 install --upgrade korrektor-py
  ```

Yoki:

- Loyihani asl manba kodidan `build` qilib, so'ng o'rnatish uchun repozitoriyani ko'chirib oling:

  ```bash
  git clone https://github.com/AbduazizZiyodov/korrektor-py.git
  cd korrektor-py/
  ```

  Loyiha direktoriyasiga o'tganingizdan so'ng `setup.py` yordamida uni `build` qiling.
  Loyiha versiyasini aniqlab olgandan so'ng, `pip` va wheel fayli yordamida o'rnatishingiz mumkin.

  ```bash
  python3 setup.py sdist bdist_wheel
  VERSION=$(python3 -c "from __version__ import version;print(version)")
  pip3 install dist/Korrektor_Py-$VERSION-py3-none-any.whl
  ```

<hr>

- Loyiha asoschisi: [Manuchehr Usmonov](https://github.com/con9799)
- Ushbu kutubxona muallifi: [Abduaziz Ziyodov](https://github.com/AbduazizZiyodov)
