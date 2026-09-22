"""Repaint the language pie in the 3D calendar with the profile's terracotta ramp.

github-profile-3d-contrib always uses GitHub's linguist colours for the pie (blue TypeScript,
yellow JavaScript...), which clash with the terracotta calendar. Those colours are the only
fill="#rrggbb" attributes in the SVG, listed biggest share first, so map them in order.
"""
import re
import sys

RAMP = ["#9a4526", "#b9552f", "#d97757", "#ebb29a", "#f6dccf"]
OTHER = "#c9c3b8"  # the grey "other" slice stays neutral

path = sys.argv[1]
svg = open(path, encoding="utf-8").read()
order = []
for c in re.findall(r'fill="(#[0-9a-fA-F]{6})"', svg):
    if c.lower() not in order:
        order.append(c.lower())
mapping = {}
ramp = iter(RAMP)
for c in order:
    mapping[c] = OTHER if c == "#444444" else next(ramp, OTHER)
svg = re.sub(r'fill="(#[0-9a-fA-F]{6})"', lambda m: f'fill="{mapping[m.group(1).lower()]}"', svg)
open(path, "w", encoding="utf-8").write(svg)
print(mapping)
