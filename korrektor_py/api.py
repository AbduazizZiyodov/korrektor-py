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

        self.headers = httpx.Headers(
            {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.TOKEN}"
            }
        )

    def send(
            self,
            endpoint: str,
            Model: BaseModel,
            **kwargs

    ) -> t.Union[httpx.Response, t.Any]:
        """Main method for communicating with API
        """
        url = self.API_URL + endpoint

        content: BaseModel = Model.parse_obj(kwargs)
        content = json.dumps(content.dict(), indent=2).encode('utf-8')

        response: httpx.Response = httpx.post(
            url,
            headers=self.headers,
            content={content},
            timeout=60  # seconds (if needs)
        )

        if 200 <= response.status_code < 400:
            return Model.Config.response_model.parse_obj(response.json())

        return response.json()
