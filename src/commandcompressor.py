# Command Compression Tool
# ------------------------

# This tool is based on this video: https://www.youtube.com/watch?v=MEawKJm-t28
# It only works with Minecraft 1.8.1 (not 1.8)

import sys

commands = sys.stdin.read().split("\n")
commands = [cmd for cmd in commands if cmd != "" and not cmd.startswith("#")]

out = "summon MinecartCommandBlock ~ ~1 ~ {"

for i in range(len(commands)):
	out += "Riding: {id: MinecartCommandBlock, "

out += "Riding: {id:FallingSand, TileID:157, Time:1}, Command: setblock ~ ~ ~ lava 7}"

for cmd in commands:
	out += ", Command: %s}" % cmd
	
print out
