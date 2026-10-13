"""Combine the snk animation and a decorative progress bar in one SVG."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1] / "assets"
for variant in ("dark", "light"):
    source = ROOT / f"snake-{variant}.svg"
    svg = source.read_text(encoding="utf-8")
    opening = re.search(r"<svg\b[^>]*>", svg)
    if not opening:
        raise ValueError(f"No SVG root in {source}")

    tag = opening.group()
    box = re.search(r'viewBox=["\']([\d.\s-]+)["\']', tag)
    if not box:
        raise ValueError(f"No viewBox in {source}; inspect snk output")
    x, y, width, height = map(float, box.group(1).split())
    extra = 46
    updated = tag[: box.start(1)] + f"{x:g} {y:g} {width:g} {height + extra:g}" + tag[box.end(1) :]
    height_attribute = re.search(r'\sheight=["\'][\d.]+(?:px)?["\']', updated)
    if height_attribute:
        updated = updated[: height_attribute.start()] + f' height="{height + extra:g}"' + updated[height_attribute.end() :]
    svg = svg[: opening.start()] + updated + svg[opening.end() :]

    dark = variant == "dark"
    bg = "#0d1117" if dark else "#ffffff"
    rail = "#283543" if dark else "#dce5e9"
    green = "#40c56b"
    margin = 7
    rail_width = width - 2 * margin
    fill_width = rail_width * 0.52
    bar = (
        f'<g id="activity-progress">'
        f'<rect x="{x:g}" y="{y + height + 1:g}" width="{width:g}" height="45" rx="7" fill="{bg}"/>'
        f'<rect x="{x + margin:g}" y="{y + height + 15:g}" width="{rail_width:g}" height="14" rx="3" fill="{rail}"/>'
        f'<rect x="{x + margin:g}" y="{y + height + 15:g}" width="{fill_width:g}" height="14" rx="3" fill="{green}">'
        f'<animate attributeName="width" values="0;{fill_width:g};{fill_width:g}" keyTimes="0;.7;1" dur="9s" repeatCount="indefinite"/>'
        f'</rect></g>'
    )
    closing = svg.rfind("</svg>")
    if closing < 0:
        raise ValueError(f"No SVG closing tag in {source}")
    combined = svg[:closing] + bar + svg[closing:]
    (ROOT / f"activity-{variant}.svg").write_text(combined, encoding="utf-8")
    source.unlink()
