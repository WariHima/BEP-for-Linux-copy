import jaconv

with open("./bep-eng.dic",mode="r",encoding="shift-jis") as f:
    data = f.read()
data = data.split("\n")

out = []
for i in data:
    contents = i.split(" ")
    if len(contents) == 3:
        eng = contents[0]
        ja = contents[1]

        ja = jaconv.hankaku2zenkaku(ja)
        out.append(f'("{eng}","{ja}"),')

out = "\n".join(out)

out_text = f"#c2025 WariHima GPL2 or latter\n\
#original data https://github.com/WariHima/BEP-for-Linux-copy bep-eng.dic\n\
ENG2JA_DIC = (\n\
{out}\n \
) "

with open ("engdict.py",encoding="utf-8", mode="w") as f:
    f.write(out_text)