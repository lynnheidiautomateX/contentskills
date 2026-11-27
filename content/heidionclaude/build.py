"""Rebuild schedule.json and README.md from posts.json. Run: python3 -I build.py"""
import json, re, datetime as dt
P = {p['n']: p for p in json.load(open('posts.json'))}
ORDER = [1,5,2,9,4,17,11,10,19,7,8,3,20,14,22,6,26,16,13,18,21,25,15,29,12,28,23,24,27,30]
SKIP = {dt.date(2026,12,24), dt.date(2026,12,25), dt.date(2026,12,31), dt.date(2027,1,1)}
CTA_DM = "Comment SUBTRACT and I'll send you the free community link."
CTA_LINK = "Free to join: heidionclaude.com/community"
BAD = re.compile(r"—|–|\b(just|really|very|basically|literally|actually|simply|certainly|absolutely|honestly)\b", re.I)

slots, d = [], dt.date(2026,11,30)
while len(slots) < len(ORDER):
    if d.weekday() in (0,2,4) and d not in SKIP: slots.append(d)
    d += dt.timedelta(days=1)

def xthread(hook, body):
    one = f"{hook}\n\n{body}\n\n{CTA_LINK}"
    if len(one) <= 280: return [one]
    parts = [hook]
    for para in body.split("\n\n"):
        if len(parts) > 1 and len(parts[-1] + "\n\n" + para) <= 280: parts[-1] += "\n\n" + para
        else: parts.append(para)
    if len(parts[-1] + "\n\n" + CTA_LINK) <= 280: parts[-1] += "\n\n" + CTA_LINK
    else: parts.append(CTA_LINK)
    assert all(len(x) <= 280 for x in parts)
    return parts

sched = []
for i, n in enumerate(ORDER):
    p = P[n]; core = f"{p['hook']}\n\n{p['body']}"
    assert not BAD.search(core), n
    s = {"slot": i+1, "post": n, "date": slots[i].isoformat(), "utc": slots[i].isoformat()+"T20:00:00Z",
         "facebook": core+"\n\n"+CTA_DM, "linkedin": core+"\n\n"+CTA_DM,
         "threads": core+"\n\n"+CTA_LINK, "twitter": xthread(p['hook'], p['body'])}
    assert len(s['threads']) <= 500
    sched.append(s)
json.dump(sched, open('schedule.json','w'), indent=1, ensure_ascii=False)

L = ["# Heidi on Claude: 30 posts, graded and scheduled\n",
"One offer for the whole run: the free community (heidionclaude.com/community), same as the series already scheduled.\n",
"- Facebook (LynnHeidi page) and LinkedIn: \"Comment SUBTRACT\" CTA. On Facebook a Blotato DM automation sends the link. On LinkedIn you reply by hand.",
"- Threads and X: the link in the post. X posts over 280 characters go out as a short thread.",
"- Instagram and TikTok are left out: both need an image or video, and these are text posts.",
f"- Mon / Wed / Fri, 12:00 Pacific, {slots[0]:%b %d %Y} to {slots[-1]:%b %d %Y}. Skips Dec 24-25 and Dec 31-Jan 1. Your Tue/Sat series stays as is.\n",
"Grades are my scores on the post-grader rubric (hook = 50%). They are predictions, not data. Replace them with saves and comments after week 2.\n",
"| Slot | Date | # | Type | Hook | Hook score | Overall |", "|---|---|---|---|---|---|---|"]
for s in sched:
    p = P[s['post']]; L.append(f"| {s['slot']} | {s['date']} | {p['n']} | {p['type']} | {p['hook']} | {p['hook_score']} | {p['overall']} |")
L.append("\n## Hooks rewritten after grading under 7\n")
for p in sorted(P.values(), key=lambda p: p['n']):
    if 'old_hook' in p: L.append(f"- **#{p['n']}** \"{p['old_hook']}\" → \"{p['hook']}\"")
L += ["\n## Real sources (no invented stories)\n",
"- #7 Shannon and #17 Joan: testimonials published on heidionclaude.com.",
"- #12 and #26: the service-based founder case on heidionclaude.com (4 weeks, roughly 6 hours a week back).",
"- #18: your almost 15 years in compliance. #21: the client roles in your published testimonials.",
"- #22's brackets are for the reader to fill, like your scheduled receipt and jargon posts.\n",
"## Full posts (Facebook version)\n"]
for s in sched:
    p = P[s['post']]; L.append(f"### {s['date']} · #{p['n']} {p['type']}\n\n{s['facebook']}\n")
L += ["## Top 3 predictions\n",
"These are my calls from the grading, not data. Check them against saves and comments after week 2.\n",
"1. **#17, Joan's quote (Dec 11).** It opens on a real client's words, which reads as proof instead of a promise. \"It sounded technical\" is the exact excuse this audience uses, so they see themselves in it. Expect comments that start with \"same\".",
"2. **#5, the 5 signs checklist (Dec 2).** People save and share lists, and shares are what Facebook rewards. Each item is a habit the reader can count against herself, and the last line (\"You need less, set up once\") is your brand in one sentence. It's also the easiest post to turn into a carousel later.",
"3. **#19, delete your prompt library (Dec 18).** It's the most contrarian hook in the batch. Every AI account tells people to save prompts, and this one tells them to delete them. Readers who agree and readers who push back both comment, and the closing question gives them an easy reply.",
"\nThe risk across all three: none of them carries a number from your own results. If you have one, adding it to #19 is the fastest upgrade.\n"]
open('README.md','w').write("\n".join(L))
print(slots[0], slots[-1], len(sched))
