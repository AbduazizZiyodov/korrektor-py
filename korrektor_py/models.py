import typing as t
from pydantic import (
    BaseModel,
    validator
)


class Text(BaseModel):
    text: t.Optional[str]


class Data(BaseModel):
    data: t.Optional[t.Any]


class Word(BaseModel):
    word: t.Optional[str]


class Response(BaseModel):
    status: str
    code: str


class ResponseText(Response, Text):
    ...


class ResponseData(Response, Data):
    ...


class Alphabet(BaseModel):
    alphabet: str

    @validator("alphabet")
    def alphabet_match(cls, value: str):
        if value not in ["cyrillic", "latin"]:
            raise ValueError(
                "Value of alphabet should be cyrillic or latin"
            )
        return value


class SpellCheckData(BaseModel):
    words: t.List[str]
    remove_modifiers: t.Optional[bool] = False

    class Config:
        response_model = ResponseData


class OcrData(BaseModel):
    image: t.Any


class DocData(Alphabet):
    doc: t.Any


class NumberToWordsData(BaseModel):
    num: int

    class Config:
        response_model = ResponseText


class TransliterateData(Alphabet, Text):
    class Config:
        response_model = ResponseText


class AutoCorrectData(Text):
    class Config:
        response_model = ResponseText


class RemoveModifiersData(Text):
    class Config:
        response_model = ResponseText


class TokenizeData(Word):
    class Config:
        response_model = ResponseText


class WordFrequencyData(Text):
    class Config:
        response_model = ResponseData


class RemoveDuplicatesData(Text):
    class Config:
        response_model = ResponseText


class AlphabetSortingData(Text):
    class Config:
        response_model = ResponseText


__all__ = [
    "SpellCheckData", "TransliterateData", "AutoCorrectData",
    "RemoveModifiersData", "TokenizeData", "NumberToWordsData",
    "WordFrequencyData", "RemoveDuplicatesData", "AlphabetSortingData",
    "ResponseData", "ResponseText"
]
