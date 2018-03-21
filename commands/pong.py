import asyncio
from commands.utils.Command import Command

class Pong(Command):

	def __init__(self):
		super().__init__(__name__.replace("commands.", ""));

	async def run(self, message, client, args):
		await client.send_message(message.channel, "Pong :ping_pong:")