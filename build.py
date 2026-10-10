# Génère les pages du site Seicho-No-Ie France à partir d'un gabarit commun.
import os
from nature import forest, branch, SPRIG

OUT = os.path.dirname(os.path.abspath(__file__))
INT = "https://www.seicho-no-ie.org/eng"
ON = ' class="on"'

NAV = [
    ("a-propos.html", "À propos"),
    ("enseignements.html", "Enseignements"),
    ("activites.html", "Activités"),
    ("zeb.html", "ZEB"),
    ("contact.html", "Contacts"),
    ("livres.html", "Livres"),
    ("actualites.html", "Actualités"),
]

def header(active):
    items = "".join(
        f'<li><a href="{h}"{ON if h == active else ""}>{t}</a></li>' for h, t in NAV
    )
    return f"""<header>
  <div class="wrap top">
    <a class="logo" href="index.html"><img src="img/logo-seicho-no-ie.png" alt="Seicho-No-Ie — International Peace by Faith"><span class="fr">France</span></a>
    <div class="lang">Autres langues :<a href="{INT}/">English</a><a href="https://www.jp.seicho-no-ie.org">日本語</a></div>
    <button class="burger" aria-label="Menu" onclick="document.getElementById('menu').classList.toggle('open')">☰</button>
  </div>
  <nav><ul id="menu">{items}</ul></nav>
</header>"""

BR_L = branch('branch tl', seed=2)
BR_R = branch('branch tr', flip=True, seed=5)
FOREST_S = forest(seed=7, height=110)
FOREST_F = forest(seed=11, height=120, layers=(("#e3eed9",1,50,70),("#cfe3c2",1,65,90)))

FOOTER = f"""<footer>
  <div class="wrap">
    <div class="cols">
      <div><h4>À propos</h4><ul>
        <li><a href="a-propos.html">Présentation</a></li>
        <li><a href="a-propos.html#histoire">Notre histoire</a></li>
        <li><a href="a-propos.html#rejoindre">Nous rejoindre</a></li></ul></div>
      <div><h4>Enseignements & activités</h4><ul>
        <li><a href="enseignements.html">Les trois principes</a></li>
        <li><a href="enseignements.html#sept-proclamations">Les Sept Proclamations</a></li>
        <li><a href="activites.html">Activités</a></li>
        <li><a href="zeb.html">Bâtiments ZEB</a></li></ul></div>
      <div><h4>Ressources</h4><ul>
        <li><a href="livres.html">Livres</a></li>
        <li><a href="actualites.html">Actualités</a></li></ul></div>
      <div><h4>Contact</h4><ul>
        <li><a href="contact.html#france">France</a></li>
        <li><a href="contact.html#europe">Europe</a></li>
        <li><a href="{INT}/">Site international</a></li></ul></div>
    </div>
    <p class="blessing">« Merci à toute chose, au ciel et sur la terre. »</p>
    <div class="copy">© SEICHO-NO-IE — Tous droits réservés</div>
  </div>
</footer>"""

def side(title, links, active=None):
    lis = "".join(
        f'<li><a href="{h}"{ON if h == active else ""}>{t}</a></li>' for h, t in links
    )
    return f'<h4>{title}</h4><ul>{lis}</ul>'

def page(fname, title, banner, crumb, body, sidebar="", desc="", crumb_html=None):
    if crumb_html is None:
        crumb_html = '<a href="index.html">ACCUEIL</a> &nbsp;›&nbsp; <span>' + crumb.upper() + "</span>" if crumb else ""
    if banner:
        top = f'<div class="banner"><h1>{banner}</h1></div><div class="crumb"><div class="wrap">{crumb_html}</div></div>'
        main = f'<main><div class="wrap layout"><div class="content">{body}</div><aside class="side">{sidebar}</aside></div></main>'
    else:
        top = ""
        main = body
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#fdf8ec">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Montserrat:ital,wght@0,600;0,800;1,800&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="proto">Prototype — site non officiel, en cours de préparation</div>
{header(fname)}
{top}
{main}
{FOOTER}
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)

# ---------- Barres latérales ----------
SIDE_ABOUT = lambda a=None: side("À propos", [
    ("a-propos.html", "Présentation"),
    ("a-propos.html#objectifs", "Nos objectifs"),
    ("a-propos.html#histoire", "Notre histoire"),
    ("a-propos.html#rejoindre", "Nous rejoindre")], a) + side("Découvrir", [
    ("enseignements.html", "Enseignements"), ("contact.html", "Contacts")])

SIDE_ACT = side("Activités", [
    ("activites.html", "Vue d'ensemble"),
    ("activites.html#alimentation", "Alimentation bas carbone"),
    ("activites.html#mode-de-vie", "Mode de vie sobre"),
    ("activites.html#creation", "Activités créatives"),
    ("activites.html#energies", "Énergies naturelles"),
    ("activites.html#iso", "ISO 14001")], "activites.html") + side("Voir aussi", [("zeb.html", "Bâtiments ZEB")])

SIDE_BOOKS = side("Livres", [
    ("livres.html#masanobu", "Rév. Masanobu Taniguchi"),
    ("livres.html#seicho", "Rév. Seicho Taniguchi"),
    ("livres.html#divers", "Autres publications")])

SIDE_CONTACT = side("Contacts", [
    ("contact.html#france", "France"),
    ("contact.html#europe", "Europe"),
    ("contact.html#monde", "Dans le monde")])

# ---------- Accueil ----------
from news_fr import ARTICLES
NEWS = [(d, t, slug) for slug, d, t, _, _ in ARTICLES]
def news_list(items):
    li = "".join(
        f'<li><time>{d.replace("-", ".")}</time><span class="tag">Communiqué</span><a href="{u}">{t}</a></li>'
        for d, t, u in items)
    return f'<ul class="news">{li}</ul>'

MOIS = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
def date_fr(d):
    y, m, j = d.split("-")
    return f"{int(j)}{'er' if j == '01' else ''} {MOIS[int(m)-1]} {y}"

SIDE_NEWS = lambda a=None: side("Communiqués", [(s, f"{d[:4]} — {t}") for s, d, t, _, _ in ARTICLES], a) + side("Voir aussi", [("actualites.html", "Toutes les actualités")])

for slug, d, t, orig, body in ARTICLES:
    art = f"""<article>
<p class="meta"><time datetime="{d}">{date_fr(d)}</time><span class="tag">Communiqué</span></p>
<h2 class="art-title">{t}</h2>
{body}
<p class="source">Version originale (anglais) : <a href="{orig}" target="_blank" rel="noopener">seicho-no-ie.org ↗</a></p>
<p><a href="actualites.html">← Retour aux actualités</a></p>
</article>"""
    page(slug, f"{t} — Seicho-No-Ie France", "Actualités", None, art, SIDE_NEWS(slug),
         desc=t, crumb_html=f'<a href="index.html">ACCUEIL</a> &nbsp;›&nbsp; <a href="actualites.html">ACTUALITÉS</a> &nbsp;›&nbsp; <span>{date_fr(d).upper()}</span>')

home = f"""
<section class="hero"><div class="wrap">
  <p class="kicker">Bienvenue chez Seicho-No-Ie France</p>
  <h1>Dieu, la nature et l'être humain ne font qu'un</h1>
  <p>Seicho-No-Ie invite chacun à redécouvrir sa vraie nature d'enfant de Dieu, à vivre dans la gratitude et à bâtir une civilisation en harmonie avec la nature, pour la paix dans le monde.</p>
  <a class="btn gold" href="enseignements.html">Découvrir les enseignements</a>
  <a class="btn soft" href="contact.html#france">Participer en France</a>
</div></section>
<section class="welcome"><div class="wrap">
  <h2>Nous sommes heureux de vous accueillir</h2>{SPRIG}
  <p>Seicho-No-Ie, « la Maison de la croissance », est un mouvement spirituel né au Japon en 1930. Il enseigne que le monde véritable, créé par Dieu, est parfait et rempli de lumière, et que chacun peut le manifester dans sa vie par des pensées, des paroles et des actes lumineux. Nos rencontres sont ouvertes à toutes et à tous, quelle que soit votre religion : nous croyons qu'une même Vérité éclaire toutes les traditions.</p>
  <p>Dans la situation actuelle du monde, la méditation <em>Shinsokan</em> et la récitation des sutras sacrés nous offrent une orientation spirituelle précieuse, pour garder le cœur tourné vers la lumière.</p>
</div></section>
<main><div class="wrap">
  <div class="banner-row">
    <a class="promo a" href="activites.html"><strong>Pour une nouvelle civilisation</strong>Alimentation bas carbone, énergies renouvelables, création en lien avec la nature : nos actions concrètes.</a>
    <a class="promo b" href="communique-2025-07-sans-viande.html"><strong>Pourquoi une alimentation sans viande ?</strong>Notre dernière publication explique les raisons de ce choix pour la planète et pour le cœur.</a>
  </div>
  <div class="event">
    <div class="event-date"><b>16–18</b><span>oct. 2026</span></div>
    <div>
      <p class="kicker" style="margin:0 0 4px">Rencontre européenne</p>
      <h3>2<sup>e</sup> Rencontre Seicho-No-Ie en Europe</h3>
      <p>Du vendredi 16 au dimanche 18 octobre 2026, à l'auberge de jeunesse de Mayence (Jugendherberge Mainz, Otto-Brunfels-Schneise 4, 55130 Mainz, Allemagne). Pour vous inscrire, contactez le bureau Seicho-No-Ie de Francfort, qui vous enverra les informations et le formulaire d'inscription.</p>
      <a class="more" href="contact.html#europe">Coordonnées du bureau de Francfort →</a>
    </div>
  </div>
  <div class="p4u">
    <div><b>P4U</b><span>Peace for Ukraine</span></div>
    <p>Lancé en mars 2022 au siège de Seicho-No-Ie, le « Bureau dans la forêt » à Hokuto (Japon), le mot d'ordre <b>P4U – Peace for Ukraine</b> est porté par les membres du monde entier pour exprimer leur compassion envers les personnes qui souffrent en Ukraine. <a href="communique-2024-05-rapport-environnemental.html#r2">Nos actions pour la paix →</a></p>
  </div>
  <div class="grid g3" style="margin-bottom:48px">
    <div class="card"><div class="num">1930</div><h3>Une revue, puis un mouvement</h3><p>Né au Japon d'une revue mensuelle, Seicho-No-Ie est aujourd'hui présent sur tous les continents.</p><a class="more" href="a-propos.html">À propos →</a></div>
    <div class="card"><div class="num">3</div><h3>Trois principes</h3><p>Le monde parfait de l'Image Vraie, la loi de l'esprit et l'unité de toutes les religions.</p><a class="more" href="enseignements.html">Enseignements →</a></div>
    <div class="card"><div class="num">ZEB</div><h3>Le premier bâtiment à énergie nette zéro du Japon</h3><p>Le « Bureau dans la forêt » produit autant d'énergie qu'il en consomme.</p><a class="more" href="zeb.html">Découvrir →</a></div>
  </div>
  <h2 class="home-news-title">Actualités</h2>
  {news_list(NEWS[:3])}
  <p style="text-align:right;margin-top:14px"><a href="actualites.html">Toutes les actualités →</a></p>
</div></main>
"""
page("index.html", "Seicho-No-Ie France", None, None, home,
     desc="Site francophone de Seicho-No-Ie : enseignements, activités, contacts en France.")

# ---------- À propos ----------
about = """
<h2>Présentation de Seicho-No-Ie</h2>
<table class="facts">
<tr><th>Nom</th><td>Seicho-No-Ie</td></tr>
<tr><th>Fondation</th><td>1<sup>er</sup> mars 1930</td></tr>
<tr><th>Fondateur</th><td>Rév. Masaharu Taniguchi</td></tr>
<tr><th>Ancien président</th><td>Rév. Seicho Taniguchi</td></tr>
<tr><th>Président</th><td>Rév. Masanobu Taniguchi</td></tr>
<tr><th>Objet de vénération</th><td>Seicho-No-Ie désigne un autre nom du Grand Univers. L'objet de vénération est compris comme la manifestation du Dieu unique et absolu ; les divinités des vraies religions sont ce même Dieu sous des noms différents, honorées avec le même respect. Aucune statue n'est érigée : une calligraphie portant le mot <em>Jissō</em> (« Image Vraie ») rappelle la Vérité universelle présente derrière toutes les religions.</td></tr>
<tr><th>Membres</th><td>1 040 503 <small>(Japon : 348 119 / autres pays : 692 384)</small></td></tr>
<tr><th>Ministres et conférenciers</th><td>24 309 <small>(Japon : 18 507 / autres pays : 5 802)</small></td></tr>
<tr><th>Centres</th><td>451 <small>(Japon : 126 / autres pays : 325)</small></td></tr>
</table>
<p style="font-size:.85rem;color:var(--muted)">Chiffres au 31 décembre 2021.</p>

<h2 id="objectifs">Nos objectifs</h2>
<p>Seicho-No-Ie veut éclairer l'humanité par la vérité exposée dans <em>La Vérité de la Vie</em> (<em>Seimei no Jissō</em>), l'œuvre principale en 40 volumes de son fondateur Masaharu Taniguchi, afin que chacun puisse vivre dans la paix, l'harmonie et le bonheur.</p>
<p>Son idée fondamentale est simple : tout être humain est enfant de Dieu, quels que soient sa nation, sa religion ou sa conduite passée.</p>

<h2 id="histoire">Notre histoire</h2>
<p>Après une longue quête de la vérité, Masaharu Taniguchi (1893-1985) prend conscience que l'être humain est, par nature, enfant de Dieu. En 1930, il lance une revue mensuelle, <em>Seicho-No-Ie</em>, pour partager la joie de cette révélation : c'est le début du mouvement.</p>
<p>De nombreux lecteurs découvrent alors leur vraie nature, surmontent les difficultés de leur vie et trouvent le bonheur. Ils en parlent spontanément autour d'eux, et l'enseignement se diffuse de proche en proche.</p>
<p>Le « Mouvement d'éveil de l'humanité » lancé par le fondateur est aujourd'hui poursuivi par le Rév. Masanobu Taniguchi (né en 1951), président actuel. Il le développe au Japon et dans les Amériques, en Asie, en Océanie et en Europe sous le nom de « Mouvement international pour la paix par la foi », afin de bâtir la paix par la foi en un Dieu de bonté.</p>
<p>Aujourd'hui, l'exploitation technologique et une activité économique excessive dépassent ce que la nature peut supporter, rendant la vie heureuse difficile pour la nature comme pour l'humanité. Seicho-No-Ie œuvre donc à poser les bases d'une « nouvelle civilisation », fondée sur l'idée que Dieu, la nature et l'être humain ne font qu'un.</p>

<h2 id="rejoindre">Nous rejoindre</h2>
<p>Toute personne qui suit les enseignements de Seicho-No-Ie et soutient les « Sept Proclamations de Lumière » peut adhérer à la Fraternité de la Sainte Mission (<em>Holy Mission Fellowship</em>).</p>
<p>Cette fraternité est un système de contribution qui soutient le mouvement dans le monde entier : elle renforce les liens entre membres et permet d'entretenir les lieux de diffusion. À ses débuts, le mouvement était financé personnellement par le fondateur ; avec sa croissance, ceux qui avaient été aidés ont voulu exprimer leur gratitude, et la fraternité a été créée en 1954.</p>
<p>Adhérer et verser chaque mois une contribution d'un cœur sincère, c'est soutenir l'œuvre de Dieu dans un esprit de don pur, selon le principe « Donnez, et il vous sera donné ».</p>
<div class="note">Pour adhérer en France, contactez le responsable indiqué sur la page <a href="contact.html#france">Contacts</a>.</div>
<p><a href="enseignements.html#sept-proclamations">Lire les Sept Proclamations de Lumière →</a></p>
"""
page("a-propos.html", "À propos — Seicho-No-Ie France", "À propos", "À propos", about, SIDE_ABOUT("a-propos.html"),
     desc="Présentation, histoire et adhésion à Seicho-No-Ie.")

# ---------- Enseignements ----------
teach = """
<h2>Les enseignements de Seicho-No-Ie</h2>
<p class="lead">L'essentiel de l'enseignement tient en trois principes : « Seul existe le monde parfait créé par Dieu », « Tout phénomène est le reflet de l'esprit » et « Toutes les religions émanent d'un seul Dieu universel ».</p>

<h2 id="image-vraie">Seul existe le monde parfait créé par Dieu (l'Image Vraie)</h2>
<p>L'Image Vraie est le monde créé par le Dieu unique et absolu ; c'est lui qui existe réellement. Il est rempli des vertus divines : les êtres humains y sont enfants de Dieu, et Dieu, la nature et l'humanité y vivent en Grande Harmonie. Autrement dit, seuls existent vraiment Dieu et le monde parfait et harmonieux qu'Il a créé.</p>
<p>Seicho-No-Ie appelle « monde phénoménal » le monde que perçoivent nos sens. La vue, l'ouïe, l'odorat, le goût et le toucher ne transmettent au cerveau qu'une petite partie de l'immense réalité ; le monde phénoménal est l'image provisoire que le cerveau construit à partir de ces informations incomplètes. C'est pourquoi guerres, terrorisme ou maladies semblent exister : ils appartiennent au monde phénoménal, et non à celui de l'Image Vraie.</p>

<h2 id="esprit">Tout phénomène est le reflet de l'esprit</h2>
<p>Ce principe, appelé aussi « loi de l'esprit », enseigne que le monde phénoménal se forme à partir de l'esprit humain. L'esprit, c'est la « parole », qui s'exprime par trois voies : le corps, à travers nos actes ; la bouche, à travers nos mots ; et la pensée, en nous-mêmes.</p>
<p>Cette loi est exacte et impartiale : des paroles négatives créent un monde négatif. Pour faire naître un monde positif, il suffit d'utiliser les paroles du monde de l'Image Vraie, celles qui expriment les vertus divines de sagesse, d'amour et de vie.</p>
<p>L'esprit comporte un niveau conscient et un niveau subconscient, et la « parole » agit sur les deux. Ces trois formes d'expression (les actes, les mots et les pensées) constituent ce que l'on appelle le <em>karma</em>.</p>

<h2 id="religions">Toutes les religions émanent d'un seul Dieu universel</h2>
<p>Ce principe ne signifie pas que toutes les religions doivent se fondre en une seule, Seicho-No-Ie. Il se lit à l'inverse : une même Vérité se déploie pour devenir toutes les religions. Les différences entre elles sont de même nature que celles des vêtements ou des cultures, qui varient selon les pays, les régions et les peuples.</p>
<p>Prenons l'image d'un œuf au plat. Le jaune, au centre, représente la Vérité universelle et fondamentale que partagent toutes les religions. Le blanc qui l'entoure varie selon les cultures, les peuples et les époques. Lorsque les religions reconnaîtront que ce cœur leur est commun et accepteront la diversité qui l'entoure, les conflits religieux prendront fin.</p>

<h2 id="gratitude">La gratitude envers toute chose</h2>
<p>Dieu a créé tous les êtres et toutes les choses (êtres humains, animaux, plantes, minéraux) pour qu'ils s'épanouissent ensemble dans l'harmonie. Au cœur de l'enseignement se trouve la <b>Révélation de la Grande Harmonie</b>, reçue par Masaharu Taniguchi en 1931, qui appelle à la gratitude envers toute chose dans l'univers :</p>
<blockquote>« Sois reconnaissant envers toutes les choses du cosmos. »</blockquote>

<h2 id="pratiques">Trois pratiques quotidiennes</h2>
<div class="grid g3">
  <div class="card"><div class="num">1</div><h3>La méditation Shinsokan</h3><p>La méditation principale de Seicho-No-Ie, qui accorde l'esprit à Dieu et au monde de l'Image Vraie.</p><a class="more" href="livres.html#seicho">Un livre pour débuter →</a></div>
  <div class="card"><div class="num">2</div><h3>Sutras et lectures</h3><p>Réciter les sutras sacrés et lire régulièrement les ouvrages de Seicho-No-Ie pour nourrir sa compréhension de la Vérité.</p><a class="more" href="livres.html">Nos livres →</a></div>
  <div class="card"><div class="num">3</div><h3>L'amour en actes</h3><p>Mettre en pratique, au quotidien, l'amour du prochain et la bienveillance envers tous les êtres.</p></div>
</div>

<h2 id="sept-proclamations">Les Sept Proclamations de Lumière</h2>
<p class="lead">Les Sept Proclamations de Lumière résument l'engagement de Seicho-No-Ie. Toute personne qui les soutient peut <a href="a-propos.html#rejoindre">rejoindre le mouvement</a>.</p>
<ol class="steps">
<li><b>Dépasser les différences.</b> Nous nous engageons à transcender toutes les différences de religion et de courant, à honorer la vie et à vivre selon les lois de la vie.</li>
<li><b>Croissance et immortalité.</b> Nous croyons que les lois par lesquelles la vie s'exprime conduisent à une croissance spirituelle sans fin, et que la vie de chaque individu est immortelle.</li>
<li><b>Étudier et partager.</b> Nous étudions les lois créatrices de la vie et en publions les résultats, afin que l'humanité puisse progresser.</li>
<li><b>L'amour et la parole créatrice.</b> Nous croyons que l'amour est la nourriture de la vie, et que la prière, les paroles d'amour et la louange sont la force créatrice qui fait naître l'amour.</li>
<li><b>Un potentiel infini.</b> Nous croyons qu'en tant qu'enfants de Dieu, nous portons en nous une force et une abondance infinies, et que l'usage de la puissance créatrice de la parole nous permet d'atteindre la liberté absolue.</li>
<li><b>Diffuser la bonne parole.</b> Nous diffusons ces enseignements par l'écriture, l'édition, les cours, les conférences, la radio, la télévision et tout autre moyen, afin d'améliorer la destinée de l'humanité par de bonnes paroles.</li>
<li><b>Agir concrètement.</b> Par une juste vision des choses, une juste manière de vivre et une juste éducation, nous menons des actions concrètes contre la maladie et les épreuves de la vie, pour établir le paradis sur cette terre.</li>
</ol>
<p class="source">Texte original (anglais) : <a href="https://www.seicho-no-ie.org/eng/about/sevenpromulgations/" target="_blank" rel="noopener">The Seven Promulgations of Light ↗</a></p>
<div class="todo">Version française établie à partir d'un résumé du texte original. À valider mot à mot avec le texte anglais (ou une traduction officielle) avant publication.</div>
<div class="note">Pour approfondir la pratique, découvrez le <a href="livres.html#seicho">Shinsokan</a>, la méditation principale de Seicho-No-Ie.</div>
"""
page("enseignements.html", "Enseignements — Seicho-No-Ie France", "Enseignements", "Enseignements", teach,
     side("Enseignements", [("#image-vraie", "L'Image Vraie"), ("#esprit", "La loi de l'esprit"), ("#religions", "L'unité des religions"), ("#gratitude", "La gratitude"), ("#pratiques", "Trois pratiques quotidiennes"), ("#sept-proclamations", "Les Sept Proclamations de Lumière")]) + side("Voir aussi", [("livres.html", "Livres"), ("a-propos.html", "À propos")]),
     desc="Les trois principes des enseignements de Seicho-No-Ie.")

# ---------- Activités ----------
acts = """
<h2>Poser les bases d'une « nouvelle civilisation »</h2>
<p>Depuis sa fondation, Seicho-No-Ie reste fidèle à deux enseignements : la gratitude envers toute chose sur terre et au ciel, et l'unité de toute chose en Dieu. Il s'engage pour l'économie des ressources : en 2001, il est devenu la première organisation religieuse certifiée ISO 14001 pour son système de management environnemental. Panneaux solaires, plantations d'arbres et de forêts, réduction de la consommation de viande : les actions sont nombreuses.</p>
<p>Nous pensons qu'en abandonnant une manière de penser centrée sur l'efficacité et l'intérêt personnel, au profit d'une vie qui respecte chacun et nous relie au monde naturel, l'humanité peut préserver notre belle planète et trouver le vrai bonheur.</p>
<p>Il s'agit de passer de la « civilisation des énergies fossiles », celle des ressources du sous-sol née de la révolution industrielle, à une « civilisation en symbiose avec la nature », fondée sur les ressources de surface et les énergies renouvelables. Autrement dit, une civilisation où l'humanité, consciente d'être enfant de Dieu, aime davantage la nature et vit en harmonie avec elle.</p>
<div class="note">Les actions concrètes sont menées par des clubs thématiques (« système par projets ») : potager biologique, vélo, artisanat.</div>

<h2 id="alimentation">Alimentation sans viande et bas carbone</h2>
<p>Ce mode de vie consiste à intégrer activement des repas sans viande et à privilégier les produits locaux et de saison. On réduit ainsi le « kilométrage alimentaire », c'est-à-dire le carburant consommé et le CO₂ émis pour transporter les aliments du champ à l'assiette, tout en soutenant les agriculteurs et pêcheurs locaux.</p>
<p>Jardinage et plantation d'arbres permettent aussi de goûter la beauté de la nature. Le <strong>Club de potager biologique</strong> met ces idées en pratique.</p>

<h2 id="mode-de-vie">Mode de vie sobre en ressources et en carbone</h2>
<p>Il s'agit de réduire les émissions de CO₂ de notre quotidien et de notre travail en économisant ressources et énergie, et en utilisant des énergies renouvelables comme le solaire. Se déplacer à vélo pour les courses, l'école ou le travail émet par exemple bien moins qu'une voiture à essence : c'est le rôle du <strong>Club vélo</strong>.</p>
<p>Seicho-No-Ie mène aussi des projets de reboisement, installe des centrales solaires, développe véhicules électriques et bornes de recharge rapide, construit des <a href="zeb.html">bâtiments à énergie nette zéro</a> et maintient sa certification ISO 14001. Au Japon, les membres peuvent recevoir des aides pour s'équiper en panneaux solaires, batteries ou véhicules électriques.</p>

<h2 id="creation">Activités créatives bas carbone, tournées vers la nature</h2>
<p>Ces activités expriment, au quotidien et avec peu d'émissions, le sentiment d'unité avec la nature, et partagent cette joie avec l'entourage. Par exemple : objets et textiles en matières naturelles, <em>etegami</em> (cartes illustrées) et <em>efūtō</em> (enveloppes illustrées) réalisés en voyage, ou œuvres d'artistes célébrant ce lien avec la nature.</p>
<p>Chacun s'exprime à sa manière et permet aux autres d'apprécier sa création ; cette joie fait grandir et rayonner le sentiment d'unité avec la nature. Le <strong>Club d'artisanat</strong> porte ces initiatives.</p>

<h2 id="energies">Mouvement pour l'expansion des énergies naturelles</h2>
<p>Pour freiner le réchauffement climatique et par opposition à l'énergie nucléaire, Seicho-No-Ie promeut le développement des énergies renouvelables, notamment solaire et géothermique.</p>
<table class="facts">
<tr><th>Projet</th><td>Centrale géothermique Seicho-No-Ie d'Oita-Beppu</td></tr>
<tr><th>Lieu</th><td>Minami Tateishi Torinoyu, ville de Beppu, préfecture d'Oita (Japon)</td></tr>
<tr><th>Puissance</th><td>50 kW</td></tr>
<tr><th>Financement</th><td>Objectif atteint : les dons ne sont plus acceptés. Merci à tous les donateurs.</td></tr>
</table>

<h2 id="iso">Certification ISO 14001</h2>
<p>En 2001, Seicho-No-Ie est devenu la première organisation religieuse au monde certifiée ISO 14001, la norme internationale des systèmes de management environnemental.</p>
"""
page("activites.html", "Activités — Seicho-No-Ie France", "Activités", "Activités", acts, SIDE_ACT,
     desc="Les activités de Seicho-No-Ie pour une civilisation en harmonie avec la nature.")

# ---------- ZEB ----------
zeb = """
<h2>Bâtiments à énergie nette zéro (ZEB)</h2>
<h3>Le premier ZEB du Japon</h3>
<p>Le « Bureau dans la forêt » de Seicho-No-Ie a été construit comme le premier bâtiment à énergie nette zéro (<em>Zero-Energy Building</em>, ZEB) du Japon. Il réduit au maximum sa consommation annuelle grâce aux économies d'énergie, et compense le reste en produisant sa propre électricité à partir du solaire et de la biomasse.</p>
<p>L'électricité produite sur place alimente aussi les microbus et véhicules électriques utilisés pour les trajets domicile-travail. Seicho-No-Ie poursuit la construction de ZEB à mesure qu'il rebâtit ses centres de diffusion et de formation au Japon.</p>

<h2>Les ZEB de Seicho-No-Ie au Japon</h2>
<div class="grid g2">
  <div class="card"><h3>Bureau dans la forêt</h3><p>Ville de Hokuto, préfecture de Yamanashi. Siège international du mouvement.</p><a class="more" href="https://www.seicho-no-ie.org/eng/zeb/office-in-the-forest/" target="_blank" rel="noopener">En savoir plus (EN) ↗</a></div>
  <div class="card"><h3>Media Center</h3><p>Ville de Hokuto, préfecture de Yamanashi.</p><a class="more" href="https://www.seicho-no-ie.org/eng/zeb/media-center/" target="_blank" rel="noopener">En savoir plus (EN) ↗</a></div>
  <div class="card"><h3>Tour de Lumière</h3><p>Shibuya, Tokyo.</p></div>
  <div class="card"><h3>Centre de diffusion d'Ibaraki</h3><p>Ville de Kasama, préfecture d'Ibaraki.</p><a class="more" href="https://www.seicho-no-ie.org/eng/zeb/ibaraki-missionary-area/" target="_blank" rel="noopener">En savoir plus (EN) ↗</a></div>
</div>
"""
page("zeb.html", "ZEB — Seicho-No-Ie France", "ZEB", "ZEB", zeb,
     side("ZEB", [("zeb.html", "Présentation")], "zeb.html") + side("Voir aussi", [("activites.html", "Activités"), ("activites.html#energies", "Énergies naturelles")]),
     desc="Les bâtiments à énergie nette zéro de Seicho-No-Ie.")

# ---------- Contacts ----------
contact = f"""
<h2>Le réseau mondial de Seicho-No-Ie</h2>
<p class="lead">Seicho-No-Ie est présent sur tous les continents. Retrouvez ci-dessous les contacts en France et en Europe.</p>

<div class="region fr" id="france">
  <h3>🇫🇷 France</h3>
  <p>Des réunions Seicho-No-Ie se tiennent régulièrement en France (ainsi qu'au Royaume-Uni, en Autriche, en Suisse, en Belgique et en Irlande). Pour connaître les lieux et les dates :</p>
  <dl>
    <dt>Contact</dt><dd>Rév. Yuji Otsuka, ministre ordonné, directeur adjoint du Département international</dd>
    <dt>E-mail</dt><dd><a href="mailto:yujiotsuka32@gmail.com">yujiotsuka32@gmail.com</a></dd>
    <dt>Siège international</dt><dd>Section internationale : +81 551-45-7792</dd>
  </dl>
  <div class="todo" style="margin-bottom:0">À compléter : lieux, jours et horaires des réunions en France, contact local francophone.</div>
</div>

<h2 id="europe">Europe</h2>
<div class="region">
  <h3>Allemagne</h3>
  <dl>
    <dt>Organisation</dt><dd>Seicho-No-Ie Freundeskreis in Deutschland e.V.</dd>
    <dt>Adresse</dt><dd>Kölner Straße 66, D-60327 Francfort-sur-le-Main</dd>
    <dt>Téléphone</dt><dd>+49 69 7394 3630</dd>
    <dt>Fax</dt><dd>+49 69 7394 3631</dd>
    <dt>Site web</dt><dd><a href="http://www.seicho-no-ie.de/" target="_blank" rel="noopener">seicho-no-ie.de</a></dd>
  </dl>
  <div class="note" style="margin-bottom:0">C'est ce bureau qui gère les inscriptions à la <b>2<sup>e</sup> Rencontre Seicho-No-Ie en Europe</b>, du 16 au 18 octobre 2026 à Mayence.</div>
</div>
<div class="region">
  <h3>Royaume-Uni, Autriche, Suisse, Belgique, Irlande</h3>
  <p style="margin:0">Même contact que pour la France (Rév. Yuji Otsuka).</p>
</div>
<div class="region">
  <h3>Portugal</h3>
  <dl>
    <dt>Adresse</dt><dd>Edifício Copombal, Viaduto Eng. Guilherme Gomes Santos, 2º andar, Pombal</dd>
    <dt>Tél./Fax</dt><dd>+351 236 211 629</dd>
  </dl>
</div>
<div class="region">
  <h3>Espagne</h3>
  <dl><dt>E-mail</dt><dd><a href="mailto:info@seichonoie-es.org">info@seichonoie-es.org</a></dd></dl>
</div>

<h2 id="monde">Dans le monde</h2>
<p>Coordonnées des autres pays (pages en anglais) :</p>
<div class="chips">
  <a href="{INT}/contact/japan/" target="_blank" rel="noopener">Japon</a>
  <a href="{INT}/contact/contact-usa/" target="_blank" rel="noopener">États-Unis</a>
  <a href="{INT}/contact/canada/" target="_blank" rel="noopener">Canada</a>
  <a href="{INT}/contact/brazil/" target="_blank" rel="noopener">Brésil</a>
  <a href="{INT}/contact/the-republic-of-china/" target="_blank" rel="noopener">Taïwan</a>
  <a href="{INT}/contact/china/" target="_blank" rel="noopener">Chine</a>
  <a href="{INT}/contact/other-country/" target="_blank" rel="noopener">Autres pays</a>
</div>
"""
page("contact.html", "Contacts — Seicho-No-Ie France", "Contacts", "Contacts", contact, SIDE_CONTACT,
     desc="Contacts Seicho-No-Ie en France, en Europe et dans le monde.")

# ---------- Livres ----------
def book(cls, title_fr, title_en, author, price, text):
    by = f'<div class="by">{author}</div>' if author else ""
    a = author.replace("Rév. ", "") if author else "Seicho-No-Ie"
    return f"""<div class="book">
  <div class="cover {cls}">{title_en}<small>{a}</small></div>
  <div>
    <h3>{title_fr}</h3>{by}
    <div class="orig">Titre original : {title_en}</div>
    <div class="price">{price}</div>
    <p>{text}</p>
    <a class="btn green" href="http://sniusa.org/" target="_blank" rel="noopener">Commander ↗</a>
  </div>
</div>"""

MT = "Rév. Masanobu Taniguchi"
ST = "Rév. Seicho Taniguchi"
books = f"""
<div class="note">Ces ouvrages sont en anglais et se commandent auprès de Seicho-No-Ie États-Unis (prix en dollars, hors frais de port et taxes).</div>
<div class="todo">À compléter : ouvrages disponibles en français et point de vente en France.</div>

<h2 id="masanobu">Livres du Rév. Masanobu Taniguchi</h2>
{book("c1", "Prières quotidiennes, volume 1", "Daily Prayers, Volume 1", MT, "12,50 $", "Prier pour la Grande Harmonie de Dieu, de la nature et de l'être humain.")}
{book("c2", "Chant à la louange de la nature", "Song in Praise of Nature", MT, "10,00 $", "Pour approfondir le sentiment d'unité entre la nature et l'être humain.")}
{book("c3", "Chant à la louange du Bodhisattva qui reflète les sons du monde", "Song in Praise of the Bodhisattva Who Reflects the Sounds of the World", MT, "12,00 $", "Pour saisir intuitivement qui est ce Bodhisattva et mieux comprendre la grande compassion de Dieu et le salut.")}

<h2 id="seicho">Livres du Rév. Seicho Taniguchi</h2>
{book("c1", "Messages de sagesse et d'amour", "Messages of Wisdom and Love", ST, "11,00 $", "De beaux messages qui éclairent le vrai sens de la sagesse et de l'amour, à appliquer dans sa vie pour se remplir d'amour divin.")}
{book("c4", "Oh, mon foyer heureux !", "Oh, My Happy Home!", ST, "10,00 $", "Un livre chaleureux, riche en témoignages, qui montre comment apaiser le stress du travail, la souffrance de la maladie et les épreuves de la vie en créant un « foyer semblable au paradis ».")}
{book("c2", "Le Shinsokan est merveilleux", "Shinsokan is Wonderful", ST, "8,00 $", "Une excellente introduction au Shinsokan, la méditation principale de Seicho-No-Ie, qui accorde l'esprit à Dieu : ce qu'il est, comment le pratiquer, et la force de vie qui naît de sa pratique quotidienne.")}
{book("c3", "Ouvrez les portes de votre vie", "Open the Doors of Your Life", ST, "12,00 $", "Un petit livre à emporter partout, aux messages réconfortants, bilingue anglais-japonais.")}
{book("c3", "Ouvrez les portes de votre vie, vol. 2", "Open the Doors of Your Life, Vol. 2", ST, "12,00 $", "Le deuxième volume de messages inspirants, bilingue anglais-japonais.")}
{book("c3", "Ouvrez les portes de votre vie, vol. 3", "Open the Doors of Your Life, Vol. 3", ST, "12,00 $", "Le troisième volume de messages inspirants, bilingue anglais-japonais.")}

<h2 id="divers">Autres publications</h2>
{book("c4", "Méditations quotidiennes pour un avenir lumineux", "Daily Meditations for a Bright Future", "", "7,50 $", "Un calendrier perpétuel de 31 pages associant messages inspirants et photos de nature. Au dos de chaque page, un espace pour vos prières personnelles. Réutilisable d'année en année.")}
"""
page("livres.html", "Livres — Seicho-No-Ie France", "Livres", "Livres", books, SIDE_BOOKS,
     desc="Livres des Rév. Masanobu et Seicho Taniguchi.")

# ---------- Actualités ----------
news = f"""
<h2>Communiqués</h2>
<p>Retrouvez ici, traduits en français, les communiqués de Seicho-No-Ie. Chaque page renvoie aussi à la version originale en anglais.</p>
{news_list(NEWS)}
<div class="todo">À compléter : actualités et événements propres à la France.</div>
"""
page("actualites.html", "Actualités — Seicho-No-Ie France", "Actualités", "Actualités", news,
     SIDE_NEWS(),
     desc="Actualités de Seicho-No-Ie.")

print("ok")
