# Metod: `number_to_words`

## **`korrektor_py.core.Korrektor.number_to_words`**

!!! tip "Metod haqida"

    Sonni matnga o’girish uchun

Argumentlari va ularning "tip"lari.

- `num:int` - So’zlarda ifodalash uchun son

> [ResponseText](/korrektor-py/objects/#korrektor_pymodelsresponsetext) - obyektini qaytaradi

Qo'llanishi:

```python title="number_to_words.py" hl_lines="8"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

num = 25678

result = korrektor.number_to_words(num)

print(result.dict())
```

```json
{
  "status": "ok",
  "code": "200",
  "text": "yigirma besh ming olti yuz yetmish sakkiz"
}
```
