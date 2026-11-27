"""Append scheduled post IDs: python3 -I logpost.py <slot> fb ig x th tt"""
import json, sys
L = json.load(open('scheduled-log.json'))
slot, ids = sys.argv[1], sys.argv[2:]
L[slot] = dict(zip(['facebook','instagram','twitter','threads','tiktok'], ids), linkedin="PENDING: reconnect LinkedIn")
json.dump(L, open('scheduled-log.json','w'), indent=1)
print('logged', sorted(L, key=int))
