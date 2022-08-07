# Metod: `remove_modifiers`

## **`korrektor_py.core.Korrektor.remove_modifiers`**

!!! tip "Metod haqida"

    Yuklamalarni tozalash uchun

Argumentlari va ularning "tip"lari.

- `text: str` - Tozalash uchun matn

> [ResponseText](/korrektor-py/objects/#korrektor_pymodelsresponsetext) - obyektini qaytaradi

Qo'llanishi:

```python title="remove_modifiers.py" hl_lines="8"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

text = "Uning ko'zlari ajablantirmoqda-ku"

result = korrektor.remove_modifiers(text)

print(result.dict())
```

```json
{
  "status": "ok",
  "code": "200",
  "text": "Uning ko'zlari ajablantirmoqda"
}
```
