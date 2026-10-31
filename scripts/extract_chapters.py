"""从工作流输出中提取各章节 Markdown（第三章尾部被截断，单独补写）。"""
import json, re, sys, pathlib

src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
out = pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)

names = ["01-基础与脉络.md", "02-语义通信与协同感知.md", "03-入门路线与开放问题.md"]
dec = json.JSONDecoder()
pos = 0
for i, name in enumerate(names):
    m = re.compile(r'"content": "').search(src, pos)
    start = m.end() - 1
    try:
        s, end = dec.raw_decode(src, start)
        pos = end
        truncated = False
    except json.JSONDecodeError:
        tail = src[start:]
        tail = tail.split("\n… [truncated:")[0]
        s = json.loads(tail + '"')
        truncated = True
    (out / name).write_text(s.rstrip() + "\n", encoding="utf-8")
    print(name, len(s), "TRUNCATED" if truncated else "ok", "| has [...]:", "[...]" in s)
