import typing as t

from korrektor_py.api import Client
from korrektor_py.models import *
from korrektor_py.models import OcrData


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
    ) -> ResponseData:
        return self.client.send(
            "spellCheck",
            SpellCheckData,
            words=words,
            remove_modifiers=remove_modifiers
        )

    def transliterate(self, alphabet: str, text: str) -> ResponseText:
        return self.client.send(
            "transliterate",
            TransliterateData,
            text=text,
            alphabet=alphabet,
        )

    def auto_correct(self, text: str) -> ResponseText:
        return self.client.send(
            "autoCorrect",
            AutoCorrectData,
            text=text,
        )

    def remove_modifiers(self, text: str) -> ResponseText:
        return self.client.send(
            "remModifiers",
            RemoveModifiersData,
            text=text,
        )

    def tokenize(self, word: str) -> ResponseText:
        return self.client.send(
            "tokenize",
            TokenizeData,
            word=word,
        )

    def number_to_words(self, num: int) -> ResponseText:
        return self.client.send(
            "numToWords",
            NumberToWordsData,
            num=num,
        )

    def word_frequency(self, text: str) -> ResponseData:
        return self.client.send(
            "wordFrequency",
            WordFrequencyData,
            text=text,
        )

    def remove_duplicates(self, text: str) -> ResponseText:
        return self.client.send(
            "removeDublicates",
            RemoveDuplicatesData,
            text=text,
        )

    def alphabet_sorting(self, text: str) -> ResponseText:
        return self.client.send(
            "alphabetSorting",
            AlphabetSortingData,
            text=text,
        )

    def ocr(self, image_file_path: str) -> ResponseText:
        with open(image_file_path, "rb") as file:
            image: bytes = file.read()

        return self.client.send(
            "ocr",
            OcrData,
            image=image,
        )

    def doc(self, doc: t.Any, alphabet: str) -> dict:
        ...
