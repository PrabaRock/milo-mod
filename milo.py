import discord
from discord.ext import commands

import datetime
import os

client = commands.Bot(command_prefix="-")
client.remove_command('help')

@client.event
async def on_ready():
	print('Logged in', client.user.name)
	print('Version - 1.0.0')
	print('Creator - PrabaRock7#3945')
	print('Release Version - v01')
	print('ᎷᎨᏝᎾ')
	await client.change_presence(status=discord.Status.online, activity=discord.Game(name="-help | MiloMod™"))

	
@client.event
async def on_member_join(member):
	print(f"{member} has joined the server.")
	
@client.event
async def on_member_remove(member):
	print(f"{member} has left the server.")
	
@client.command()
async def help(ctx):
	
	embed = discord.Embed(title="List Of Commands", colour=discord.Colour(0xff0000))
	
	embed.set_thumbnail(url="https://i.imgur.com/cUrQeXr.png")
	embed.set_footer(text=f"Command Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
	
	embed.add_field(name="**Fun**", value="-hello, -ping")
	embed.add_field(name="**Bot Related Commands**", value="-botinfo, -botsource,  -botsupportserver")
	embed.add_field(name="**Moderation**", value="-clear, -kick, -ban, -unban, -avatar, -useravatar")
	await ctx.send(embed=embed)
	
@client.command()
async def hello(ctx):
	await ctx.send("Hello!" + ", " + ctx.message.author.mention)
	
@client.command()
async def ping(ctx):
	
	embed = discord.Embed(colour=discord.Colour(0x00ff00), timestamp=datetime.datetime.utcfromtimestamp(1564047819))
	embed.set_author(name="Ping")
	embed.add_field(name=f"*Pong*", value=f"**:ping_pong: {round(client.latency * 1000)}ms**")
	embed.set_footer(text=f"Req By {ctx.author}", icon_url=ctx.author.avatar_url)
	await ctx.send(embed=embed)
	
@client.command()
async def clear(ctx, amount : int):
	await ctx.channel.purge(limit=amount)
	
@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"Please Specify **number of messages** to *delete* {ctx.author.mention}")
	
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	
@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"Please Specify a **member** to *kick* {ctx.author.mention}")
	
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	
@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"Please Specify a **member** to *ban* {ctx.author.mention}")
	
@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')
	
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			
@unban.error
async def unban_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f"Please Specify a **member** to *unban* {ctx.author.mention}")
			
@client.command()
async def botinfo(ctx):
	
	embed = discord.Embed(colour=discord.Colour(0x00ffff), description="Milo Bot info")
	embed.set_thumbnail(url="https://i.imgur.com/cUrQeXr.png")
	
	embed.add_field(name="Bot Info", value=f"Hello {ctx.author}, thanks for showing intrest to get info about me :grin:. Im Coded using Python. For list of commnads please type -help. My Owner is <@589647651939549206>. Im a simple bot i don't have advanced commands, that's a fault.")
	embed.add_field(name="External Links", value="[Patreon](https://patreon.com/PrabaRock7), [Ko-Fi](https://ko-fi.com/prabarock7)")
	await ctx.send(embed=embed)
	
@client.command()
async def botsupportserver(ctx):
	
	embed = discord.Embed(title="Support server")
	embed.add_field(name="Server Link", value="Touch the below link to join the server")
	await ctx.send(content="https://discord.gg/FeD6RUs", embed=embed)
	
@client.command()
async def avatar(ctx):
	show_avatar = discord.Embed(
	
	         color = discord.Color.dark_blue()
	)
	show_avatar.set_image(url="{}".format(ctx.author.avatar_url))
	await ctx.send(embed=show_avatar)
	
@client.command()
async def useravatar(ctx, member : discord.Member):
	show_avatar = discord.Embed(
	
	         color = discord.Color.dark_blue()
	)
	show_avatar.set_image(url="{}".format(member.avatar_url))
	await ctx.send(embed=show_avatar)
	

client.run(os.getenv("TOKEN"))
