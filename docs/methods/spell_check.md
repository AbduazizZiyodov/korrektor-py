# Metod: `spell_check`

> Deyarli barcha tavsiflar API'ning rasmiy qo'llanmasidan olindi.

!!! note "Eslatma"

    `Optional[...]` - bilan ko'rsatilgan barcha argumentlar majburiy emas deb hisoblanadi.

## **`korrektor_py.core.Korrektor.spell_check`**

!!! tip "Metod haqida"

    Imlo xatoliklarni tekshirish uchun

Argumentlari va ularning "tip"lari.

- `words:List[str]` - Tekshirish uchun so’zlar massivi.
- `remove_modifiers:Optional[bool]` - So’zlarni tekshirish jarayonida yuklamalarni tozalash. Misol uchun
  bormoqda-ku so’zi uchun bormoqda so’zi qabul qilinadi.

> [ResponseData](/korrektor-py/objects/#korrektor_pymodelsresponsedata) - obyektini qaytaradi

Qo'llanishi:

```python title="spell_check.py" hl_lines="12"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

remove_modifiers = True
words = [
    "saloma",
    "dunyo"
]

result = korrektor.spell_check(words, remove_modifiers)

print(result.dict())
```

Natija:

```json
{
  "status": "ok",
  "code": "200",
  "data": [
    {
      "word": "dunyo",
      "status": "correct"
    },
    {
      "word": "saloma",
      "status": "misspell",
      "suggestion": ["salom", "alloma", "salo"]
    }
  ]
}
```
