# Metod: `remove_duplicates`

## **`korrektor_py.core.Korrektor.remove_duplicates`**

!!! tip "Metod haqida"

    Duplikatlarni tozalash uchun

Argumentlari va ularning "tip"lari.

- `text: str` - Duplikatlarni o’chirish uchun uchun matn

> [ResponseText](/korrektor-py/objects/#korrektor_pymodelsresponsetext) - obyektini qaytaradi

Qo'llanishi:

```python title="remove_duplicates.py" hl_lines="8"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

text = "salom salom dunyo"

result = korrektor.remove_duplicates(text)

print(result.dict())
```

```json
{
  "status": "ok",
  "code": "200",
  "text": "salom dunyo"
}
```
