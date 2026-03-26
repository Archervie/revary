import discord
from discord import app_commands
from discord.ext import commands

from datetime import datetime

from src.core import BaseGroupCog
from src.utils import is_authorized


@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(dms=True, guilds=True, private_channels=True)
class UserCog(BaseGroupCog, name="user"):
    """ """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__(bot)

    @app_commands.user_install()
    @app_commands.allowed_contexts(dms=True, guilds=True, private_channels=True)
    @app_commands.command(description="get avatar", name="avatar")
    async def avatar(
        self,
        interaction: discord.Interaction,
        user: discord.User | None = None,
        size: int = 512,
    ) -> None:
        """ """
        target_user = user or interaction.user

        assert user
        avatar = user.avatar or user.default_avatar

        try:
            size_int = int(size)
            avatar_url = avatar.replace(format="png", size=size_int).url

            assert self.bot.user
            embed = discord.Embed(
                color=(
                    target_user.color.value if user.color else self.bot.user.color.value
                ),
                title=f"{target_user}'s avatar: {size}x{size}",
                url=avatar_url,
                timestamp=datetime.now(),
            )

            embed.set_image(url=avatar_url)

            await interaction.response.send_message(embed=embed)

        except ValueError:
            await interaction.response.send_message(
                "Please provide a valid size: 2^x from 2 to 4096.", ephemeral=True
            )


# Adds the misc cog
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UserCog(bot))
