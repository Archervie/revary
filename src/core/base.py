import discord
from discord import app_commands
from discord.ext import commands

from utils.log_utils import Logger


class BaseCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()

        self.bot = bot
        logger = Logger()
        self.logger = logger.logger(f"bot.{self.__name__}")

    def log_command(self, interaction: discord.Interaction) -> None:
        if interaction.command:
            assert isinstance(interaction.command, app_commands.Command)
            command_name = interaction.command.name
            self.logger.info(f"{interaction.user} successfully ran {command_name}!")
        else:
            self.logger.error("An error occurred.", exc_info=True)


class BaseGroupCog(commands.GroupCog):

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        logger = Logger()
        self.logger = logger.logger(f"bot.{self.__class__.__name__}")

    def log_command(self, interaction: discord.Interaction) -> None:
        if interaction.command:
            assert isinstance(interaction.command, app_commands.Command)
            assert interaction.command.parent
            command_name = (
                f"{interaction.command.parent.name}.{interaction.command.name}"
            )
            self.logger.info(f"{interaction.user} successfully ran {command_name}!")
        else:
            self.logger.error("An error occurred.", exc_info=True)
