import discord
from discord.ext.commands import Bot
from discord.ext import commands

from commands.pong import Pong

Client = discord.Client();
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
	print("Mario Bot is ready!")

commands = [Pong()]

@client.event
async def on_message(message):
	message_content = message.content.lower();
	command_prefix = client.command_prefix;
	if not message_content.startswith(command_prefix):
		return;

	args = message_content.split(" ")[1:]

	if message_content == command_prefix+"help":
		command_list = "";

		for i, command in enumerate(commands):
			command_list += command.getName() + (", " if (i + 1) != len(commands) else "")

		await client.send_message(message.channel, "Commands: "+command_list);

	else:

		for command in commands:
			if message_content.replace(command_prefix, "") == command.getName().lower():
				await command.run(message, client, args)

client.run("bot-token")