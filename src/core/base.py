import discord
from discord import app_commands
from discord.ext import commands

from src.utils.log_utils import Logger


class BaseCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()

        self.bot = bot
        self.logger = Logger().logger(self.__class__.__name__.lower())

    async def on_app_command_completion(self, interaction: discord.Interaction):
        assert isinstance(interaction.command, app_commands.Command)
        command_name = interaction.command.name
        self.logger.info(f"{interaction.user} successfully ran {command_name}")


class BaseGroupCog(commands.GroupCog):

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.logger = Logger().logger(self.__class__.__name__.lower())

    async def on_app_command_completion(self, interaction: discord.Interaction):
        assert isinstance(interaction.command, app_commands.Command)
        command_name = interaction.command.name
        self.logger.info(f"{interaction.user} successfully ran {command_name}")
