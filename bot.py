import discord
from discord.ext import commands
import random
import json
import keep_alive


# 讀檔案
with open('setting.json','r',encoding='UTF8') as jfile:
    jdata = json.load(jfile)
    
# 呼叫 bot前面加什麼字串
bot = commands.Bot(command_prefix='!')


# bot 啟動事件
@bot.event
async def on_ready():
    print(">> bot is online <<")



# command對話指令
# ctx = context(上下文), 針對發出指令的所在頻道回應

# 測試用ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

# 抽卡
@bot.command()
async def 抽卡(ctx):
    random_pic = random.choice(jdata['url_pic']) #隨機取json字典裡的url
    user_name = ctx.message.author.mention #存放user name用
    await ctx.send(f'{user_name}  玩家抽卡！\n牌組發出一陣耀眼的光芒...\n\n\n恭喜...你的夥伴是\n' + random_pic)

# 碩碩
@bot.command()
async def 碩碩(ctx):
    rd_rabbit_pic = random.choice(jdata['rabbit_pic']) #隨機取json字典裡的pic
    user_name = ctx.message.author.mention #存放user name用
    await ctx.send(f'{user_name}  點兔騎士向著小學全速的前進～～\n' + rd_rabbit_pic)

# ayaya
@bot.command()
async def ayaya(ctx):
    rd_ayaya_pic = random.choice(jdata['ayaya_pic']) #隨機取json字典裡的pic
    await ctx.send(f'(ᗒᗨᗕ)／ あやや！あやや！＼(ᗒᗨᗕ)\n＼(ᗒᗨᗕ) AYAYA！AYAYA！(ᗒᗨᗕ)／\n' + rd_ayaya_pic)

# 沒事
@bot.command()
async def 沒事(ctx):
    user_name = ctx.message.author.mention
    await ctx.send(f'{user_name}  不要再玩本宮了，再玩就把你poi掉~')

# 抱抱
@bot.command()
async def 抱抱(ctx):
    user_name = ctx.message.author.mention
    await ctx.send(f'{user_name}  想要抱抱,快來抱抱他吧😭😭😭')

# 掰掰
@bot.command()
async def 掰掰(ctx):
    user_name = ctx.message.author.mention
    await ctx.send(f'{user_name}  掰掰~有空要回來喝茶聊天啊~歡迎你的下一次光臨(〃´∀｀)ノ゙  ')

# isay
@bot.command()
async def isay(ctx):
    await ctx.send(f'Hey! Hey! Hey! START:DASH!')

# san
@bot.command()
async def san(ctx):
    await ctx.send(f'＼(・ω・＼)SAN値！(／・ω・)／ピンチ！\n＼(・ω・＼)SAN値！(／・ω・)／ピンチ！')

# 老司機
@bot.command()
async def 老司機(ctx):
    user_name = ctx.message.author.mention
    await ctx.send(f'看  {user_name}  那駕駛技術。。。原來是老司機！大家別上他的車！')

# 人類
@bot.command()
async def 人類(ctx):
    await ctx.send(f'你們人類總是要重覆同一樣的錯啊~給我休息一下可以嗎?!?😧')

# 魚
@bot.command()
async def 魚(ctx):
    await ctx.send(f'魚~♬ 好大的魚.虎紋鯊魚~🐟')

# 笨蛋
@bot.command()
async def 笨蛋(ctx):
    await ctx.send(f'八嘎八嘎～ 八嘎八嘎～ 八嘎八嘎～ 1 2 ⑨！')

# 喵
@bot.command()
async def 喵(ctx):
    await ctx.send(f'ㄨ喵! ㄨ喵! ㄨ喵! ㄨ喵! ㄨ喵! ㄨ喵! ㄨ喵!')

# 喵內
@bot.command()
async def 喵內(ctx):
    await ctx.send(f'(❛◡❛✿)喵內！喔嗨唷～喵內 塔答以媽～撒思嘎喵內(*´∀`)~♥')



# 執行bot
if __name__ == '__main__':
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])
