import discord
from discord.ext import commands
import os
import requests
import json
import re
import pprint
bot = commands.Bot(command_prefix='!')
n_and_urls={ }
def update_data():
  global n_and_urls
  languages=['en', 'ru', 'ko', 'de', 'fr', 'pt', 'zh-hans', 'zh-hant', 'es', 'it', 'pl']
  for langs in languages:
    response = requests.get("https://api.warframe.market/v1/items",headers={'Content-type': 'application/json','Language':langs})
    json_data = json.loads(response.text)
    pat="'item_name': ['\"]((?<=\").*?'.*?|.+?)['\"]"
    names=re.findall(pat,(str(json_data.values())));
    names = [ name.lower() for name in names ]
    urls=re.findall("'url_name': '(.*?)'",(str(json_data.values())));
    n_and_urls.update((zip(names, urls)))
  #response = requests.get("https://api.warframe.market/v1/items",headers={'Content-type': 'application/json','Language':languages[1]})
  #json_data = json.loads(response.text)
  #pat="'item_name': ['\"]((?<=\").*?'.*?|.+?)['\"]"
  #something=re.findall("{.*?}",(str(json_data.values())));
  #names=re.findall(pat,(str(json_data.values())));
  #print (names);
  #urls=re.findall("'url_name': '(.*?)'",(str(json_data.values())));
  #print (urls);
  #names = [ name.lower() for name in names ]
  #print (names);
  #n_and_urls=dict(zip(names, urls))
  if (n_and_urls):
    return ("Updated succesfully")
  else:
    return ("Update failed")

#def get_prices(url):
  
  
def get_link(arg):
  if (n_and_urls.get(arg)):
    return("https://warframe.market/items/"+n_and_urls.get(arg))
  else:
    return ('not found')
  
def get_item(arg):
  response = requests.get("https://api.warframe.market/v1/items")
  json_data = json.loads(response.text)
  #print (json_data.keys());
  #"'item_name': '(.*?)'|'item_name': \"(.*?)\""
  pattern1="'item_name': ['\"](.+?'??.+?)['\"]"
  pat2="'item_name': ['\"]((?<=\").*?'.*?|.+?)['\"]"
  pattern="(?:'item_name': ['](.+?)['])|(?:'item_name': [\"](.+?)[\"])";
  something=re.findall("{.*?}",(str(json_data.values())));
  #"'item_name': ['\"](.*?)['\"]"
  names=re.findall(pat2,(str(json_data.values())));
  urls=re.findall("'url_name': '(.*?)'",(str(json_data.values())));
  n_and_urls=dict(zip(names, urls))
  #print (json_data,sep='\n')
  #print (len(names))
  #print (len(urls))
  #pprint.pprint (n_and_urls)
  #print (re.findall("{.*?}",(str(json_data.values())))[2]);
  #print (len(list(json_data.values())));
  #print (json_data.items());
  #print (arg)
  if (n_and_urls.get(arg)):
    return("https://warframe.market/items/"+n_and_urls.get(arg))
  else:
    return ('not found')
  
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(update_data());

@bot.command()    
async def Granum(ctx):
  await ctx.send('FUCK YOU!')

@bot.command()
async def list(ctx, *, arg):
    await ctx.send(get_item(arg))

@bot.command()
async def link(ctx, *, arg):
    print (arg.lower())
    await ctx.send(get_link(arg.lower()))

@bot.command()
async def update(ctx):
    await ctx.send(update_data())
#get_item("");
#update_data();
#pprint.pprint(n_and_urls)
bot.run('*bot code*') 

