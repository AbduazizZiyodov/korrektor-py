import typing as t
from pydantic import (
    BaseModel,
    validator
)


class Text(BaseModel):
    text: str


class Word(BaseModel):
    word: str


class Alphabet(BaseModel):
    alphabet: str

    @validator("alphabet")
    def alphabet_match(cls, value: str):
        if value not in ["cyrillic", "latin"]:
            raise ValueError("Value of alphabet should be cyrillic or latin")
        return value


class SpellCheckData(BaseModel):
    words: t.List[str]
    remove_modifiers: t.Optional[bool] = False


class OcrData(BaseModel):
    image: t.Any


class DocData(Alphabet):
    doc: t.Any


class NumberToWordsData(BaseModel):
    num: int


class TransliterateData(Alphabet, Text):
    ...


class AutoCorrectData(Text):
    ...


class RemoveModifiersData(Text):
    ...


class TokenizeData(Word):
    ...


class WordFrequencyData(Text):
    ...


class RemoveDuplicatesData(Text):
    ...


class AlphabetSortingData(Text):
    ...
