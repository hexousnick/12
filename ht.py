# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys, codecs
from gtts import gTTS
from googletrans import Translator

#===================SELF========================
try:
    client = LineClient(authToken='auth_')
except:
    client = LineClient()
channel = LineChannel(client)
poll = LinePoll(client)
#==================BOT LOGIN SUCCESS===============

#=================   BOT SETUP  ==================
clientMid = client.getProfile().mid
renBot = [clientMid]
KCML = [client]

vol = """[ HELLO TONG ^_^ ]

Self tong:
Me <- Look your contact
Speed/Sp <- Look speedbot
Mention <- Tagall
Check:on <- Check reader
Check:off <- Stop check reader
Reboot <- Restart bot
Broadcast [text] <- BC All Group!
Creator <- For look creator!

Protect tong:
Protectkick:[on/off] <- Protect from kicker

Kicker tong:
!boom <- Kick member w Mention
!kickall

[ S E L F B O T ]"""

protect = {
    "kick":{},
    "msgkick": False
}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
            if op.type == 19:
                if op.param1 in protect["kick"]:
                    if op.param2 in renBot:
                        pass
                    else:
                        try:
                            random.choice(KCML).kickoutFromGroup(op.param1, [op.param2])
                        except:
                            client.kickoutFromGroup(op.param1, [op.param2])
                else:
                    pass
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                msg.from_ = msg._from
                try:
                    if msg.contentType == 0:
                        try:
                            if protect["msgkick"] == True:
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in renBot:
                                        client.kickoutFromGroup(receiver, [target])
                                protect["msgkick"] = False
                        except:
                            protect["msgkick"] = False
                            client.sendText(receiver, 'Kick via mention has aborted!')
                    if msg.contentType == 0:
                        if msg.toType in [0,2]:
                            if text.lower() == 'help':
                                client.sendText(receiver, vol)
                            elif text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() in ['speed','sp']:
                                start = time.time()
                                client.sendText(receiver, "Load data response...")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "[T I M E Response] : \n%s" % (elapsed_time))
                            elif text.lower() == 'mention':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 100:
                                    client.mention(receiver, nama)
                                if jml > 100 and jml < 200:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                if jml > 200 and jml < 300:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                if jml > 300 and jml < 400:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                if jml > 400 and jml < 501:
                                    for i in range(0, 100):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(101, 200):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(201, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(301, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                    for m in range(401, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(receiver, nm5)             
                            elif text.lower() == 'check:on':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                                client.sendText(receiver, "Cek sider on!")
                            elif text.lower() == 'check:off':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, "Check reader off!")
                                else:
                                    client.sendText(receiver, "Type Check:on to get data siders")
                            elif text.lower() == 'reboot':
                                restart_program()
                            elif text.lower() == "!boom":
                                client.sendText(receiver, "Silahkan tag orangnya bre... Bebas mau berapa aja!")
                                time.sleep(0.5)
                                protect["msgkick"] = True
                            elif text.lower().startswith("protectkick"):
                                pset = text.split(":")
                                pk = text.replace(pset[0] + ":","")
                                if pk == "on":
                                    if receiver in protect["kick"]:
                                        client.sendText(receiver, "Protect kick already On!")
                                    else:
                                        protect["kick"][receiver] = True
                                        client.sendText(receiver, "Protect kick set On!")
                                if pk == "off":
                                    if receiver in protect["kick"]:
                                        del protect["kick"][receiver]
                                        client.sendText(receiver, "Protect kick set Off!")
                                    else:
                                        client.sendText(receiver, "Protect kick already Off!")
                            elif text.lower() == '!kickall':
                                if msg.toType == 2:
                                    gs = client.getGroup(receiver)
                                    client.sendText(receiver,"Just some casual cleansing ô!")
                                    targets = []
                                    for g in gs.members:
                                        targets.append(g.mid)
                                    if targets == []:
                                        client.sendText(receiver, 'Dah rata bosqu!')
                                    else:
                                        for target in targets:
                                            client.kickoutFromGroup(receiver, [target])
                                else:
                                    client.sendText(receiver, 'Lu ngapain onin selain di grup?')
                            elif text.lower().startswith("broadcast"):
                                txt = text.split(" ")
                                tastk = text.replace(txt[0] + " ","")
                                sx = client.getGroupIdsJoined()
                                for ak in sx:
                                    client.sendText(receiver, '[ B R O A D C A S T ]\n' + ak)
                            elif text.lower() == 'creator':
                                client.tag(receiver, "uebcbec2df1e585a2bc487d71de2b26fb")
                                client.sendMessage(receiver, None, contentMetadata={'mid': "uebcbec2df1e585a2bc487d71de2b26fb"}, contentType=13)
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                client.sendText(op.param1, '[55] NOTIFIED_READ_MESSAGE : '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
