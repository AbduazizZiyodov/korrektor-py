import json
import httpx
import typing as t
import httpx._types as types
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

    def get(
        self,
        endpoint: str,
        timeout: t.Optional[types.TimeoutTypes] = None,
    ) -> httpx.Response:
        url = self.API_URL + endpoint

        return httpx.get(
            url,
            headers=self.headers,
            timeout=timeout
        )

    def post(
            self,
            endpoint: str,
            content: t.Optional[types.RequestContent] = None,
            data: t.Optional[types.RequestData] = None,
            files: t.Optional[types.RequestFiles] = None,
            timeout: t.Optional[types.TimeoutTypes] = None,

    ) -> httpx.Response:
        url = self.API_URL + endpoint

        if content and isinstance(content, dict):
            content = json.dumps(content, indent=2).encode('utf-8')

        return httpx.post(
            url,
            data=data, files=files,
            headers=self.headers,
            content=content,
            timeout=timeout
        )
