import re
import sys

input = sys.stdin.readline

ip = input().strip()

"""
# FIXME
0000:1::2
0000:0000:0000:0000:0000:0001:0000:0002
"""

res = re.sub("::", ":check:", ip).strip(":").split(":")

while len(res) < 8:
    res.insert(res.index("check"), "0000")
if "check" in res:
    res[res.index("check")] = "0000"

for idx in range(len(res)):
    res[idx] = res[idx].zfill(4)


print(":".join(res))