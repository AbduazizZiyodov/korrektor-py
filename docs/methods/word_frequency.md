# Metod: `word_frequency`

## **`korrektor_py.core.Korrektor.word_frequency`**

!!! tip "Metod haqida"

    Chastotani hisoblash uchun

Argumentlari va ularning "tip"lari.

- `text:str` - So’zlar chastotasini hisoblash uchun matn

> [ResponseData](/korrektor-py/objects/#korrektor_pymodelsresponsedata) - obyektini qaytaradi

Qo'llanishi:

```python title="word_frequency.py" hl_lines="12"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

text = "Bugun ajoyib kun. Men bugun ajoyib yangi ishlarni amalga oshiraman."

result = korrektor.word_frequency(text)

print(result.dict())
```

Natija:

```json
{
  "status": "ok",
  "code": "200",
  "data": {
    "ajoyib": 2,
    "Bugun": 1,
    "kun": 1,
    "Men": 1,
    "bugun": 1,
    "yangi": 1,
    "ishlarni": 1,
    "amalga": 1,
    "oshiraman": 1
  }
}
```
