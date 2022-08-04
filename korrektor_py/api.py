import json
import httpx
import typing as t
from pydantic import BaseModel


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
            "Authorization": f"Bearer {self.TOKEN}"
        })

    def send(
            self,
            endpoint: str,
            Model: BaseModel,
            **kwargs

    ) -> t.Union[httpx.Response, t.Any]:
        """Main method for communicating with API
        """
        url = self.API_URL + endpoint

        if endpoint not in ["ocr", "doc"]:
            files = None
            content: BaseModel = Model.parse_obj(kwargs)
            content = json.dumps(content.dict(), indent=2)\
                .encode('utf-8')
            headers = self.headers_json
        else:
            content = None
            files = Model.parse_obj(kwargs).dict()
            headers = self.headers

        response: httpx.Response = httpx.post(
            url,
            timeout=60,  # seconds (if needs)
            files=files,
            headers=headers,
            content=content,
        )

        if response.json()["code"] == "200":
            return Model.Config\
                .response_model.parse_obj(response.json())

        return response.json()
