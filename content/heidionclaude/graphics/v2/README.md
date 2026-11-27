# V2 single graphics (not scheduled)

New versions of the 27 single graphics (every post except the #5, #17 and #19 carousels).
The scheduled posts in Blotato still use the original graphics in `../png` and `../jpg`.
Nothing here is live until Heidi says to swap them in.

What changed from v1:
- One oversized element per graphic (giant number, app screen, stamp, sticky note) instead of one shared layout.
- All text inside the graphic is 32px or larger, so it reads at phone feed size. `render_v2.mjs` flags anything smaller.
- The on-image line is a short punchline, not a copy of the caption's first line.

Files: `png/v2-post-NN.png` (NN = post number), `v2-contact-sheet.jpg` (all 27 in post order).
Rebuild: `python3 -I build_v2.py && node render_v2.mjs`
