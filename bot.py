import discord
from discord.ext import commands
import random
import json
import keep_alive


# 讀檔案
with open('setting.json','r',encoding='UTF8') as jfile:
    jdata = json.load(jfile)
    
# 呼叫 bot前面加什麼字串
# intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


# bot 啟動事件
@bot.event
async def on_ready():
    print(">> bot is online <<")


# 以下對話指令, bot 指令
# ctx = context(上下文), 針對發出指令的所在頻道回應
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
    #jdata['ayaya_pic'] 也有圖庫
    rd_ayaya_gif = random.choice(jdata['ayaya_gif']) #隨機取json字典裡的pic
    await ctx.send(f'(ᗒᗨᗕ)／ あやや！あやや！＼(ᗒᗨᗕ)\n＼(ᗒᗨᗕ) AYAYA！AYAYA！(ᗒᗨᗕ)／\n' + rd_ayaya_gif)

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
    isay_gif = str(jdata['isay_gif'][0])
    await ctx.send(f'Hey! Hey! Hey! START:DASH!\n' + isay_gif)

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
    rd_MyaNee_gif = random.choice(jdata['MyaNee_gif']) #隨機取json字典裡的pic
    await ctx.send(f'(❛◡❛✿)喵內！～喵內(*´∀`)~♥\n' + rd_MyaNee_gif)

# 超跑
@bot.command()
async def 超跑(ctx):
  await ctx.send(f'轟隆隆隆🤣🤣隆隆隆隆衝衝衝衝😏😏😏拉風😎😎😎引擎發動🔑🔑🔑引擎發動+🚗+👉+🚗 \n\
讓😯 看到的人以為是夢😱😱 還沒醒來😴😴 就已經無影無蹤👻👻 \n\
風 💨💨 敲醒每一個面孔😲😲 我是明天🤙🤙 被 贊嘆的驚悚😵😵 \n\
讓😨😨 看到的人全部感動😭😭 \n\
0⃣到💯K only 4⃣秒鐘😏😏 \n\
紅燈停 綠燈行🚥🚥 看到行人要當心🚶♀🚶♀ 快車道 慢車道😈😈平安回家才是王道 💪💪 \n\
開車🚗🚗不是騎車🏍🏍不怕沒戴安全帽👲👲只怕警察👮♂👮♂ BI BI BI 叫我路邊靠 😩😩 \n\
BI BI BI BI BI 大燈忘了開😏😏 BI BI BI BI BI 駕照沒有帶🤫🤫\n\
BI BI BI BI BI 偷偷講電話😎😎 BI BI BI BI BI 沒繫安全帶 😬😬\n\
我的夢幻車子🚗🚗就是最辣🌶🌶的美女👸👸 有她陪伴😏😏哪怕車上只有收音機 📻📻\n\
我就像隻野狼🐺🐺身上披著羊🐑🐑的皮 我的心情🤪🤪好比開著一架戰鬥機🛩🛩')

# 穿山甲
@bot.command()
async def 穿山甲(ctx):
    pangolin_gif = str(jdata['pangolin_gif'][0]) #取json字典裡的url
    await ctx.send(f':motor_scooter::motorcycle:欸幹:astonished:！ \n\
穿山甲欸:face_with_monocle::face_with_monocle:！ \n\
嗚呼:sunglasses::sunglasses::triumph::triumph:！ \n\
這可以養嗎:zany_face::zany_face:！？ \n\
欸蟑螂，這可以養嗎:thinking::thinking:！ \n\
我不知道:face_with_monocle::face_with_monocle: \n\
你抓回家:triumph::triumph:！ \n\
欸借過借過不要跑:astonished::astonished::astonished:！ \n\
嗚嗚他跑掉了:scream::scream:！ \n\
嗚呼呼:triumph::triumph::triumph:！ \n\
喔好屌:eggplant:喔！ \n' 
+ pangolin_gif)

# 霸主
@bot.command()
async def 霸主(ctx):
    rd_bachu_pic = random.choice(jdata['bachu_pic']) #取json字典裡的url
    await ctx.send('王希銘：\n' + rd_bachu_pic)


# 執行bot
if __name__ == '__main__':
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])