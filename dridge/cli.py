#!/usr/bin/env python
from __future__ import annotations

import click


@click.group()
@click.version_option()
def cli():
    pass


@cli.command()
def proxy():
    from granian import Granian
    from granian.constants import Interfaces

    server = Granian(
        target="dridge.proxy.asgi:app",
        address="0.0.0.0",
        port=25443,
        interface=Interfaces.ASGI,
    )

    server.serve()


@cli.command()
def worker():
    from granian import Granian
    from granian.constants import Interfaces

    server = Granian(
        target="dridge.worker.asgi:app",
        address="0.0.0.0",
        port=25080,
        interface=Interfaces.ASGI,
    )

    server.serve()


def main():
    cli()


if __name__ == "__main__":
    main()
