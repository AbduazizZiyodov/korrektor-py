import os
import json
import httpx
import typing as t
from pydantic import BaseModel

from korrektor_py.models import (
    Alphabet,
    FileResponse,
    ResponseText,
    ResponseData,
    ResponseError
)

from korrektor_py.exceptions import WrongFileFormat
from korrektor_py.utils import check_file_format, get_file_info


class Client:
    def __init__(
        self,
        token: str = None,
        base_api_url: t.Optional[str] = "https://korrektor.uz/api/",
    ):
        self.TOKEN = token
        self.API_URL = base_api_url
        self.headers = httpx.Headers({
            "Authorization": f"Bearer {self.TOKEN}"
        })
        self.headers_json = httpx.Headers({
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-type": "application/json"
        })

    def send_json(
            self,
            endpoint: str,
            Model: BaseModel,
            **kwargs

    ) -> t.Union[ResponseText, ResponseData, ResponseError]:
        url = self.API_URL + endpoint

        request_dict: dict = Model.parse_obj(kwargs).dict()
        data = json.dumps(request_dict, indent=2).encode('utf-8')

        response: httpx.Response = httpx.post(
            url,
            timeout=60,
            content=data,
            headers=self.headers_json,
        )
        response_content = response.json()

        if response_content["code"] != "200":
            return ResponseError(**response_content)

        return Model.Config.response_model.parse_obj(response_content)

    def send_image(
        self,
        endpoint: str,
        image_file_path: str
    ) -> t.Union[ResponseText,  ResponseError]:
        url = self.API_URL + endpoint

        with open(image_file_path, "rb") as file:
            image: bytes = file.read()

        response: httpx.Response = httpx.post(
            url,
            timeout=60,
            headers=self.headers,
            files={"image": image},
        )

        response_content: dict = response.json()

        if response_content["code"] != "200":
            return ResponseError(**response_content)

        return ResponseText(**response_content)

    def send_document(
        self,
        endpoint: str,
        document_path: str,
        alphabet: str,
        save_path: t.Optional[str] = None,
    ) -> t.Union[ResponseError, FileResponse]:
        url = self.API_URL + endpoint

        alphabet: BaseModel = Alphabet(alphabet=alphabet)
        file_name, file_format = get_file_info(document_path)

        if save_path is None:
            save_path = f"korrektor.uz-{file_name}.{file_format}"

        response: httpx.Response = httpx.post(
            url,
            timeout=60,
            headers=self.headers,
            data=alphabet.dict(),
            files={"doc": open(document_path, "rb")}
        )

        if response.headers["content-type"].startswith("application/json"):
            return ResponseError.parse_obj(response.json())

        with open(save_path, "wb") as file:
            file.write(response.content)

        return FileResponse(
            file_name=save_path,
            status="File saved."
        )
