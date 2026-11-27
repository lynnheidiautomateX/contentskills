"""V2 single graphics (1080x1350) for the 27 posts without carousels.
One oversized element each, text 32px or larger, punchline differs from the caption's first line.
Run: python3 -I build_v2.py   then: node render_v2.mjs
Does not touch the scheduled graphics in ../png or ../jpg.
"""
import sys, pathlib
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
from build_graphics import FONTS, THEMES  # noqa: E402

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{background:var(--bg);color:var(--ink);font-family:Lexend,sans-serif;position:relative;overflow:hidden}
.tag{position:absolute;top:56px;left:72px;right:72px;display:flex;justify-content:space-between;z-index:5;
  font:500 26px Lexend;letter-spacing:.22em;color:var(--lab);text-transform:uppercase}
.foot{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:center;z-index:5;
  font:500 30px Lexend;color:var(--ink)}
.pill{font:600 34px Lexend;padding:22px 38px;border-radius:999px;background:var(--acc);color:var(--bg)}
.s{font-family:Newsreader,serif;font-weight:500;letter-spacing:-.02em;line-height:.98}
.s em{font-style:italic;font-weight:400;color:var(--acc)}
.abs{position:absolute}
.card{background:#FBF8F2;color:#1A1816;border-radius:28px;box-shadow:0 30px 70px rgba(30,10,30,.25)}
.strike{position:relative;display:inline-block}
.strike:after{content:"";position:absolute;left:-10px;right:-10px;top:52%;height:14px;background:#A0466F;transform:rotate(-3deg)}
.stamp{border:12px solid #A0466F;color:#A0466F;border-radius:20px;font:700 120px Lexend;letter-spacing:.06em;padding:6px 40px;display:inline-block}
.mark{background:linear-gradient(transparent 58%, rgba(160,70,111,.6) 58%, rgba(160,70,111,.6) 92%, transparent 92%);padding:0 6px}
.sticky{background:#FFF6C9;color:#1A1816;box-shadow:0 24px 50px rgba(0,0,0,.2)}
"""

def g(theme, kicker, body, pill):
    t = THEMES[theme]
    v = ";".join(f"--{k}:{x}" for k, x in t.items())
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{FONTS}"><style>{CSS}</style></head>
<body style="{v}"><div class="tag"><span>Heidi on Claude</span><span>{kicker}</span></div>{body}
<div class="foot"><span>heidionclaude.com</span><span class="pill">{pill}</span></div></body></html>"""

def head(text, top=None, bottom=None, size=110, color=None):
    pos = f"top:{top}px" if top is not None else f"bottom:{bottom}px"
    c = f";color:{color}" if color else ""
    return f'<div class="abs s" style="left:72px;right:72px;{pos};font-size:{size}px{c}">{text}</div>'

S = {}

# 1 closed tab
S[1] = g("paper", "Sound familiar?", """
<div class="abs card" style="left:72px;right:72px;top:170px;height:470px;overflow:hidden">
 <div style="background:#EFE9DE;height:150px;display:flex;align-items:flex-end;padding-left:30px">
  <div style="background:#FBF8F2;border-radius:26px 26px 0 0;padding:28px 40px;display:flex;align-items:center;gap:60px">
   <span class="s" style="font-size:64px;color:#38203E">Claude</span>
   <span style="width:96px;height:96px;border-radius:50%;background:#A0466F;color:#fff;font:600 64px Lexend;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 18px rgba(160,70,111,.25)">×</span></div></div>
 <div style="padding:110px 50px 44px;font:400 36px/1.4 Lexend;color:#9a9089">“In today's fast-paced digital landscape, businesses like yours…”</div></div>
<svg class="abs" style="left:436px;top:238px" width="120" height="155" viewBox="0 0 70 90"><path d="M5 5 L5 70 L22 55 L35 85 L47 80 L34 50 L58 50 Z" fill="#fff" stroke="#1A1816" stroke-width="4"/></svg>
""" + head("You closed the tab. <em>The setup was the problem.</em>", bottom=190, size=104), "Fix the setup ↓")

# 2 prompt engineering
S[2] = g("plum", "Myth", """
<div class="abs s" style="left:72px;right:72px;top:190px;font-size:92px;color:#EFDEE2;opacity:.6">Advanced Prompt Engineering Course<br><span style="font-size:52px">12 modules · 40 hours · $497</span></div>
<div class="abs" style="right:90px;top:520px;transform:rotate(-10deg)"><span class="stamp" style="background:#54295A;color:#FBF8F2;border-color:#FBF8F2;font-size:160px">SKIP</span></div>
""" + head("Brief Claude like <em>a sharp new hire.</em>", bottom=190, size=104), "Context wins ↓")

# 3 task that shouldn't exist
S[3] = g("rose", "Your turn", """
<div class="abs" style="left:72px;right:72px;top:170px;display:grid;grid-template-columns:repeat(5,1fr);gap:16px">
 """ + "".join(f'<div style="height:150px;border-radius:18px;background:{"#A0466F" if i==7 else "#FBF8F2"};{"box-shadow:0 0 0 12px rgba(160,70,111,.3);" if i==7 else "opacity:.7;"}display:flex;align-items:center;justify-content:center;font:600 56px Lexend;color:#fff">{"???" if i==7 else ""}</div>' for i in range(15)) + """</div>
<div class="abs" style="right:90px;top:600px;width:330px;height:150px;border-radius:24px;background:#1A1816;color:#fff;font:600 56px Lexend;display:flex;align-items:center;justify-content:center;box-shadow:0 14px 0 #000">delete</div>
""" + head("Not delegate. <em>Delete.</em>", bottom=190, size=130), "Name yours ↓")

# 4 re-explaining
bub = "".join(f'<div style="display:flex;justify-content:flex-end;margin-bottom:22px;opacity:{o}"><div style="background:#54295A;color:#fff;border-radius:40px;padding:30px 40px;font:400 40px Lexend">So, my business is…</div></div>' for o in (.3,.55,.8,1))
S[4] = g("deep", "Write it once", f"""
<div class="abs" style="left:72px;right:72px;top:170px">{bub}</div>
<div class="abs" style="left:72px;top:330px;font:600 40px Lexend;color:#A0466F;transform:rotate(-6deg)">Chat #47 ↺</div>
""" + head("Claude shouldn't hear your intro <em>47 times.</em>", bottom=190, size=100), "1 page fixes it ↓")

# 6 ask too fast
S[6] = g("ink", "1 line fixes it", """
<div class="abs" style="left:72px;right:72px;top:420px;border-radius:44px;background:#2A2622;border:4px solid #B68A3E;padding:44px 50px;display:flex;align-items:center;gap:30px">
 <div class="s" style="flex:1;font-size:66px;color:#F8F4ED">Ask me 5 questions before you answer.</div>
 <div style="flex:none;width:120px;height:120px;border-radius:50%;background:#D9BE74;color:#1A1816;font:600 64px Lexend;display:flex;align-items:center;justify-content:center">↑</div></div>
""" + head("Generic answers? <em>You asked too fast.</em>", bottom=190, size=104, color="#F8F4ED"), "Try it today ↓")

# 7 Shannon
S[7] = g("rose", "Client story", """
<div class="abs s" style="left:60px;top:200px;font-size:520px;line-height:.85;color:#A0466F">75</div>
<div class="abs" style="left:72px;top:670px;font:600 48px Lexend;color:#38203E">pages. Out of date.</div>
""" + head("Updated <em>in one evening.</em>", bottom=330, size=112) + """
<div class="abs" style="left:72px;right:72px;bottom:190px;font:500 34px Lexend;color:#54295A">Shannon, online seller</div>""", "Start from the last one ↓")

# 8 robotic
S[8] = g("plum", "Myth", """
<div class="abs card" style="left:72px;right:72px;top:180px;padding:56px">
 <div class="s" style="font-size:72px;color:#9a9089"><span class="strike">Unlock your potential with innovative solutions.</span></div></div>
""" + head("Not robotic. <em>Under-briefed.</em>", bottom=320, size=120, color="#FBF8F2") + """
<div class="abs" style="left:72px;right:72px;bottom:190px;font:500 36px Lexend;color:#EFDEE2">Feed it 3 of your real posts first.</div>""", "Try it ↓")

# 9 poll
S[9] = g("berry", "Vote", """
<div class="abs" style="left:72px;right:72px;top:160px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
 """ + "".join(f'<div class="card" style="height:340px;padding:30px;display:flex;flex-direction:column;justify-content:space-between"><span class="s" style="font-size:170px;color:#A0466F;line-height:.8">{l}</span><span style="font:500 36px/1.2 Lexend">{t}</span></div>' for l,t in (("A","No idea where to start"),("B","Sounds generic"),("C","Don't trust it"),("D","OK… it's time"))) + """</div>
""" + head("Is time <em>really</em> the problem?", bottom=190, size=84, color="#FBF8F2"), "Comment your letter ↓")

# 10 to-do cut
todo = [("Reply to Sam", 0), ("Redo pricing PDF", 1), ("Post on 4 apps", 1), ("Send proposal", 0), ("Rewrite bio again", 1)]
S[10] = g("paper", "Monday, 10 minutes", f"""
<div class="abs card" style="left:72px;right:72px;top:170px;padding:30px 56px;transform:rotate(-2deg)">
 {''.join(f'<div style="font:400 50px Lexend;padding:16px 0;border-bottom:2px solid #EFE9DE;color:{"#b5aaa0" if c else "#1A1816"}"><span class="{"strike" if c else ""}">{t}</span></div>' for t,c in todo)}</div>
<div class="abs" style="right:60px;top:640px;transform:rotate(8deg);background:#A0466F;color:#fff;font:600 64px Lexend;padding:16px 36px;border-radius:20px">−3</div>
""" + head("Fewer tasks. <em>Not a prettier list.</em>", bottom=190, size=100), "Steal the prompt ↓")

# 11 feed
S[11] = g("ink", "Permission granted", """
<div class="abs" style="left:72px;right:72px;top:200px">
 """ + "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;background:#2A2622;border-radius:26px;padding:30px 36px;margin-bottom:20px;opacity:{o}"><span style="font:500 40px Lexend;color:#F8F4ED">{t}</span><span style="font:600 34px Lexend;color:#1A1816;background:#D9BE74;border-radius:999px;padding:12px 26px">Unfollow</span></div>' for t,o in (("“10 NEW tools 🚨”",1),("“You're behind”",.75),("“I automated it all”",.5))) + """</div>
""" + head("You're not behind. <em>Your feed is loud.</em>", bottom=190, size=104, color="#F8F4ED"), "Mute the noise ↓")

# 12 five hours
S[12] = g("rose", "Be honest", """
<div class="abs s" style="left:50px;top:140px;font-size:520px;line-height:.85;color:#54295A">+5<span style="font-size:200px">h</span></div>
<div class="abs" style="left:72px;right:72px;top:640px;display:flex;flex-wrap:wrap;gap:18px">
 <span class="card" style="padding:20px 32px;font:500 40px Lexend;color:#b5aaa0"><span class="strike">More work</span></span>
 """ + "".join(f'<span class="card" style="padding:20px 32px;font:500 40px Lexend">{x}</span>' for x in ("Rest","Sell","Dinner at home")) + """</div>
""" + head("What would you <em>do</em> with them?", bottom=190, size=96), "Tell me ↓")

# 13 same reply
S[13] = g("deep", "Inbox", """
<div class="abs card" style="left:72px;right:72px;top:190px;padding:50px">
 <div style="font:600 32px Lexend;letter-spacing:.12em;color:#8C6A2A">RE: WHAT'S THE NEXT STEP?</div>
 <div class="s" style="font-size:64px;margin-top:20px;color:#38203E">Thanks so much for reaching out! The next step is…</div></div>
<div class="abs" style="right:80px;top:560px;transform:rotate(-10deg)"><span class="stamp" style="background:#EFE9DE">AGAIN?</span></div>
""" + head("Stop writing it <em>from scratch.</em>", bottom=190, size=110), "Copy the prompt ↓")

# 14 first draft
S[14] = g("plum", "Myth", """
<div class="abs" style="left:50%;top:160px;transform:translateX(-50%);width:560px;height:560px;border-radius:50%;background:conic-gradient(#D9BE74 0 70%, rgba(255,255,255,.14) 70% 100%);display:flex;align-items:center;justify-content:center">
 <div style="width:430px;height:430px;border-radius:50%;background:#54295A;display:flex;flex-direction:column;align-items:center;justify-content:center">
  <div class="s" style="font-size:200px;color:#FBF8F2">70%</div><div style="font:500 36px Lexend;color:#EFDEE2">draft 1</div></div></div>
""" + head("A head start, <em>not a verdict.</em>", bottom=190, size=110, color="#FBF8F2"), "Keep going ↓")

# 15 fewer ideas
S[15] = g("paper", "Content", """
<div class="abs" style="left:72px;right:72px;top:180px;display:flex;align-items:center;justify-content:center;gap:50px">
 <div class="s" style="font-size:440px;color:#54295A;line-height:.85">1</div>
 <div style="font:600 120px Lexend;color:#B68A3E">→</div>
 <div class="s" style="font-size:440px;color:#A0466F;line-height:.85">9</div></div>
<div class="abs" style="left:72px;right:72px;top:620px;display:flex;justify-content:space-between;font:500 36px Lexend;color:#5A5048"><span>idea</span><span>3 angles × 3 hooks</span></div>
""" + head("Fewer ideas. <em>Used harder.</em>", bottom=190, size=110), "Save the method ↓")

# 16 tools vs habit
tiles = "".join(f'<div style="aspect-ratio:1;border-radius:20px;background:{"#D9BE74" if i==13 else "#2A2622"};display:flex;align-items:center;justify-content:center;font:600 64px Lexend;color:#1A1816">{"1" if i==13 else ""}</div>' for i in range(20))
S[16] = g("ink", "Reality check", f"""
<div class="abs" style="left:72px;right:72px;top:170px;display:grid;grid-template-columns:repeat(5,1fr);gap:16px">{tiles}</div>
""" + head("20 tools won't stick. <em>1 habit will.</em>", bottom=190, size=104, color="#F8F4ED"), "Pick 1 ↓")

# 18 never alone
never = ["Legal wording", "Tax decisions", "Medical advice", "Firing someone", "Sending unread"]
S[18] = g("deep", "Know the limits", f"""
<div class="abs" style="right:40px;top:120px;font-size:420px;line-height:1;opacity:.9">🔒</div>
<div class="abs" style="left:72px;top:190px">
 {''.join(f'<div style="font:500 44px Lexend;padding:12px 0;color:#38203E"><span class="s" style="color:#A0466F;font-size:56px">✕</span>&nbsp; {t}</div>' for t in never)}
 <div style="font:500 34px Lexend;color:#5A5048;margin-top:10px">+2 more in the post</div></div>
""" + head("The tool drafts. <em>The owner decides.</em>", bottom=190, size=100), "Save this ↓")

# 20 pushback
S[20] = g("paper", "Better decisions", """
<div class="abs" style="left:72px;right:200px;top:180px;background:#FBF8F2;border-radius:44px;padding:40px 50px;box-shadow:0 20px 50px rgba(0,0,0,.12)">
 <div class="s" style="font-size:72px;color:#9a9089"><span class="strike">Great plan! Love it!</span></div></div>
<div class="abs sticky" style="left:220px;right:72px;top:430px;padding:44px;transform:rotate(-3deg)">
 <div class="s" style="font-size:70px">“Poke holes in this. What would a skeptic say?”</div></div>
""" + head("Ask for <em>pushback,</em> not praise.", bottom=190, size=110), "Get pushback ↓")

# 21 not tech people
S[21] = g("rose", "Myth", """
<div class="abs" style="left:72px;top:150px;font:600 40px Lexend;color:#54295A">Lines of code my clients write:</div>
<div class="abs s" style="left:40px;top:250px;font-size:560px;line-height:.9;color:#A0466F">0</div>
<div class="abs" style="left:520px;right:72px;top:280px;display:flex;flex-direction:column;gap:16px">
 """ + "".join(f'<div class="card" style="padding:18px 28px;font:500 36px Lexend;transform:rotate({r}deg)">{t}</div>' for t,r in (("Business coach",-2),("Online seller",1.5),("Researcher",-1),("Studio owner",2))) + """</div>
""" + head("You know enough. <em>Claude organizes it.</em>", bottom=190, size=100), "You're ready ↓")

# 22 newsletter
S[22] = g("ink", "Before / after", """
<div class="abs" style="left:72px;right:72px;top:170px;border-radius:28px;background:#2A2622;padding:36px 44px;opacity:.75">
 <div style="font:600 32px Lexend;color:#a79d93">BEFORE</div><div class="s" style="font-size:60px;color:#F8F4ED;margin-top:8px"><span class="strike">Write me a newsletter.</span></div></div>
<div class="abs" style="left:72px;right:72px;top:420px;border-radius:28px;background:#FBF8F2;padding:36px 44px;border:6px solid #D9BE74">
 <div style="font:600 32px Lexend;color:#8C6A2A">AFTER</div>
 <div style="font:500 38px/1.45 Lexend;color:#1A1816;margin-top:8px">Audience. Goal. Tone.<br>Last month's issue.<br>Ask me 3 questions first.</div></div>
""" + head("Same tool. <em>More context.</em>", bottom=190, size=110, color="#F8F4ED"), "Steal the after ↓")

# 23 strategy
S[23] = g("deep", "Permission", """
<div class="abs card" style="left:72px;top:190px;width:520px;height:560px;padding:44px;border-radius:10px;transform:rotate(-5deg)">
 <div class="s" style="font-size:60px;color:#9a9089">AI_Strategy_v4.pdf</div><div style="font:500 36px Lexend;color:#b5aaa0;margin-top:14px">42 pages · not started</div>
 <div style="font:600 280px Lexend;color:#A0466F;text-align:center;line-height:1;margin-top:20px">✕</div></div>
<div class="abs sticky" style="right:72px;top:330px;width:380px;padding:44px;transform:rotate(4deg)">
 <div class="s" style="font-size:66px">1 task.<br>1 try.<br>This week.</div></div>
""" + head("Experiment <em>beats strategy.</em>", bottom=190, size=110), "Run 1 ↓")

# 24 meeting notes
S[24] = g("plum", "Under a minute", """
<div class="abs" style="left:72px;right:72px;top:170px;display:flex;flex-direction:column;gap:22px">
 """ + "".join(f'<div class="card" style="padding:34px 44px;display:flex;align-items:center;gap:30px"><span class="s" style="font-size:110px;color:#A0466F;line-height:.8">{i}</span><span style="font:600 52px Lexend;color:#38203E">{t}</span></div>' for i,t in ((1,"Decided"),(2,"Who does what"),(3,"Still open"))) + """</div>
""" + head("Your notes need <em>3 lists.</em>", bottom=190, size=110, color="#FBF8F2"), "Copy the 3 lists ↓")

# 25 tabs
S[25] = g("rose", "Be honest", """
<div class="abs" style="left:0;right:0;top:150px;background:#C9BFB2;padding:20px 20px 0;display:flex;gap:8px">
 """ + "".join(f'<div style="flex:1;height:100px;border-radius:18px 18px 0 0;background:{"#FBF8F2" if i==0 else "#D8CFC2"};padding:30px 18px;font:500 32px Lexend;color:#5A5048;white-space:nowrap;overflow:hidden">{t}</div>' for i,t in enumerate(("Claude","AI #2","AI #3","+16"))) + """</div>
<div class="abs" style="left:0;right:0;top:270px;height:440px;background:#FBF8F2"></div>
<div class="abs s" style="left:0;right:0;top:300px;text-align:center;font-size:360px;color:#A0466F;line-height:1">19</div>
""" + head("tabs open. <em>Keep 1.</em>", bottom=190, size=120), "Your number? ↓")

# 26 case study
S[26] = g("paper", "Case study", """
<div class="abs s" style="left:50px;top:130px;font-size:520px;line-height:.85;color:#54295A">~6h</div>
<div class="abs" style="left:72px;top:620px;font:600 48px Lexend;color:#A0466F">back every week.</div>
""" + head("Her follow-ups <em>run on their own now.</em>", bottom=190, size=100), "Learn to build it ↓")

# 27 overwhelm
S[27] = g("berry", "Reframe", """
<div class="abs" style="left:72px;right:72px;top:180px;display:flex;gap:22px">
 """ + "".join(f'<div class="card" style="flex:1;padding:44px 10px;text-align:center"><div class="s" style="font-size:240px;color:#A0466F;line-height:.85">1</div><div style="font:600 44px Lexend;color:#38203E;margin-top:16px">{t}</div></div>' for t in ("task","prompt","week")) + """</div>
""" + head("Overwhelm isn't a skills problem. <em>It's a plan problem.</em>", bottom=190, size=92, color="#FBF8F2"), "Make the plan ↓")

# 28 one page
S[28] = g("deep", "Subtract", """
<div class="abs card" style="left:180px;right:180px;top:170px;height:600px;padding:50px;border-radius:10px;transform:rotate(2deg)">
 <div style="display:flex;justify-content:space-between;font:600 32px Lexend;color:#8C6A2A"><span>MY CLAUDE SETUP</span><span>1 / 1</span></div>
 """ + "".join(f'<div style="font:600 42px Lexend;color:#54295A;margin-top:34px"><span class="s" style="color:#A0466F;font-size:56px">{i}</span>&nbsp; {t}</div>' for i,t in enumerate(("Business note","3 prompts","Voice samples","Never-do list"),1)) + """</div>
""" + head("Longer than a page? <em>You're adding.</em>", bottom=190, size=100), "Build yours ↓")

# 29 cheating
S[29] = g("ink", "Agree?", """
<div class="abs" style="left:72px;right:72px;top:190px;display:grid;grid-template-columns:repeat(4,1fr);gap:18px">
 """ + "".join(f'<div class="card" style="background:#2A2622;color:#F8F4ED;padding:36px 0;text-align:center;{"border:4px solid #D9BE74" if t=="Claude" else ""}"><div style="font-size:110px">{e}</div><div style="font:600 34px Lexend;margin-top:14px;color:{"#D9BE74" if t=="Claude" else "#a79d93"}">{"Cheating?" if t=="Claude" else "Help"}</div></div>' for e,t in (("🧮","Calc"),("👩‍💼","CPA"),("📄","Template"),("✦","Claude"))) + """</div>
""" + head("Doing it all yourself <em>isn't a virtue.</em>", bottom=190, size=104, color="#F8F4ED"), "Where's your line? ↓")

# 30 one thing
S[30] = g("paper", "If you only do one thing", """
<div class="abs s" style="left:40px;top:190px;font-size:640px;line-height:.85;color:#A0466F">1</div>
<div class="abs" style="left:470px;right:72px;top:250px;display:flex;flex-direction:column;gap:20px">
 """ + "".join(f'<div class="card" style="padding:26px 30px;font:500 38px/1.25 Lexend">{t}</div>' for t in ("Pick a weekly task","Define “great”","Try it today")) + """</div>
""" + head("Then tell me: <em>win or flop?</em>", bottom=190, size=110), "Report back ↓")

# 29 (redesign) S29_EXAM: "cheating" is a school word, so show the exam
PEN = "#B8325F"
rules = ["No calculator", "No accountant", "No templates", "No Claude"]
lines = "".join(f'<div style="position:absolute;left:0;right:0;top:{y}px;height:2px;background:#D6E2EE"></div>' for y in range(150, 690, 62))
S[29] = g("plum", "Agree?", f"""
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&display=swap">
<div class="abs" style="left:96px;right:96px;top:150px;height:700px;transform:rotate(-2.5deg)">
 <div class="abs" style="inset:0;background:#FDFCF7;border-radius:6px;box-shadow:0 40px 90px rgba(0,0,0,.45);overflow:hidden">
  {lines}
  <div style="position:absolute;left:84px;top:0;bottom:0;width:3px;background:rgba(184,50,95,.35)"></div>
  <div style="position:absolute;left:120px;right:50px;top:44px;display:flex;justify-content:space-between;align-items:baseline">
   <span style="font:700 40px Lexend;letter-spacing:.08em;color:#1A1816">FINAL EXAM</span>
   <span style="font:500 32px Lexend;color:#5A5048">Running your business</span></div>
  <div style="position:absolute;left:120px;top:118px;font:600 34px Lexend;color:#1A1816;letter-spacing:.12em">RULES:</div>
  <div style="position:absolute;left:120px;right:60px;top:176px">
   {''.join(f'<div style="height:62px;display:flex;align-items:center;font:500 44px Lexend;color:#1A1816"><span class="strike" style="--c:{PEN}">{r}</span></div>' for r in rules)}
   <div style="height:62px;display:flex;align-items:center;font:500 44px Lexend;color:#1A1816"><span class="strike">Do it all yourself</span></div></div>
  <div style="position:absolute;left:110px;top:500px;font:700 124px Caveat,cursive;color:{PEN};transform:rotate(-6deg);line-height:1">This isn't school.</div>
 </div></div>
<style>.strike:after{{background:{PEN};height:9px;top:55%}}</style>
""" + head("Using Claude <em>isn't cheating.</em>", bottom=190, size=118, color="#FBF8F2"), "Where's your line? ↓")

# 11 (redesign) S11_LOCK: a lock screen buried in AI-hype notifications, Do Not Disturb on
notes = [("#A0466F","Hustle Hub","🚨 This changes EVERYTHING","now"),
         ("#B68A3E","@growthguru","You're falling behind","2m"),
         ("#54295A","AI Daily","10 new AI tools you NEED","5m"),
         ("#8C6A2A","@10xfounder","I automated my whole life","9m")]
cards = "".join(f"""<div style="background:rgba(251,248,242,.92);border-radius:34px;padding:24px 28px;margin-bottom:14px;display:flex;gap:22px;align-items:center;opacity:{1-i*.12};transform:scale({1-i*.015})">
 <div style="flex:none;width:76px;height:76px;border-radius:20px;background:{c}"></div>
 <div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between;font:600 32px Lexend;color:#1A1816"><span>{a}</span><span style="color:#8a8079;font-weight:500">{t}</span></div>
 <div style="font:400 34px Lexend;color:#3A3530;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{m}</div></div></div>""" for i,(c,a,m,t) in enumerate(notes))
S[11] = g("ink", "Permission granted", f"""
<div class="abs" style="left:150px;right:150px;top:130px;height:720px;border-radius:70px;border:14px solid #2A2622;overflow:hidden;background:linear-gradient(160deg,#54295A,#1A1816 75%);box-shadow:0 40px 90px rgba(0,0,0,.6)">
 <div style="text-align:center;margin-top:40px;font:300 120px Lexend;color:#FBF8F2;letter-spacing:-.02em">7:12</div>
 <div style="text-align:center;font:500 32px Lexend;color:#EFDEE2;margin-top:-6px">47 notifications · before coffee</div>
 <div style="padding:28px 22px 0">{cards}</div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(transparent,#1A1816)"></div></div>
<div class="abs" style="left:250px;right:250px;top:770px;border-radius:999px;background:#D9BE74;padding:22px 30px;display:flex;align-items:center;justify-content:space-between;box-shadow:0 24px 50px rgba(0,0,0,.5)">
 <span style="font:600 38px Lexend;color:#1A1816">Unfollow 3 accounts</span>
 <span style="width:64px;height:64px;border-radius:50%;background:#1A1816;color:#D9BE74;font:700 38px Lexend;display:flex;align-items:center;justify-content:center">✓</span></div>
""" + head("You're not behind. <em>Your feed is loud.</em>", bottom=180, size=104, color="#F8F4ED"), "Mute the noise ↓")

if __name__ == "__main__":
    out = HERE / "html"; out.mkdir(exist_ok=True)
    expected = [n for n in range(1, 31) if n not in (5, 17, 19)]
    assert sorted(S) == expected, sorted(set(expected) ^ set(S))
    for n, doc in S.items():
        assert "—" not in doc and "–" not in doc, n
        (out / f"v2-post-{n:02d}.html").write_text(doc)
    print("wrote", len(S))
