from typing import Callable, Iterable, Optional

from fastapi import FastAPI, APIRouter, Response, Request
from fastapi.routing import APIRoute
from policies import *
app = FastAPI()


class CustomAPIRoute(APIRoute):
    def __init__(
        self,
        path: str,
        endpoint: Callable,
        *,
        policies: Optional[Iterable[str]] = None,
        **kwargs
    ) -> None:
        super().__init__(path, endpoint, **kwargs)
        self.policies = policies

    def check_policies(self):
        a= ["a","b","c"]
        listPolicy = self.policies
        for e in listPolicy:
            if e in a:
                return "a"
        return "abv"
 
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request.state.policies = self.policies
            response = await original_route_handler(request)
            print(response)
            return response

        return custom_route_handler


class CustomAPIRouter(APIRouter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.route_class = CustomAPIRoute

    def add_api_route(
        self,
        path: str,
        endpoint: Callable,
        *,
        policies: Optional[Iterable[str]] = None,
        **kwargs
    ) -> None:
        
        route = self.route_class(
            path=path, endpoint=endpoint, policies=policies, **kwargs
        )
        self.routes.append(route)

    def api_route(
        self, path: str, *,policies: Optional[Iterable[str]] = None, **kwargs
    ) -> Callable:
        
        def decorator(func: Callable) -> Callable:
            self.add_api_route(path, func, policies = policies, **kwargs)
            return func
        return decorator

    def get(
        self, path: str, *, policies: Optional[Iterable[str]] = None, **kwargs
    ) -> Callable:
        return self.api_route(path, policies = policies, **kwargs)

    

