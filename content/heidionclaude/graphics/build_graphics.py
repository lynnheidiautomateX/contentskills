"""Build the 30 post graphics (1080x1350) as HTML, in the Heidi on Claude look.
Run: python3 -I build_graphics.py   then: node render.mjs
"""
import json, pathlib

OUT = pathlib.Path(__file__).parent
FONTS = ("https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600"
         "&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400;1,6..72,500"
         "&family=JetBrains+Mono:wght@400;500&display=swap")

THEMES = {
  # bg, headline ink, accent (italics), label, card bg, card ink, line
  "paper": dict(bg="#F8F4ED", ink="#54295A", acc="#A0466F", lab="#A0466F", card="#FBF8F2", cink="#1A1816", line="#D9BE74"),
  "plum":  dict(bg="#54295A", ink="#FBF8F2", acc="#EFDEE2", lab="#EFDEE2", card="#FBF8F2", cink="#1A1816", line="#D9BE74"),
  "rose":  dict(bg="#EFDEE2", ink="#38203E", acc="#A0466F", lab="#A0466F", card="#FBF8F2", cink="#1A1816", line="#B68A3E"),
  "ink":   dict(bg="#1A1816", ink="#F8F4ED", acc="#D9BE74", lab="#D9BE74", card="#2A2622", cink="#F8F4ED", line="#B68A3E"),
  "deep":  dict(bg="#EFE9DE", ink="#38203E", acc="#A0466F", lab="#8C6A2A", card="#FBF8F2", cink="#1A1816", line="#B68A3E"),
  "berry": dict(bg="#A0466F", ink="#FBF8F2", acc="#F3D9E2", lab="#F3D9E2", card="#FBF8F2", cink="#1A1816", line="#D9BE74"),
}

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{background:var(--bg);color:var(--ink);font-family:Lexend,sans-serif;position:relative;overflow:hidden}
.top{position:absolute;top:58px;left:96px;right:96px;display:flex;justify-content:space-between;
  font:500 26px Lexend;letter-spacing:.22em;color:var(--lab);text-transform:uppercase}
.wrap{position:absolute;left:96px;right:96px;top:170px;bottom:200px;display:flex;flex-direction:column}
.kick{font:500 28px Lexend;letter-spacing:.2em;text-transform:uppercase;color:var(--lab);margin-bottom:22px}
h1{font-family:Newsreader,serif;font-weight:500;font-size:var(--hs,92px);line-height:1.04;letter-spacing:-.015em;color:var(--ink)}
h1 em{font-style:italic;color:var(--acc);font-weight:400}
.vis{flex:1;position:relative;margin-top:48px}
.foot{position:absolute;left:96px;right:96px;bottom:64px;display:flex;justify-content:space-between;align-items:center}
.url{font:500 32px Lexend;color:var(--ink)}
.pill{font:600 34px Lexend;padding:24px 40px;border-radius:999px;background:var(--acc);color:var(--bg)}
.card{background:var(--card);color:var(--cink);border-radius:22px;box-shadow:0 24px 60px rgba(40,20,40,.18)}
.mono{font-family:'JetBrains Mono',monospace}
.serif{font-family:Newsreader,serif}
.strike{position:relative;display:inline-block}
.strike:after{content:"";position:absolute;left:-6px;right:-6px;top:52%;height:9px;background:#A0466F;transform:rotate(-2deg)}
.chip{display:inline-block;padding:12px 24px;border-radius:999px;font:500 28px Lexend}
.center{display:flex;align-items:center;justify-content:center}
"""

def page(theme, kicker, head, vis, pill, hs=None, top_right=""):
    t = THEMES[theme]
    vars_ = ";".join(f"--{k}:{v}" for k, v in t.items()) + (f";--hs:{hs}px" if hs else "")
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head>
<body style="{vars_}">
<div class="top"><span>Heidi on Claude</span><span>{top_right}</span></div>
<div class="wrap"><div class="kick">{kicker}</div><h1>{head}</h1><div class="vis">{vis}</div></div>
<div class="foot"><span class="url">heidionclaude.com</span><span class="pill">{pill}</span></div>
</body></html>"""

def bubble(text, me=True, style=""):
    bg = "#54295A" if me else "#FBF8F2"
    fg = "#FBF8F2" if me else "#1A1816"
    al = "flex-end" if me else "flex-start"
    return (f'<div style="display:flex;justify-content:{al};margin:12px 0">'
            f'<div style="max-width:78%;background:{bg};color:{fg};padding:22px 30px;border-radius:30px;'
            f'font:400 30px/1.35 Lexend;box-shadow:0 10px 30px rgba(0,0,0,.12);{style}">{text}</div></div>')

def check(text, on=True, color="#A0466F"):
    box = (f'<span style="flex:none;width:52px;height:52px;border-radius:12px;border:4px solid {color};'
           f'display:flex;align-items:center;justify-content:center;font:600 34px Lexend;'
           f'background:{color if on else "transparent"};color:#FBF8F2">{"✓" if on else ""}</span>')
    return (f'<div style="display:flex;gap:26px;align-items:center;font:400 36px/1.25 Lexend;margin:18px 0">'
            f'{box}<span>{text}</span></div>')

S = {}

# 1 Story: the closed tab
S[1] = page("paper", "Sound familiar?", "You typed one line. <em>Then you closed the tab.</em>", """
<div class="card" style="position:absolute;inset:0 0 10px 0;overflow:hidden">
 <div style="background:#EFE9DE;height:78px;display:flex;align-items:flex-end;padding-left:24px;gap:10px">
  <div style="background:#FBF8F2;border-radius:16px 16px 0 0;padding:16px 26px;font:500 26px Lexend;display:flex;gap:40px;align-items:center">
   Claude <span style="display:inline-flex;width:46px;height:46px;border-radius:50%;background:#A0466F;color:#fff;align-items:center;justify-content:center;font:600 28px Lexend;box-shadow:0 0 0 10px rgba(160,70,111,.22)">×</span></div></div>
 <div style="padding:30px 40px">
  """ + bubble("Write a post for my business.") + bubble(
  '<span style="color:#8a8079">In today\'s fast-paced digital landscape, businesses like yours are leveraging innovative solutions to unlock…</span>', False) + """
  <div style="margin-top:26px;font:500 26px Lexend;color:#A0466F;letter-spacing:.06em">↑ A STRANGER WROTE THIS. NOT YOU.</div>
 </div></div>""", "Fix the setup →", hs=96)

# 2 Myth: prompt engineering course
S[2] = page("plum", "Myth", "Skip the <em>prompt engineering</em> course.", """
<div class="card" style="position:absolute;left:30px;right:30px;top:10px;bottom:40px;transform:rotate(-3deg);border:6px double #B68A3E;padding:48px;text-align:center">
 <div style="font:500 24px Lexend;letter-spacing:.3em;color:#8C6A2A">CERTIFICATE OF COMPLETION</div>
 <div class="serif" style="font-size:62px;margin-top:26px;color:#38203E">Advanced Prompt Engineering</div>
 <div style="font:400 28px Lexend;color:#5A5048;margin-top:20px">12 modules · 40 hours · $497</div>
 <div style="margin-top:44px;font:400 30px Lexend;color:#5A5048">What you needed instead:</div>
 <div class="serif" style="font-style:italic;font-size:52px;color:#A0466F;margin-top:10px">“Brief it like a new hire.”</div>
 <div style="position:absolute;right:50px;bottom:40px;transform:rotate(-10deg);border:8px solid #A0466F;color:#A0466F;font:600 64px Lexend;padding:6px 26px;border-radius:14px;letter-spacing:.08em;opacity:.92">SKIP</div>
</div>""", "Context wins →", hs=100)

# 3 Question: the task that shouldn't exist
days = ["Mon","Tue","Wed","Thu","Fri"]
cells = ""
for i, d in enumerate(days):
    blocks = ""
    for j in range(4):
        hit = (i == 2 and j == 1)
        if hit:
            blocks += ('<div style="height:96px;border-radius:12px;background:#A0466F;color:#fff;font:600 24px Lexend;'
                       'display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 8px rgba(160,70,111,.25);position:relative">'
                       '???<span style="position:absolute;top:-24px;right:-20px;background:#1A1816;color:#fff;border-radius:999px;padding:6px 14px;font:600 20px Lexend">DELETE</span></div>')
        else:
            blocks += '<div style="height:96px;border-radius:12px;background:#EFE9DE"></div>'
    cells += f'<div style="flex:1;display:flex;flex-direction:column;gap:14px"><div style="font:500 24px Lexend;color:#5A5048;text-align:center">{d}</div>{blocks}</div>'
S[3] = page("rose", "Your turn", "There's 1 task in your week that <em>shouldn't exist.</em>",
  f'<div class="card" style="position:absolute;inset:0 0 10px 0;padding:36px;display:flex;gap:16px">{cells}</div>',
  "Name yours ↓", hs=90)

# 4 Re-explaining
reps = "".join(bubble("So, my business is… I serve… my tone is…", True,
        f"opacity:{o};font-size:26px") for o in (0.35, 0.55, 0.8))
S[4] = page("deep", "The expensive habit", "Re-explaining your business <em>every single chat.</em>", f"""
<div style="position:absolute;left:0;width:56%;top:0">{reps}
 <div style="font:600 30px Lexend;color:#A0466F;text-align:right;margin-top:8px">Chat #47 ↺</div></div>
<div class="card" style="position:absolute;right:0;width:38%;top:30px;bottom:30px;padding:30px;transform:rotate(2deg)">
 <div style="font:600 24px Lexend;letter-spacing:.15em;color:#8C6A2A">1 PAGE</div>
 <div class="serif" style="font-size:40px;margin:10px 0 18px;color:#38203E">About my business</div>
 {''.join(f'<div style="font:400 24px/1.4 Lexend;color:#3A3530;border-top:2px solid #EFE9DE;padding:10px 0">{x}</div>' for x in ['Who I serve','How I sound','3 things I never say','My best work'])}
 <div style="margin-top:14px" class="chip" ><span style="background:#54295A;color:#fff;padding:10px 18px;border-radius:999px;font:500 22px Lexend">Written once ✓</span></div>
</div>""", "Write it once →", hs=90)

# 5 Checklist
items = ['6 tabs of “AI tools to try”', '40 saved prompts, never used', 'Every chat starts from zero',
         'Judged Claude on 1 bad answer', 'You feel behind everyone online']
S[5] = page("paper", "Count yours", "5 signs AI is <em>adding</em> to your week.", f"""
<div class="card" style="position:absolute;inset:0 0 10px 0;padding:40px 50px">
 {''.join(check(t, on=i in (0,1,2)) for i,t in enumerate(items))}
 <div style="margin-top:26px;border-top:3px dashed #D9BE74;padding-top:24px;display:flex;justify-content:space-between;align-items:center">
  <span class="serif" style="font-size:46px;color:#54295A">3 or more?</span>
  <span class="serif" style="font-style:italic;font-size:46px;color:#A0466F">You need less.</span></div>
</div>""", "Save this →", hs=100)

# 6 Ask me 5 questions
qs = ["Who reads this?", "What should they do after?", "What tone?", "Any example I like?", "What's off-limits?"]
S[6] = page("ink", "1 line fixes it", "Generic answers? <em>You asked too fast.</em>", f"""
<div class="card" style="position:absolute;left:0;right:0;top:0;padding:34px 40px;border:2px solid #B68A3E">
 <div class="mono" style="font-size:22px;color:#D9BE74;letter-spacing:.1em">ADD BEFORE YOUR REQUEST</div>
 <div class="serif" style="font-size:52px;line-height:1.15;margin-top:12px">“Ask me 5 questions before you answer.”</div></div>
<div style="position:absolute;left:0;right:0;bottom:10px;display:flex;flex-wrap:wrap;gap:16px">
 {''.join(f'<span class="chip" style="background:#2A2622;color:#F8F4ED;border:2px solid #5A5048"><b style="color:#D9BE74">{i+1}</b>&nbsp; {q}</span>' for i,q in enumerate(qs))}</div>
""", "Try it today →", hs=96)

# 7 Shannon
S[7] = page("rose", "Client story", "A 75-page guide. <em>Updated in one evening.</em>", """
<div style="position:absolute;left:10px;top:20px;width:430px;height:540px">
 <div class="card" style="position:absolute;inset:0;transform:rotate(-6deg);opacity:.6"></div>
 <div class="card" style="position:absolute;inset:0;transform:rotate(-3deg);opacity:.8"></div>
 <div class="card" style="position:absolute;inset:0;padding:40px">
  <div style="font:600 22px Lexend;letter-spacing:.2em;color:#8C6A2A">THE GUIDE</div>
  <div class="serif" style="font-size:56px;color:#38203E;margin-top:10px"><span class="strike">2025</span> edition</div>
  <div style="font:400 26px Lexend;color:#5A5048;margin-top:16px">75 pages</div>
  <div style="margin-top:30px;display:flex;flex-direction:column;gap:14px">""" + "".join(
   f'<div style="height:14px;border-radius:7px;background:#EFE9DE;width:{w}%"></div>' for w in (90,75,85,60,80,50)) + """</div></div></div>
<div style="position:absolute;right:0;top:60px;width:380px">
 <div class="serif" style="font-style:italic;font-size:46px;line-height:1.2;color:#38203E">“Back to me for review the same evening, with designs and all.”</div>
 <div style="font:500 26px Lexend;color:#A0466F;margin-top:24px;letter-spacing:.08em">SHANNON, ONLINE SELLER</div></div>
""", "Start from the last version →", hs=90)

# 8 Robotic vs blank chat
S[8] = page("plum", "Myth", "AI isn't robotic. <em>Blank chats are.</em>", """
<div class="card" style="position:absolute;left:0;top:10px;width:45%;bottom:20px;padding:30px;opacity:.95">
 <div style="font:600 22px Lexend;letter-spacing:.15em;color:#8a8079">BLANK CHAT</div>
 <div style="margin-top:24px;height:200px;border:3px dashed #D9BE74;border-radius:18px;display:flex;align-items:center;justify-content:center;font:400 28px Lexend;color:#aaa">nothing to go on</div>
 <div style="font:400 26px/1.45 Lexend;color:#8a8079;margin-top:24px">“Unlock your potential with our innovative solutions.”</div></div>
<div style="position:absolute;right:0;top:10px;width:48%;bottom:20px">
 """ + "".join(f'<div class="card" style="padding:22px 26px;margin-bottom:16px;transform:rotate({r}deg)"><div style="font:600 20px Lexend;color:#A0466F;letter-spacing:.12em">YOUR POST #{i}</div><div style="height:12px;background:#EFE9DE;border-radius:6px;margin-top:12px;width:90%"></div><div style="height:12px;background:#EFE9DE;border-radius:6px;margin-top:10px;width:70%"></div></div>' for i,r in ((1,-2),(2,1.5),(3,-1))) + """
 <div style="font:600 30px Lexend;color:#EFDEE2;margin-top:14px">→ sounds like you</div></div>
""", "Feed it 3 posts →", hs=100)

# 9 Poll
opts = [("A","Don't know where to start"),("B","Answers sound generic"),("C","Don't trust it yet"),("D","OK… it's time")]
S[9] = page("berry", "Vote", "I don't think <em>time</em> is your AI problem.", f"""
<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;gap:22px">
 {''.join(f'<div class="card" style="padding:30px;display:flex;flex-direction:column;justify-content:space-between{";opacity:.6" if l=="D" else ""}"><span class="serif" style="font-size:110px;line-height:1;color:#A0466F">{l}</span><span style="font:500 32px/1.25 Lexend">{t}</span></div>' for l,t in opts)}
</div>""", "Comment your letter ↓", hs=96)

# 10 To-do cut
todo = [("Reply to Sam's email", False), ("Redo pricing PDF", True), ("Post on 4 platforms", True), ("Client call prep", False),
        ("Reformat old invoices", True), ("Rewrite bio again", True), ("Send proposal", False)]
S[10] = page("paper", "Monday, 10 minutes", "Your to-do list doesn't need an app. <em>It needs a cut.</em>", f"""
<div class="card" style="position:absolute;left:60px;right:60px;top:0;bottom:10px;padding:40px 50px;transform:rotate(-1.5deg);background:#FBF8F2">
 {''.join(f'<div style="font:400 36px Lexend;padding:12px 0;border-bottom:2px solid #EFE9DE;color:{"#b5aaa0" if cut else "#1A1816"}"><span class="{"strike" if cut else ""}">{t}</span></div>' for t,cut in todo)}
 <div style="position:absolute;right:-30px;bottom:30px;transform:rotate(8deg);background:#A0466F;color:#fff;font:600 44px Lexend;padding:14px 30px;border-radius:16px">−4 tasks</div>
</div>""", "Steal the prompt →", hs=86)

# 11 Feed of noise
S[11] = page("ink", "Permission granted", "You're not behind. <em>You follow too many people.</em>", """
<div style="position:absolute;left:150px;right:150px;top:0;bottom:0;border-radius:50px;border:10px solid #3A3530;background:#2A2622;padding:30px;overflow:hidden">
 """ + "".join(f'<div style="background:#3A3530;border-radius:20px;padding:22px 24px;margin-bottom:16px;opacity:{o}"><div style="font:600 26px Lexend;color:#F8F4ED">{t}</div><div style="display:flex;justify-content:space-between;margin-top:12px"><span style="font:400 22px Lexend;color:#a79d93">@ai_guru · 2m</span><span style="font:600 22px Lexend;color:#D9BE74">Unfollow</span></div></div>' for t,o in (("10 NEW AI tools you NEED 🚨",1),("I automated my whole life",.8),("You're falling behind if…",.6),("47 prompts to 10x you",.4),("Stop everything. Read this.",.25))) + """
</div>""", "Mute the noise →", hs=92)

# 12 Five hours
S[12] = page("rose", "Be honest", "5 extra hours a week. <em>What would you do?</em>", """
<div style="position:absolute;inset:0;display:flex;gap:40px;align-items:center">
 <div class="serif" style="font-size:300px;line-height:.85;color:#54295A">+5<span style="font-size:90px">h</span></div>
 <div style="flex:1;display:flex;flex-direction:column;gap:16px">
  <div class="card" style="padding:20px 28px;font:400 34px Lexend;color:#b5aaa0"><span class="strike">More work</span></div>
  """ + "".join(f'<div class="card" style="padding:20px 28px;font:500 34px Lexend">{x}</div>' for x in ("Rest","Sell","Create","Home for dinner")) + """
 </div></div>""", "Tell me ↓", hs=96)

# 13 Same reply again
S[13] = page("deep", "Inbox", "You've already written <em>this reply.</em>", """
<div style="position:absolute;inset:0 40px 20px 40px">
 """ + "".join(f'<div class="card" style="position:absolute;left:{x}px;right:{-x}px;top:{y}px;padding:28px 34px;opacity:{o}"><div style="font:600 22px Lexend;color:#8C6A2A;letter-spacing:.12em">RE: WHAT\'S THE NEXT STEP?</div><div style="font:400 28px/1.4 Lexend;margin-top:10px">Thanks so much for reaching out! The next step is…</div><div style="font:500 22px Lexend;color:#8a8079;margin-top:12px">{d}</div></div>' for x,y,o,d in ((-30,0,.5,"March"),(-15,120,.7,"June"),(0,240,1,"Today. From scratch. Again."))) + """
 <div style="position:absolute;left:0;bottom:0;background:#54295A;color:#fff;border-radius:18px;padding:22px 30px;font:500 30px Lexend">✦ Draft saved, in your voice · You send it.</div>
</div>""", "Copy the prompt →", hs=100)

# 14 Drafts
S[14] = page("plum", "Myth", "The first draft <em>isn't supposed to be good.</em>", """
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:34px">
 """ + "".join(f'<div><div style="display:flex;justify-content:space-between;font:500 30px Lexend;color:#FBF8F2;margin-bottom:12px"><span>{l}</span><span>{p}%</span></div><div style="height:46px;border-radius:23px;background:rgba(255,255,255,.15)"><div style="height:100%;width:{p}%;border-radius:23px;background:{c}"></div></div><div style="font:400 26px Lexend;color:#EFDEE2;margin-top:10px">{n}</div></div>' for l,p,c,n in (("Draft 1",70,"#D9BE74","Most people quit here."),("Draft 2",88,"#EFDEE2","“Here's what's off. Fix it.”"),("Draft 3",97,"#FBF8F2","Ready to send."))) + """
</div>""", "Keep going →", hs=100)

# 15 One idea -> week
S[15] = page("paper", "Content", "Fewer ideas. <em>Used harder.</em>", """
<div style="position:absolute;inset:0">
 <div class="card" style="position:absolute;left:50%;top:0;transform:translateX(-50%);padding:24px 44px;background:#54295A;color:#fff;font:600 34px Lexend">1 idea</div>
 <svg style="position:absolute;inset:0" width="888" height="660" viewBox="0 0 888 660"><g stroke="#B68A3E" stroke-width="4" fill="none">
  <path d="M444 80 C444 140 150 140 150 200"/><path d="M444 80 L444 200"/><path d="M444 80 C444 140 738 140 738 200"/>
  <path d="M150 270 L70 380"/><path d="M150 270 L150 380"/><path d="M150 270 L230 380"/>
  <path d="M444 270 L364 380"/><path d="M444 270 L444 380"/><path d="M444 270 L524 380"/>
  <path d="M738 270 L658 380"/><path d="M738 270 L738 380"/><path d="M738 270 L818 380"/></g></svg>
 """ + "".join(f'<div class="card" style="position:absolute;left:{x-110}px;top:200px;width:220px;padding:18px;text-align:center;font:500 28px Lexend;color:#A0466F">Angle {i+1}</div>' for i,x in enumerate((150,444,738))) + \
 "".join(f'<div style="position:absolute;left:{x-34}px;top:380px;width:68px;height:68px;border-radius:50%;background:#EFDEE2;display:flex;align-items:center;justify-content:center;font:600 22px Lexend;color:#54295A">H{k+1}</div>' for k,x in enumerate((70,150,230,364,444,524,658,738,818))) + """
 <div class="serif" style="position:absolute;left:0;right:0;top:500px;text-align:center;font-size:58px;font-style:italic;color:#A0466F">= a week of posts</div>
</div>""", "Save the method →", hs=110)

# 16 Tools vs habit
apps = "".join(f'<div style="aspect-ratio:1;border-radius:18px;background:#3A3530;opacity:.5"></div>' for _ in range(19))
S[16] = page("ink", "Reality check", "Every new AI tool is <em>why none of them stick.</em>", f"""
<div style="position:absolute;left:0;top:0;width:52%;display:grid;grid-template-columns:repeat(5,1fr);gap:12px">{apps}
 <div style="aspect-ratio:1;border-radius:18px;background:#D9BE74;display:flex;align-items:center;justify-content:center;font:600 40px Lexend;color:#1A1816">1</div></div>
<div style="position:absolute;right:0;top:0;width:42%" class="card">
 <div style="padding:26px"><div style="font:600 22px Lexend;letter-spacing:.15em;color:#D9BE74">1 HABIT · 14 DAYS</div>
 <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:8px;margin-top:18px">
 {''.join('<div style="aspect-ratio:1;border-radius:8px;background:#A0466F;color:#fff;display:flex;align-items:center;justify-content:center;font:600 20px Lexend">✓</div>' for _ in range(14))}</div>
 <div style="font:400 24px/1.4 Lexend;margin-top:18px;color:#F8F4ED">Same time. 1 small task. Every day.</div></div></div>
""", "Pick 1 habit →", hs=92)

# 17 Joan quote
S[17] = page("plum", "In her words", "“I put this off for a year because it <em>sounded technical.”</em>", """
<div style="position:absolute;left:0;right:0;bottom:30px">
 <div style="height:3px;background:#D9BE74;width:120px;margin-bottom:28px"></div>
 <div style="font:600 30px Lexend;letter-spacing:.15em;color:#EFDEE2">JOAN · CLINICAL RESEARCHER</div>
 <div class="serif" style="font-style:italic;font-size:48px;color:#FBF8F2;margin-top:18px">By the end of the weekend she was running it on her own.</div>
</div>""", "Simple. Done. →", hs=100)

# 18 Never alone
never = ["Final legal wording","Tax decisions","Medical advice","Firing someone","Anything you won't proofread","Replacing your judgment","Sending without reading"]
S[18] = page("deep", "15 years in compliance taught me", "7 things I'd never let Claude <em>do alone.</em>", f"""
<div class="card" style="position:absolute;inset:0 0 10px 0;padding:30px 44px">
 {''.join(f'<div style="display:flex;gap:22px;align-items:center;font:400 33px Lexend;padding:11px 0;border-bottom:2px solid #EFE9DE"><span class="serif" style="font-size:40px;color:#A0466F;width:34px">{i+1}</span>{t}<span style="margin-left:auto;font-size:30px">🔒</span></div>' for i,t in enumerate(never))}
 <div class="serif" style="font-style:italic;font-size:40px;color:#54295A;margin-top:18px">The tool drafts. The owner decides.</div></div>
""", "Save this →", hs=88)

# 19 Prompt library
files = "".join(f'<div style="background:#EFE9DE;border-radius:10px;padding:10px 14px;font:400 20px Lexend;color:#8a8079;opacity:.75">prompt_{i:02d}.txt</div>' for i in range(1, 15))
S[19] = page("berry", "Subtract", "Your saved prompt library is <em>slowing you down.</em>", f"""
<div class="card" style="position:absolute;left:0;top:0;width:58%;bottom:20px;padding:28px">
 <div style="font:600 26px Lexend;color:#54295A">📁 Saved prompts <span style="color:#A0466F">(40)</span></div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:20px">{files}</div>
 <div style="font:500 22px Lexend;color:#8a8079;margin-top:12px">…and 26 more you've never opened</div></div>
<div style="position:absolute;right:0;top:30px;width:36%">
 <div style="font:600 26px Lexend;color:#FBF8F2;letter-spacing:.12em;margin-bottom:14px">KEEP 3</div>
 {''.join(f'<div class="card" style="padding:20px 24px;margin-bottom:14px;font:500 28px Lexend;color:#54295A">★ {t}</div>' for t in ("Reply in my voice","Poke holes","Plan my week"))}
 <div style="font:600 30px Lexend;color:#FBF8F2;margin-top:16px">🗑 Delete 37</div></div>
""", "Which 1 stays? ↓", hs=90)

# 20 Pushback
S[20] = page("paper", "Better decisions", "Stop asking Claude if <em>your plan is good.</em>", """
<div style="position:absolute;inset:0;padding:0 10px">
 """ + bubble("Is my plan good?") + bubble('<span class="strike" style="color:#8a8079">Great plan! Love it!</span>', False) + """
 <div class="card" style="margin-top:30px;padding:30px 36px;background:#FFF6C9;color:#1A1816;transform:rotate(-1.5deg);border-radius:6px">
  <div style="font:600 22px Lexend;letter-spacing:.15em;color:#8C6A2A">ASK THIS INSTEAD</div>
  <div class="serif" style="font-size:44px;line-height:1.2;margin-top:10px">“Poke holes in this plan. What would a skeptical customer say?”</div></div>
</div>""", "Get pushback →", hs=96)

# 21 Not tech people
roles = ["Business coach","Online seller","Clinical researcher","Boutique studio owner","Independent consultant"]
S[21] = page("rose", "Myth", "The people getting the most from Claude <em>aren't tech people.</em>", f"""
<div style="position:absolute;inset:0;display:flex;flex-wrap:wrap;gap:18px;align-content:flex-start">
 {''.join(f'<div class="card" style="padding:0;overflow:hidden;transform:rotate({r}deg)"><div style="background:#A0466F;color:#fff;font:600 20px Lexend;letter-spacing:.2em;padding:10px 24px">HELLO, I\'M A</div><div class="serif" style="font-size:42px;padding:18px 24px;color:#38203E">{t}</div></div>' for t,r in zip(roles,(-2,1.5,-1,2,-1.5)))}
 <div style="width:100%;font:600 40px Lexend;color:#54295A;margin-top:18px">Lines of code written: <span style="color:#A0466F">0</span></div>
</div>""", "You know enough →", hs=86)

# 22 Before/after newsletter
S[22] = page("ink", "Before / after", "“Write me a newsletter” is why <em>yours sounds like everyone's.</em>", """
<div style="position:absolute;inset:0;display:flex;flex-direction:column;gap:22px">
 <div class="card" style="padding:24px 30px;opacity:.7"><div class="mono" style="font-size:20px;color:#a79d93">BEFORE</div><div class="mono" style="font-size:30px;margin-top:8px">Write me a newsletter.</div></div>
 <div class="card" style="padding:24px 30px;border:3px solid #D9BE74"><div class="mono" style="font-size:20px;color:#D9BE74">AFTER</div>
  <div class="mono" style="font-size:24px;line-height:1.5;margin-top:8px">Write this month's newsletter for <b style="color:#D9BE74">[audience]</b>.<br>Goal: replies about <b style="color:#D9BE74">[offer]</b>.<br>Tone: warm, direct, no hype.<br>Last month's issue: <b style="color:#D9BE74">[paste]</b>.<br>Ask me 3 questions first.</div></div>
</div>""", "Steal the after →", hs=80)

# 23 Strategy vs experiment
S[23] = page("deep", "Permission", "Stop planning your <em>AI strategy.</em>", """
<div style="position:absolute;left:0;top:20px;width:52%;height:470px">
 """ + "".join(f'<div class="card" style="position:absolute;inset:0;transform:translate({k*14}px,{k*14}px) rotate({k-2}deg);padding:34px"><div class="serif" style="font-size:40px;color:#8a8079">AI Strategy v{k+1}</div><div style="font:400 22px Lexend;color:#b5aaa0;margin-top:10px">42 pages · not started</div></div>' for k in range(4)) + """
 <div style="position:absolute;inset:-10px;display:flex;align-items:center;justify-content:center"><div style="font:600 110px Lexend;color:#A0466F;transform:rotate(-12deg)">✕</div></div></div>
<div class="card" style="position:absolute;right:20px;top:90px;width:38%;padding:34px;background:#FFF6C9;border-radius:6px;transform:rotate(3deg)">
 <div style="font:600 22px Lexend;letter-spacing:.15em;color:#8C6A2A">THIS WEEK</div>
 <div class="serif" style="font-size:46px;line-height:1.15;color:#1A1816;margin-top:12px">1 task.<br>1 try.<br>Notice.</div></div>
""", "Run 1 experiment →", hs=110)

# 24 Meeting notes -> decisions
messy = "".join(f'<div style="font:400 {s}px Lexend;color:#8a8079;transform:rotate({r}deg);margin:6px 0">{t}</div>' for t,s,r in (
  ("…so maybe Q2? or not", 24, -2), ("Jen to check w/ vendor??", 22, 1), ("pricing?? revisit", 26, -1), ("call back Thurs", 22, 2), ("who owns the launch email", 24, -1.5), ("tabled: rebrand", 22, 1)))
S[24] = page("plum", "Under a minute", "Nobody needs your notes. <em>They need what was decided.</em>", f"""
<div class="card" style="position:absolute;left:0;top:0;width:40%;bottom:20px;padding:26px;background:#FBF8F2">{messy}</div>
<div style="position:absolute;left:41%;top:40%;font:600 60px Lexend;color:#D9BE74">→</div>
<div style="position:absolute;right:0;top:0;width:48%;display:flex;flex-direction:column;gap:16px">
 {''.join(f'<div class="card" style="padding:22px 26px"><div style="font:600 22px Lexend;letter-spacing:.15em;color:#A0466F">{h}</div><div style="font:400 26px Lexend;margin-top:8px">{b}</div></div>' for h,b in (("DECIDED","Launch email goes out Q2"),("OWNERS","Jen: vendor check · Thu"),("OPEN","Pricing, rebrand")))}</div>
""", "Copy the 3 lists →", hs=90)

# 25 Tabs
tabs = "".join(f'<div style="flex:1;min-width:0;background:{"#FBF8F2" if i==0 else "#D8CFC2"};border-radius:12px 12px 0 0;padding:12px 8px;font:500 16px Lexend;color:#5A5048;white-space:nowrap;overflow:hidden">{t}</div>'
               for i,t in enumerate(["Claude","ChatGPT","Gemini","Perplexity","Notion AI","Jasper","Copy.ai","Canva AI","Gamma","+10"]))
S[25] = page("rose", "Be honest", "Every AI tab you have open is a decision <em>you haven't made.</em>", f"""
<div class="card" style="position:absolute;inset:0 0 10px 0;overflow:hidden">
 <div style="background:#C9BFB2;display:flex;gap:4px;padding:12px 12px 0">{tabs}</div>
 <div style="padding:40px;text-align:center">
  <div class="serif" style="font-size:200px;line-height:1;color:#A0466F">19</div>
  <div style="font:500 30px Lexend;color:#5A5048">tabs open. How many are yours?</div>
  <div style="margin-top:30px;display:inline-block;background:#54295A;color:#fff;font:600 32px Lexend;padding:18px 36px;border-radius:999px">Close all · keep 1</div></div></div>
""", "Comment your number ↓", hs=86)

# 26 Case study timeline
S[26] = page("paper", "Case study", "Her leads lived in her inbox <em>and her memory.</em>", """
<div style="position:absolute;inset:0">
 <div style="position:absolute;left:30px;right:30px;top:60px;height:6px;background:#D9BE74;border-radius:3px"></div>
 """ + "".join(f'<div style="position:absolute;left:{x}%;top:0;width:24%;transform:translateX(-50%);text-align:center"><div style="width:44px;height:44px;border-radius:50%;background:{c};margin:40px auto 0;border:6px solid #F8F4ED"></div><div style="font:600 22px Lexend;letter-spacing:.12em;color:#A0466F;margin-top:12px">WEEK {w}</div><div style="font:400 26px/1.3 Lexend;margin-top:6px;color:#3A3530">{t}</div></div>' for x,w,c,t in ((10,1,"#B68A3E","Client journey mapped"),(37,2,"#B68A3E","Leak points named"),(63,3,"#A0466F","Follow-up built"),(90,4,"#54295A","Runs on its own"))) + """
 <div class="card" style="position:absolute;left:0;right:0;bottom:10px;padding:34px 40px;display:flex;align-items:center;gap:30px;background:#54295A;color:#fff">
  <div class="serif" style="font-size:130px;line-height:1">~6h</div>
  <div style="font:500 34px/1.3 Lexend">back every week.<br><span style="color:#EFDEE2;font-weight:400">She had me build it. You can learn to.</span></div></div>
</div>""", "Learn to build it →", hs=96)

# 27 Not a skills problem
S[27] = page("berry", "Reframe", "<span class='strike'>Skills problem</span><br><em>You care. That's all it is.</em>", """
<div style="position:absolute;inset:0;display:flex;gap:20px;align-items:flex-end">
 """ + "".join(f'<div class="card" style="flex:1;padding:30px;text-align:center;transform:translateY({-k*40}px)"><div class="serif" style="font-size:96px;color:#A0466F;line-height:1">1</div><div style="font:600 30px Lexend;color:#38203E;margin-top:8px">{t}</div></div>' for k,t in enumerate(("task","prompt","week"))) + """
</div>""", "Make the plan →", hs=100)

# 28 One page setup
S[28] = page("deep", "Subtract", "Your whole Claude setup <em>fits on 1 page.</em>", """
<div class="card" style="position:absolute;left:120px;right:120px;top:0;bottom:10px;padding:40px 46px;border-radius:8px">
 <div style="display:flex;justify-content:space-between;font:600 22px Lexend;letter-spacing:.15em;color:#8C6A2A"><span>MY CLAUDE PLAYBOOK</span><span>PAGE 1 OF 1</span></div>
 """ + "".join(f'<div style="margin-top:26px"><div style="font:600 28px Lexend;color:#54295A"><span class="serif" style="color:#A0466F;font-size:36px">{i+1}</span>&nbsp; {t}</div><div style="height:10px;background:#EFE9DE;border-radius:5px;margin-top:12px;width:88%"></div><div style="height:10px;background:#EFE9DE;border-radius:5px;margin-top:8px;width:64%"></div></div>' for i,t in enumerate(("My business note","My 3 most-used prompts","2 examples of my voice","My “never do” list"))) + """
</div>""", "Build yours →", hs=100)

# 29 Cheating
helpers = [("🧮","Calculator"),("👩‍💼","Accountant"),("📄","Template"),("✦","Claude")]
S[29] = page("ink", "Agree?", "Using Claude isn't cheating. <em>Doing it all yourself isn't a virtue.</em>", f"""
<div style="position:absolute;inset:0;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-content:center">
 {''.join(f'<div class="card" style="padding:30px 10px;text-align:center;{"border:3px solid #D9BE74" if t=="Claude" else ""}"><div style="font-size:70px;color:#D9BE74">{e}</div><div style="font:500 26px Lexend;margin-top:12px">{t}</div><div style="font:600 22px Lexend;margin-top:14px;color:{"#D9BE74" if t=="Claude" else "#a79d93"}">{"Cheating?" if t=="Claude" else "Help"}</div></div>' for e,t in helpers)}
 <div class="serif" style="grid-column:1/-1;font-style:italic;font-size:46px;color:#F8F4ED;text-align:center;margin-top:30px">The taste and the relationships are still yours.</div>
</div>""", "Where's your line? ↓", hs=86)

# 30 Do 1 thing
S[30] = page("paper", "If you only do one thing", "Ignore everything else I posted. <em>Do this 1 thing.</em>", """
<div style="position:absolute;inset:0;display:flex;gap:40px;align-items:center">
 <div class="serif" style="font-size:420px;line-height:.8;color:#A0466F">1</div>
 <div class="card" style="flex:1;padding:34px 40px">""" + "".join(check(t, False, "#54295A") for t in ("Pick 1 weekly task","Write what “great” looks like","Try it with Claude today")) + """
  <div style="font:500 28px Lexend;color:#A0466F;margin-top:14px">Then tell me: win or flop?</div></div>
</div>""", "Report back ↓", hs=92)

if __name__ == "__main__":
    html = OUT / "html"; html.mkdir(exist_ok=True)
    assert sorted(S) == list(range(1, 31))
    for n, doc in S.items():
        (html / f"post-{n:02d}.html").write_text(doc)
    print("wrote", len(S))
