import importlib.util
from typing import Generator, List

from aiogram import Router, Dispatcher as AIOgramDispatcher

from src.config import HANDLERS, HANDLERS_ROOT, MONGO_TOKEN
from src.errors import RouterDoesNotExist
from src.ext.resolve_handlers import resolve_handlers
from src.triggers import core as triggers


class Dispatcher(AIOgramDispatcher):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_router(self, file_path: str) -> Router:
        module_spec = importlib.util.spec_from_file_location(
            "dynamic_module", file_path
        )

        if module_spec is None or module_spec.loader is None:
            raise RouterDoesNotExist

        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)

        if not hasattr(module, "router"):
            raise RouterDoesNotExist

        return module.router

    def fetch_routers(self) -> Generator[Router, None, None]:
        handler_files = resolve_handlers(HANDLERS, HANDLERS_ROOT)
        for handler_file in handler_files:
            yield self.get_router(handler_file)

    def register_routers(self) -> None:
        for router in self.fetch_routers():
            triggers.loading_router.notify(router)
            self.include_router(router)