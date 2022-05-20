import discord
welcome_channel_id = 972495523464511520
class MyClient(discord.Client):
  #Einloggen
  async def on_ready(self):
    print("Im Online right now bitches")
    welcome_channel = client.get_channel(welcome_channel_id)
    await welcome_channel.send("This server has added more security.... Please Click Verify to verify you aren't a robot ✅")

Rollen=[972491774004195378]
@bot.command()
async def getrole(ctx, role: discord.Role=None):
  if role is None:
    await ctx.send("Give the role")
  else:
    if role.id in Rollen:
      await ctx.authore.add_roles(role)
      await ctx.send(f"You just got the {role}")
    else:
      await ctx.send("You can not get the role")

client = MyClient()
client.run("OTc2ODk5Nzg1OTM0MTMxMjEw.GXKGdX.SSRnrmpqIGKxK1MOqGoBMjyRr3BY-iXa3xdDKo")