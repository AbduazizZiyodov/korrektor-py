# Metod: `tokenize`

## **`korrektor_py.core.Korrektor.tokenize`**

!!! tip "Metod haqida"

    Bo’ginlarga ajratish uchun

Argumentlari va ularning "tip"lari.

- `word:str` - Bo’ginlarga ajratish uchun so’z

> [ResponseText](/korrektor-py/objects/#korrektor_pymodelsresponsetext) - obyektini qaytaradi

Qo'llanishi:

```python title="tokenize.py" hl_lines="8"
from korrektor_py import Korrektor

TOKEN =  ...
korrektor = Korrektor(TOKEN)

word = "olamning"

result = korrektor.tokenize(word)

print(result.dict())
```

```json
{
  "status": "ok",
  "code": "200",
  "text": "o-lam-ning"
}
```
