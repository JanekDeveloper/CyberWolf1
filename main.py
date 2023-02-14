import os
import asyncio
from keep_alive import keep_alive
keep_alive()
import disnake
from disnake.ext import commands, tasks
import disnake, random, aiohttp, asyncio
from disnake import Webhook
from asyncio import sleep
import datetime
import time
import requests
import animec
import json
import io






intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="c!", intents=intents)
bot.remove_command('help')
token = ""



random_activity_custom = ["раса Старых богов существует?","Üc207-Pr-4f57t9","Ekusu Makina","48 человек... были убиты..... помянем","Ашенте!","196835,2 км/с","- Этот мир... всегда был просто Игрой","В поисках Шуви...","Sorry, Рику...","Disbord!"]
random_activity_server = ["c!help"]
random_activity_choice = [random_activity_server, random_activity_custom]

@bot.event
async def on_ready():
    print("I AM READY!")
    activity = disnake.Game(name= "c!help")
    await bot.change_presence(activity=activity)
    random_activity_server.append(f"{len(bot.guilds)} server(s)!")
    await bot.wait_until_ready()
    activity_update.start()

@tasks.loop(minutes = 5)
async def activity_update():
    activity = disnake.Game(name=random.choice(random.choice(random_activity_choice)))
    await bot.change_presence(activity=activity)



@bot.event
async def on_guild_join(guild):
    emb = disnake.Embed(
        title = 'Cyber Wolf',
        description = f"**Hello, I'm a Cyber Wolf disnake bot created by Janek#2549.\nBot official server:\n https://discord.gg/8sADnpZ4xY .\nTo see the list of my commands write:** `c!help`",
        color = 0xe90000
    )
    await guild.text_channels[0].send(embed=emb)



@bot.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.CommandOnCooldown):
         tme = f'{round(error.retry_after, 1)}'
         ntme = '.'.join(tme.split('.')[:-1])
         embed = disnake.Embed(
             title = 'Error :x:',
             description = f'You will only be able to use this command in `{ntme} seconds`.',
             color = disnake.Colour.from_rgb(255, 1, 7)
         )
         msg = await ctx.send(embed=embed)
     elif isinstance(error, commands.MissingPermissions):
         lol2 = disnake.Embed(
             title = '💻 Lack of rights',
             description = "You do not have sufficient permissions to execute this command",
             color=0xff0000
         )
         await ctx.author.send(embed=lol2)



    




    









@bot.command()
async def info(ctx):
     members = len(set(bot.get_all_members()))
     emb = disnake.Embed(title='Information about the bot.', description='All the main information about this bot.',
                         timestamp=ctx.message.created_at, color=0x2F3136)
     emb.add_field(name='Bot Server', value='[Press](https://discord.gg/8sADnpZ4xY)')
     emb.add_field(name='Youtube', value='[Click to Go](https://youtube.com/channel/UCla2irSqUgadg6oqrMVW42Q)')
     emb.add_field(name='Number of Members', value=f"{members}")
     emb.add_field(name='Number of Servers', value=f'{len(bot.guilds)}')
     emb.add_field(name='Creator', value='Janek#2549')
     emb.add_field(name='Version', value='0.0.7 alpha')
     emb.set_footer(text=f'2022 All rights reserved ©️Janek#2549', icon_url=f'https://images-ext-2.disnakeapp.net/external/3zTor6gW_ho2mVciyudm7joilaIh0NrBU6FtFBieVV4/%3Fsize%3D1024/https/cdn.disnakeapp.com/avatars/695690814491328642/fd60b5bfa1a306865b487142e4486770.webp')
     await ctx.send(embed=emb) 



bite = ['https://tenor.com/view/anime-bite-biting-angry-fight-gif-12390216', 'https://tenor.com/view/azumanga-cat-bite-anime-gif-18449891']
        
        
        
        
        
@bot.command()
async def bite(ctx, member: disnake.Member = None):
            if member is None:
            	member = ctx.author
            	embed = disnake.Embed(color=member.color, title="Reaction: bite")
            	embed.description = f"{ctx.author.mention} bites {member.mention}"
            	url = (random.choice(bite))
            	embed.set_image(url=url)
            	await ctx.send(embed=embed)
    
    
    

@bot.command()
@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send(embed = disnake.Embed(title = 'Changing the prefix', description = f'Command prefix change was successful👩‍🏭', color = 0x635942))


@bot.command()
async def uinfo(ctx,member:disnake.Member):
    emb = disnake.Embed(title=f'About user {member}',color=0xc27c0e)
    emb.add_field(name="Joined at:",value=member.joined_at,inline=False)
    emb.add_field(name='Nickname:',value=member.display_name,inline=False)
    emb.add_field(name='ID:',value=member.id,inline=False)
    emb.add_field(name="Account created at:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Used:  {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)
    await ctx.message.delete()






    
    



@bot.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: disnake.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.guild.ban(member)
    emb = disnake.Embed(title='BAN', timestamp=ctx.message.created_at, colour=disnake.Colour.from_rgb(207, 215, 255))
    emb.add_field(name='**Moderator**', value=ctx.message.author.mention, inline=True)
    emb.add_field(name='****User banned**', value=ctx.member.mention, inline=False)
    emb.add_field(name='**Reason**', value=reason, inline=False)
    emb.set_footer(text=f'Requested: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)




@bot.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: disnake.Member, reasonkick=None):
    await ctx.guild.kick(member)
    emb = disnake.Embed(title='Kick', timestamp=ctx.message.created_at, colour=disnake.Colour.from_rgb(207, 215, 255))
    emb.add_field(name='**Moderator**', value=ctx.message.author.mention, inline=True)
    emb.add_field(name='****User banned**', value=member.mention, inline=False)
    emb.add_field(name='**Reason**', value=reasonkick, inline=False)
    emb.set_footer(text=f'Requested: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)



@bot.command(usage="<member> [reason]")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: disnake.Member, *, reason="You didn't give a reason"):
        guild = ctx.guild
        mutedRole = disnake.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        mute = disnake.Embed(description=f"**Member went to mute.**\n\n"
                                         f"**Moderator:**: {ctx.author.mention}\n"
                                         f"**Member:**: {member.mention}", colour=disnake.Colour.blue())
        mute.add_field(name="Reason", value=reason)
        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(embed=mute)
        
       

@bot.command()
async def afk(ctx, rease):
        guild = ctx.guild
        afkRole = disnake.utils.get(guild.roles, name="afk")

        if not afkRole:
            afkRole = await guild.create_role(name="afk")

            for channel in guild.channels:
                await channel.set_permissions(afkRole, speak=False, send_messages=False, read_message_history=False,
                                              read_messages=False)
        afc = disnake.Embed(description=f"**{ctx.author.mention} in AFK.**\n\n", colour=disnake.Colour.blue())
        afc.add_field(name="For a reason", value=rease)
        await ctx.author.add_roles(afkRole, reason="reason")
        await ctx.send(embed=afc)
        





@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)
    await channel.delete_messages(messages)
    mestext = disnake.Embed(
          title=f"Cleared {amount} posts",
          description=f"**Moderator:** {ctx.author.mention}\n", colour=disnake.Colour.blue())
    await ctx.send(embed=mestext)


@bot.command(pass_context=True)
async def saytext(ctx, *, sayingtext):
    await ctx.message.delete()
    embed = disnake.Embed(
        title="Successfully sent",
        description=sayingtext,
        color=0xff0000)
    await ctx.send(embed=embed)
    
    
    
    
    
    
@bot.command(usage="<member>")
@commands.has_permissions(manage_messages=True)
async def unmute( ctx, member: disnake.Member):
        mutedRole = disnake.utils.get(ctx.guild.roles, name="Muted")

        await member.remove_roles(mutedRole)
        unmute = disnake.Embed(description=f"**User unmute.**\n\n"
                                           f"**Moderator:** {ctx.author.mention}\n"
                                           f"**User:** {member.mention}", colour=disnake.Colour.blue())
        await ctx.send(embed=unmute)


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: disnake.Member, nick):
    await member.edit(nick=nick)
    govno1 = disnake.Embed(
          title=f"Success!",
          description=f"Nick {member} successfully changed to **{nick}** ✅\n", colour=disnake.Colour.blue())
    await ctx.send(embed=govno1)
    
@bot.command()
async def hhhelp(ctx):
        embed = disnake.Embed(
        title='📌 | Help',
        description="c!ban (member) (reason)  - ban user.\n c!kick (member) (reason) - kick user.\n c!ava (member) - Submits the user's avatar.\n c!saytext - shows your text in embed.\n c!mute - mute user.\n c!unmute - unmute user.\n c!clear - cleaning up messages.\n c!shar - randomly answers your question.\n c!nick - change member's nickname.\n c!setprefix (prefix) - change prerix.\n c!info - bot information",
        color=0x2F3136
        )
        await ctx.send(embed=embed)


@bot.command()
async def dog(ctx):
            async with aiohttp.ClientSession() as ses:
                async with ses.get('https://some-random-api.ml/animal/dog') as r:
                    if r.status in range(200, 299):
                    	data = await r.json()
                    	image = data["image"]
                    	fact = data["fact"]
                    	await ctx.send(fact)
                    	await ctx.send(image)
                    	await ses.close()
                    else:
                    		await ctx.send("Error when making request")
                    		await ses.close()

@bot.command()
async def cat(ctx):
            async with aiohttp.ClientSession() as ses:
                async with ses.get('https://some-random-api.ml/animal/cat') as r:
                    if r.status in range(200, 299):
                    	data = await r.json()
                    	image = data["image"]
                    	await ctx.send(image)
                    	await ses.close()
                    else:
                    		await ctx.send("Error when making request")
                    		await ses.close()


@bot.command()
async def gstart(ctx, mins : int, * , prize: str):
    embed = disnake.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60) 

    embed.add_field(name = "Ends At:", value = f"{end} UTC")
    embed.set_footer(text = f"Ends {mins} mintues from now!")

    my_msg = await ctx.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(mins*60)


    new_msg = await ctx.channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await ctx.send(f"Congratulations! {winner.mention} won {prize}!")


def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]



@bot.command()
async def giveaway(ctx):
    await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

    questions = ["Which channel should it be hosted in?", 
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await bot.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)
    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = bot.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        return            

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


    embed = disnake.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    embed.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won {prize}!")

@bot.command()
async def reroll(ctx, channel : disnake.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The id was entered incorrectly.")
        return
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! The new winner is {winner.mention}.!")



@bot.command()
async def meme(ctx):
    embed = disnake.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@bot.command()
async def weather(ctx, *, city: str=None):
    try:
        if city is None:
            await ctx.message.add_reaction("❌")
        else:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=17063a3dd338e3cc73025afe67c4d8e1").json()

            if response["cod"] == 200:
                emb = disnake.Embed(
                    title=f"Weather in city: {response['name']}",
                    description=f"""
                    > **🌡 Temperature**: {round(response['main']['temp'] - 273, 0)}°C
                    > **💨 Wind speed**: {response['wind']['speed']} m/s
                    > **☁Cloudiness**: {response['clouds']['all']}%
                    > **📊 Status**: {response['weather'][0]['description']}
                    > **📅 Pressure**: {response['main']['pressure']}
                    > **👁‍🗨 Visibility**: {response['visibility']}
                    """,
                    timestamp=ctx.message.created_at,
                    colour=disnake.Color.from_rgb(
                        128, 128, 128
                    )
                )
                await ctx.reply(embed=emb, mention_author=False)
            else:
                emb = disnake.Embed(
                    title="**ERROR 404**",
                    colour=disnake.Color.from_rgb(
                        255, 0, 0
                    )
                )
                message = await ctx.reply(embed=emb, mention_author=False)
                await sleep(9)
                await message.delete()
    except Exception as _EX:
        print(f'[ERROR] : ({_EX}) : weather')








@bot.command()
async def anime(ctx, *,querry):
    try:
        anime = animec.Anime(querry)
    except:
        await ctx.send("No Anime Found")
        return
    embed = disnake.Embed(title=anime.title_english, description=f"{anime.description[200:]}...", color=0xc000ff )
    embed.add_field(name="Episodes:", value=str(anime.episodes))
    embed.add_field(name="Ratings:", value=str(anime.rating))
    embed.add_field(name="Broadcasts", value=str(anime.broadcast))
    embed.add_field(name="Status", value=str(anime.status))
    embed.add_field(name="Type", value=str(anime.type))
    embed.set_thumbnail(url=anime.poster)
    await ctx.message.reply(embed=embed)





@bot.command()
async def pat(ctx,member:disnake.Member):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animu/pat')
      json = await request.json()
      
      embed = disnake.Embed(title="юти)",description=f"{ctx.author.mention} stroked {member.mention}", color=disnake.Color.purple())
      embed.set_image(url=json['link'])
      await ctx.send(embed=embed)




       
   


@bot.command()
async def hug(ctx, member: disnake.Member = None):
    
    if member==ctx.author:return await ctx.send(embed=disnake.Embed(title=":(",description=f"you can't hug yourself...",color=disnake.Color.red()))
    if not member:
        await ctx.send(embed=disnake.Embed(title=":(",description=f"{ctx.author.mention} bro, to my chagrin you can't hug the air...\n\nmention someone(",color=disnake.Color.red()))
              
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animu/hug')
      json = await request.json()
      
      embed = disnake.Embed(title="юти)",description=f"{ctx.author.mention} hugged {member.mention}", color=disnake.Color.purple())
      embed.set_image(url=json['link'])
      await ctx.send(embed=embed)
   
    
        
    

       
@bot.command()
async def wink(ctx,member:disnake.Member):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/animu/wink')
      json = await request.json()
     
      embed = disnake.Embed(title="юти)",description=f"{ctx.author.mention} winked {member.mention}", color=disnake.Color.purple())
      embed.set_image(url=json['link'])
      await ctx.send(embed=embed)



@bot.command()
async def short(ctx, *, link):
        response=requests.get(f'https://clck.ru/--?url={link}')
        await ctx.send(content=f'<{response.text}>')










blacknegr = ['Anonymous BOT', 'Voice BOT', 'Multi-Bypass Nuker', 'Chaos BOT', 'Nitro Bot', 'Curtana', 'Артём', 'no-scum.com']










@bot.event
async def on_member_join(member):
    if member.bot and member.name in blacknegr:
        await member.ban(reason="CRASH BOT!!!")
        async for entry in member.guild.audit_logs(
                action=disnake.AuditLogAction.bot_add):
            adder = entry.user
            break
        try:
            await member.guild.ban(adder,
                                   reason="Добавил краш бота",
                                   delete_message_days=0)
        except:
            await member.guild.text_channels[0].send(
                f"@everyone <@{member.guild.owner_id}>",
                embed=disnake.Embed(
                    title="Добавили краш-бота",
                    description=f"Советую забанить {adder}, я сам не смог",
                    color=0xff0000))   



@bot.command()
async def python(ctx, *, code = None):
	admins = [695690814491328642,660176203755552768] # тут айди раз решённых людей через запятую
	if ctx.author.id in admins:
		if not code == None:
			try:
				exec(str(code))
				embed = disnake.Embed(
					title = "Запуск кода",
					description = f"```py \n{code}```",
					color = 0x31ff2e)
				await ctx.reply(embed = embed)
			except Exception as e:
				embed = disnake.Embed(
					title = "Ошибка в коде",
					description = f"```python> \n{str(type(e).__name__)}: {str(e)}```",
					color = 0xff0000)
				await ctx.reply(embed = embed)





@bot.command()
async def server(ctx):
        region = ctx.guild.region
        owner = ctx.guild.owner.mention
        all = len(ctx.guild.members)
        members = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
        bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
        channels = [len(list(filter(lambda m: str(m.type) == "text", ctx.guild.channels))),
                    len(list(filter(lambda m: str(m.type) == "voice", ctx.guild.channels)))]
        embed = disnake.Embed(title=f"{ctx.guild} information")
        embed.add_field(name="Statuses", value=f"Online: {statuses[0]} Idle: {statuses[1]} DND: {statuses[2]} Offline: {statuses[3]}")
        embed.add_field(name="Members", value=f"All: {all} Humans: {members} Bots: {bots}")
        embed.add_field(name="Channels", value=f"All: {channels[0] + channels[1]} Text: {channels[0]} Voice: {channels[1]}")
        embed.add_field(name="Members", value=f"All: {all} Humans: {members} Bots: {bots}")
        embed.add_field(name="Region", value=region)
        embed.add_field(name="Owner", value=owner)
        await ctx.send(embed=embed)




@bot.command()
async def achiev(ctx, achievement):
            async with aiohttp.ClientSession() as Session:
                async with Session.get(f'https://minecraftskinstealer.com/achievement/17/Achievement+Get%21/{achievement}') as achievement:
                	imageData = io.BytesIO(await achievement.read())
                	await Session.close()
                	
                	await ctx.send(file=disnake.File(imageData, 'achievement.png'))




@bot.command()
async def stick(ctx):
    loading = True
    text = ""
    message = await ctx.reply("-")
    while loading:
        text = "|"
        await message.edit(content = text)
        await asyncio.sleep(0.4)
        text = "/"
        await message.edit(content = text)
        await asyncio.sleep(0.4)
        text = "-"
        await message.edit(content = text)
        await asyncio.sleep(0.4)
        text2 = "\n"
        text2 = repr(text2)
        text2 = text2.replace("'", "")
        text2 = text2.replace("n", "")
        text = text2
        await message.edit(content = text)
    await asyncio.sleep(10)
    loading = False



@bot.command()
async def test(ctx):
  await ctx.send("Помощь", 
  components = [
  Select(
         placeholder = "Вибери пункт",
         options = [
            SelectOption(
              label = "Основное",
              value = "Option 1",
              description = "Основние команди бота",
              emoji = '🧰'
            ),
           SelectOption(
              label = "Модерация",
              value = "Option 2",
              description = "Команди для модерирования сервера",
              emoji = '🦺'
            ),
           SelectOption(
              label = "Настройки",
              value = "Option 3",
              description = "Настройки бота",
              emoji = '🛠'
            ),
         ])])



@bot.command()
async def ava(ctx, *,  avamember : disnake.Member):
    userAvatarUrl = avamember.avatar_url
    embed = disnake.Embed(
                title="Аватар пользователя | 👤",
                colour=0x00008B)
    embed.set_image(url=f'{userAvatarUrl}')
    await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
        emb = disnake.Embed(
        title='📌 | Help',
        description="Commands",
        color=0x2F3136)
        emb.add_field(name='Moderation', value='c!ban (member) (reason)  - ban user.\nc!kick (member) (reason) - kick user.\nc!mute (member) - mute user.\nc!unmute (member) - unmute user.')
        emb.add_field(name='Server', value='c!server - server information')
        emb.add_field(name='Fun', value='c!shar - randomly answers your question.\nc!afk (reasone) - go to afk.\nc!cat - random cat image.\nc!dog - random dog image.\nc!meme - random meme.\nc!achiev (text) - achievement minecraft meme.\nc!stick -spinning_stick')
        emb.add_field(name='GIVEAWAYS!(BETA!)', value='c!giveaway - start giveaway.')
        emb.add_field(name='Users', value='c!ava (member) - Submits the user avatar.\nc!nick - change member nickname.\nc!uinfo (member) - user information.')
        emb.add_field(name='Roleplay', value='c!wink - wink at a person.\nc!pat - pet a person\nc!hug - hag a person')
        emb.add_field(name='Anime', value='c!anime (anime name) - search anime')
        emb.add_field(name='Utils', value='c!weather (city) - show weather in city. P.S. You can enter city in any language.\nc!short (link url) - link shortener.')
        emb.add_field(name='Bot', value='c!info - bot information.\nc!help - command list\nc!setprefix (new prefix).')
        emb.add_field(name='Other', value='c!saytext - shows your text in embed.')
        emb.set_footer(text=f"Used:  {ctx.message.author}")
        
        await ctx.send(embed=emb)









bot.run(token)