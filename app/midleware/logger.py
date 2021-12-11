from typing import Callable
from loguru import logger
from fastapi import Request, Response


class LoggerMiddleWare:
    """
    MiddleWare для логирования запросов
    """

    @staticmethod
    async def set_body(request: Request, body: bytes) -> None:
        async def receive():
            return {'type': 'http.request', 'body': body}

        request._receive = receive

    async def get_body(self, request: Request) -> bytes:
        body = await request.body()
        await self.set_body(request, body)
        return body

    async def __call__(
            self, request: Request, call_next,
            *args, **kwargs
    ):
        raw_request_body = await request.body()
        # Последующие действия нужны,
        # чтобы не перезатереть тело запроса
        # и не уйти в зависание event-loop'a
        # при последующем получении тела ответа
        await self.set_body(request, raw_request_body)
        raw_request_body = await self.get_body(request)
        request_body = raw_request_body.decode()
        logger.debug(
            f'accept request method: {request.method} from client: {request.client.host}.'
            f' url: {request.url}, params : {request.query_params}'
            f' body: {request_body}')

        response = await call_next(request)

        body = b""
        async for chunk in response.body_iterator:
            body += chunk
        logger.debug(
            f'Response to client {request.client.host} body: {body.decode()}')
        return Response(
            content=body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
