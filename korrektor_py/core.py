import typing as t

from korrektor_py.models import *
from korrektor_py.api import Client
from korrektor_py.models import FileResponse


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
        return self.client.send_json(
            "spellCheck",
            SpellCheckData,
            words=words,
            remove_modifiers=remove_modifiers
        )

    def transliterate(self, alphabet: str, text: str) -> ResponseText:
        return self.client.send_json(
            "transliterate",
            TransliterateData,
            text=text,
            alphabet=alphabet,
        )

    def auto_correct(self, text: str) -> ResponseText:
        return self.client.send_json(
            "autoCorrect",
            AutoCorrectData,
            text=text,
        )

    def remove_modifiers(self, text: str) -> ResponseText:
        return self.client.send_json(
            "remModifiers",
            RemoveModifiersData,
            text=text,
        )

    def tokenize(self, word: str) -> ResponseText:
        return self.client.send_json(
            "tokenize",
            TokenizeData,
            word=word,
        )

    def number_to_words(self, num: int) -> ResponseText:
        return self.client.send_json(
            "numToWords",
            NumberToWordsData,
            num=num,
        )

    def word_frequency(self, text: str) -> ResponseData:
        return self.client.send_json(
            "wordFrequency",
            WordFrequencyData,
            text=text,
        )

    def remove_duplicates(self, text: str) -> ResponseText:
        return self.client.send_json(
            "removeDuplicates",
            RemoveDuplicatesData,
            text=text,
        )

    def alphabet_sorting(self, text: str) -> ResponseText:
        return self.client.send_json(
            "alphabetSorting",
            AlphabetSortingData,
            text=text,
        )

    def ocr(self, image_file_path: str) -> ResponseText:
        return self.client.send_image(
            "ocr",
            image_file_path=image_file_path,
        )

    def doc(
        self,
        document_path: str,
        alphabet: str,
        save_path: t.Optional[str] = None,
    ) -> FileResponse:
        return self.client.send_document(
            "doc",
            document_path=document_path,
            alphabet=alphabet,
            save_path=save_path,
        )
