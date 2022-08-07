# Metod: `alphabet_sorting`

## **`korrektor_py.core.Korrektor.alphabet_sorting`**

!!! tip "Metod haqida"

    O’zbek alifbosiga asoslanib matnni saralash uchun

Argumentlari va ularning "tip"lari.

- `text: str` - Saralash uchun uchun matn

> [ResponseText](/korrektor-py/objects/#korrektor_pymodelsresponsetext) - obyektini qaytaradi

Qo'llanishi:

```python title="alphabet_sorting.py" hl_lines="8"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

text = "shahlo\nsalom\no'zbek\nsalom\ndunyo"

result = korrektor.alphabet_sorting(text)

print(result.dict())
```

```json
{
  "status": "ok",
  "code": "200",
  "text": "dunyo\nsalom\nsalom\no\u2018zbek\nshahlo"
}
```
