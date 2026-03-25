import discord
from discord import app_commands
from discord.ext import commands

from core import BaseGroupCog
from utils import is_authorized


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(dms=True, guilds=True, private_channels=True)
class MiscCog(BaseGroupCog, name="misc"):
    """test"""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__(bot)

    @app_commands.user_install()
    @app_commands.allowed_contexts(dms=True, guilds=True, private_channels=True)
    @app_commands.command(description="Test command", name="test")
    # @is_authorized()
    async def example(self, interaction: discord.Interaction) -> None:
        """test"""
        await interaction.response.send_message("test complete", ephemeral=True)
        if not interaction.command_failed:
            self.log_command(interaction)


# Adds the misc cog
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MiscCog(bot))
 