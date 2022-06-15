import os
import telebot
import re
import traceback
import random
from nbnhhsh import nbnhhsh
from bilibili_api import sync, video

API_KEY = os.environ['api']
bot = telebot.TeleBot(API_KEY, parse_mode='MarkdownV2')
spwd = [['_','\_'], ['*','\*'], ['[','\['], [']','\]'], ['(','\('], [')','\)'], ['~','\~'], ['`','\`'], ['>','\>'], ['#','\#'], ['+','\+'], ['-','\-'], ['=','\='], ['|','\|'], ['{','\{'], ['}','\}'], ['.','\.'], ['!','\!']]
rep = ''
repable = True

@bot.message_handler(commands=['abbr'])
def abbr(message):
  try:
    print("ABBR Request Received from " + message.from_user.username + "\n")
    tit = '*'+message.text[5:54]+' \u6709\u53ef\u80fd\u662f*\n\- '
    res = nbnhhsh.suo(message.text[5:54])
    res = res.replace('\uff0c','\n- ')
    for wd in spwd:
        res = res.replace(wd[0],wd[1])
    res = res.replace('\uff08',' ||')
    res = res.replace('\uff09','||')
    bot.reply_to(message, tit+res)
  except Exception:
    print('Execution not Successful')
    emsg = "\nMessage Unformatted:\n"+message.text+"\n\n"+traceback.format_exc()+"\nIdentifier:\n"+str(random.randint(-2147483648,2147483647))
    print(emsg)
    for wd in spwd:
        emsg = emsg.replace(wd[0],wd[1])
    emsg = '*\u51fa\u9519\u4e86\uff01*\n\u8bf7\u8054\u7cfb[\u7ba1\u7406\u5458](https://t\.me/Patchouli\_MineCreeper)\u5e76\u9644\u4e0a\u60a8\u53d1\u9001\u7684\u5185\u5bb9\u4e0e\u4e0b\u5217\u4fe1\u606f\u3002\n```'+emsg+'```'
    bot.reply_to(message, emsg)

@bot.message_handler(func=lambda msg:'BV' in msg.text)
def bv(message):
  try:
    for index in [substr.start() for substr in re.finditer('BV' , message.text)]:
      print("BV Request Received from " + message.from_user.username + "\n")
      bv = message.text[index:index+12]
      response = bv
      v = video.Video(bvid=bv)
      info = sync(v.get_info())
      response += '\nav'+str(info.get('aid'))
      tit = info.get('title')
      for wd in spwd:
        tit = tit.replace(wd[0],wd[1])
      response += '\n——————\u89c6\u9891\u6982\u8ff0——————'
      response += '\n*'+tit+'*'
      resp2raw = '\n'+info.get('desc')
      resp2raw += '\n🕗 \u5171\u8ba1\u65f6\u957f\uff1a'+str(info.get('duration'))+'\u79d2'
      for wd in spwd:
        resp2raw = resp2raw.replace(wd[0],wd[1])
      response += resp2raw
      if info.get('stat').get('argue_msg') != '':
        resp2raw = info.get('stat').get('argue_msg')
        for wd in spwd:
          resp2raw = resp2raw.replace(wd[0],wd[1])
        response += '\n⚠️_'+resp2raw+'_'
      resp2raw = '\n——————\u4f5c\u8005\u4fe1\u606f——————'
      resp2raw += '\n'+info.get('owner').get('name')
      resp2raw += ' (UID:'+str(info.get('owner').get('mid'))+')'
      for wd in spwd:
        resp2raw = resp2raw.replace(wd[0],wd[1])
      response += resp2raw
      response += '\n——————\u53cd\u9988\u6570\u636e——————'
      response += '\n▶️ \u64ad\u653e\u6570\u91cf\uff1a'+str(info.get('stat').get('view'))
      response += '\n🗡 \u5f39\u5e55\u6570\u91cf\uff1a'+str(info.get('stat').get('danmaku'))
      response += '\n💬 \u8bc4\u8bba\u6570\u91cf\uff1a'+str(info.get('stat').get('reply'))
      response += '\n👍🏻 \u70b9\u8d5e\u6570\u91cf\uff1a'+str(info.get('stat').get('like'))
      response += '\n📁 \u6536\u85cf\u6570\u91cf\uff1a'+str(info.get('stat').get('favorite'))
      response += '\n❤ \u6295\u5e01\u6570\u91cf\uff1a'+str(info.get('stat').get('coin'))
      response += '\n\nhttps://www\.bilibili\.com/video/'+bv
      bot.reply_to(message, response)
  except Exception:
    print('Execution not Successful')
    emsg = "\nMessage Unformatted:\n"+message.text+"\n\n"+traceback.format_exc()+"\nIdentifier:\n"+str(random.randint(-2147483648,2147483647))
    print(emsg)
    for wd in spwd:
        emsg = emsg.replace(wd[0],wd[1])
    emsg = '*\u51fa\u9519\u4e86\uff01*\n\u8bf7\u8054\u7cfb[\u7ba1\u7406\u5458](https://t\.me/Patchouli\_MineCreeper)\u5e76\u9644\u4e0a\u60a8\u53d1\u9001\u7684\u5185\u5bb9\u4e0e\u4e0b\u5217\u4fe1\u606f\u3002\n```'+emsg+'```'
    bot.reply_to(message, emsg)


@bot.message_handler(func=lambda msg:msg.text!='')
def repeat(message):
  try:
    print("Single Message Received from " + message.from_user.username + "\n")
    global rep
    global repable
    if(message.text == rep):  
      if(repable):
        bot.send_message(message.chat.id, message.text)
        repable = False
    else:
      repable = True
      rep = message.text
  except Exception:
    print('Execution not Successful')
    emsg = "\nMessage Unformatted:\n"+message.text+"\n\n"+traceback.format_exc()+"\nIdentifier:\n"+str(random.randint(-2147483648,2147483647))
    print(emsg)
    for wd in spwd:
      emsg = emsg.replace(wd[0],wd[1])
    emsg = '*\u51fa\u9519\u4e86\uff01*\n\u8bf7\u8054\u7cfb[\u7ba1\u7406\u5458](https://t\.me/Patchouli\_MineCreeper)\u5e76\u9644\u4e0a\u60a8\u53d1\u9001\u7684\u5185\u5bb9\u4e0e\u4e0b\u5217\u4fe1\u606f\u3002\n```'+emsg+'```'
    bot.reply_to(message, emsg)

bot.polling()
