import asyncio
import logging
import os
from pathlib import Path
from typing import Union

import discord
from dotenv import load_dotenv

from revu import Revu


discord.utils.setup_logging(level=logging.INFO, root=True)


async def main() -> None:
    """
    Run the bot.
    """

    bot = Revu()

    dotenv_path: Union[str, os.PathLike[str]] = Path(".env")
    load_dotenv(dotenv_path=dotenv_path)

    await asyncio.gather(
        bot.start(os.environ["REVU_TOKEN"]),
    )


# Runs everything
asyncio.run(main())
