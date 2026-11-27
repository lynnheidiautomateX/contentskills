"""Build 7-slide carousels for posts #5, #17 and #19 (1080x1350), same look as the single graphics.
Run: python3 -I build_carousels.py   then: node render.mjs carousel
"""
import sys, pathlib
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from build_graphics import page, check  # noqa: E402

def big_num(n, color="#A0466F"):
    return f'<div class="serif" style="font-size:300px;line-height:.8;color:{color}">{n}</div>'

def fix_card(label, text, theme_dark=False):
    return (f'<div class="card" style="padding:34px 40px;margin-top:30px">'
            f'<div style="font:600 24px Lexend;letter-spacing:.18em;color:#A0466F">{label}</div>'
            f'<div class="serif" style="font-size:52px;line-height:1.15;color:#38203E;margin-top:12px">{text}</div></div>')

def cta_slide(theme, head, line, pr):
    vis = f"""
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;gap:26px">
 <div class="serif" style="font-style:italic;font-size:52px;line-height:1.2">{line}</div>
 <div class="card" style="padding:34px 40px;background:#FBF8F2">
  <div style="font:600 24px Lexend;letter-spacing:.18em;color:#A0466F">FREE COMMUNITY</div>
  <div style="font:500 40px Lexend;color:#38203E;margin-top:10px">heidionclaude.com/community</div>
  <div style="font:400 28px Lexend;color:#5A5048;margin-top:10px">Post what you're stuck on. I answer there.</div></div>
</div>"""
    return page(theme, "Your move", head, vis, pr, hs=96, top_right="7 / 7")

C = {}

# ---------- #5: 5 signs ----------
signs = [
  ("6 tabs of “AI tools to try”", "Every open tab is a decision you haven't made.", "Close them all. Keep 1 tool for 30 days."),
  ("40 saved prompts, never used", "Saving feels like progress. Using is progress.", "Keep the 3 you'd miss. Delete the rest."),
  ("Every chat starts from zero", "You re-explain your business every time.", "Write 1 page about your business. Start every chat with it."),
  ("You judged Claude on 1 bad answer", "The first draft isn't the result. It's the start.", "Reply: “Here's what's off. Fix it.” Then again."),
  ("You feel behind everyone online", "The feed shows you everyone's best day.", "Mute the accounts that make you feel it."),
]
themes5 = ["plum", "rose", "deep", "plum", "rose"]
C["05"] = [page("paper", "Count yours", "5 signs AI is <em>adding</em> to your week.", f"""
<div class="card" style="position:absolute;inset:0 0 10px 0;padding:40px 50px">
 {''.join(check(s[0], on=False) for s in signs)}
 <div style="margin-top:22px;font:600 30px Lexend;color:#A0466F;text-align:right">Swipe and count →</div></div>""",
  "Swipe →", hs=100, top_right="1 / 7")]
for i, ((sign, why, fix), th) in enumerate(zip(signs, themes5)):
    dark = th == "plum"
    C["05"].append(page(th, f"Sign {i+1} of 5", sign, f"""
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end">
 <div style="display:flex;align-items:flex-end;gap:30px">{big_num(i+1, "#EFDEE2" if dark else "#A0466F")}
  <div style="font:400 36px/1.35 Lexend;padding-bottom:30px">{why}</div></div>
 {fix_card("SUBTRACT", fix)}
</div>""", "Count it ✓" if i < 4 else "Your total? →", hs=88, top_right=f"{i+2} / 7"))
C["05"].append(cta_slide("ink", "3 or more? You don't need more AI. <em>You need less, set up once.</em>",
                         "Comment your number below.", "Join free →"))

# ---------- #17: Joan ----------
C["17"] = [
 page("plum", "In her words", "“I put this off for a year because it <em>sounded technical.</em>”", """
<div style="position:absolute;left:0;right:0;bottom:30px">
 <div style="height:3px;background:#D9BE74;width:120px;margin-bottom:28px"></div>
 <div style="font:600 30px Lexend;letter-spacing:.15em;color:#EFDEE2">JOAN · CLINICAL RESEARCHER</div>
 <div style="font:500 32px Lexend;color:#FBF8F2;margin-top:18px">Here's what changed in one weekend →</div></div>""",
  "Swipe →", hs=100, top_right="1 / 7"),
 page("paper", "Who she is", "A clinical researcher. <em>Not a tech person.</em>", """
<div style="position:absolute;inset:0;display:flex;flex-direction:column;gap:20px;justify-content:center">
 <div class="card" style="padding:30px 36px;font:400 36px Lexend"><span class="strike" style="color:#b5aaa0">Writes code</span></div>
 <div class="card" style="padding:30px 36px;font:500 36px Lexend">Knows her work deeply ✓</div>
 <div class="card" style="padding:30px 36px;font:500 36px Lexend">Had a process in her head ✓</div>
 <div class="card" style="padding:30px 36px;font:500 36px Lexend">Had a pile of documents ✓</div></div>""",
  "Sound like you? →", hs=96, top_right="2 / 7"),
 page("rose", "The first step", "We started with <em>a pile of her documents.</em>", """
<div style="position:absolute;left:60px;right:60px;top:30px;bottom:20px">
 """ + "".join(f'<div class="card" style="position:absolute;left:{x}px;top:{y}px;width:420px;height:300px;transform:rotate({r}deg);padding:30px"><div style="font:600 22px Lexend;letter-spacing:.15em;color:#8C6A2A">{t}</div>' + "".join(f'<div style="height:12px;background:#EFE9DE;border-radius:6px;margin-top:16px;width:{w}%"></div>' for w in (90,70,80,55)) + '</div>' for x,y,r,t in ((0,0,-6,"NOTES"),(300,70,4,"FORMS"),(120,230,-2,"EMAILS"))) + """
</div>""", "Not a blank page →", hs=100, top_right="3 / 7"),
 page("deep", "Then", "We walked her process, <em>step by step.</em>", """
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:18px">
 """ + "".join(f'<div style="display:flex;align-items:center;gap:26px"><div style="flex:none;width:86px;height:86px;border-radius:50%;background:{c};color:#fff;display:flex;align-items:center;justify-content:center;font:600 36px Lexend">{i}</div><div class="card" style="flex:1;padding:24px 30px;font:500 34px Lexend">{t}</div></div>' for i,(t,c) in enumerate((("What comes in","#B68A3E"),("What she does with it","#A0466F"),("What goes out","#54295A")),1)) + """
 <div class="serif" style="font-style:italic;font-size:44px;color:#A0466F;margin-top:16px">Her process, in her words.</div></div>""",
  "Then →", hs=100, top_right="4 / 7"),
 page("plum", "By Sunday", "By the end of the weekend <em>she was running it on her own.</em>", """
<div style="position:absolute;inset:0;display:flex;gap:16px;align-items:flex-end">
 """ + "".join(f'<div class="card" style="flex:1;padding:26px 16px;text-align:center;{"background:#D9BE74" if d=="Sun" else ""}"><div style="font:600 30px Lexend;color:#38203E">{d}</div><div style="font:400 24px Lexend;color:#5A5048;margin-top:10px">{t}</div></div>' for d,t in (("Before","Put off for a year"),("After 1 weekend","Running it herself"))) + """
</div>""", "Her verdict →", hs=96, top_right="5 / 7"),
 page("rose", "Her words", "<span style='font-size:150px'>“Simple, valuable, <em>done.</em>”</span>", """
<div style="position:absolute;left:0;bottom:30px;font:600 30px Lexend;letter-spacing:.15em;color:#A0466F">JOAN · CLINICAL RESEARCHER</div>""",
  "The lesson →", hs=100, top_right="6 / 7"),
]
C["17"].append(cta_slide("ink", "Overwhelm looks like incompetence. <em>Usually it's missing structure.</em>",
                         "If it sounded technical to you too, start here.", "Join free →"))

# ---------- #19: prompt library ----------
files = "".join(f'<div style="background:#EFE9DE;border-radius:10px;padding:10px 14px;font:400 22px Lexend;color:#8a8079">prompt_{i:02d}.txt</div>' for i in range(1, 19))
C["19"] = [
 page("berry", "Subtract", "Your saved prompt library is <em>slowing you down.</em>", f"""
<div class="card" style="position:absolute;inset:0 0 20px 0;padding:30px">
 <div style="font:600 28px Lexend;color:#54295A">📁 Saved prompts <span style="color:#A0466F">(40)</span></div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:20px;opacity:.8">{files}</div>
 <div style="font:600 28px Lexend;color:#A0466F;margin-top:20px">Here's the 4-step cut →</div></div>""",
  "Swipe →", hs=96, top_right="1 / 7"),
 page("ink", "Why it hurts", "Every saved prompt is <em>a decision you make again.</em>", """
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:20px">
 """ + "".join(f'<div class="card" style="padding:26px 32px;font:400 34px Lexend;opacity:{o}">{t}</div>' for t,o in (("Which one was for emails?",1),("Is this the new version?",.8),("Do I need to edit it first?",.6),("Never mind. I'll write it myself.",.4))) + """
</div>""", "The fix →", hs=96, top_right="2 / 7"),
 page("paper", "Step 1", "Open your saved prompts. <em>Count them.</em>", f"""
<div style="position:absolute;inset:0;display:flex;align-items:center;gap:40px">
 {big_num("?")}
 <div class="card" style="flex:1;padding:34px 40px;font:400 34px/1.4 Lexend">Notes app, docs, bookmarks, screenshots.<br><b style="color:#A0466F">All of them count.</b></div></div>""",
  "Step 2 →", hs=100, top_right="3 / 7"),
 page("rose", "Step 2", "Keep the 3 <em>you'd miss tomorrow.</em>", """
<div style="position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;gap:20px">
 """ + "".join(f'<div class="card" style="padding:30px 36px;font:500 40px Lexend;color:#54295A">★ {t}</div>' for t in ("Reply in my voice","Poke holes in my plan","Plan my week")) + """
 <div style="font:400 28px Lexend;color:#5A5048">Yours will be different. The number stays 3.</div></div>""",
  "Step 3 →", hs=100, top_right="4 / 7"),
 page("berry", "Step 3", "Delete the rest. <em>Yes, all of them.</em>", """
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">
 <div class="card" style="padding:50px 60px;text-align:center">
  <div style="font-size:150px;line-height:1">🗑</div>
  <div class="serif" style="font-size:90px;color:#A0466F;margin-top:10px">−37</div>
  <div style="font:400 30px Lexend;color:#5A5048;margin-top:10px">You'll write a better one when you need it.</div></div></div>""",
  "Step 4 →", hs=100, top_right="5 / 7"),
 page("deep", "Step 4", "Put your 3 <em>where you work.</em>", """
<div class="card" style="position:absolute;left:100px;right:100px;top:0;bottom:20px;padding:40px;border-radius:8px">
 <div style="font:600 22px Lexend;letter-spacing:.15em;color:#8C6A2A">MY 3 PROMPTS · 1 PAGE</div>
 """ + "".join(f'<div style="margin-top:30px"><div style="font:600 30px Lexend;color:#54295A"><span class="serif" style="color:#A0466F;font-size:40px">{i}</span>&nbsp; {t}</div><div style="height:10px;background:#EFE9DE;border-radius:5px;margin-top:12px;width:85%"></div><div style="height:10px;background:#EFE9DE;border-radius:5px;margin-top:8px;width:60%"></div></div>' for i,t in enumerate(("Reply in my voice","Poke holes in my plan","Plan my week"),1)) + """
 <div style="font:400 26px Lexend;color:#5A5048;margin-top:30px">In a Claude Project's instructions, or 1 doc you keep open.</div></div>""",
  "Last one →", hs=100, top_right="6 / 7"),
]
C["19"].append(cta_slide("plum", "Fewer prompts. <em>Used every day.</em>",
                         "Which 1 would you keep? Tell me in the comments.", "Join free →"))

if __name__ == "__main__":
    out = HERE / "html"; out.mkdir(exist_ok=True)
    for n, slides in C.items():
        assert len(slides) == 7, n
        for i, doc in enumerate(slides, 1):
            assert "—" not in doc and "–" not in doc
            (out / f"carousel-{n}-{i}.html").write_text(doc)
    print("wrote", sum(len(s) for s in C.values()))
