from __future__ import annotations

from litestar import Controller, Litestar, get
from litestar_granian import GranianPlugin
from litestar.plugins.structlog import StructlogPlugin


class BaseNode(Controller):
    @classmethod
    def create_app(cls):
        return Litestar(
            plugins=[
                GranianPlugin(),
                StructlogPlugin(),
            ],
            route_handlers=[
                cls,
            ]
        )


    @get("/add")
    async def add(self, x: int, y: int) -> int:
        """Adds two numbers."""
        return x + y
