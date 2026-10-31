"""把 SVG 中的字体栈改为中文字体优先，避免 CairoSVG 导出 PNG 时中文显示为方框。

CairoSVG 不会按字形回退字体：匹配到 Helvetica/Arial 后，中文字符就渲染不出来。
Microsoft YaHei / PingFang SC 同时包含拉丁字符，放在最前面不影响英文显示。
"""
import re
import sys
from pathlib import Path

CJK_FIRST = "'Microsoft YaHei', 'PingFang SC', 'Noto Sans CJK SC', "

path = Path(sys.argv[1])
svg = path.read_text(encoding="utf-8")
fixed = re.sub(r"(font-family\s*[:=]\s*[\"']?)\s*'Helvetica Neue'", r"\1" + CJK_FIRST + "'Helvetica Neue'", svg)
path.write_text(fixed, encoding="utf-8")
print(f"{path}: font-family={svg.count('font-family')} changed={svg != fixed}")
