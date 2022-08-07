import os
import constants
import typing as t
from pydantic import BaseModel
from korrektor_py import models
from korrektor_py import Korrektor

TOKEN = os.getenv("KORREKTOR_TOKEN")
korrektor = Korrektor(TOKEN)


def check_fields(fields: list, data: BaseModel) -> bool:
    return all(
        [
            field in data.dict().keys()
            for field in fields
        ]
    )


def assert_response_ok(
    _type: str,
    result: t.Union[models.ResponseText, models.ResponseData]
) -> None:

    assert result.status == "ok"
    assert result.code == "200"

    assert check_fields(["status", "code", _type], result)


def test_spell_check():
    result = korrektor.spell_check(
        **constants.SPELLCHECK_DATA
    )
    print(result)
    assert_response_ok("data", result)


def test_transliterate():
    result = korrektor.transliterate(
        **constants.TRANSLITERATE_DATA
    )
    print(result)
    assert_response_ok("text", result)


def test_auto_correct():
    result = korrektor.auto_correct(
        **constants.AUTOCORRECT_DATA
    )
    print(result)
    assert_response_ok("text", result)


def test_remove_modifiers():
    result = korrektor.remove_modifiers(
        **constants.REMOVEMODIFIERS_DATA
    )
    print(result)
    assert_response_ok("text", result)


def test_tokenize():
    result = korrektor.tokenize(**constants.TOKENIZE_DATA)
    assert_response_ok("text", result)


def test_number_to_words():
    result = korrektor.number_to_words(
        **constants.NUMBER_TO_WORDS_DATA
    )
    print(result)
    assert_response_ok("text", result)


def test_word_frequency():
    result = korrektor.word_frequency(**constants.WORD_FREQUENCY_DATA)
    print(result)
    assert len(result.data) > 0
    assert_response_ok("data", result)


def test_remove_duplicates():
    result = korrektor.remove_duplicates(
        **constants.REMOVE_DUPLICATES_DATA
    )
    print(result)
    assert_response_ok("text", result)


def test_alphabet_sorting():
    result = korrektor.alphabet_sorting(
        **constants.ALPHABET_SORTING_DATA
    )
    print(result)
    assert_response_ok("text", result)


def test_ocr():
    result = korrektor.ocr(constants.OCR_DATA)
    print(result)
    assert_response_ok("text", result)


def test_dpc():
    result = korrektor.doc(**constants.DOC_DATA)
    print(result)
    assert result.status == "File saved."
    assert os.path.isfile(constants.DOC_DATA["save_path"])
