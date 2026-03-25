import discord
from discord.ext import commands

from utils.log_utils import Logger

cogs = ["misc"]


class Revu(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix=".", intents=discord.Intents.all())
        logger = Logger()
        self.logger = logger.logger("Revu")

    async def setup_hook(self) -> None:
        for cog in cogs:
            await self.load_extension(f"revu.cogs.{cog}")
            self.logger.info(f"Loaded {cog}")
        await self.tree.sync()
        self.logger.info("Finished setting up, now booting.")
        return await super().setup_hook()

    async def on_ready(self) -> None:
        await self.change_presence(activity=discord.Game("Kill Ballad"))
        self.logger.info("Status green, now operating.")
