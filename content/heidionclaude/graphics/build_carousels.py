"""7-slide carousels for posts #5, #17 and #19 (1080x1350). Every slide has its own layout.
Run: python3 -I build_carousels.py   then: node render.mjs carousel
"""
import sys, pathlib
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from build_graphics import FONTS, THEMES  # noqa: E402

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{background:var(--bg);color:var(--ink);font-family:Lexend,sans-serif;position:relative;overflow:hidden}
.tag{position:absolute;top:56px;left:72px;right:72px;display:flex;justify-content:space-between;z-index:5;
  font:500 24px Lexend;letter-spacing:.22em;color:var(--lab);text-transform:uppercase}
.foot{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:center;z-index:5;
  font:500 28px Lexend;color:var(--ink)}
.swipe{font:600 28px Lexend;color:var(--acc)}
.pill{font:600 34px Lexend;padding:24px 40px;border-radius:999px;background:var(--acc);color:var(--bg)}
.s{font-family:Newsreader,serif;font-weight:500;letter-spacing:-.02em;line-height:.98}
.s em{font-style:italic;font-weight:400;color:var(--acc)}
.l{font-family:Lexend,sans-serif}
.abs{position:absolute}
.card{background:#FBF8F2;color:#1A1816;border-radius:24px;box-shadow:0 30px 70px rgba(30,10,30,.25)}
.mark{background:linear-gradient(transparent 58%, rgba(160,70,111,.6) 58%, rgba(160,70,111,.6) 92%, transparent 92%);padding:0 6px}
.strike{position:relative;display:inline-block}
.strike:after{content:"";position:absolute;left:-8px;right:-8px;top:52%;height:14px;background:#A0466F;transform:rotate(-3deg)}
.stamp{border:10px solid #A0466F;color:#A0466F;border-radius:18px;font:700 80px Lexend;letter-spacing:.06em;padding:4px 30px;display:inline-block}
"""

def slide(theme, n, body, last=False, pill="Join free →"):
    t = THEMES[theme]
    v = ";".join(f"--{k}:{x}" for k, x in t.items())
    right = f'<span class="pill">{pill}</span>' if last else '<span class="swipe">Swipe →</span>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head>
<body style="{v}"><div class="tag"><span>Heidi on Claude</span><span>{n} / 7</span></div>{body}
<div class="foot"><span>heidionclaude.com</span>{right}</div></body></html>"""

def cta(theme, line1, line2, ask):
    return slide(theme, 7, f"""
<div class="abs s" style="left:72px;right:72px;top:190px;font-size:104px">{line1}<br><em>{line2}</em></div>
<div class="abs" style="left:72px;right:72px;bottom:190px">
 <div class="s" style="font-style:italic;font-size:50px;margin-bottom:28px">{ask}</div>
 <div class="card" style="padding:36px 44px;display:flex;align-items:center;gap:30px">
  <div style="flex:none;width:96px;height:96px;border-radius:50%;background:#A0466F;color:#fff;font:600 50px Lexend;display:flex;align-items:center;justify-content:center">→</div>
  <div><div style="font:600 24px Lexend;letter-spacing:.18em;color:#A0466F">FREE COMMUNITY</div>
  <div style="font:500 40px Lexend;color:#38203E;margin-top:6px">heidionclaude.com/community</div>
  <div style="font:400 26px Lexend;color:#5A5048;margin-top:6px">Post what you're stuck on. I answer there.</div></div></div></div>""",
        last=True)

C = {}

# ======================= #5  5 signs =======================
c5 = []
c5.append(slide("ink", 1, """
<div class="abs s" style="right:60px;top:170px;font-size:740px;line-height:.8;color:#D9BE74">5</div>
<div class="abs s" style="left:72px;right:72px;bottom:430px;font-size:104px;color:#F8F4ED">signs AI is making your week <em>longer.</em></div>
<div class="abs" style="left:72px;right:72px;bottom:200px">
 <div style="display:flex;justify-content:space-between;font:500 26px Lexend;color:#a79d93;margin-bottom:12px"><span>Your week</span><span style="color:#D9BE74">over 100%</span></div>
 <div style="height:44px;border-radius:22px;background:#2A2622;position:relative">
  <div style="position:absolute;left:0;top:0;bottom:0;width:100%;border-radius:22px;background:linear-gradient(90deg,#B68A3E,#A0466F)"></div>
  <div style="position:absolute;right:-30px;top:-8px;bottom:-8px;width:90px;border-radius:30px;background:#A0466F;box-shadow:0 0 0 6px #1A1816"></div></div>
 <div style="font:500 28px Lexend;color:#F8F4ED;margin-top:24px">Count yours as you swipe.</div></div>"""))
tabs = "".join(f'<div style="flex:{f};min-width:0;height:74px;background:{"#FBF8F2" if i==0 else "#D8CFC2"};border-radius:14px 14px 0 0;padding:20px 12px;font:500 20px Lexend;color:#5A5048;white-space:nowrap;overflow:hidden">{t}</div>'
               for i,(t,f) in enumerate([("AI tools to try",3),("Try this one",2),("Top 50 AI",2),("New!!",1.4),("Must-have",1.4),("",1),("",.8),("",.7),("",.6),("",.5),("",.5),("",.4)]))
c5.append(slide("rose", 2, f"""
<div class="abs" style="left:0;right:0;top:150px;background:#C9BFB2;padding:16px 16px 0;display:flex;gap:6px">{tabs}</div>
<div class="abs" style="left:0;right:0;top:240px;height:300px;background:#FBF8F2"></div>
<div class="abs s" style="left:72px;top:290px;font-size:330px;color:#A0466F;line-height:.8">1</div>
<div class="abs s" style="left:72px;right:72px;top:620px;font-size:96px;color:#38203E">6 tabs of “AI tools <em>to try.</em>”</div>
<div class="abs l" style="left:72px;right:440px;top:950px;font:400 34px/1.4 Lexend;color:#3A3530">Every open tab is a decision you haven't made.</div>
<div class="abs" style="right:72px;top:900px;width:340px;background:#FFF6C9;padding:30px;transform:rotate(4deg);box-shadow:0 20px 40px rgba(0,0,0,.15)">
 <div style="font:600 22px Lexend;letter-spacing:.15em;color:#8C6A2A">SUBTRACT</div>
 <div class="s" style="font-size:44px;color:#1A1816;margin-top:8px">Close them all. Keep 1 for 30 days.</div></div>"""))
rows = "".join(f'<div style="display:flex;justify-content:space-between;padding:20px 0;border-bottom:2px solid #EFE9DE;font:400 28px Lexend"><span>{t}</span><span style="color:#b5aaa0;font-size:22px">opened: never</span></div>'
               for t in ("Best email prompt 🔥","Viral hook formula","Copy of copy of prompt","SAVE THIS one","Mega prompt v7","Prompt for prompts"))
c5.append(slide("plum", 3, f"""
<div class="abs s" style="left:72px;right:72px;top:150px;font-size:110px;color:#FBF8F2"><span style="color:#EFDEE2">2.</span> 40 saved prompts. <em>0 used.</em></div>
<div class="abs card" style="left:150px;right:150px;top:470px;height:640px;border-radius:56px;padding:44px;overflow:hidden;border:12px solid #38203E">
 <div style="font:600 30px Lexend;color:#54295A;margin-bottom:6px">Notes · Prompts <span style="background:#A0466F;color:#fff;border-radius:999px;padding:2px 14px;font-size:24px">40</span></div>{rows}</div>
<div class="abs" style="right:60px;top:880px;transform:rotate(-12deg)"><span class="stamp" style="background:#FBF8F2">KEEP 3</span></div>"""))
days = "".join(f'<div style="display:flex;gap:20px;align-items:center;margin-bottom:22px;opacity:{o}"><div style="flex:none;font:600 22px Lexend;color:#8C6A2A;width:110px">{d}</div><div style="background:#54295A;color:#fff;border-radius:28px;padding:20px 28px;font:400 28px Lexend">So, my business is… my clients are… my tone is…</div></div>'
               for d,o in (("Chat 1",.35),("Chat 2",.5),("Chat 12",.7),("Chat 47",1)))
c5.append(slide("deep", 4, f"""
<div class="abs s" style="left:72px;top:150px;font-size:330px;color:#A0466F;line-height:.8">3</div>
<div class="abs s" style="left:330px;right:72px;top:170px;font-size:92px;color:#38203E">Every chat starts <em>from zero.</em></div>
<div class="abs" style="left:72px;right:72px;top:520px">{days}</div>
<div class="abs card" style="left:72px;right:72px;bottom:170px;padding:30px 40px;display:flex;align-items:center;gap:26px">
 <div style="font:600 22px Lexend;letter-spacing:.15em;color:#A0466F;flex:none">SUBTRACT</div>
 <div class="s" style="font-size:42px;color:#38203E">Write 1 page about your business. Start every chat with it.</div></div>"""))
c5.append(slide("rose", 5, """
<div class="abs card" style="left:110px;right:110px;top:170px;height:620px;padding:50px;transform:rotate(-3deg);border-top:22px solid #A0466F">
 <div style="font:600 24px Lexend;letter-spacing:.2em;color:#8C6A2A">CLAUDE · REPORT CARD</div>
 <div style="display:flex;align-items:center;gap:40px;margin-top:30px">
  <div class="s" style="font-size:300px;color:#A0466F;line-height:.8"><span class="strike">F</span></div>
  <div style="font:400 32px/1.4 Lexend;color:#3A3530">Graded on<br><b>1 answer.</b><br>No second try.</div></div>
 <div class="s" style="font-style:italic;font-size:54px;color:#54295A;margin-top:30px">→ Draft 1 of 3</div></div>
<div class="abs s" style="left:72px;right:72px;top:860px;font-size:88px;color:#38203E"><span style="color:#A0466F">4.</span> You judged Claude on <em>1 bad answer.</em></div>
<div class="abs l" style="left:72px;right:72px;bottom:170px;font:500 32px Lexend;color:#54295A">Fix: reply “Here's what's off. Fix it.” Then again.</div>"""))
posts = "".join(f'<div style="background:#2A2622;border-radius:22px;padding:24px 28px;margin-bottom:16px;display:flex;justify-content:space-between;align-items:center"><span style="font:500 28px Lexend;color:#F8F4ED">{t}</span><span style="width:96px;height:52px;border-radius:26px;background:#A0466F;position:relative;flex:none"><span style="position:absolute;right:6px;top:6px;width:40px;height:40px;border-radius:50%;background:#fff"></span></span></div>'
                for t in ("“I 10x'd my output” 🚀","“You're falling behind”","“Stop everything. New tool.”"))
c5.append(slide("ink", 6, f"""
<div class="abs s" style="left:72px;right:72px;top:150px;font-size:112px;color:#F8F4ED"><span style="color:#D9BE74">5.</span> You feel behind <em>everyone online.</em></div>
<div class="abs" style="left:72px;right:72px;top:600px">
 <div style="display:flex;justify-content:flex-end;font:600 24px Lexend;letter-spacing:.15em;color:#D9BE74;margin-bottom:14px">MUTED ✓</div>{posts}</div>
<div class="abs l" style="left:72px;right:72px;bottom:170px;font:400 34px/1.4 Lexend;color:#d8cfc2">The feed shows you everyone's best day. <b style="color:#D9BE74">Mute it.</b></div>"""))
c5.append(cta("plum", "3 or more?", "You need less AI, set up once.", "Comment your number below."))
C["05"] = c5

# ======================= #17 Joan =======================
c17 = []
c17.append(slide("plum", 1, """
<div class="abs s" style="left:40px;top:120px;font-size:520px;line-height:.8;color:#A0466F">“</div>
<div class="abs s" style="left:72px;right:60px;top:470px;font-size:118px;color:#FBF8F2">I put this off for a year because it <span class="mark" style="font-style:italic">sounded technical.</span></div>
<div class="abs" style="left:72px;right:72px;bottom:180px;display:flex;align-items:center;gap:24px">
 <div style="width:90px;height:4px;background:#D9BE74"></div>
 <div style="font:600 28px Lexend;letter-spacing:.15em;color:#EFDEE2">JOAN · CLINICAL RESEARCHER</div></div>"""))
c17.append(slide("paper", 2, """
<div class="abs card" style="left:140px;right:140px;top:200px;padding:0;overflow:hidden;transform:rotate(-4deg)">
 <div style="background:#A0466F;color:#fff;padding:28px 40px;font:700 34px Lexend;letter-spacing:.2em">HELLO, I'M</div>
 <div style="padding:40px"><div class="s" style="font-size:96px;color:#38203E">Joan</div>
  <div style="font:400 32px Lexend;color:#5A5048;margin-top:10px">Clinical researcher</div>
  <div style="margin-top:34px;border-top:3px dashed #D9BE74;padding-top:26px;display:flex;justify-content:space-between;font:500 30px Lexend"><span>Lines of code written</span><span style="color:#A0466F">0</span></div></div></div>
<div class="abs s" style="left:72px;right:72px;bottom:190px;font-size:104px;color:#38203E">Not a tech person. <em>That was never the problem.</em></div>"""))
docs = "".join(f'<div class="abs card" style="left:{x}px;top:{y}px;width:480px;height:600px;transform:rotate({r}deg);padding:40px;border-radius:8px"><div style="font:600 24px Lexend;letter-spacing:.2em;color:#8C6A2A">{t}</div>' + "".join(f'<div style="height:14px;background:#EFE9DE;border-radius:7px;margin-top:22px;width:{w}%"></div>' for w in (90,72,84,60,78,50,66)) + '</div>'
               for x,y,r,t in ((40,160,-9,"NOTES"),(520,140,7,"FORMS"),(140,330,-2,"EMAILS"),(470,380,4,"CHECKLISTS")))
c17.append(slide("rose", 3, f"""{docs}
<div class="abs" style="left:0;right:0;bottom:0;height:460px;background:linear-gradient(transparent,#EFDEE2 35%)"></div>
<div class="abs s" style="left:72px;right:72px;bottom:180px;font-size:104px;color:#38203E">We started with <em>a pile of her documents.</em></div>"""))
c17.append(slide("ink", 4, """
<div class="abs s" style="left:72px;right:72px;top:150px;font-size:104px;color:#F8F4ED">Then we walked her process, <em>step by step.</em></div>
<svg class="abs" style="left:0;top:520px" width="1080" height="560" viewBox="0 0 1080 560">
 <path d="M220 120 C 420 40, 500 300, 540 280 S 760 140, 860 320" stroke="#D9BE74" stroke-width="6" fill="none" stroke-dasharray="18 14"/></svg>
<div class="abs card" style="left:72px;top:560px;width:300px;padding:28px;text-align:center;font:600 32px Lexend;color:#38203E">What comes in</div>
<div class="abs card" style="left:390px;top:760px;width:300px;padding:28px;text-align:center;font:600 32px Lexend;color:#38203E">What she does</div>
<div class="abs card" style="right:72px;top:860px;width:300px;padding:28px;text-align:center;font:600 32px Lexend;color:#38203E;background:#D9BE74">What goes out</div>
<div class="abs s" style="left:72px;bottom:180px;font-style:italic;font-size:48px;color:#D9BE74">Her process, in her words.</div>"""))
c17.append(slide("deep", 5, """
<style>.foot span:first-child{color:#F8F4ED}</style><div class="abs" style="left:0;top:0;bottom:0;width:50%;background:#1A1816"></div>
<div class="abs" style="left:72px;top:250px;width:400px">
 <div style="font:600 26px Lexend;letter-spacing:.2em;color:#a79d93">BEFORE</div>
 <div class="s" style="font-size:240px;color:#F8F4ED;margin-top:10px;white-space:nowrap">1<span style="font-size:110px"> yr</span></div>
 <div style="font:400 34px Lexend;color:#a79d93;margin-top:10px">put off</div></div>
<div class="abs" style="left:612px;top:250px;width:400px">
 <div style="font:600 26px Lexend;letter-spacing:.2em;color:#8C6A2A">AFTER</div>
 <div class="s" style="font-size:240px;color:#A0466F;margin-top:10px">1</div>
 <div style="font:400 34px Lexend;color:#3A3530;margin-top:10px">weekend</div></div>
<div class="abs card" style="left:72px;right:72px;bottom:170px;padding:34px 40px">
 <div class="s" style="font-size:56px;color:#38203E">By the end of the weekend she was <em>running it on her own.</em></div></div>"""))
c17.append(slide("plum", 6, """
<div class="abs" style="left:0;right:0;top:170px;display:flex;flex-direction:column">
 <div class="s" style="font-size:210px;padding:16px 72px;background:#FBF8F2;color:#38203E">Simple.</div>
 <div class="s" style="font-size:210px;padding:16px 72px;background:#EFDEE2;color:#54295A">Valuable.</div>
 <div class="s" style="font-size:210px;padding:16px 72px;background:#A0466F;color:#FBF8F2;font-style:italic">Done.</div></div>
<div class="abs" style="left:72px;bottom:180px;font:600 28px Lexend;letter-spacing:.15em;color:#EFDEE2">JOAN, IN HER OWN WORDS</div>"""))
c17.append(cta("ink", "Overwhelm looks like incompetence.", "Usually it's missing structure.", "If it sounded technical to you too, start here."))
C["17"] = c17

# ======================= #19 prompt library =======================
c19 = []
c19.append(slide("berry", 1, """
<div class="abs" style="left:170px;top:180px;width:740px;height:520px">
 <div class="abs" style="left:0;top:0;width:300px;height:90px;background:#F3D9E2;border-radius:24px 24px 0 0"></div>
 <div class="abs" style="left:0;top:60px;right:0;bottom:0;background:#F3D9E2;border-radius:0 24px 24px 24px;box-shadow:0 40px 80px rgba(0,0,0,.3)"></div>
 <div class="abs s" style="left:60px;bottom:50px;font-size:64px;color:#38203E">Saved prompts</div>
 <div class="abs" style="right:-40px;top:10px;width:190px;height:190px;border-radius:50%;background:#1A1816;color:#fff;font:700 96px Lexend;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 12px #A0466F">40</div></div>
<div class="abs s" style="left:72px;right:72px;top:780px;font-size:150px;color:#FBF8F2">Delete your <em>prompt library.</em></div>
<div class="abs" style="left:72px;bottom:180px;font:500 32px Lexend;color:#F3D9E2">Yes, really. 4 steps →</div>"""))
bubbles = "".join(f'<div class="abs card" style="left:{x}px;top:{y}px;padding:26px 34px;border-radius:40px;font:500 34px Lexend;color:#38203E;opacity:{o}">{t}</div>'
                  for x,y,t,o in ((72,600,"Which one was for emails?",1),(330,740,"Is this the new version?",.85),(110,880,"Do I edit it first?",.7),(300,1020,"Never mind. I'll write it myself.",.55)))
c19.append(slide("ink", 2, f"""
<div class="abs s" style="left:72px;right:72px;top:150px;font-size:108px;color:#F8F4ED">Every saved prompt is <em>a decision you make again.</em></div>{bubbles}"""))
c19.append(slide("paper", 3, """
<div class="abs" style="left:72px;top:160px;font:600 30px Lexend;letter-spacing:.2em;color:#A0466F">STEP 1</div>
<div class="abs" style="left:72px;right:72px;top:240px;display:flex;gap:20px">
 """ + "".join('<div class="s" style="flex:1;height:420px;border-radius:24px;background:#38203E;color:#FBF8F2;display:flex;align-items:center;justify-content:center"><span style="font-size:300px">?</span></div>' for _ in range(2)) + """</div>
<div class="abs s" style="left:72px;right:72px;top:720px;font-size:110px;color:#38203E">Count them. <em>All of them.</em></div>
<div class="abs" style="left:72px;right:72px;bottom:180px;font:400 34px Lexend;color:#5A5048">Notes app, docs, bookmarks, screenshots.</div>"""))
c19.append(slide("rose", 4, """
<div class="abs" style="left:72px;top:160px;font:600 30px Lexend;letter-spacing:.2em;color:#A0466F">STEP 2</div>
<div class="abs s" style="left:72px;right:72px;top:220px;font-size:110px;color:#38203E">Keep the 3 <em>you'd miss.</em></div>
""" + "".join(f'<div class="abs card" style="left:{x}px;top:{y}px;width:640px;padding:34px 40px;transform:rotate({r}deg);display:flex;gap:24px;align-items:center"><span style="font-size:60px;color:#D9BE74">★</span><span style="font:600 40px Lexend;color:#54295A">{t}</span></div>' for x,y,r,t in ((72,560,-3,"Reply in my voice"),(330,740,2,"Poke holes in my plan"),(140,920,-1,"Plan my week"))) + """
<div class="abs" style="right:72px;bottom:180px;font:400 26px Lexend;color:#5A5048">Yours will differ. The number stays 3.</div>"""))
c19.append(slide("ink", 5, """
<div class="abs" style="left:72px;top:160px;font:600 30px Lexend;letter-spacing:.2em;color:#D9BE74">STEP 3</div>
<div class="abs card" style="left:120px;right:120px;top:300px;padding:56px;border-radius:30px;text-align:center">
 <div style="font-size:90px">🗑</div>
 <div style="font:600 46px Lexend;color:#1A1816;margin-top:16px">Delete 37 items?</div>
 <div style="font:400 30px Lexend;color:#5A5048;margin-top:12px">You'll write a better one when you need it.</div>
 <div style="display:flex;gap:20px;margin-top:44px">
  <div style="flex:1;padding:26px;border-radius:18px;background:#EFE9DE;font:600 34px Lexend;color:#5A5048">Cancel</div>
  <div style="flex:1;padding:26px;border-radius:18px;background:#A0466F;font:600 34px Lexend;color:#fff;position:relative">Delete
   <svg style="position:absolute;right:30px;bottom:-60px" width="70" height="90" viewBox="0 0 70 90"><path d="M5 5 L5 70 L22 55 L35 85 L47 80 L34 50 L58 50 Z" fill="#fff" stroke="#1A1816" stroke-width="4"/></svg></div></div></div>
<div class="abs s" style="left:72px;right:72px;bottom:180px;font-size:96px;color:#F8F4ED">Yes. <em>All of them.</em></div>"""))
c19.append(slide("deep", 6, """
<div class="abs" style="left:72px;top:160px;font:600 30px Lexend;letter-spacing:.2em;color:#8C6A2A">STEP 4</div>
<div class="abs s" style="left:72px;right:72px;top:220px;font-size:104px;color:#38203E">Put your 3 <em>where you work.</em></div>
<div class="abs card" style="left:180px;right:180px;top:520px;height:620px;padding:44px;border-radius:8px;transform:rotate(2deg)">
 <div style="display:flex;justify-content:space-between;font:600 22px Lexend;letter-spacing:.15em;color:#8C6A2A"><span>MY 3 PROMPTS</span><span>PAGE 1 OF 1</span></div>
 """ + "".join(f'<div style="margin-top:36px"><div style="font:600 32px Lexend;color:#54295A"><span class="s" style="color:#A0466F;font-size:46px">{i}</span>&nbsp; {t}</div><div style="height:12px;background:#EFE9DE;border-radius:6px;margin-top:14px;width:85%"></div><div style="height:12px;background:#EFE9DE;border-radius:6px;margin-top:10px;width:60%"></div></div>' for i,t in enumerate(("Reply in my voice","Poke holes in my plan","Plan my week"),1)) + """
 <div style="font:400 24px Lexend;color:#5A5048;margin-top:34px">In a Claude Project's instructions, or 1 doc you keep open.</div></div>"""))
c19.append(cta("plum", "Fewer prompts.", "Used every day.", "Which 1 would you keep? Tell me in the comments."))
C["19"] = c19

if __name__ == "__main__":
    out = HERE / "html"; out.mkdir(exist_ok=True)
    for n, slides in C.items():
        assert len(slides) == 7, n
        for i, doc in enumerate(slides, 1):
            assert "—" not in doc and "–" not in doc
            (out / f"carousel-{n}-{i}.html").write_text(doc)
    print("wrote", sum(len(s) for s in C.values()))
