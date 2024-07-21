from __future__ import annotations

from litestar import Controller, Litestar, get
from litestar.plugins.structlog import StructlogPlugin
from litestar_granian import GranianPlugin


class BaseNode(Controller):
    @classmethod
    def create_app(cls) -> Litestar:
        return Litestar(
            plugins=[
                GranianPlugin(),
                StructlogPlugin(),
            ],
            route_handlers=[
                cls,
            ],
        )


    @get("/add")
    async def add(self, x: int, y: int) -> int:
        """Add two numbers."""
        return x + y
