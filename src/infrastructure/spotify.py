from dataclasses import dataclass
from enum import Enum
from typing import Any

from aiohttp import ClientSession


class RequestMethod(Enum):
    get = 'get'
    post = 'post'
    put = 'put'
    patch = 'patch'
    delete = 'delete'
    head = 'head'
    options = 'options'


@dataclass
class Request:
    method: RequestMethod
    url: str
    params: dict | None = None
    data: dict | None = None
    headers: dict | None = None
    cookies: dict | None = None


@dataclass
class Response:
    data: dict
    headers: dict
    status: int


@dataclass
class Session(ClientSession):
    async def read(self, url: str, params: dict, headers: dict) -> Any | None:
        response = await self.get(url=url, params=params, headers=headers)
        return Response(
            status=response.status,
            data=await response.json(),
            headers=dict(response.headers),
        )

    async def write(self, url: str, data: dict, headers: dict) -> Response:
        response = await self.post(url=url, data=data, headers=headers)
        return Response(
            status=response.status,
            data=await response.json(),
            headers=dict(response.headers),
        )

    async def update(self, url: str, data: dict, headers: dict) -> Response:
        response = await self.put(url=url, data=data, headers=headers)
        return Response(
            status=response.status,
            data=await response.json(),
            headers=dict(response.headers),
        )

    async def remove(self, url: str, params: dict, headers: dict) -> Response:
        response = await self.delete(url=url, params=params, headers=headers)
        return Response(
            status=response.status,
            data=await response.json(),
            headers=dict(response.headers),
        )

    async def run(self, request: Request) -> Response:
        response = await self.request(
            method=str(request.method),
            url=request.url,
            params=request.params,
            headers=request.headers,
            data=request.data,
            cookies=request.cookies,
        )
        return Response(
            status=response.status,
            data=await response.json(),
            headers=dict(response.headers),
        )
