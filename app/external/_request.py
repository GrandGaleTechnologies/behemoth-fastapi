from typing import Any

import httpx


class InternalRequestClient:
    """
    Internal client for async requests
    """

    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout
        self.client = httpx.AsyncClient(base_url=base_url, timeout=timeout)

    async def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """
        Send a GET request to the specified endpoint.
        """
        response = await self.client.get(endpoint, params=params, headers=headers)
        return response

    async def post(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """
        Send a POST request to the specified endpoint.
        """
        response = await self.client.post(
            endpoint, data=data, json=json, headers=headers
        )
        return response

    async def put(
        self,
        endpoint: str,
        data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """
        Send a PUT request to the specified endpoint.
        """
        response = await self.client.put(endpoint, data=data, headers=headers)
        return response

    async def delete(
        self, endpoint: str, headers: dict[str, str] | None = None
    ) -> httpx.Response:
        """
        Send a DELETE request to the specified endpoint.
        """
        response = await self.client.delete(endpoint, headers=headers)
        return response

    async def close(self):
        """
        Close the client connection.
        """
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
