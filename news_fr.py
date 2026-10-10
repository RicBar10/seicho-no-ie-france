# Contenu français des communiqués (importé par build.py)
from urllib.parse import quote

UP = "https://www.seicho-no-ie.org/eng/wp-content/uploads/"
IMG_ELEVAGE = UP + quote("畜産-1.jpg")
IMG_AMAZONIE = UP + quote("アマゾン.jpg")
PDF_RAPPORT = UP + "2022_sni_performance_report_en.pdf"

# (slug, date, titre, url originale, corps HTML)
ARTICLES = []

# ---------------------------------------------------------------- 2025-07
ARTICLES.append(("communique-2025-07-sans-viande.html", "2025-07-04",
"Pourquoi ne pas manger de viande ? En quoi la viande pose-t-elle problème ?",
"https://www.seicho-no-ie.org/eng/news/nwes_202507/", f"""
<p class="lead">À travers ce site, Seicho-No-Ie souhaite encourager le plus grand nombre de personnes à réduire autant que possible leur consommation de viande. La raison : manger de la viande détruit la nature et ses écosystèmes, et nous pensons aussi que c'est un obstacle à la paix dans le monde.</p>

<h3>L'élevage, un moteur du réchauffement climatique</h3>
<p>Des phénomènes météorologiques extrêmes se produisent désormais fréquemment partout dans le monde. Ils sont dus au réchauffement climatique, provoqué par l'augmentation du dioxyde de carbone et des autres gaz à effet de serre dans l'atmosphère. Qu'est-ce qui émet de telles quantités de gaz à effet de serre et accélère le réchauffement ? Malheureusement, ce sont nos propres activités.</p>
<p>Parmi elles, l'une a un impact majeur sur l'aggravation du réchauffement : l'élevage. Selon l'Organisation des Nations unies pour l'alimentation et l'agriculture (FAO), il représente environ 12 % des émissions mondiales de gaz à effet de serre. Les ruminants comme les bovins rejettent en particulier de grandes quantités de méthane, un gaz au fort pouvoir de réchauffement.</p>
<figure><img src="{IMG_ELEVAGE}" alt="Bovins et porcs en élevage intensif" loading="lazy"></figure>

<h3>Le transport du bétail accélère aussi le réchauffement</h3>
<div class="todo">Section à traduire à partir du texte original (non récupéré automatiquement).</div>

<h3>Incendies de la forêt amazonienne et consommation de viande</h3>
<p>La plus grande forêt tropicale du monde, qui s'étend sur le bassin de l'Amazone en Amérique du Sud, abrite une biodiversité exceptionnelle. Elle joue un rôle important pour freiner le réchauffement climatique, mais elle est brûlée pour faire place à l'agriculture. Les terres défrichées servent de pâturages et à la culture de fourrage pour le bétail, notamment les bovins à viande. Cela montre à quel point la consommation de viande est massive : on peut dire qu'en mangeant de la viande, nous participons indirectement à la destruction de la forêt amazonienne.</p>
<figure><img src="{IMG_AMAZONIE}" alt="Parcelle de forêt amazonienne défrichée et brûlée" loading="lazy"></figure>

<h3>La consommation de viande aggrave la faim et le manque d'eau dans le monde</h3>
<p>Une grande partie des céréales produites dans le monde sert à nourrir le bétail plutôt que les êtres humains. Il faut plusieurs kilos de céréales pour produire un seul kilo de viande, et la production de bœuf nécessite d'énormes quantités d'eau. Pendant ce temps, de nombreuses personnes souffrent de la faim et du manque d'eau.</p>

<h3>Nos choix de consommateurs façonnent l'avenir</h3>
<p>Acheter de la viande, c'est envoyer aux producteurs le signal qu'il existe une demande. À l'inverse, chacun de nos choix d'achat peut faire évoluer la production et donc l'avenir. Commençons, pas à pas, à adopter une alimentation qui prend soin des êtres humains, des animaux et de l'environnement.</p>

<div class="todo">Traduction établie à partir des extraits disponibles. À vérifier et compléter avec le texte anglais intégral (chiffres précis, notes et références).</div>
"""))

# ---------------------------------------------------------------- 2024-05
def kv(rows):
    return '<table class="facts">' + "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in rows) + "</table>"

ARTICLES.append(("communique-2024-05-rapport-environnemental.html", "2024-05-15",
"Notre rapport de performance environnementale 2022",
"https://www.seicho-no-ie.org/eng/news/news_202405/", f"""
<p class="lead">Nous vous présentons le rapport de performance environnementale de Seicho-No-Ie, établi selon la norme internationale ISO 14001, pour l'année 2022 (janvier à décembre).</p>

<div class="report-head">
  <a href="{PDF_RAPPORT}" target="_blank" rel="noopener"><img src="img/rapport-2022-couverture-01.jpg" alt="Couverture du rapport de performance environnementale 2022" loading="lazy"></a>
  <div>
    {kv([("Publication", "1<sup>er</sup> mars 2024"),
         ("Auteur", "Personne juridique religieuse « Seicho-No-Ie », Siège international, Département de la symbiose environnementale"),
         ("Responsables", "Département de la symbiose environnementale (Tanaka, Kono)"),
         ("Contact", "8240-2103 Oizumicho Nishiide, Hokuto, Yamanashi, Japon<br>Tél. : +81 551-45-7747 (ligne directe)")])}
    <a class="btn green" href="{PDF_RAPPORT}" target="_blank" rel="noopener">Télécharger le rapport original (PDF, anglais)</a>
  </div>
</div>

<div class="stats">
  <div><b>15 ans</b><span>de « zéro carbone » sur les 3 sites principaux</span></div>
  <div><b>66 sites</b><span>à bilan carbone nul ou négatif</span></div>
  <div><b>2,85 GWh</b><span>produits par les grandes centrales solaires et géothermique</span></div>
  <div><b>107 M¥</b><span>collectés pour l'aide d'urgence à l'Ukraine</span></div>
</div>

<nav class="toc"><b>Sommaire</b>
<ol>
<li><a href="#r1">Actions de sensibilisation au sein de l'organisation</a></li>
<li><a href="#r2">Actions de sensibilisation hors de l'organisation</a></li>
<li><a href="#r3">Résultats du mouvement « zéro carbone »</a></li>
</ol></nav>

<h2 id="r1">1. Actions de sensibilisation au sein de l'organisation religieuse</h2>
<p>Fondé sur la vérité religieuse selon laquelle « Dieu, la nature et l'être humain ne font qu'un », et dans le but d'amener chacun à adopter un mode de vie durable en harmonie avec la nature, Seicho-No-Ie promeut une manière de vivre qui contribue à résoudre les problèmes environnementaux mondiaux.</p>

<h3>Message vidéo du Nouvel An</h3>
<p>Le 1<sup>er</sup> janvier 2022, le message vidéo du Nouvel An du Rév. Masanobu Taniguchi, président de Seicho-No-Ie, a été publié sur le site officiel. Alors que la pandémie de coronavirus entrait dans sa troisième année, il y a rappelé l'importance du « mode de vie du cadran solaire » (ne retenir que les moments lumineux) en ces temps incertains. Il a expliqué que le rôle de Seicho-No-Ie est de tirer les leçons de ces catastrophes et de ces échecs, d'éveiller la volonté de Dieu et de Bouddha qui demeure en nous, et d'agir avec joie pour bâtir une « nouvelle civilisation » visant la Grande Harmonie de Dieu, de la nature et de l'être humain. La vidéo a été sous-titrée en anglais, portugais, chinois, coréen, espagnol et allemand.</p>

<h3>Liens vers les vidéos SNI</h3>
<p>Une page web regroupe les vidéos du Rév. Masanobu Taniguchi, de Mme Junko Taniguchi (présidente de l'Association de la Colombe blanche de Seicho-No-Ie) et de conférenciers de Seicho-No-Ie, dont des ministres ordonnés. Cette initiative est née de la nécessité de freiner la propagation du coronavirus, qui rendait difficile la tenue en présentiel des conférences publiques, séminaires de formation spirituelle, réunions de lecteurs et autres événements. Les vidéos ont été largement utilisées pour l'étude personnelle, lors de forums en ligne et d'activités de sensibilisation à la protection de l'environnement, et comme guide et source de motivation pour une vie plus lumineuse.</p>
<p><a href="https://snivideolinks.ubemstudygroup.com/" target="_blank" rel="noopener">Accéder aux vidéos SNI ↗</a></p>

<h3>Livres et revues mensuelles</h3>
<p>Seicho-No-Ie encourage le passage à un mode de vie de « nouvelle civilisation », où la nature et l'être humain prospèrent ensemble, à travers la publication et la diffusion d'ouvrages tels que <em>Bâtissons une « nouvelle civilisation »</em> (vol. 1, « Les bases du mouvement », et vol. 2, « Le développement concret du mouvement »), sous la direction du Rév. Masanobu Taniguchi, ou <em>La vie quotidienne dans la forêt</em> de Mme Junko Taniguchi.</p>
<p>Des articles sur la protection de l'environnement ont paru dans chaque numéro de la revue des membres (<em>Bulletin Seicho-No-Ie</em>) et des revues destinées au grand public : <em>Inochi-No-Wa</em> (« Le cercle de la vie », revue générale), <em>Shirohato</em> (« Colombe blanche », revue féminine) et <em>Hidokei 24</em> (« Cadran solaire 24 », revue pour les jeunes).</p>

<h3>Activités par projets (PBS)</h3>
<p>Pour accompagner le passage de l'« ancienne civilisation », où l'être humain détruit la nature et provoque le réchauffement climatique pour satisfaire ses désirs, à une « nouvelle civilisation », où la prospérité de la nature est celle de l'être humain, Seicho-No-Ie fait vivre ses valeurs et un mode de vie bas carbone au quotidien grâce à son système par projets (PBS), organisé en trois clubs. Il organise de petits événements et diffuse le mouvement en ligne, notamment sur Facebook.</p>
<div class="grid g3">
  <div class="card"><h3>Club de potager biologique</h3><p>Il met en pratique et promeut une « alimentation sans viande et bas carbone ». Ses membres cultivent leurs propres légumes et céréales biologiques sur leur balcon ou au potager, pour savourer et partager avec leur entourage les bienfaits locaux et de saison de la nature. Le club recommande aussi d'acheter des produits biologiques, sans pesticides, locaux et de saison.<br><small>Livre : <em>Changer l'avenir depuis la table</em></small></p></div>
  <div class="card"><h3>Club vélo</h3><p>Il promeut un « mode de vie sobre en ressources et bas carbone ». Le vélo n'utilise pas de carburant fossile et n'émet pas de CO₂ : l'utiliser au quotidien réduit nettement nos émissions. Enfants et adultes du monde entier partagent la joie d'apprendre à pédaler et de rouler dans le vent. Le club œuvre pour la paix en faisant connaître la vie saine et spirituellement riche qu'offre le vélo.<br><small>Livre : <em>La paix à vélo</em></small></p></div>
  <div class="card"><h3>Club d'artisanat</h3><p>Il promeut une « expression bas carbone centrée sur la nature ». Ses membres fabriquent à la main des objets du quotidien : baguettes, cadres photo, étuis à livres, pochettes… Ils choisissent des matériaux respectueux de la nature, comme le bois local et les fibres naturelles. Plutôt que la surproduction et la surconsommation d'objets bon marché, le club prône un mode de vie qui prend soin des choses qui nous entourent.<br><small>Livre : <em>L'artisanat sauvera le monde</em></small></p></div>
</div>

<h3>Activités en ligne et engagement à la maison</h3>
<p>Seicho-No-Ie a mené des actions de sensibilisation sur Internet. Son site officiel met en avant les activités des clubs PBS ; des forums en ligne (Facebook, Zoom…) ont permis de visionner ensemble les vidéos du Rév. Masanobu Taniguchi, de Mme Junko Taniguchi et des conférenciers, puis d'échanger impressions et opinions.</p>
<p>Les membres, en tant que pratiquants d'un mode de vie éthique fondé sur la foi, ont été invités à utiliser le <em>Journal du cadran solaire</em> (édition 2022), pour noter chaque jour leurs gestes « écologiques », et le <em>Seikatsu no kirokuhyo</em>, un tableau mensuel de leurs émissions de CO₂. Imprimé à 36 000 exemplaires par le Siège international pour les membres, ce tableau permet de relever la consommation et les émissions liées à l'électricité, au gaz, à l'eau, au kérosène et à l'essence, et de déduire les émissions évitées grâce à l'électricité solaire revendue. Objectif : réduire ses émissions par rapport à l'année précédente. Distribué depuis 2001, il aide les familles à diminuer leur empreinte carbone.</p>
<p>Depuis la libéralisation du marché de l'électricité au Japon en avril 2016, Seicho-No-Ie recommande aussi de choisir des fournisseurs proposant une part plus élevée d'énergies renouvelables, plutôt qu'une électricité d'origine nucléaire ou thermique.</p>

<h2 id="r2">2. Actions de sensibilisation hors de l'organisation</h2>

<h3>Protection des forêts et lutte contre la faim</h3>
<p>Dans un esprit de lutte contre la faim, la cantine du personnel du « Bureau dans la forêt » ne sert, une fois par mois, qu'un bol de soupe et un bol de riz, et l'économie réalisée est reversée au Programme alimentaire mondial des Nations unies (PAM). Pour contribuer, même modestement, à freiner la déforestation, Seicho-No-Ie fait aussi des dons au WWF Japon.</p>
{kv([("Don au WWF pour la protection des forêts", "Dons au « Projet de conservation des forêts d'Indonésie » du WWF Japon : collecte pour la préservation de la biodiversité, part des ventes des livres du Rév. Masanobu Taniguchi (dont ceux coécrits avec Mme Junko Taniguchi) et 200 000 yens par mois issus des « dons pour les forêts » des trois revues mensuelles (1 yen par revue). <b>Total 2022 : 1 291 851 yens.</b> Ces fonds financent patrouilles, reboisement, études et éducation à l'environnement autour de deux parcs nationaux de Sumatra et dans trois États de Bornéo."),
     ("Un bol de soupe, un bol de riz", "Depuis avril 2014, une fois par mois, la cantine du personnel sert ce repas frugal en solidarité avec les personnes qui souffrent de la faim, et reverse 300 yens par repas servi. Ce mouvement s'est étendu à tous les sites de Seicho-No-Ie dans le monde. <b>Total 2022 : 177 000 yens (590 repas)</b>, versés au siège du PAM à Rome via l'Association japonaise pour le PAM."),
     ("Collecte « en un clic » contre la faim", "L'Association de prospérité de Seicho-No-Ie, qui réunit des chefs d'entreprise adhérant à ses enseignements, reverse chaque mois au PAM des dons d'entreprises partenaires, proportionnels au nombre de clics reçus sur son site. <b>Total 2022 : 948 708 yens, de 14 partenaires.</b>")])}

<h3>Agir pour la paix : « Peace for Ukraine » (P4U)</h3>
<p>Environnement, ressources et paix sont étroitement liés. Après avoir obtenu la certification ISO 14001 pour agir sur l'environnement et les ressources, Seicho-No-Ie a ressenti le besoin d'agir aussi pour la paix. Il a lancé l'initiative « Peace for Ukraine » (P4U) en soutien au peuple ukrainien :</p>
<ul class="checks">
<li>création d'un groupe Facebook public appelant à la paix en Ukraine ;</li>
<li>adoption d'un logo P4U pour les actions liées à l'initiative ;</li>
<li>collectes de fonds dans tout le pays pour l'aide d'urgence à l'Ukraine ;</li>
<li>créations artisanales aux couleurs du drapeau ukrainien ;</li>
<li>drapeau ukrainien hissé en signe d'amitié avec le peuple ukrainien ;</li>
<li>préparation de plats ukrainiens pour se sentir plus proche de l'Ukraine.</li>
</ul>

<h3>Aide à l'Ukraine, banque alimentaire, agrivoltaïsme, éolien</h3>
<p>À travers ces actions, Seicho-No-Ie explique pourquoi une religion s'engage de la sorte, et montre le lien profond entre environnement, ressources et paix.</p>
{kv([("Collecte d'urgence pour l'Ukraine", "<b>107 079 999 yens</b> collectés au 27 septembre 2022."),
     ("Mini-bibliothèques", "Installation, pour le grand public, de mini-bibliothèques proposant des livres sur l'Ukraine et des publications de Seicho-No-Ie."),
     ("Ex-voto pour la paix", "Réalisation d'images votives pour prier pour la paix en Ukraine ; les dons recueillis ont été versés à la collecte d'urgence."),
     ("Banque alimentaire", "Le Siège international participe bénévolement aux activités de l'association « Food bank Yamanashi » (Minami Alps), notamment l'emballage des denrées."),
     ("Agrivoltaïsme sur des terres en friche", "L'association SSFK (Akasaka, Tokyo) a installé un système agrivoltaïque (815,36 kWh), qui produit de l'énergie renouvelable tout en redonnant vie à des terres agricoles abandonnées."),
     ("Éolienne contre le nucléaire", "La SSFK a installé une petite éolienne (19,8 kW) à Oma (Shimokita, Aomori) pour plaider en faveur de la sortie du nucléaire.")])}

<h2 id="r3">3. Résultats du mouvement « zéro carbone »</h2>

<h3>Zéro carbone sur 66 sites</h3>
<p>Depuis 2007, Seicho-No-Ie mène un mouvement « zéro carbone » visant à ramener à zéro les émissions de CO₂ liées à ses activités religieuses. Après quinze ans, les résultats ont encore progressé en 2022 grâce à l'amélioration continue de la démarche ISO 14001.</p>
<table class="facts num">
<tr><th></th><td><b>3 sites principaux</b><br><small>Siège international, Temple principal, Temple d'Uji</small></td><td><b>61 autres sites</b><br><small>Centres de diffusion et de formation spirituelle</small></td></tr>
<tr><th>Émissions</th><td>146 576 kg CO₂</td><td>566 629,9 kg CO₂</td></tr>
<tr><th>Compensation</th><td>−1 944 445,5 kg CO₂</td><td>−2 681 672,9 kg CO₂</td></tr>
<tr><th>Bilan final</th><td><b>−1 797 862,4 kg CO₂</b></td><td><b>−2 115 043 kg CO₂</b></td></tr>
<tr><th>Résultat</th><td>Zéro carbone pour la 15<sup>e</sup> année consécutive</td><td>Zéro carbone pour la 2<sup>e</sup> année consécutive, sans achat de crédits carbone</td></tr>
</table>
<p style="font-size:.9rem;color:var(--muted)">Périmètre des 3 sites principaux : émissions des huit types d'énergie retenus au Japon (électricité, gaz de ville, GPL, kérosène, fioul lourd A, essence, gazole, eau et assainissement), plus les déplacements du personnel, les voyages professionnels et les participants aux événements du siège. La compensation est une estimation fondée sur l'électricité solaire revendue, l'absorption par les forêts et les réductions issues de la collecte pour les énergies renouvelables.</p>
<p>Principaux facteurs de réussite :</p>
<ul class="checks">
<li>des efforts constants pour réduire la consommation d'énergie ;</li>
<li>le choix de fournisseurs d'énergie à plus faible facteur d'émission ;</li>
<li>les panneaux solaires installés sur place ;</li>
<li>l'absorption de CO₂ par les forêts possédées par l'organisation ;</li>
<li>le reboisement mené par les membres ;</li>
<li>la répartition, entre les zones de diffusion, des réductions obtenues par les grandes centrales solaires, au prorata de leurs dons à la collecte pour les énergies renouvelables.</li>
</ul>
<p style="font-size:.9rem;color:var(--muted)">Photos du rapport : centrale solaire de 1 255 kW construite par le Temple d'Uji à Ayabe (Kyoto) ; panneaux de 30 kW du centre d'Okayama ; centrale solaire de Fukushima Nishigo.</p>

<h3>Développer les énergies renouvelables</h3>
<p>Seicho-No-Ie développe ce mouvement pour faire advenir un mode de vie encore plus harmonieux entre nature et êtres humains, où la société adopte pleinement les énergies renouvelables, abandonne réellement le nucléaire et freine le réchauffement climatique.</p>
{kv([("Collecte pour les énergies renouvelables", "<b>12 080 000 yens</b> reçus en 2022, soit <b>585 210 000 yens</b> depuis son lancement le 1<sup>er</sup> juillet 2014. Depuis 2017, les donateurs qui le souhaitent voient leur nom inscrit sur une plaque près des panneaux solaires et sur un site web japonais."),
     ("Centrale géothermique d'Oita-Beppu", "Première centrale géothermique de l'organisation, en service depuis octobre 2020. Puissance : 50 kW ; production 2022 : <b>114 829 kWh</b>. Elle fonctionne 24 h/24 avec un facteur de charge supérieur à 80 % (contre 12 % pour le solaire), ce qui en fait une centrale de base. Le centre de diffusion voisin d'Oita profite de son électricité et d'eau thermale chauffée grâce à son surplus d'énergie."),
     ("Aides aux membres (2022)", "Panneaux solaires : 8 dossiers, 951 000 yens (20 000 yens par kW).<br>Véhicules électriques : 17 dossiers, 4 937 000 yens (300 000 yens max. par véhicule, dans la limite de 10 % du prix).<br>Batteries lithium-ion : 18 dossiers, 1 575 000 yens (10 000 yens par kWh).")])}

<h3>Les réductions de CO₂ de Seicho-No-Ie</h3>
<p>Les grandes centrales et les panneaux installés sur les autres sites contribuent fortement à la compensation carbone de toute l'organisation.</p>
<table class="facts num">
<tr><th>Électricité produite en 2022</th><td></td></tr>
<tr><th>Centrale solaire de Kyoto Joyo <small>(depuis mars 2015)</small></th><td>1 953 701 kWh <small>≈ 678 foyers</small></td></tr>
<tr><th>Centrale solaire de Fukushima Nishigo <small>(depuis déc. 2015)</small></th><td>785 062 kWh <small>≈ 273 foyers</small></td></tr>
<tr><th>Centrale géothermique d'Oita-Beppu <small>(depuis oct. 2020)</small></th><td>114 829 kWh <small>≈ 40 foyers</small></td></tr>
<tr><th>Total</th><td><b>2 853 592 kWh</b> <small>≈ 991 foyers</small></td></tr>
<tr><th>CO₂ évité</th><td><b>1 071 753 kg</b> <small>≈ absorption annuelle de 76 553 cèdres du Japon</small></td></tr>
</table>
<p><b>Les efforts des membres.</b> Depuis 2020, Seicho-No-Ie évalue la participation de chacun et les efforts de chaque centre de diffusion : forêts des centres et des membres, reboisement et remise des tableaux d'émissions servent à compenser le carbone. En 2022, <b>1 291 486 kg de CO₂</b> ont ainsi été compensés, soit l'absorption annuelle de 92 249 cèdres du Japon. 42 zones de diffusion ont remis leurs tableaux (36 en 2021) et 1 200 membres (676 en 2021, soit +77,5 %).</p>
<p><b>Véhicules électriques.</b> En introduisant voitures et microbus électriques, bornes de recharge rapide et systèmes V2H (du véhicule à la maison), Seicho-No-Ie réduit les émissions liées aux déplacements. Des bornes de recharge rapide gratuites sont installées progressivement sur ses sites au Japon. Les membres peuvent recevoir 300 000 yens pour l'achat d'un véhicule électrique, 10 000 yens par kWh de batterie stationnaire et 20 000 yens par kW de solaire ou de petit éolien (sous conditions).</p>
<p style="font-size:.9rem;color:var(--muted)">Hypothèses de calcul : un foyer émet environ 2 720 kg de CO₂ par an ; un cèdre du Japon en absorbe environ 14 kg par an.</p>

<h3>Solaire et géothermie : le nouveau centre d'Oita</h3>
<p>La zone de diffusion d'Oita a célébré l'achèvement de son nouveau centre, à Beppu. En exploitant au maximum les énergies du ciel et de la terre, le solaire et la géothermie, il est devenu un bâtiment à énergie nette zéro (ZEB). Il utilise trois sources renouvelables : l'électricité de la centrale géothermique voisine (49 kW), la chaleur de l'eau thermale chauffée par son surplus, et ses propres panneaux solaires en toiture (29,82 kW).</p>
<div class="grid g2">
  <div class="card"><h3>Un lieu ancré dans son territoire</h3><p>Pierres locales de Beppu dans les massifs et les haies ; plantation de l'abricotier du Japon de Bungo (symbole de la préfecture), de l'osmanthe odorant (fleur de la ville) et du kabosu, un agrume local. Seicho-No-Ie souhaite faire de ce centre, attentif aux ressources et à l'environnement locaux, un lieu qui diffuse le message d'une « nouvelle civilisation » où nature et êtres humains coexistent.</p></div>
  <div class="card"><h3>La chaleur du bois</h3><p>Construit principalement en cèdre et en cyprès du Japon des préfectures d'Oita et de Kumamoto, le centre résiste à des séismes de magnitude 7. Sa grande salle de formation, dotée de fenêtres à différentes hauteurs, d'exutoires de fumée et de ventilateurs de plafond, favorise la ventilation naturelle et la prévention des infections.</p></div>
  <div class="card"><h3>Stockage de dernière génération</h3><p>En plus de batteries lithium-ion de 135 kWh, le centre dispose d'un système V2H qui permet aux véhicules électriques de l'alimenter en cas de besoin, par exemple en situation d'urgence.</p></div>
  <div class="card"><h3>Eau chaude géothermique</h3><p>L'eau à 75 °C fournie par la centrale géothermique alimente les bains, bains de pieds, douches et lavabos.</p></div>
</div>

<h3>Bâtiments hors réseau et ZEB : les résultats</h3>
<p>Le « Bureau dans la forêt » a été conçu dès l'origine comme un ZEB. En 2020, des batteries de grande capacité y ont été installées, avec un système « hors réseau » fonctionnant uniquement aux énergies renouvelables, et le bureau a été déconnecté du réseau électrique. Ce modèle est progressivement appliqué aux centres de diffusion du Japon lors de leur reconstruction.</p>
<figure><img src="img/rapport-2022-zeb-13.jpg" alt="Page du rapport présentant les bâtiments hors réseau et ZEB" loading="lazy"><figcaption>Page 13 du rapport original</figcaption></figure>
<table class="facts num">
<tr><th>Bâtiment</th><td><b>Production 2022</b></td><td><b>Consommation</b></td><td><b>Revente</b></td></tr>
<tr><th>Bureau dans la forêt <small>(Hokuto, Yamanashi) — hors réseau depuis 2020, batteries de 3 648 kWh</small></th><td>510 087 kWh</td><td>—</td><td>—</td></tr>
<tr><th>Tour de Lumière de Harajuku <small>(Shibuya, Tokyo) — bâtiment historique de l'ancien siège</small></th><td>36 108 kWh</td><td>25 859 kWh <small>(12 615 produits sur place, 13 244 achetés)</small></td><td>23 493 kWh</td></tr>
<tr><th>Media Center <small>(Hokuto, Yamanashi) — relations publiques, édition, studio, galerie</small></th><td>54 000 kWh</td><td>27 161 kWh <small>(11 970 produits sur place, 15 191 achetés)</small></td><td>42 030 kWh</td></tr>
<tr><th>Centre de diffusion de Fukushima <small>(Koriyama) — premier bâtiment hors réseau d'une zone de diffusion, janvier 2020</small></th><td>90 092 kWh</td><td>21 891 kWh</td><td>—</td></tr>
<tr><th>Centre de diffusion d'Ibaraki <small>(Kasama)</small></th><td>68 380 kWh</td><td>25 568 kWh <small>(12 865 produits sur place, 12 703 achetés)</small></td><td>55 515 kWh</td></tr>
</table>
<p>La Tour de Lumière de Harajuku, le Media Center et le centre d'Ibaraki produisent davantage d'énergie qu'ils n'en consomment sur l'année : ce sont des <b>bâtiments à énergie positive (BEPOS)</b>, un niveau supérieur au ZEB.</p>
"""))

# ---------------------------------------------------------------- 2024-04
ARTICLES.append(("communique-2024-04-politique-environnementale.html", "2024-04-16",
"Membre d'une société mondiale : politique de diffusion et politique environnementale de Seicho-No-Ie",
"https://www.seicho-no-ie.org/eng/news/news_202404/", """
<h3>Constat fondamental</h3>
<p>Seicho-No-Ie, fondé en 1930, enseigne la gratitude envers toute chose dans l'univers et affirme que tous les êtres humains sont enfants de Dieu.</p>
<p>Dans sa quête du bonheur, l'humanité a pourtant gravement dégradé l'environnement. Il en résulte le changement climatique, des catastrophes plus fréquentes, la baisse de la production alimentaire, des déplacements de populations et de l'instabilité politique.</p>
<p>Nous pensons que la solution réside dans un état d'esprit religieux : vivre avec la nature. Seicho-No-Ie s'engage à développer un mode de vie qui « grandit avec la nature » et à soutenir les personnes touchées par les catastrophes.</p>

<h3>Lignes d'action</h3>
<ol class="steps">
<li>Faire prendre conscience au personnel que nos enseignements appellent à aimer toute l'humanité et tous les êtres vivants.</li>
<li>Dans toutes nos activités, tenir compte de leurs effets sur les écosystèmes naturels ainsi que sur les traditions et cultures locales.</li>
<li>Réduire notre impact environnemental grâce aux énergies renouvelables, au reboisement et aux véhicules à faibles émissions.</li>
<li>Réduire les déchets, réutiliser et recycler.</li>
<li>Économiser ressources et énergie par la discipline personnelle, et vivre en harmonie avec la nature plutôt que de chercher à la dominer.</li>
<li>Faire des achats éthiques et écologiques : produits locaux, de saison et issus du commerce équitable, dans le respect du bien-être animal et sans travail des enfants.</li>
<li>Respecter les lois, règlements, accords et règles internes en matière d'environnement et d'éthique.</li>
<li>Mettre en place et améliorer en continu un système de management environnemental éthique, chaque département fixant ses propres objectifs.</li>
<li>Rendre cette politique accessible au personnel via un site interne, et au public sur Internet.</li>
</ol>

<table class="facts">
<tr><th>Publication</th><td>11 octobre 2000</td></tr>
<tr><th>Révision des lignes d'action</th><td>5 décembre 2001</td></tr>
<tr><th>Révision du constat et des lignes d'action</th><td>3 avril 2024</td></tr>
<tr><th>Signataire</th><td>Tatsufumi Yukishima, président du conseil et directeur général, personne juridique religieuse « Seicho-No-Ie »</td></tr>
</table>
<p>Ce texte est également disponible en PDF en anglais, portugais, espagnol, chinois et coréen sur le site international.</p>
<div class="todo">Traduction établie à partir d'une version condensée. À comparer mot à mot avec le texte original avant publication, s'agissant d'un document officiel signé.</div>
"""))

# ---------------------------------------------------------------- 2022-04
ARTICLES.append(("communique-2022-04-ukraine.html", "2022-04-18",
"Accueil de personnes évacuées d'Ukraine",
"https://www.seicho-no-ie.org/eng/news/news_202204-01/", """
<p class="lead">Le Siège international de Seicho-No-Ie accueillera des personnes évacuées d'Ukraine ayant subi de lourdes pertes, comme celle de membres de leur famille ou de leur logement, à la suite de l'invasion russe. Nous les accueillerons comme des enfants de Dieu, nos semblables.</p>
<table class="facts">
<tr><th>Capacité d'accueil</th><td>En principe, un foyer.</td></tr>
<tr><th>Condition linguistique</th><td>Au moins un membre du foyer doit maîtriser l'anglais suffisamment pour la vie quotidienne.</td></tr>
<tr><th>Durée</th><td>En principe un an et 90 jours : 90 jours sous statut de visiteur temporaire, puis un an sous statut d'« activités désignées », qui autorise le travail et donne accès à l'assurance maladie nationale.</td></tr>
<tr><th>Soutien apporté</th><td>Un logement meublé, les produits de première nécessité, les frais de voyage jusqu'au Japon, ainsi que les transports et l'hébergement sur place.</td></tr>
<tr><th>Contact</th><td>Section des affaires internationales, Département des affaires générales, Siège international de Seicho-No-Ie<br>Tél. : +81 (0)551-45-7777<br>E-mail : <a href="mailto:xbl14447@nifty.com">xbl14447@nifty.com</a></td></tr>
</table>
<div class="note">Ce communiqué date d'avril 2022. Vérifiez auprès du Siège international si cette offre est toujours d'actualité.</div>
"""))
