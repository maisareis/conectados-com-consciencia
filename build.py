"""Gera index.html e posts/ a partir de fonte/. Uso: python3 build.py"""
import re, json, html, pathlib
R = pathlib.Path(__file__).parent
SITE = "Conectados com Consciência"
D = json.loads((R/"fonte/edicoes.json").read_text(encoding="utf8")); E, X = D["edicoes"], D["extras"]
COR = ["#1e88e5", "#f5a300", "#f4511e", "#8e24aa", "#2e9e5b"]
SEC = {"dica": ("💡", "Dica rápida"), "sabia": ("🤯", "Você sabia?"), "desafio": ("🧠", "Desafio rápido"), "link": ("🔗", "Link útil"), "frase": ("💬", "Frase do mês"), "verif": ("⚠️", "Verificação rápida")}
txt = lambda s: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()
def key(t):
    t = re.sub(r"^[^\wÀ-ÿ]+", "", txt(t).lower())
    for k, w in (("dica", "dica"), ("sabia", "você sabia"), ("desafio", "desafio"), ("link", "link útil"), ("frase", "frase do m"), ("verif", "verificação rápida")):
        if t.startswith(w): return k
def parse(stem):
    b = (R/f"fonte/{stem}.html").read_text(encoding="utf8")
    b = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n@@\1@@\n", b, flags=re.S)
    b = re.sub(r"<p>(.*?)</p>", lambda m: f"\n@@{txt(m.group(1))}@@\n" if len(txt(m.group(1))) < 32 and key(m.group(1)) else m.group(0), b, flags=re.S)
    sub = ""
    for p in re.findall(r"<p>.*?</p>", b, flags=re.S):
        t = txt(p)
        if re.match(r"^(📅\s*)?Edição\s*#\d+", t):
            m = re.search(r"Tema:\s*(.+)", t)
            if m and not sub: sub = m.group(1)
            b = b.replace(p, "", 1)
        elif (t.isupper() and len(t) < 70) or (t.startswith("Conectados com Consciência") and len(t) < 40):
            b = b.replace(p, "", 1)
        elif t.lower().startswith("tema do mês:"):
            title = t.split(":", 1)[1].strip()
            if not sub: sub = title; b = b.replace(p, "", 1)
            else: b = b.replace(p, f"\n@@{title}@@\n", 1)
    parts = re.split(r"\n@@(.*?)@@\n", b); flow = parts[0]; blocks = []; cur = None
    for t, c in zip(parts[1::2], parts[2::2]):
        k = key(t)
        if k: cur = [k, c]; blocks.append(cur)
        elif cur: cur[1] += f"<h3>{txt(t)}</h3>{c}"
        else: flow += f"<h2>{txt(t)}</h2>{c}"
    end = ""
    if blocks:
        m = re.search(r"<p>(?:(?!</p>).)*?Te vemos na próxima.*", blocks[-1][1], flags=re.S)
        if m: end = m.group(0); blocks[-1][1] = blocks[-1][1][:m.start()]
    return sub, flow, blocks, end
def block(k, c):
    if k == "desafio":
        ps = re.findall(r"<p>.*?</p>", c, flags=re.S)
        for i, p in enumerate(ps):
            if re.match(r"^\(?(Resposta|Spoiler|Gabarito|✅)", txt(p), re.I):
                j = c.index(p); c = c[:j] + "<details><summary>Ver resposta</summary>" + c[j:] + "</details>"; break
    ic, lb = SEC[k]
    return f'<section class="blk k-{k}"><h2>{ic} {lb}</h2>{c}</section>'
HEAD = lambda t, d, p: f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(t)}</title><meta name="description" content="{html.escape(d)}"><link rel="stylesheet" href="{p}assets/style.css"></head><body><a class="skip" href="#c">Ir para o conteúdo</a>'
TOP = lambda p: f'<header class="top"><div class="w"><a href="{p}index.html"><b>🛡️ {SITE}</b></a><nav aria-label="Principal"><a href="{p}index.html#edicoes">Edições</a><a href="{p}index.html#especiais">Especiais</a><a href="{p}index.html#caso">Caso Cisco</a><a href="{p}index.html#material">Material</a><a href="{p}index.html#sobre">Sobre</a></nav></div></header>'
FOOT = '<footer><div class="w">Por Maisa Reis Araujo · <a href="https://github.com/maisareis">GitHub</a> · Licença <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pt-br">CC BY-NC-SA 4.0</a><br>Conteúdo educativo, simplificado de propósito. Confira as fontes indicadas em cada edição.</div></footer></body></html>'
info = {}
for i, e in enumerate(E):
    sub, flow, blocks, end = parse(e["slug"]); info[e["slug"]] = sub; s = e["slug"]
    dl = f'<div class="dl"><a href="../edicoes/pdf-colorido/{s}.pdf">⬇ PDF colorido</a><a href="../edicoes/pdf/{s}.pdf">⬇ PDF simples</a></div>' if e["pdf"] else ""
    pv = f'<a href="{E[i-1]["slug"]}.html">← Edição {E[i-1]["n"]}<br><small>{E[i-1]["titulo"]}</small></a>' if i else "<span></span>"
    nx = f'<a href="{E[i+1]["slug"]}.html">Edição {E[i+1]["n"]} →<br><small>{E[i+1]["titulo"]}</small></a>' if i < len(E)-1 else "<span></span>"
    (R/"posts"/f"{s}.html").write_text(HEAD(f'Edição {e["n"]}: {e["titulo"]} · {SITE}', sub or e["titulo"], "../") + TOP("../") +
      f'<div class="hero sm"><div class="w n"><span class="pill">EDIÇÃO {e["n"]} · {e["mes"].upper()}</span><h1>{e["titulo"]}</h1><p>{sub}</p>{dl}</div></div><main id="c" class="w n"><article>{flow}{"".join(block(k, c) for k, c in blocks)}<div class="end">{end}</div><nav class="pn" aria-label="Edições">{pv}{nx}</nav></article></main>' + FOOT, encoding="utf-8")
kinds = {"especial-pdf-perigoso": "Edição especial", "especial-ataque-com-pdf-passo-a-passo": "Edição especial", "especial-credenciais-salvas": "Edição especial", "o-que-e-a-cisco-talos": "Caso Cisco 2022"}
for x in X:
    body = (R/f"fonte/{x['slug']}.html").read_text(encoding="utf8")
    (R/"posts"/f"{x['slug']}.html").write_text(HEAD(f'{x["titulo"]} · {SITE}', x["titulo"], "../") + TOP("../") +
      f'<div class="hero sm"><div class="w n"><span class="pill">{kinds[x["slug"]].upper()}</span><h1>{x["titulo"]}</h1></div></div><main id="c" class="w n"><article>{body}<nav class="pn"><a href="../index.html">← Início</a><span></span></nav></article></main>' + FOOT, encoding="utf-8")
cards = "".join(f'<a class="card" style="--c:{COR[i%5]}" href="posts/{e["slug"]}.html"><div class="num">{e["n"]}</div><div><small>{e["mes"].upper()}</small><b>{e["titulo"]}</b><span>{info[e["slug"]]}</span></div></a>' for i, e in enumerate(E))
esp = "".join(f'<a class="card" style="--c:{COR[(i+2)%5]}" href="posts/{x["slug"]}.html"><div class="num">★</div><div><small>ESPECIAL</small><b>{x["titulo"]}</b></div></a>' for i, x in enumerate(X[:3]))
T = lambda c, h, t: f'<a style="--c:{c}" href="{h}">{t}</a>'
tiles = "".join([T("#1e88e5", "infograficos/checklist-seguranca-digital.html", "✅ Checklist de segurança digital"), T("#f5a300", "infograficos/quadrinho-agosto.png", "🎨 Quadrinho: senhas"),
  T("#f4511e", "ameacas/tipos-de-ameacas-ciberneticas.pdf", "🗺️ Mapa dos tipos de ameaças"), T("#8e24aa", "infograficos/informativo-senhas-versao-geral.html", "🔐 Senhas: versão geral"),
  T("#2e9e5b", "infograficos/informativo-senhas-versao-tecnica.html", "🧪 Senhas: versão técnica"), T("#1e88e5", "plano-agosto-senhas/plano-semanal-agosto.pdf", "📅 Plano de um mês de campanha")] +
  [T(COR[i % 5], f"infograficos/infografico-{m}.html", f"📊 Infográfico: {m.replace('-', ' ')}") for i, m in enumerate(["agosto", "agosto-parte2", "setembro", "outubro", "novembro", "dezembro"])])
(R/"index.html").write_text(HEAD(SITE, "Campanha de conscientização em segurança digital: edições mensais com dicas práticas, desafios, infográficos e um caso real.", "") + TOP("") + f'''
<div class="hero"><div class="w"><span class="pill">SEGURANÇA DIGITAL NO DIA A DIA</span><h1>Proteja suas contas sem precisar entender de tecnologia.</h1>
<p>Uma edição por mês, sempre com dica prática, uma curiosidade e um desafio rápido. Leia em poucos minutos e use hoje.</p><a class="btn" href="#edicoes">Começar a ler</a><a class="btn o" href="#material">Ver o material</a></div></div>
<main id="c" class="w"><section><div class="feat"><div><b>📆 Uma por mês</b>Cada edição trata de um assunto: senhas, golpes, privacidade e mais.</div><div><b>⚡ Leitura rápida</b>Texto curto, sem jargão, com exemplos do cotidiano.</div><div><b>🧠 Aprenda testando</b>Todo mês tem um desafio com a resposta explicada.</div></div></section>
<section id="edicoes"><h2 class="t">As 13 edições</h2><p class="sub">Comece pela que mais combina com você. Não precisa seguir a ordem.</p><div class="grid">{cards}</div></section>
<section id="especiais"><h2 class="t">Edições especiais</h2><p class="sub">Temas que merecem um aprofundamento.</p><div class="grid">{esp}</div></section>
<section id="caso"><div class="band"><h2>🚨 Caso real: Cisco, 2022</h2><p>Uma senha vazada e um segundo fator de verificação contornado foram a porta de entrada. Veja como aconteceu e o que você pode aprender com isso.</p>
<a class="btn" href="casos/cisco-2022/caso-cisco-infografico.html">Ver o infográfico</a><a class="btn o" href="casos/cisco-2022/caso-cisco-2022.pdf">Resumo em PDF</a><a class="btn o" href="posts/o-que-e-a-cisco-talos.html">O que é a Cisco Talos?</a></div></section>
<section id="material"><h2 class="t">Material para usar e compartilhar</h2><p class="sub">Infográficos, checklist, quadrinho e mais.</p><div class="tiles">{tiles}</div></section>
<section id="sobre"><h2 class="t">Sobre</h2><p class="n">Sou Maisa Reis Araujo, trabalho com suporte e estou me especializando em defesa cibernética. Criei esta campanha para o ambiente corporativo, mas ela não chegou a ser lançada. Em vez de deixar o material parado, publiquei aqui para qualquer pessoa usar.</p></section></main>''' + FOOT, encoding="utf-8")
print("ok")
