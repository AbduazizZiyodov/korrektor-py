# Metod: `transliterate`

## **`korrektor_py.core.Korrektor.transliterate`**

!!! tip "Metod haqida"

    Matnlarni transliteratsiya qilish uchun

Argumentlari va ularning "tip"lari.

- `alphabet: str` - Matnni qaysi alifboga o’girish. `cyrillic` yoki `latin`
- `text: str` - Transliteratsiya qilish uchun matn

> [ResponseText](/korrektor-py/objects/#korrektor_pymodelsresponsetext) - obyektini qaytaradi

Qo'llanishi:

```python title="transliterate.py" hl_lines="9"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

text = "Salom dunyo"
alphabet = "cyrillic"

result = korrektor.transliterate(alphabet, text)

print(result.dict())
```

Natija:

```json
{
  "text": "Салом дунё",
  "status": "ok",
  "code": "200"
}
```
