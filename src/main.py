import asyncio
import logging
import os
from pathlib import Path
from typing import Union

import discord
from dotenv import load_dotenv

from src.core.revu import Revu
from src.utils.log_utils import Logger


async def main() -> None:
    """
    Run the bot.
    """

    # Loads all .env files (used for now)
    dotenv_path: Union[str, os.PathLike[str]] = Path(".env")
    load_dotenv(dotenv_path=dotenv_path)

    bot = Revu()

    async with asyncio.TaskGroup() as tg:
        tg.create_task(bot.start(os.environ["REVU_TOKEN"]))


# Runs everything
if __name__ == "__main__":
    asyncio.run(main())
