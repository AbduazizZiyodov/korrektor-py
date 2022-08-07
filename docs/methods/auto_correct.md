# Metod: `auto_correct`

## **`korrektor_py.core.Korrektor.auto_correct`**

!!! tip "Metod haqida"

    Matnlarni korreksiya qilish uchun

Argumentlari va ularning "tip"lari.

- `text: str` - Korreksiya qilish uchun matn

> [ResponseText](/korrektor-py/objects/#korrektor_pymodelsresponsetext) - obyektini qaytaradi

Qo'llanishi:

```python title="auto_correct.py" hl_lines="8"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

text = "O'zbekcha matn"

result = korrektor.auto_correct(text)

print(result.dict())
```

Natija:

```json
{
  "status": "ok",
  "code": "200",
  "text": "O\u2018zbekcha matn"
}
```
