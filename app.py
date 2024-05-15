from random import randint
from twitchio.ext import commands
import requests

riot_api_key="RGAPI-3f11339e-8b6d-455a-81e9-399c0cb2c55b"

bot = commands.Bot(token="fh34l7b25oktw4y2t7x7xaavl78d2f", prefix="!", initial_channels=["coochamp", "coochampbot", "odiumamatio", "muhanzics","flipylol","killua_uc","brohan","pusi","mikeycarry"])

@bot.command()
async def cookie(ctx: commands.Context) -> None:
    await ctx.send(f"{ctx.author.name} gets a cookie!")

def puuid2summlvl(puuid):
    resp=requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://jp1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://ph2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://sg2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://th2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://tw2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    resp=requests.get("https://vn2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        return resp.json()['summonerLevel']
    return False

def puuid2rank(puuid):
    resp=requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://oc1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://tr1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://jp1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://jp1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://la1.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://la2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://la2.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://ph2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://ph2.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://ru.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://ru.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://sg2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://sg2.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://th2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://th2.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://tw2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://tw2.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    resp=requests.get("https://vn2.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
    if 'summonerLevel' in resp.json():
        resp2=requests.get("https://vn2.api.riotgames.com/lol/league/v4/entries/by-summoner/"+resp.json()["id"]+"?api_key="+riot_api_key)
        for l in resp2.json():
            if l["queueType"]=="RANKED_SOLO_5x5":
                return l["tier"]+" "+l["rank"]+" "+str(l["leaguePoints"])
    return False


@bot.command()
async def cheer(ctx: commands.Context)-> None:
    await ctx.send("pusiCheer pusiCheer pusiCheer pusiCheer pusiCheer")

@bot.command()
async def think(ctx: commands.Context)-> None:
    await ctx.send("NOBODY CARES")

@bot.command()
async def pary(ctx: commands.Context)-> None:
    await ctx.send("i love you pary 🥰")


@bot.command()
async def riot(ctx: commands.Context)-> None:
    await ctx.send("NICE GAME RIOT Madgeclap")


@bot.command()
async def patty(ctx: commands.Context)-> None:
    await ctx.send("she’s she, nothing else ")


@bot.command()
async def hate(ctx: commands.Context)-> None:
    await ctx.send("Me too Madge")

@bot.command()
async def lurk(ctx: commands.Context)-> None:
    await ctx.send("Have a nice day sir o7")


@bot.command()
async def ranksoloq(ctx: commands.Context,leagueid,leagueid1="",leagueid2="",leagueid3="",leagueid4="")-> None:
    rank=""
    name=leagueid
    if "#" in leagueid:
        rank=puuid2rank(tag2puuid(leagueid))
    elif "#" in leagueid1:
        name=leagueid+" "+leagueid1
    elif "#" in leagueid2:
        name=leagueid+" "+leagueid1+" "+leagueid2
    elif "#" in leagueid3:
        name=leagueid+" "+leagueid1+" "+leagueid2+" "+leagueid3
    elif "#" in leagueid4:
        name=leagueid+" "+leagueid1+" "+leagueid2+" "+leagueid3+" "+leagueid4
    
    if tag2puuid(name):
        if puuid2rank(tag2puuid(name)):
            rank= puuid2rank(tag2puuid(name))
            await ctx.send(name+" is "+rank+"LP!")
            return
        else:
            await ctx.send("This user has no SoloQ/DuoQ Rank")
            return
    else:
        ctx.send("User does not exist")
        return

    


@bot.command(name="leaguelvl")
async def leaguelvl(ctx: commands.Context, leagueid,leagueid1="",leagueid2="",leagueid3="",leagueid4="") -> None:
    lvl=""
    name=leagueid
    if "#" in leagueid:
        name=leagueid
    elif "#" in leagueid1:
        name=leagueid+" "+leagueid1
    elif "#" in leagueid2:
        name=leagueid+" "+leagueid1+" "+leagueid2
    elif "#" in leagueid3:
        name=leagueid+" "+leagueid1+" "+leagueid2+" "+leagueid3
    elif "#" in leagueid4:
        name=leagueid+" "+leagueid1+" "+leagueid2+" "+leagueid3+" "+leagueid4
        
    if tag2puuid(name):
        if puuid2summlvl(tag2puuid(name)):
            lvl= puuid2summlvl(tag2puuid(name))
            await ctx.send(f"{name} is {lvl} lvl!")
            return
        else:
            ctx.send("User does not exist")
            return
    else:
        ctx.send("User does not exist")
        return

    

@bot.command()
async def jam(ctx: commands.Context) -> None:
    await ctx.send("pusiJam pusiJam pusiJam pusiJam pusiJam ")


@bot.command(name="hehe")
async def hehe(ctx: commands.Context) -> None:
    await ctx.send("im bot rn xdd")

@bot.command(name="pokecatch") 
async def pokecatch(ctx: commands.Context) -> None:
    await ctx.send(" PausersHype ")



def tag2puuid(nametag):
    id=nametag.split("#")
    resp=requests.get("https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"+id[0]+"/"+id[1]+"?api_key="+riot_api_key)
    if "puuid" in resp.json():
        puuid=resp.json()['puuid']
        print(puuid)
        return puuid
    else:
        return False
    

def puuid2id(puuid):
    if puuid:
        resp=requests.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+puuid+"?api_key="+riot_api_key)
        return resp.json()[id]
    else:
        return False



bot.run()


