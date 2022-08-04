import json
import typing as t
from .api import Client


class Korrektor:
    def __init__(
        self,
        token: str = None,
        base_api_url: t.Optional[str] = "https://korrektor.uz/api/",
    ) -> None:
        self.client = Client(token, base_api_url)

    def spell_check(
        self,
        words: t.List[str],
        remove_modifiers: t.Optional[bool] = False,
    ):
        ...

    def transliterate(alphabet: str, text: str):
        ...

    def auto_correct(text: str):
        ...

    def remove_modifiers(text: str):
        ...

    def tokenize(word: str):
        ...

    def number_to_words(num: int):
        ...

    def word_frequency(text: str):
        ...

    def remove_duplicates(text: str):
        ...

    def alphabet_sorting(text: str):
        ...

    def ocr(image: t.Any):
        ...

    def doc(doc: t.Any, alphabet: str):
        ...
