h,m,s =input().split(":")
h = int(h)
m = int(m)
s = int(s)
seg_total = h*3600 + m*60 + s
print(f"La se foram {seg_total} segundos que nao voltam mais...")
