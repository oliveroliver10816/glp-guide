#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds the GLP-1 category guide in 9 locales.
Every keyword string below came from a live google.<cctld>/complete/search?client=chrome pull
(2026-07-22) — the copy is built ON the real queries, not invented.
"""
import os, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://oliveroliver10816.github.io/glp-guide"
UPDATED = "2026-07-22"

# ---------------------------------------------------------------- products
# key -> (display name, url per locale)
P = {
  "ozem":   "Ozem+",
  "ozalyn": "Ozalyn",
  "retafit": "RetaFit",
  "glpure": "GLPure",
}

LOCALES = {}

# ============================== DE ==============================
LOCALES["de"] = dict(
  lang="de", path="", hreflang=["de","de-AT","de-CH"],
  title="Ozempic-Alternative als Tablette? GLP-1 Kapseln 2026 im Überblick",
  desc="Rezeptfreie Ozempic-Alternativen &amp; GLP-1 Kapseln 2026 im Überblick: Ozem+, Ozalyn, RetaFit, GLPure — ehrlich eingeordnet. Keine Spritze, kein Rezept.",
  brandline="Kapsel-Kompass · unabhängiger Marktüberblick",
  eyebrow="GLP-1 &amp; Ozempic-Alternativen · 2026",
  h1a="Ozempic-Alternative als Tablette?", h1b="Die rezeptfreien GLP-1 Kapseln 2026 im Überblick",
  lede="„Ozempic Tabletten“, „Wegovy Alternative rezeptfrei“, „GLP-1 Kapseln“, „Abnehmtabletten statt Spritze“ — diese Suchbegriffe explodieren gerade. Wir ordnen ein, welche rezeptfreien Kapseln dahinterstecken, was sie kosten und wo es sie wirklich gibt.",
  updated="Zuletzt aktualisiert", readtime="Lesezeit ca. 6 Minuten",
  toc="Direkt zu einem Produkt", toc_faq="Häufige Fragen",
  intro="Seit <b>Retatrutid</b> und die Abnehmspritzen <b>Ozempic</b>, <b>Wegovy</b> und <b>Mounjaro</b> in den Schlagzeilen sind, suchen täglich Zehntausende nach einer <b>Ozempic-Alternative als Tablette</b> — rezeptfrei, ohne Spritze, ohne Arztbesuch. Wichtig vorweg: <b>Die Spritzen selbst sind verschreibungspflichtig und nicht rezeptfrei zu haben.</b> Was es rezeptfrei gibt, sind <b>Nahrungsergänzungsmittel in Kapselform</b> mit Inhaltsstoffen wie Niacin, Grüntee, Berberin oder Chrom. Sie sind keine Medikamente.",
  tvtitle="Ein Hinweis, der für alle gilt", tvshow="Die Höhle der Löwen",
  tv="In der <b>Höhle der Löwen</b> wurde nie ein Abnehmprodukt vorgestellt. Jede Anzeige, die einen TV-Auftritt oder ein Jury-Investment behauptet — für welche Kapsel auch immer — ist eine Fälschung. Kauf nie über solche Anzeigen, sondern nur über den offiziellen Shop der Marke.",
  h_vs="Tabletten oder Spritze — was ist der Unterschied?",
  vs="Die meistgestellte Frage ist <b>„Ozempic Tabletten oder Spritze“</b>. Der Unterschied ist grundsätzlich: Ozempic und Wegovy sind verschreibungspflichtige <b>Injektionen</b> mit dem Wirkstoff Semaglutid. Rezeptfreie <b>GLP-1 Kapseln</b> sind Nahrungsergänzungsmittel — sie enthalten kein Semaglutid und wirken nicht wie ein Medikament. Wer „<b>Ozempic Tabletten kaufen</b>“ sucht, findet rezeptfrei ausschließlich Nahrungsergänzung.",
  h_buy="Gibt es die Kapseln in Apotheke, dm oder Rossmann?",
  buy="Kurz: nein. Suchanfragen wie <b>„Abnehmtabletten Apotheke“</b>, <b>„GLP-1 Kapseln dm“</b> oder <b>„Abnehmtabletten Rossmann“</b> laufen ins Leere — die hier gelisteten Marken werden ausschließlich über ihren <b>eigenen offiziellen Online-Shop</b> verkauft. Auch bei Amazon, Temu oder „Gutschein“-Seiten von Drittanbietern gibt es sie nicht; dort drohen Fälschungen ohne Garantie.",
  h_cost="Was kosten rezeptfreie GLP-1 Kapseln?",
  cost="Die Preise liegen je nach Marke bei rund <b>40 bis 75 Euro pro Einzelflasche</b>, mit deutlichen Rabatten in Mehrfach-Paketen — der Rabatt steckt im Paket, offizielle Gutscheincodes gibt es in der Regel nicht. Fast immer handelt es sich um einen <b>Einmalkauf ohne Abo</b>, oft mit einer 30-Tage-Geld-zurück-Garantie. Verbindliche Preise stehen nur im jeweiligen offiziellen Shop.",
  h_safe="Nebenwirkungen und wer sie nicht nehmen sollte",
  safe="Weil es Nahrungsergänzungsmittel sind, sind die Zutaten deklariert und meist gut verträglich. Die meisten Formeln enthalten jedoch <b>Koffein</b> (Grüntee, Guarana) — nicht geeignet für Kinder, Schwangere und Stillende oder bei Koffein-Empfindlichkeit. Wer Medikamente nimmt oder Vorerkrankungen hat, sollte vor der Einnahme ärztlich abklären. Ein Nahrungsergänzungsmittel ersetzt keine ausgewogene Ernährung.",
  summary="<b>Kurz zusammengefasst:</b> Wer nach einer <b>Ozempic-Alternative in Tablettenform</b>, <b>rezeptfreien GLP-1 Kapseln</b> oder <b>Abnehmtabletten statt Spritze</b> sucht, findet rezeptfrei nur Nahrungsergänzungsmittel — keine Medikamente. Miss sie an Inhaltsstoffen, transparenten Preisen und Geld-zurück-Garantie, nicht an TV-Gerüchten.",
  h_faq="Häufige Fragen", shopcta="Zum offiziellen {} Shop", langlabel="Sprache",
  disc='Dieser Überblick dient der Information und ist keine medizinische Beratung. Die genannten Produkte sind Nahrungsergänzungsmittel und kein Ersatz für eine ärztliche Behandlung oder verschreibungspflichtige Medikamente. „Ozempic“, „Wegovy“, „Mounjaro“ und „Die Höhle der Löwen“ sind Marken der jeweiligen Rechteinhaber; es besteht keine Verbindung. Diese Seite kann eine Provision für Bestellungen über die verlinkten offiziellen Shops erhalten, ohne Mehrkosten für dich. Stand: Juli 2026.',
  products=[
    ("ozem","https://ozem-plus.store/","DE · AT · CH · IT · PL · NL",
     "ozem plus erfahrungen · ozem plus kaufen · ozem plus kapseln · ozem plus fake oder echt · ozem plus seriös · ozem plus preis · ozem plus dm",
     "Ozem+ ist derzeit die meistgesuchte rezeptfreie Kapsel dieser Liste — vor allem im deutschsprachigen Raum. Rund um Ozem+ häufen sich Fragen wie „ozem plus erfahrungen“, „ozem plus fake oder echt“ und „ozem plus seriös“: typische Zeichen dafür, dass Menschen vor dem Kauf Sicherheit suchen. Ozem+ ist ein <b>Nahrungsergänzungsmittel als natürliche Ozempic-Alternative</b>, kein Medikament, und wird als Einmalkauf mit Paketrabatten verkauft — nicht in Apotheke, dm oder Rossmann, sondern nur im offiziellen Shop."),
    ("ozalyn","https://osanix.shop/de/","UK · DE · AT · NL · BE · DK · SE",
     "ozalyn kapseln erfahrungen · ozalyn kaufen · ozalyn bewertungen · ozalyn kapseln inhaltsstoffe · ozalyn einnahme · ozalyn trustpilot",
     "Ozalyn wird in mehr Ländern gesucht als die meisten Wettbewerber — von Großbritannien über die DACH-Region bis Benelux und Skandinavien. Gefragt sind vor allem „ozalyn kapseln erfahrungen“, „ozalyn inhaltsstoffe“ und „ozalyn einnahme“: Menschen wollen wissen, was drin ist und wie man es nimmt. Ozalyn ist ebenfalls ein <b>rezeptfreies Kapsel-Präparat zur Stoffwechsel-Unterstützung</b> und keine Abnehmspritze."),
    ("retafit","https://tryretafit.com/de/","DE · AT · CH · UK · DK · NO · FR",
     "reta fit · reta 3 · reta abnehmen · retafit erfahrungen · reta tabletten · retatrutide alternative · reta kosten",
     "RetaFit ist die jüngste Marke dieser Liste und reitet auf dem Hype um den Wirkstoff <b>Retatrutid</b> („reta“). Gesucht wird nach „reta fit“, „reta abnehmen“ und — durch eine Namensverwechslung mit einem anderen Produkt — auch nach „reta 3“. Wichtig: <b>RetaFit ist nicht der Wirkstoff Retatrutid</b>, sondern eine rezeptfreie Kapsel mit Niacin, Grüntee, Guarana und N-Acetyl-L-Carnitin.",
     ("https://tryretafit.com/de/reta-3/","Reta 3 vs. RetaFit erklärt")),
    ("glpure","https://glpure.shop/de/","EU · international",
     "glpure · glpure reviews · glpure glp 1 · glp-1 kapseln kaufen · glp-1 supplement",
     "GLPure spricht direkt die Suche nach „glp-1 supplement“ und „glp-1 kapseln“ an. Die Marke ist kleiner und weniger gesucht als Ozem+ oder Ozalyn, taucht aber zuverlässig bei „glpure reviews“ und „glpure glp 1“ auf. Auch hier gilt: rezeptfreies Nahrungsergänzungsmittel, keine Spritze, kein Rezept."),
  ],
  faq=[
    ("Gibt es eine Ozempic-Alternative als Tablette ohne Rezept?",
     "Ozempic (Semaglutid) und Wegovy sind verschreibungspflichtige Injektionen und als solche nicht rezeptfrei erhältlich. Was rezeptfrei existiert, sind Nahrungsergänzungsmittel in Kapselform, die als natürliche Ozempic-Alternative beworben werden — etwa Ozem+, Ozalyn, RetaFit oder GLPure. Sie sind keine Medikamente und ersetzen keine ärztliche Behandlung; sie unterstützen den Stoffwechsel über Inhaltsstoffe wie Niacin, Grüntee, Berberin oder Chrom."),
    ("Waren diese Kapseln in der Höhle der Löwen?",
     "Nein. In der gesamten Geschichte von Die Höhle der Löwen wurde nie ein Abnehmprodukt vorgestellt. Jede Anzeige, die einen Auftritt in der Show oder ein Investment der Jury behauptet — egal für welche Kapsel — ist eine Fälschung. Die Verbraucherzentrale und das Portal Mimikama warnen seit Jahren vor diesem Muster."),
    ("Was kosten rezeptfreie GLP-1 Kapseln?",
     "Die Preise liegen je nach Marke bei rund 40 bis 75 Euro pro Einzelflasche, mit deutlichen Rabatten in Mehrfach-Paketen. Es handelt sich fast immer um einen Einmalkauf ohne Abo, oft mit einer 30-Tage-Geld-zurück-Garantie. Konkrete Preise findest du nur im jeweiligen offiziellen Shop."),
    ("Wo kann man Ozem+, Ozalyn oder RetaFit kaufen?",
     "Diese Marken werden nicht in Apotheke, dm oder Rossmann verkauft, sondern ausschließlich über ihren jeweiligen offiziellen Online-Shop. Nur dort gibt es die Original-Formel, die offiziellen Paketpreise und die Geld-zurück-Garantie. Vorsicht bei Amazon-, Temu- oder Gutschein-Seiten von Drittanbietern."),
    ("Ozempic Tabletten oder Spritze — was ist der Unterschied?",
     "Ozempic und Wegovy sind verschreibungspflichtige Injektionen mit dem Wirkstoff Semaglutid. Rezeptfreie GLP-1 Kapseln sind Nahrungsergänzungsmittel ohne Semaglutid und wirken nicht wie ein Medikament. Eine rezeptfreie Tablette mit dem Wirkstoff der Spritze gibt es nicht."),
    ("Haben GLP-1 Kapseln Nebenwirkungen?",
     "Die meisten Formeln enthalten Koffein aus Grüntee oder Guarana und sind deshalb nicht geeignet für Kinder, Schwangere, Stillende oder bei Koffein-Empfindlichkeit. Wer Medikamente einnimmt oder Vorerkrankungen hat, sollte die Einnahme vorher ärztlich abklären."),
    ("Gibt es einen Gutschein- oder Rabattcode?",
     "In der Regel nicht. Der Rabatt steckt direkt in den Mehrfach-Paketen des offiziellen Shops. Seiten, die angebliche Gutscheincodes anbieten, führen meist nur zu Werbelinks ohne gültigen Code."),
    ("Wie schnell wirken rezeptfreie GLP-1 Kapseln?",
     "Nahrungsergänzungsmittel wirken nicht wie ein Medikament und liefern keine garantierten Ergebnisse. Sie sind als tägliche Routine über mehrere Wochen gedacht, begleitend zu ausgewogener Ernährung und Bewegung."),
  ],
)

# ============================== EN ==============================
LOCALES["en"] = dict(
  lang="en", path="en", hreflang=["en","en-GB"],
  title="Ozempic Alternative Pills? GLP-1 Supplements 2026 Compared",
  desc="Over-the-counter Ozempic alternatives &amp; GLP-1 supplements in 2026: Ozalyn, RetaFit and GLPure — honestly explained. No injection, no prescription.",
  brandline="Capsule Compass · independent market overview",
  eyebrow="GLP-1 &amp; Ozempic alternatives · 2026",
  h1a="Ozempic alternative in pill form?", h1b="The over-the-counter GLP-1 supplements of 2026",
  lede="“Ozempic pills”, “weight loss pills that work”, “GLP-1 supplements UK”, “natural Ozempic alternatives” — these searches are climbing fast. Here is what the over-the-counter capsules behind them actually are, what they cost, and where you can genuinely buy them.",
  updated="Last updated", readtime="6 min read",
  toc="Jump to a product", toc_faq="FAQ",
  intro="Since <b>retatrutide</b> and the weight-loss injections <b>Ozempic</b>, <b>Wegovy</b> and <b>Mounjaro</b> hit the headlines, tens of thousands of people search every day for an <b>Ozempic alternative in pill form</b> — over the counter, no injection, no doctor. First, the important part: <b>the injections themselves are prescription-only and are not available over the counter.</b> What does exist over the counter are <b>food supplements in capsule form</b> using ingredients such as niacin, green tea, berberine or chromium. They are not medicines.",
  tvtitle="One note that applies to all of them", tvshow="Dragons' Den",
  tv="No weight-loss product has ever been backed on <b>Dragons' Den</b>. Any advert claiming a TV appearance or an investor deal — for any capsule — is fake. Never buy through those adverts; use the brand's official shop only.",
  h_vs="Ozempic pills vs injection — what is the difference?",
  vs="The most common question is <b>“Ozempic pills vs injection”</b>. The difference is fundamental: Ozempic and Wegovy are prescription <b>injections</b> containing semaglutide. Over-the-counter <b>GLP-1 supplements</b> are food supplements — they contain no semaglutide and do not work like a drug. If you are searching “<b>ozempic pills online</b>” or “<b>ozempic pills cost</b>”, what is actually available without a prescription is supplements.",
  h_buy="Can you buy them in Boots, Holland &amp; Barrett or on Amazon?",
  buy="In short: no. Searches like <b>“glp-1 supplement Boots”</b>, <b>“glp-1 supplement Holland and Barrett”</b> or <b>“natural ozempic amazon”</b> lead nowhere — the brands listed here are sold exclusively through their <b>own official online shop</b>. They are not stocked by high-street chains, and third-party marketplace or “discount code” pages risk counterfeits with no guarantee.",
  h_cost="What do over-the-counter GLP-1 supplements cost?",
  cost="Expect roughly <b>£40 to £75 per single bottle</b> depending on the brand, with substantial savings on multi-bottle bundles — the discount sits in the bundle, and official voucher codes generally do not exist. It is almost always a <b>one-time purchase with no subscription</b>, usually with a 30-day money-back guarantee. Binding prices appear only in each official shop.",
  h_safe="Side effects and who should avoid them",
  safe="Because these are food supplements the ingredients are declared and generally well tolerated. Most formulas do contain <b>caffeine</b> (green tea, guarana), so they are not suitable for children, pregnant or breastfeeding women, or anyone sensitive to caffeine. If you take medication or have a pre-existing condition, check with your doctor first. A supplement does not replace a balanced diet.",
  summary="<b>In short:</b> if you are looking for <b>Ozempic alternatives for weight loss</b>, <b>GLP-1 supplements that work</b> or <b>weight loss pills over the counter</b>, what is genuinely available without a prescription is food supplements — not medicines. Judge them on their ingredients, transparent pricing and money-back guarantee, not on TV rumours.",
  h_faq="Frequently asked questions", shopcta="Go to the official {} shop", langlabel="Language",
  disc='This overview is for information only and is not medical advice. The products mentioned are food supplements and are not a substitute for medical treatment or prescription medicines. “Ozempic”, “Wegovy”, “Mounjaro” and “Dragons\' Den” are trademarks of their respective owners; no affiliation is implied. This page may earn a commission on orders placed through the linked official shops, at no extra cost to you. Last reviewed: July 2026.',
  products=[
    ("ozalyn","https://osanix.shop/","UK · DE · AT · NL · BE · DK · SE",
     "ozalyn ingredients · ozalyn uk · ozalyn supplements · ozalyn trustpilot · ozalyn side effects · ozalyn reviews",
     "Ozalyn is the most-searched brand of this group in the UK. The questions people ask — “ozalyn ingredients”, “ozalyn side effects”, “ozalyn trustpilot” — are the classic pre-purchase checks: what is in it, is it safe, can I trust it. Ozalyn is an <b>over-the-counter capsule supplement for metabolic support</b>, not a weight-loss injection, sold as a one-time purchase through its official shop only."),
    ("retafit","https://tryretafit.com/","UK · DE · AT · CH · DK · NO · FR",
     "retafit · reta fit · retafit reviews · retafit tablets · reta pills · retatrutide alternative",
     "RetaFit is the newest brand here and rides the attention around the drug candidate <b>retatrutide</b> (“reta”). People search “reta fit”, “retafit reviews” and “retafit tablets”. The key point: <b>RetaFit is not retatrutide</b> — it is an over-the-counter capsule with niacin, green tea, guarana and N-acetyl-L-carnitine, sold in five countries with a 30-day money-back guarantee.",
     ("https://tryretafit.com/dragons-den/","RetaFit &amp; Dragons' Den — the facts")),
    ("glpure","https://glpure.shop/","EU · international",
     "glpure · glpure reviews · glpure glp 1 · glp-1 supplement tablets · glp-1 supplements that work",
     "GLPure targets the English-language search for “glp-1 supplement” and “glp-1 supplement tablets” head-on. It is a smaller brand than Ozalyn, but shows up consistently for “glpure reviews” and “glpure glp 1”. Same category rules apply: an over-the-counter food supplement, no injection, no prescription, official shop only."),
  ],
  faq=[
    ("Is there an Ozempic alternative in pill form without a prescription?",
     "Ozempic (semaglutide) and Wegovy are prescription-only injections and are not available over the counter. What does exist over the counter are food supplements in capsule form marketed as natural Ozempic alternatives — such as Ozalyn, RetaFit or GLPure. They are not medicines and do not replace medical treatment; they support metabolism through ingredients such as niacin, green tea, berberine or chromium."),
    ("Were these capsules on Dragons' Den?",
     "No. No weight-loss product has ever been backed on Dragons' Den. Any advert claiming an appearance on the show or an investment from the panel — for any capsule — is fake. Buy only through the brand's official shop."),
    ("Ozempic pills vs injection — what is the difference?",
     "Ozempic and Wegovy are prescription injections containing semaglutide. Over-the-counter GLP-1 supplements are food supplements without semaglutide and do not work like a drug. There is no over-the-counter tablet containing the injection's active ingredient."),
    ("What do GLP-1 supplements cost?",
     "Roughly £40 to £75 per single bottle depending on the brand, with significant savings on multi-bottle bundles. It is almost always a one-time purchase with no subscription, usually covered by a 30-day money-back guarantee. Exact prices are shown only in each official shop."),
    ("Can I buy them at Boots, Holland &amp; Barrett or on Amazon?",
     "No. These brands are sold exclusively through their own official online shops, not through high-street chains or marketplaces. Third-party listings risk counterfeit products sold without the official guarantee."),
    ("Do GLP-1 supplements have side effects?",
     "Most formulas contain caffeine from green tea or guarana, so they are not suitable for children, pregnant or breastfeeding women, or anyone sensitive to caffeine. If you take medication or have a pre-existing condition, speak to your doctor before starting."),
    ("Is there a discount or voucher code?",
     "Usually not. The discount is built into the multi-bottle bundles in the official shop. Sites offering supposed voucher codes generally just lead to advertising links with no working code."),
    ("How quickly do they work?",
     "Food supplements do not work like medicines and cannot promise results. They are designed as a daily routine over several weeks alongside a balanced diet and regular activity."),
  ],
)

# ============================== FR ==============================
LOCALES["fr"] = dict(
  lang="fr", path="fr", hreflang=["fr","fr-BE"],
  title="Alternative à l'Ozempic sans ordonnance ? Gélules GLP-1 2026",
  desc="Alternatives à l'Ozempic sans ordonnance et compléments GLP-1 en 2026 : Ozem+, RetaFit, Ozalyn, GLPure — expliqués honnêtement. Sans piqûre, sans ordonnance.",
  brandline="Boussole Gélules · panorama indépendant du marché",
  eyebrow="GLP-1 &amp; alternatives à l'Ozempic · 2026",
  h1a="Une alternative à l'Ozempic en gélules ?", h1b="Le panorama 2026 des compléments GLP-1 sans ordonnance",
  lede="« alternative ozempic sans ordonnance », « pilule minceur efficace », « complément alimentaire GLP-1 », « médicament pour perdre du poids sans ordonnance » — ces recherches explosent. Voici ce que sont réellement les gélules concernées, leur prix, et où on peut vraiment les acheter.",
  updated="Dernière mise à jour", readtime="6 min de lecture",
  toc="Aller à un produit", toc_faq="Questions fréquentes",
  intro="Depuis que le <b>rétatrutide</b> et les injections amincissantes <b>Ozempic</b>, <b>Wegovy</b> et <b>Mounjaro</b> font la une, des dizaines de milliers de personnes cherchent chaque jour une <b>alternative à l'Ozempic en comprimés</b> — sans ordonnance, sans piqûre, sans rendez-vous médical. Précision essentielle : <b>les injections sont soumises à prescription et ne s'obtiennent pas sans ordonnance.</b> Ce qui existe sans ordonnance, ce sont des <b>compléments alimentaires en gélules</b> à base de niacine, thé vert, berbérine ou chrome. Ce ne sont pas des médicaments.",
  tvtitle="Un avertissement valable pour toutes les marques", tvshow="Qui veut être mon associé",
  tv="Aucun produit minceur n'a jamais été validé dans <b>Qui veut être mon associé</b>. Toute publicité affirmant un passage à la télévision ou un investissement d'un jury — pour n'importe quelle gélule — est un faux. N'achetez jamais via ces publicités, uniquement via la boutique officielle de la marque.",
  h_vs="Gélules ou injection — quelle différence ?",
  vs="La question la plus posée est <b>« ozempic gélules avis »</b> ou comprimés contre piqûre. La différence est fondamentale : l'Ozempic et le Wegovy sont des <b>injections</b> sur ordonnance contenant du sémaglutide. Les <b>gélules GLP-1</b> sans ordonnance sont des compléments alimentaires — elles ne contiennent pas de sémaglutide et n'agissent pas comme un médicament. Il n'existe pas de comprimé sans ordonnance contenant la substance active de l'injection.",
  h_buy="Peut-on les acheter en pharmacie ou sur Amazon ?",
  buy="Non. Les recherches du type <b>« pilule minceur efficace en pharmacie »</b> n'aboutissent pas pour ces marques : elles sont vendues <b>exclusivement via leur propre boutique officielle en ligne</b>. Ni pharmacie, ni parapharmacie, ni Amazon ou Temu. Les pages proposant de prétendus « codes promo » renvoient généralement vers de simples liens publicitaires.",
  h_cost="Combien coûtent les gélules GLP-1 sans ordonnance ?",
  cost="Comptez environ <b>40 à 75 € le flacon à l'unité</b> selon la marque, avec des remises importantes sur les lots de plusieurs flacons — la remise est dans le lot, il n'y a généralement pas de code promo officiel. Il s'agit presque toujours d'un <b>achat unique sans abonnement</b>, souvent assorti d'une garantie satisfait ou remboursé de 30 jours. Les prix fermes ne figurent que dans la boutique officielle.",
  h_safe="Effets indésirables et contre-indications",
  safe="Ce sont des compléments alimentaires : les ingrédients sont déclarés et généralement bien tolérés. La plupart des formules contiennent toutefois de la <b>caféine</b> (thé vert, guarana) — déconseillées aux enfants, aux femmes enceintes ou allaitantes et aux personnes sensibles à la caféine. En cas de traitement ou de pathologie, demandez un avis médical avant toute prise. Un complément ne remplace pas une alimentation équilibrée.",
  summary="<b>En résumé :</b> si vous cherchez une <b>alternative à l'Ozempic sans ordonnance</b>, une <b>pilule minceur</b> ou un <b>complément GLP-1</b>, ce qui est réellement disponible sans ordonnance ce sont des compléments alimentaires — pas des médicaments. Jugez-les sur leurs ingrédients, la transparence des prix et la garantie, pas sur des rumeurs télévisées.",
  h_faq="Questions fréquentes", shopcta="Voir la boutique officielle {}", langlabel="Langue",
  disc="Ce panorama est fourni à titre informatif et ne constitue pas un avis médical. Les produits cités sont des compléments alimentaires et ne remplacent ni un traitement médical ni un médicament sur ordonnance. « Ozempic », « Wegovy », « Mounjaro » et « Qui veut être mon associé » sont des marques de leurs détenteurs respectifs ; aucune affiliation n'est sous-entendue. Cette page peut percevoir une commission sur les commandes passées via les boutiques officielles liées, sans surcoût pour vous. Mise à jour : juillet 2026.",
  products=[
    ("ozem","https://ozem-plus.store/","DE · AT · CH · IT · PL · NL · FR",
     "ozem plus avis · ozem plus test · ozem plus glp 1 · ozem plus review · ozem plus tabletten",
     "Ozem+ est la gélule sans ordonnance la plus recherchée de cette liste en Europe. Les requêtes « ozem plus avis » et « ozem plus test » dominent : les gens cherchent une confirmation avant d'acheter. Ozem+ est un <b>complément alimentaire présenté comme alternative naturelle à l'Ozempic</b>, pas un médicament, vendu en achat unique avec des remises par lot, uniquement dans sa boutique officielle."),
    ("retafit","https://tryretafit.com/fr/","FR · DE · AT · CH · UK · DK · NO",
     "retafit avis · reta gélules · reta perte de poids · rétatrutide alternative · reta comprimés",
     "RetaFit est la marque la plus récente et surfe sur l'attention portée au <b>rétatrutide</b> (« reta »). Point important : <b>RetaFit n'est pas du rétatrutide</b>, mais une gélule sans ordonnance à base de niacine, thé vert, guarana et N-acétyl-L-carnitine. Vendue dans cinq pays, en achat unique, avec une garantie satisfait ou remboursé de 30 jours.",
     ("https://tryretafit.com/fr/qui-veut-etre-mon-associe/","RetaFit &amp; QVEMA — les faits")),
    ("ozalyn","https://osanix.shop/fr/","UK · DE · AT · NL · BE · DK · SE",
     "ozalyn capsules avis · ozalyn avis · ozalyn capsules · ozalyn trustpilot",
     "Ozalyn est recherchée dans de nombreux pays européens, notamment via « ozalyn capsules avis » et « ozalyn avis ». Comme les autres, il s'agit d'un <b>complément en gélules pour le soutien du métabolisme</b>, sans ordonnance, vendu exclusivement via sa boutique officielle avec ses prix par lot."),
    ("glpure","https://glpure.shop/fr/","UE · international",
     "glpure avis · glpure glp 1 · complément alimentaire glp 1 · supplément glp 1",
     "GLPure cible directement la recherche « complément alimentaire glp 1 » et « supplément glp 1 ». Marque plus confidentielle que Ozem+ ou Ozalyn, elle apparaît régulièrement sur « glpure avis ». Mêmes règles : complément alimentaire sans ordonnance, pas d'injection, boutique officielle uniquement."),
  ],
  faq=[
    ("Existe-t-il une alternative à l'Ozempic sans ordonnance ?",
     "L'Ozempic (sémaglutide) et le Wegovy sont des injections soumises à prescription et ne sont pas disponibles sans ordonnance. Ce qui existe sans ordonnance, ce sont des compléments alimentaires en gélules présentés comme alternatives naturelles à l'Ozempic — comme Ozem+, RetaFit, Ozalyn ou GLPure. Ce ne sont pas des médicaments et ils ne remplacent aucun traitement ; ils soutiennent le métabolisme via des ingrédients comme la niacine, le thé vert, la berbérine ou le chrome."),
    ("Ces gélules sont-elles passées dans Qui veut être mon associé ?",
     "Non. Aucun produit minceur n'a jamais été validé dans l'émission. Toute publicité affirmant un passage à la télévision ou un investissement d'un jury — pour n'importe quelle gélule — est un faux. Achetez uniquement via la boutique officielle de la marque."),
    ("Gélules ou injection : quelle différence ?",
     "L'Ozempic et le Wegovy sont des injections sur ordonnance contenant du sémaglutide. Les gélules GLP-1 sans ordonnance sont des compléments alimentaires sans sémaglutide, qui n'agissent pas comme un médicament. Aucun comprimé sans ordonnance ne contient la substance active de l'injection."),
    ("Combien coûtent ces gélules ?",
     "Environ 40 à 75 € le flacon à l'unité selon la marque, avec des remises importantes sur les lots. Il s'agit presque toujours d'un achat unique sans abonnement, souvent avec une garantie satisfait ou remboursé de 30 jours. Les prix exacts ne figurent que dans la boutique officielle."),
    ("Peut-on les acheter en pharmacie ou sur Amazon ?",
     "Non. Ces marques sont vendues exclusivement via leur propre boutique officielle en ligne, ni en pharmacie ni sur les marketplaces. Les annonces de tiers exposent à des contrefaçons sans garantie."),
    ("Y a-t-il des effets indésirables ?",
     "La plupart des formules contiennent de la caféine issue du thé vert ou du guarana : elles sont déconseillées aux enfants, aux femmes enceintes ou allaitantes et aux personnes sensibles à la caféine. En cas de traitement ou de pathologie, demandez un avis médical avant toute prise."),
    ("Existe-t-il un code promo ?",
     "En général non. La remise est intégrée aux lots de plusieurs flacons dans la boutique officielle. Les sites annonçant des codes promo renvoient le plus souvent vers de simples liens publicitaires."),
    ("En combien de temps agissent-elles ?",
     "Les compléments alimentaires n'agissent pas comme des médicaments et ne garantissent aucun résultat. Ils sont conçus comme une routine quotidienne sur plusieurs semaines, en complément d'une alimentation équilibrée et d'une activité régulière."),
  ],
)

# ============================== IT ==============================
LOCALES["it"] = dict(
  lang="it", path="it", hreflang=["it"],
  title="Alternativa a Ozempic in pastiglie? Integratori GLP-1 2026",
  desc="Alternative a Ozempic senza ricetta e integratori GLP-1 nel 2026: Ozem+ e GLPure spiegati onestamente. Niente puntura, niente ricetta.",
  brandline="Bussola Capsule · panoramica indipendente del mercato",
  eyebrow="GLP-1 &amp; alternative a Ozempic · 2026",
  h1a="Alternativa a Ozempic in pastiglie?", h1b="La panoramica 2026 degli integratori GLP-1 senza ricetta",
  lede="« alternativa ozempic per dimagrire », « ozempic pastiglie prezzo », « pillole dimagranti efficaci », « integratore glp 1 per dimagrire » — sono tra le ricerche in più rapida crescita. Ecco che cosa sono davvero queste capsule, quanto costano e dove si acquistano realmente.",
  updated="Ultimo aggiornamento", readtime="6 min di lettura",
  toc="Vai a un prodotto", toc_faq="Domande frequenti",
  intro="Da quando la <b>retatrutide</b> e le iniezioni dimagranti <b>Ozempic</b>, <b>Wegovy</b> e <b>Mounjaro</b> sono finite sui giornali, ogni giorno decine di migliaia di persone cercano un'<b>alternativa a Ozempic in pastiglie</b> — senza ricetta, senza puntura, senza visita medica. Chiariamo subito: <b>le iniezioni sono farmaci con obbligo di ricetta e non si comprano liberamente.</b> Ciò che esiste senza ricetta sono <b>integratori alimentari in capsule</b> con ingredienti come niacina, tè verde, berberina o cromo. Non sono medicinali.",
  tvtitle="Un avviso valido per tutti i marchi", tvshow=None,
  tv="Nessun prodotto dimagrante è mai stato approvato o finanziato in un programma televisivo di investitori. Ogni pubblicità che dichiara un passaggio in TV o l'investimento di un personaggio noto — per qualunque capsula — è falsa. Non acquistare mai tramite quelle pubblicità, ma solo dallo shop ufficiale del marchio.",
  h_vs="Pastiglie o iniezione — qual è la differenza?",
  vs="La domanda più frequente riguarda <b>« ozempic pastiglie »</b> contro la puntura. La differenza è sostanziale: Ozempic e Wegovy sono <b>iniezioni</b> con obbligo di ricetta a base di semaglutide. Gli <b>integratori GLP-1</b> senza ricetta sono integratori alimentari — non contengono semaglutide e non agiscono come un farmaco. Non esiste una pastiglia senza ricetta con il principio attivo dell'iniezione.",
  h_buy="Si trovano in farmacia o su Amazon?",
  buy="No. Ricerche come <b>« pillole dimagranti in farmacia »</b> o <b>« ozempic pastiglie amazon »</b> non portano a questi marchi: sono venduti <b>esclusivamente tramite il proprio shop ufficiale online</b>. Né farmacia, né parafarmacia, né Amazon o Temu. Le pagine che promettono « codici sconto » rimandano quasi sempre a semplici link pubblicitari.",
  h_cost="Quanto costano gli integratori GLP-1?",
  cost="Il prezzo si aggira sui <b>40–75 € a flacone singolo</b> a seconda del marchio, con sconti consistenti sulle confezioni multiple — lo sconto è nel pacchetto e di norma non esistono codici promozionali ufficiali. Si tratta quasi sempre di un <b>acquisto unico senza abbonamento</b>, spesso con garanzia soddisfatti o rimborsati di 30 giorni. I prezzi vincolanti sono solo nello shop ufficiale.",
  h_safe="Effetti collaterali e controindicazioni",
  safe="Essendo integratori alimentari, gli ingredienti sono dichiarati e in genere ben tollerati. La maggior parte delle formule contiene però <b>caffeina</b> (tè verde, guaranà): sconsigliate a bambini, donne in gravidanza o allattamento e a chi è sensibile alla caffeina. In caso di terapie in corso o patologie, sentire il medico prima dell'uso. Un integratore non sostituisce un'alimentazione equilibrata.",
  summary="<b>In sintesi:</b> chi cerca un'<b>alternativa a Ozempic per dimagrire</b>, <b>pillole dimagranti senza ricetta</b> o un <b>integratore GLP-1</b> trova senza ricetta soltanto integratori alimentari — non medicinali. Valutali su ingredienti, trasparenza dei prezzi e garanzia, non su voci televisive.",
  h_faq="Domande frequenti", shopcta="Vai allo shop ufficiale {}", langlabel="Lingua",
  disc="Questa panoramica ha scopo informativo e non costituisce un consiglio medico. I prodotti citati sono integratori alimentari e non sostituiscono trattamenti medici o farmaci con obbligo di ricetta. « Ozempic », « Wegovy » e « Mounjaro » sono marchi dei rispettivi titolari; non è sottintesa alcuna affiliazione. Questa pagina può ricevere una commissione sugli ordini effettuati tramite gli shop ufficiali collegati, senza costi aggiuntivi per te. Aggiornamento: luglio 2026.",
  products=[
    ("ozem","https://ozem-plus.store/it/","IT · DE · AT · CH · PL · NL",
     "ozem plus recensioni · ozem plus opinioni · ozem plus glp 1 · ozem plus prezzo",
     "Ozem+ è la capsula senza ricetta più cercata di questa panoramica in Europa ed è disponibile in italiano. Le domande ricorrenti — « recensioni », « opinioni », « funziona » — sono i tipici controlli prima dell'acquisto. Ozem+ è un <b>integratore alimentare proposto come alternativa naturale a Ozempic</b>, non un farmaco, venduto con acquisto unico e sconti sulle confezioni multiple, solo nello shop ufficiale."),
    ("glpure","https://glpure.shop/it/","UE · internazionale",
     "glpure recensioni · glpure glp 1 · integratore glp 1 per dimagrire · miglior integratore glp 1",
     "GLPure punta direttamente sulla ricerca « integratore glp 1 » e « miglior integratore glp 1 ». È un marchio più piccolo di Ozem+, ma compare con regolarità nelle ricerche « glpure recensioni ». Valgono le stesse regole: integratore alimentare senza ricetta, nessuna iniezione, solo shop ufficiale."),
  ],
  faq=[
    ("Esiste un'alternativa a Ozempic senza ricetta?",
     "Ozempic (semaglutide) e Wegovy sono iniezioni con obbligo di ricetta e non sono acquistabili liberamente. Ciò che esiste senza ricetta sono integratori alimentari in capsule proposti come alternative naturali a Ozempic — come Ozem+ o GLPure. Non sono medicinali e non sostituiscono alcuna terapia; sostengono il metabolismo con ingredienti come niacina, tè verde, berberina o cromo."),
    ("Queste capsule sono state in televisione?",
     "No. Nessun prodotto dimagrante è mai stato approvato o finanziato in un programma televisivo di investitori. Ogni pubblicità che lo afferma è falsa. Acquista solo tramite lo shop ufficiale del marchio."),
    ("Pastiglie o iniezione: qual è la differenza?",
     "Ozempic e Wegovy sono iniezioni su ricetta a base di semaglutide. Gli integratori GLP-1 senza ricetta non contengono semaglutide e non agiscono come farmaci. Non esiste una pastiglia senza ricetta con il principio attivo dell'iniezione."),
    ("Quanto costano?",
     "Circa 40–75 € a flacone singolo secondo il marchio, con sconti consistenti sulle confezioni multiple. Quasi sempre è un acquisto unico senza abbonamento, spesso con garanzia soddisfatti o rimborsati di 30 giorni. I prezzi esatti sono solo nello shop ufficiale."),
    ("Si comprano in farmacia o su Amazon?",
     "No. Questi marchi sono venduti esclusivamente tramite il proprio shop ufficiale online, non in farmacia né sui marketplace. Gli annunci di terzi espongono al rischio di contraffazioni senza garanzia."),
    ("Hanno effetti collaterali?",
     "La maggior parte delle formule contiene caffeina da tè verde o guaranà: sono sconsigliate a bambini, donne in gravidanza o allattamento e a chi è sensibile alla caffeina. In caso di terapie o patologie, consultare il medico prima dell'uso."),
    ("Esiste un codice sconto?",
     "In genere no. Lo sconto è già incluso nelle confezioni multiple dello shop ufficiale. I siti che promettono codici rimandano quasi sempre a link pubblicitari."),
    ("In quanto tempo agiscono?",
     "Gli integratori alimentari non agiscono come farmaci e non garantiscono risultati. Sono pensati come routine quotidiana per diverse settimane, insieme a un'alimentazione equilibrata e attività fisica."),
  ],
)

# ============================== PL ==============================
LOCALES["pl"] = dict(
  lang="pl", path="pl", hreflang=["pl"],
  title="Zamiennik Ozempic w tabletkach? Suplementy GLP-1 2026",
  desc="Zamiennik Ozempic bez recepty i suplementy GLP-1 w 2026: Ozem+ — uczciwie wyjaśnione. Bez zastrzyku, bez recepty.",
  brandline="Kompas Kapsułek · niezależny przegląd rynku",
  eyebrow="GLP-1 i zamienniki Ozempic · 2026",
  h1a="Zamiennik Ozempic w tabletkach?", h1b="Przegląd suplementów GLP-1 bez recepty 2026",
  lede="„ozempic zamiennik bez recepty”, „tabletki na odchudzanie bez recepty”, „ozempic tabletki cena”, „suplement glp 1 opinie” — te wyszukiwania rosną najszybciej. Wyjaśniamy, czym naprawdę są te kapsułki, ile kosztują i gdzie da się je faktycznie kupić.",
  updated="Ostatnia aktualizacja", readtime="6 min czytania",
  toc="Przejdź do produktu", toc_faq="Najczęstsze pytania",
  intro="Odkąd <b>retatrutyd</b> oraz zastrzyki odchudzające <b>Ozempic</b>, <b>Wegovy</b> i <b>Mounjaro</b> trafiły na nagłówki, dziesiątki tysięcy osób każdego dnia szukają <b>zamiennika Ozempic w tabletkach</b> — bez recepty, bez zastrzyku, bez wizyty u lekarza. Najważniejsze na wstępie: <b>same zastrzyki są lekami na receptę i nie są dostępne bez recepty.</b> Bez recepty dostępne są <b>suplementy diety w kapsułkach</b> ze składnikami takimi jak niacyna, zielona herbata, berberyna czy chrom. To nie są leki.",
  tvtitle="Ostrzeżenie dotyczące wszystkich marek", tvshow=None,
  tv="Żaden produkt odchudzający nie został nigdy zatwierdzony ani sfinansowany w telewizyjnym programie inwestorskim. Każda reklama twierdząca, że produkt wystąpił w telewizji lub zdobył inwestora — niezależnie od marki — jest fałszywa. Nigdy nie kupuj przez takie reklamy, tylko przez oficjalny sklep marki.",
  h_vs="Tabletki czy zastrzyki — jaka jest różnica?",
  vs="Najczęstsze pytanie to <b>„ozempic tabletki czy zastrzyki”</b>. Różnica jest zasadnicza: Ozempic i Wegovy to <b>zastrzyki na receptę</b> zawierające semaglutyd. Suplementy <b>GLP-1 bez recepty</b> to suplementy diety — nie zawierają semaglutydu i nie działają jak lek. Nie istnieje tabletka bez recepty z substancją czynną zastrzyku.",
  h_buy="Czy można je kupić w aptece, Rossmannie lub na Allegro?",
  buy="Nie. Wyszukiwania w stylu <b>„tabletki na odchudzanie z apteki”</b> czy <b>„tabletki na odchudzanie rossmann”</b> nie prowadzą do tych marek — są sprzedawane <b>wyłącznie przez własny oficjalny sklep internetowy</b>. Ani apteka, ani drogeria, ani Allegro czy Temu. Strony obiecujące „kody rabatowe” najczęściej prowadzą tylko do linków reklamowych.",
  h_cost="Ile kosztują suplementy GLP-1 bez recepty?",
  cost="Ceny to zwykle <b>ok. 180–330 zł za pojedynczą butelkę</b> w zależności od marki, ze znacznymi rabatami przy zestawach wielopakowych — rabat jest w zestawie, a oficjalne kody rabatowe zwykle nie istnieją. Prawie zawsze jest to <b>jednorazowy zakup bez abonamentu</b>, często z 30-dniową gwarancją zwrotu pieniędzy. Wiążące ceny podaje wyłącznie oficjalny sklep.",
  h_safe="Skutki uboczne i przeciwwskazania",
  safe="Ponieważ są to suplementy diety, skład jest zadeklarowany i zwykle dobrze tolerowany. Większość formuł zawiera jednak <b>kofeinę</b> (zielona herbata, guarana) — nie są przeznaczone dla dzieci, kobiet w ciąży i karmiących ani osób wrażliwych na kofeinę. Przy przyjmowaniu leków lub chorobach przewlekłych skonsultuj się z lekarzem. Suplement nie zastępuje zbilansowanej diety.",
  summary="<b>W skrócie:</b> szukając <b>zamiennika Ozempic bez recepty</b>, <b>tabletek na odchudzanie bez recepty</b> lub <b>suplementu GLP-1</b>, bez recepty znajdziesz wyłącznie suplementy diety — nie leki. Oceniaj je po składzie, przejrzystości cen i gwarancji zwrotu, a nie po telewizyjnych plotkach.",
  h_faq="Najczęstsze pytania", shopcta="Przejdź do oficjalnego sklepu {}", langlabel="Język",
  disc="Ten przegląd ma charakter informacyjny i nie stanowi porady medycznej. Wymienione produkty są suplementami diety i nie zastępują leczenia ani leków na receptę. „Ozempic”, „Wegovy” i „Mounjaro” są znakami towarowymi odpowiednich właścicieli; nie sugerujemy żadnego powiązania. Ta strona może otrzymać prowizję od zamówień złożonych przez podlinkowane oficjalne sklepy, bez dodatkowych kosztów dla Ciebie. Aktualizacja: lipiec 2026.",
  products=[
    ("ozem","https://ozem-plus.store/pl/","PL · DE · AT · CH · IT · NL",
     "ozem plus opinie · ozem plus glp 1 · ozem plus tabletki · ozem plus cena",
     "Ozem+ to najczęściej wyszukiwana kapsułka bez recepty w tym zestawieniu i jest dostępna po polsku. Dominują zapytania „ozem plus opinie” — typowy sygnał, że ludzie szukają potwierdzenia przed zakupem. Ozem+ to <b>suplement diety przedstawiany jako naturalny zamiennik Ozempic</b>, nie lek, sprzedawany jako jednorazowy zakup z rabatami na zestawy, wyłącznie w oficjalnym sklepie."),
  ],
  faq=[
    ("Czy istnieje zamiennik Ozempic bez recepty?",
     "Ozempic (semaglutyd) i Wegovy to zastrzyki na receptę i nie są dostępne bez recepty. Bez recepty dostępne są suplementy diety w kapsułkach reklamowane jako naturalny zamiennik Ozempic — na przykład Ozem+. Nie są to leki i nie zastępują leczenia; wspierają metabolizm składnikami takimi jak niacyna, zielona herbata, berberyna czy chrom."),
    ("Czy te kapsułki były w telewizji?",
     "Nie. Żaden produkt odchudzający nie został nigdy zatwierdzony ani sfinansowany w telewizyjnym programie inwestorskim. Każda reklama, która tak twierdzi, jest fałszywa. Kupuj wyłącznie przez oficjalny sklep marki."),
    ("Tabletki czy zastrzyki — jaka jest różnica?",
     "Ozempic i Wegovy to zastrzyki na receptę zawierające semaglutyd. Suplementy GLP-1 bez recepty nie zawierają semaglutydu i nie działają jak lek. Nie istnieje tabletka bez recepty z substancją czynną zastrzyku."),
    ("Ile kosztują?",
     "Zwykle około 180–330 zł za pojedynczą butelkę w zależności od marki, ze znacznymi rabatami przy zestawach. Prawie zawsze jest to jednorazowy zakup bez abonamentu, często z 30-dniową gwarancją zwrotu pieniędzy. Dokładne ceny podaje tylko oficjalny sklep."),
    ("Czy można kupić je w aptece lub Rossmannie?",
     "Nie. Te marki są sprzedawane wyłącznie przez własny oficjalny sklep internetowy, nie w aptekach, drogeriach ani na platformach sprzedażowych. Oferty od osób trzecich grożą podróbkami bez gwarancji."),
    ("Czy mają skutki uboczne?",
     "Większość formuł zawiera kofeinę z zielonej herbaty lub guarany, dlatego nie są przeznaczone dla dzieci, kobiet w ciąży i karmiących ani osób wrażliwych na kofeinę. Przy lekach lub chorobach przewlekłych skonsultuj się z lekarzem."),
    ("Czy jest kod rabatowy?",
     "Zazwyczaj nie. Rabat jest wliczony w zestawy wielopakowe w oficjalnym sklepie. Strony obiecujące kody prowadzą najczęściej do linków reklamowych."),
    ("Jak szybko działają?",
     "Suplementy diety nie działają jak leki i nie gwarantują efektów. Są pomyślane jako codzienna rutyna przez kilka tygodni, obok zbilansowanej diety i aktywności fizycznej."),
  ],
)

# ============================== NL ==============================
LOCALES["nl"] = dict(
  lang="nl", path="nl", hreflang=["nl","nl-BE"],
  title="Ozempic alternatief in pilvorm? GLP-1 supplementen 2026",
  desc="Ozempic alternatief zonder recept en GLP-1 supplementen in 2026: Ozem+ en Ozalyn eerlijk uitgelegd. Geen injectie, geen recept.",
  brandline="Capsule Kompas · onafhankelijk marktoverzicht",
  eyebrow="GLP-1 &amp; Ozempic-alternatieven · 2026",
  h1a="Ozempic alternatief in pilvorm?", h1b="Het overzicht 2026 van GLP-1 supplementen zonder recept",
  lede="„ozempic alternatief pil”, „afslankpillen glp 1”, „ozempic pillen prijs”, „glp-1 supplement kopen” — deze zoekopdrachten groeien hard. Hier lees je wat deze capsules werkelijk zijn, wat ze kosten en waar je ze echt kunt kopen.",
  updated="Laatst bijgewerkt", readtime="6 min lezen",
  toc="Ga naar een product", toc_faq="Veelgestelde vragen",
  intro="Sinds <b>retatrutide</b> en de afslankinjecties <b>Ozempic</b>, <b>Wegovy</b> en <b>Mounjaro</b> in het nieuws zijn, zoeken dagelijks tienduizenden mensen naar een <b>Ozempic alternatief in pilvorm</b> — zonder recept, zonder injectie, zonder huisarts. Belangrijk vooraf: <b>de injecties zelf zijn receptplichtig en niet vrij verkrijgbaar.</b> Wat wél vrij verkrijgbaar is, zijn <b>voedingssupplementen in capsulevorm</b> met ingrediënten als niacine, groene thee, berberine of chroom. Het zijn geen geneesmiddelen.",
  tvtitle="Een waarschuwing die voor alle merken geldt", tvshow=None,
  tv="Geen enkel afslankproduct is ooit goedgekeurd of gefinancierd in een televisieprogramma met investeerders. Elke advertentie die een tv-optreden of een investering claimt — voor welke capsule dan ook — is nep. Koop nooit via zulke advertenties, maar uitsluitend via de officiële webshop van het merk.",
  h_vs="Pillen of injecties — wat is het verschil?",
  vs="De meestgestelde vraag is <b>„ozempic pillen of injecties”</b>. Het verschil is fundamenteel: Ozempic en Wegovy zijn receptplichtige <b>injecties</b> met semaglutide. <b>GLP-1 supplementen</b> zonder recept zijn voedingssupplementen — zij bevatten geen semaglutide en werken niet als een geneesmiddel. Een vrij verkrijgbare pil met de werkzame stof van de injectie bestaat niet.",
  h_buy="Zijn ze te koop bij Etos, Holland &amp; Barrett of Kruidvat?",
  buy="Nee. Zoekopdrachten als <b>„afslankpillen etos”</b>, <b>„afslankpillen holland en barrett”</b> of <b>„glp-1 supplement etos”</b> leiden niet naar deze merken — ze worden <b>uitsluitend via hun eigen officiële webshop</b> verkocht. Niet bij drogisterijen, niet via bol of Amazon. Pagina's met zogenaamde „kortingscodes” verwijzen meestal alleen naar advertentielinks.",
  h_cost="Wat kosten GLP-1 supplementen zonder recept?",
  cost="Reken op ongeveer <b>40 tot 75 euro per losse fles</b> afhankelijk van het merk, met flinke kortingen op meerdere flessen — de korting zit in het pakket en officiële kortingscodes bestaan doorgaans niet. Het gaat vrijwel altijd om een <b>eenmalige aankoop zonder abonnement</b>, meestal met 30 dagen niet-goed-geld-terug. Bindende prijzen staan alleen in de officiële webshop.",
  h_safe="Bijwerkingen en wie ze beter niet gebruikt",
  safe="Omdat het voedingssupplementen zijn, staan de ingrediënten op het etiket en worden ze meestal goed verdragen. De meeste formules bevatten wel <b>cafeïne</b> (groene thee, guarana) — niet geschikt voor kinderen, zwangere vrouwen, vrouwen die borstvoeding geven of mensen die gevoelig zijn voor cafeïne. Gebruik je medicijnen of heb je een aandoening, overleg dan eerst met je arts. Een supplement vervangt geen evenwichtige voeding.",
  summary="<b>Kort samengevat:</b> wie zoekt naar een <b>Ozempic alternatief zonder recept</b>, <b>afslankpillen</b> of een <b>GLP-1 supplement</b>, vindt zonder recept uitsluitend voedingssupplementen — geen geneesmiddelen. Beoordeel ze op ingrediënten, transparante prijzen en garantie, niet op tv-geruchten.",
  h_faq="Veelgestelde vragen", shopcta="Naar de officiële {} webshop", langlabel="Taal",
  disc="Dit overzicht is uitsluitend informatief en is geen medisch advies. De genoemde producten zijn voedingssupplementen en vervangen geen medische behandeling of receptplichtige geneesmiddelen. „Ozempic”, „Wegovy” en „Mounjaro” zijn merken van de betreffende rechthebbenden; er wordt geen verband gesuggereerd. Deze pagina kan een commissie ontvangen op bestellingen via de gelinkte officiële webshops, zonder extra kosten voor jou. Bijgewerkt: juli 2026.",
  products=[
    ("ozem","https://ozem-plus.store/nl/","NL · BE · DE · AT · CH · IT · PL",
     "ozem plus ervaringen · ozem plus review · ozem plus capsules · ozem plus glp 1",
     "Ozem+ is de meestgezochte capsule zonder recept in dit overzicht en is in het Nederlands beschikbaar. Zoekopdrachten als „ozem plus ervaringen” en „ozem plus capsules” overheersen — mensen zoeken bevestiging vóór aankoop. Ozem+ is een <b>voedingssupplement dat wordt gepresenteerd als natuurlijk Ozempic-alternatief</b>, geen geneesmiddel, verkocht als eenmalige aankoop met pakketkorting, uitsluitend in de officiële webshop."),
    ("ozalyn","https://osanix.shop/nl/","NL · BE · UK · DE · AT · DK · SE",
     "ozalyn reviews · ozalyn kopen · ozalyn trustpilot · ozalyn betrouwbaar · ozalyn capsules review",
     "Ozalyn wordt in Nederland en België opvallend vaak gezocht, met name via „ozalyn betrouwbaar”, „ozalyn trustpilot” en „ozalyn kopen” — allemaal vertrouwensvragen die mensen stellen vlak voor de aankoop. Ook Ozalyn is een <b>capsulesupplement ter ondersteuning van de stofwisseling</b>, geen afslankinjectie, en wordt uitsluitend via de eigen officiële webshop verkocht."),
  ],
  faq=[
    ("Bestaat er een Ozempic alternatief zonder recept?",
     "Ozempic (semaglutide) en Wegovy zijn receptplichtige injecties en zijn niet vrij verkrijgbaar. Wat wel vrij verkrijgbaar is, zijn voedingssupplementen in capsulevorm die worden aangeprezen als natuurlijk Ozempic-alternatief — zoals Ozem+ of Ozalyn. Het zijn geen geneesmiddelen en ze vervangen geen behandeling; ze ondersteunen de stofwisseling met ingrediënten als niacine, groene thee, berberine of chroom."),
    ("Zijn deze capsules op televisie geweest?",
     "Nee. Geen enkel afslankproduct is ooit goedgekeurd of gefinancierd in een televisieprogramma met investeerders. Elke advertentie die dat claimt is nep. Koop uitsluitend via de officiële webshop van het merk."),
    ("Pillen of injecties — wat is het verschil?",
     "Ozempic en Wegovy zijn receptplichtige injecties met semaglutide. GLP-1 supplementen zonder recept bevatten geen semaglutide en werken niet als een geneesmiddel. Een vrij verkrijgbare pil met de werkzame stof van de injectie bestaat niet."),
    ("Wat kosten ze?",
     "Ongeveer 40 tot 75 euro per losse fles afhankelijk van het merk, met flinke kortingen op meerdere flessen. Het is vrijwel altijd een eenmalige aankoop zonder abonnement, meestal met 30 dagen niet-goed-geld-terug. Exacte prijzen staan alleen in de officiële webshop."),
    ("Zijn ze te koop bij Etos, Kruidvat of Holland &amp; Barrett?",
     "Nee. Deze merken worden uitsluitend via hun eigen officiële webshop verkocht, niet bij drogisterijketens of marktplaatsen. Aanbiedingen van derden brengen het risico van namaak zonder garantie met zich mee."),
    ("Hebben ze bijwerkingen?",
     "De meeste formules bevatten cafeïne uit groene thee of guarana en zijn daarom niet geschikt voor kinderen, zwangere vrouwen, vrouwen die borstvoeding geven of mensen die gevoelig zijn voor cafeïne. Gebruik je medicijnen of heb je een aandoening, overleg dan eerst met je arts."),
    ("Is er een kortingscode?",
     "Meestal niet. De korting zit al in de voordeelpakketten van de officiële webshop. Sites die kortingscodes beloven verwijzen doorgaans alleen naar advertentielinks."),
    ("Hoe snel werken ze?",
     "Voedingssupplementen werken niet als geneesmiddelen en garanderen geen resultaat. Ze zijn bedoeld als dagelijkse routine gedurende meerdere weken, naast evenwichtige voeding en voldoende beweging."),
  ],
)

# ============================== DA ==============================
LOCALES["da"] = dict(
  lang="da", path="da", hreflang=["da"],
  title="Ozempic alternativ i pilleform? GLP-1 kosttilskud 2026",
  desc="Ozempic alternativ uden recept og GLP-1 kosttilskud i 2026: Ozalyn, RetaFit og GLPure — ærligt forklaret. Ingen sprøjte, ingen recept.",
  brandline="Kapsel-Kompas · uafhængigt markedsoverblik",
  eyebrow="GLP-1 &amp; Ozempic-alternativer · 2026",
  h1a="Ozempic alternativ i pilleform?", h1b="Overblikket 2026 over GLP-1 kosttilskud uden recept",
  lede="„slankepiller uden recept”, „ozempic piller pris”, „vægttab piller håndkøb”, „glp 1 kosttilskud erfaringer” — disse søgninger vokser hurtigt. Her er hvad kapslerne bag dem reelt er, hvad de koster, og hvor man faktisk kan købe dem.",
  updated="Sidst opdateret", readtime="6 min læsning",
  toc="Gå til et produkt", toc_faq="Ofte stillede spørgsmål",
  intro="Siden <b>retatrutid</b> og slankesprøjterne <b>Ozempic</b>, <b>Wegovy</b> og <b>Mounjaro</b> kom i overskrifterne, søger titusindvis dagligt efter et <b>Ozempic alternativ i pilleform</b> — uden recept, uden sprøjte, uden lægebesøg. Vigtigt først: <b>selve sprøjterne er receptpligtige og kan ikke købes i håndkøb.</b> Det, der findes uden recept, er <b>kosttilskud i kapselform</b> med ingredienser som niacin, grøn te, berberin eller krom. Det er ikke lægemidler.",
  tvtitle="En advarsel der gælder alle mærker", tvshow="Løvens Hule",
  tv="Der har aldrig været et slankeprodukt i <b>Løvens Hule</b>. Enhver annonce, der hævder en optræden i programmet eller en investering fra panelet — uanset kapsel — er falsk. Køb aldrig via sådanne annoncer, kun via mærkets officielle shop.",
  h_vs="Piller eller sprøjte — hvad er forskellen?",
  vs="Det mest stillede spørgsmål er <b>„ozempic piller”</b> kontra sprøjte. Forskellen er grundlæggende: Ozempic og Wegovy er receptpligtige <b>injektioner</b> med semaglutid. <b>GLP-1 kosttilskud</b> uden recept er kosttilskud — de indeholder ikke semaglutid og virker ikke som lægemiddel. Der findes ingen håndkøbspille med sprøjtens aktive stof.",
  h_buy="Kan man købe dem i Matas, apoteket eller føtex?",
  buy="Nej. Søgninger som <b>„slankepiller matas”</b>, <b>„slankepiller apoteket”</b> eller <b>„vægttab piller håndkøb”</b> fører ikke til disse mærker — de sælges <b>udelukkende via deres egen officielle webshop</b>. Hverken Matas, apotek, NORMAL, føtex eller Amazon. Sider med påståede „rabatkoder” fører oftest blot til reklamelinks.",
  h_cost="Hvad koster GLP-1 kosttilskud uden recept?",
  cost="Regn med cirka <b>300–800 kr. pr. enkelt flaske</b> afhængigt af mærket, med markante besparelser på flerpakker — rabatten ligger i pakken, og officielle rabatkoder findes normalt ikke. Det er næsten altid et <b>engangskøb uden abonnement</b>, oftest med 30 dages pengene-tilbage-garanti. Bindende priser står kun i den officielle webshop.",
  h_safe="Bivirkninger og hvem der bør undlade dem",
  safe="Da der er tale om kosttilskud, er ingredienserne deklareret og tåles normalt godt. De fleste formler indeholder dog <b>koffein</b> (grøn te, guarana) — ikke egnet til børn, gravide, ammende eller personer med koffeinfølsomhed. Tager du medicin eller har en kronisk sygdom, så tal med din læge først. Et kosttilskud erstatter ikke en varieret kost.",
  summary="<b>Kort fortalt:</b> søger du et <b>Ozempic alternativ uden recept</b>, <b>slankepiller uden recept</b> eller et <b>GLP-1 kosttilskud</b>, findes der uden recept udelukkende kosttilskud — ikke lægemidler. Bedøm dem på ingredienser, gennemsigtige priser og pengene-tilbage-garanti, ikke på tv-rygter.",
  h_faq="Ofte stillede spørgsmål", shopcta="Til den officielle {} shop", langlabel="Sprog",
  disc="Dette overblik er kun til information og er ikke lægefaglig rådgivning. De nævnte produkter er kosttilskud og erstatter ikke lægebehandling eller receptpligtig medicin. „Ozempic”, „Wegovy”, „Mounjaro” og „Løvens Hule” er varemærker tilhørende de respektive ejere; der antydes ingen forbindelse. Denne side kan modtage provision for ordrer via de linkede officielle shops, uden ekstra omkostninger for dig. Opdateret: juli 2026.",
  products=[
    ("ozalyn","https://osanix.shop/da/","DK · UK · DE · AT · NL · BE · SE",
     "ozalyn danmark · ozalyn pris · ozalyn kapsler · ozalyn erfaringer · ozalyn trustpilot",
     "Ozalyn er det mest søgte mærke i denne oversigt i Danmark, især via „ozalyn danmark”, „ozalyn pris” og „ozalyn kapsler”. Det er de klassiske spørgsmål lige inden et køb: hvad koster det, og kan man stole på det. Ozalyn er et <b>kapseltilskud til stofskiftestøtte</b> uden recept, ikke en slankesprøjte, og sælges udelukkende via den officielle webshop."),
    ("retafit","https://tryretafit.com/da/","DK · DE · AT · CH · UK · NO · FR",
     "retafit · reta fit · reta vægttab · retafit anmeldelser · reta kapsler",
     "RetaFit er det nyeste mærke i oversigten og trækker på opmærksomheden omkring <b>retatrutid</b> („reta”). Vigtigt: <b>RetaFit er ikke retatrutid</b>, men en håndkøbskapsel med niacin, grøn te, guarana og N-acetyl-L-carnitin. Fås i fem lande som engangskøb med 30 dages pengene-tilbage-garanti.",
     ("https://tryretafit.com/da/loevens-hule/","RetaFit &amp; Løvens Hule — fakta")),
    ("glpure","https://glpure.shop/dk/","EU · international",
     "glpure · glpure anmeldelser · glp 1 kosttilskud · glp 1 kosttilskud erfaringer",
     "GLPure retter sig direkte mod søgningen „glp 1 kosttilskud” og „glp 1 kosttilskud erfaringer”. Mærket er mindre end Ozalyn, men dukker konsekvent op i disse søgninger. Samme regler gælder: kosttilskud uden recept, ingen sprøjte, kun officiel webshop."),
  ],
  faq=[
    ("Findes der et Ozempic alternativ uden recept?",
     "Ozempic (semaglutid) og Wegovy er receptpligtige injektioner og kan ikke købes i håndkøb. Det, der findes uden recept, er kosttilskud i kapselform, som markedsføres som naturligt Ozempic-alternativ — for eksempel Ozalyn, RetaFit eller GLPure. Det er ikke lægemidler og erstatter ikke behandling; de støtter stofskiftet via ingredienser som niacin, grøn te, berberin eller krom."),
    ("Har disse kapsler været i Løvens Hule?",
     "Nej. Der har aldrig været et slankeprodukt i Løvens Hule. Enhver annonce, der hævder en optræden i programmet eller en investering fra panelet — uanset kapsel — er falsk. Køb kun via mærkets officielle webshop."),
    ("Piller eller sprøjte — hvad er forskellen?",
     "Ozempic og Wegovy er receptpligtige injektioner med semaglutid. GLP-1 kosttilskud uden recept indeholder ikke semaglutid og virker ikke som lægemiddel. Der findes ingen håndkøbspille med sprøjtens aktive stof."),
    ("Hvad koster de?",
     "Cirka 300 til 800 kr. pr. enkelt flaske afhængigt af mærket, med markante besparelser på flerpakker. Det er næsten altid et engangskøb uden abonnement, oftest med 30 dages pengene-tilbage-garanti. Præcise priser står kun i den officielle webshop."),
    ("Kan man købe dem i Matas eller på apoteket?",
     "Nej. Disse mærker sælges udelukkende via deres egen officielle webshop, ikke i Matas, på apoteket eller via markedspladser. Tilbud fra tredjepart indebærer risiko for kopivarer uden garanti."),
    ("Har de bivirkninger?",
     "De fleste formler indeholder koffein fra grøn te eller guarana og er derfor ikke egnede til børn, gravide, ammende eller personer med koffeinfølsomhed. Tager du medicin eller har en kronisk sygdom, så tal med din læge først."),
    ("Findes der en rabatkode?",
     "Normalt ikke. Rabatten ligger allerede i flerpakkerne i den officielle webshop. Sider, der lover rabatkoder, fører oftest blot til reklamelinks."),
    ("Hvor hurtigt virker de?",
     "Kosttilskud virker ikke som lægemidler og kan ikke garantere resultater. De er tænkt som en daglig rutine over flere uger sammen med varieret kost og bevægelse."),
  ],
)

# ============================== SV ==============================
LOCALES["sv"] = dict(
  lang="sv", path="sv", hreflang=["sv"],
  title="Ozempic alternativ receptfritt? GLP-1 kosttillskott 2026",
  desc="Ozempic alternativ receptfritt och GLP-1 kosttillskott 2026: Ozem+, Ozalyn och GLPure — ärligt förklarat. Ingen spruta, inget recept.",
  brandline="Kapsel-Kompassen · oberoende marknadsöversikt",
  eyebrow="GLP-1 &amp; Ozempic-alternativ · 2026",
  h1a="Ozempic alternativ receptfritt?", h1b="Översikten 2026 över GLP-1 kosttillskott utan recept",
  lede="„ozempic alternativ receptfritt”, „bantningspiller som funkar”, „ozempic tabletter pris”, „glp-1 kosttillskott bäst i test” — de här sökningarna växer snabbt. Här är vad kapslarna bakom dem faktiskt är, vad de kostar och var man verkligen kan köpa dem.",
  updated="Senast uppdaterad", readtime="6 min läsning",
  toc="Gå till en produkt", toc_faq="Vanliga frågor",
  intro="Sedan <b>retatrutid</b> och viktminskningssprutorna <b>Ozempic</b>, <b>Wegovy</b> och <b>Mounjaro</b> hamnade i rubrikerna söker tiotusentals människor dagligen efter ett <b>Ozempic alternativ receptfritt</b> — utan spruta och utan läkarbesök. Viktigt först: <b>sprutorna själva är receptbelagda och säljs inte receptfritt.</b> Det som finns receptfritt är <b>kosttillskott i kapselform</b> med ingredienser som niacin, grönt te, berberin eller krom. De är inte läkemedel.",
  tvtitle="En varning som gäller alla varumärken", tvshow=None,
  tv="Ingen viktminskningsprodukt har någonsin godkänts eller finansierats i ett tv-program med investerare. Varje annons som påstår ett tv-framträdande eller en investering — oavsett kapsel — är falsk. Köp aldrig via sådana annonser, utan endast via varumärkets officiella butik.",
  h_vs="Tabletter eller spruta — vad är skillnaden?",
  vs="Den vanligaste frågan är <b>„ozempic tabletter”</b> kontra spruta. Skillnaden är grundläggande: Ozempic och Wegovy är receptbelagda <b>injektioner</b> med semaglutid. <b>GLP-1 kosttillskott</b> receptfritt är kosttillskott — de innehåller inte semaglutid och verkar inte som ett läkemedel. Det finns ingen receptfri tablett med sprutans aktiva substans.",
  h_buy="Finns de på Apoteket eller Kronans Apotek?",
  buy="Nej. Sökningar som <b>„bantningspiller apoteket”</b>, <b>„ozempic tabletter apoteket”</b> eller <b>„viktminskning tabletter apoteket”</b> leder inte till dessa varumärken — de säljs <b>uteslutande via sin egen officiella webbutik</b>. Varken apotek, hälsokostbutik eller Amazon. Sidor som utlovar „rabattkoder” leder oftast bara till annonslänkar.",
  h_cost="Vad kostar GLP-1 kosttillskott receptfritt?",
  cost="Räkna med cirka <b>450–850 kr per enskild flaska</b> beroende på varumärke, med tydliga rabatter på flerpack — rabatten ligger i paketet och officiella rabattkoder finns normalt inte. Det rör sig nästan alltid om ett <b>engångsköp utan abonnemang</b>, oftast med 30 dagars pengarna-tillbaka-garanti. Bindande priser finns endast i den officiella butiken.",
  h_safe="Biverkningar och vem som bör avstå",
  safe="Eftersom det handlar om kosttillskott är ingredienserna deklarerade och tolereras oftast väl. De flesta formler innehåller dock <b>koffein</b> (grönt te, guarana) — inte lämpliga för barn, gravida, ammande eller personer som är känsliga för koffein. Tar du mediciner eller har en sjukdom bör du rådgöra med läkare först. Ett kosttillskott ersätter inte en balanserad kost.",
  summary="<b>Kort sagt:</b> söker du ett <b>Ozempic alternativ receptfritt</b>, <b>bantningspiller som funkar</b> eller ett <b>GLP-1 kosttillskott</b>, finns receptfritt endast kosttillskott — inte läkemedel. Bedöm dem utifrån ingredienser, transparenta priser och garanti, inte utifrån tv-rykten.",
  h_faq="Vanliga frågor", shopcta="Till den officiella {}-butiken", langlabel="Språk",
  disc="Den här översikten är endast informativ och utgör inte medicinsk rådgivning. De nämnda produkterna är kosttillskott och ersätter inte medicinsk behandling eller receptbelagda läkemedel. „Ozempic”, „Wegovy” och „Mounjaro” är varumärken som tillhör respektive ägare; ingen koppling antyds. Den här sidan kan få provision på beställningar via de länkade officiella butikerna, utan extra kostnad för dig. Uppdaterad: juli 2026.",
  products=[
    ("ozem","https://ozem-plus.store/","SE · DE · AT · CH · IT · PL · NL",
     "ozem plus test · ozem plus glp 1 · ozem plus recension · ozem plus erfarenheter",
     "Ozem+ är den mest sökta receptfria kapseln i den här översikten i Europa. Sökningar som „ozem plus test” och „ozem plus recension” dominerar — människor söker bekräftelse före köp. Ozem+ är ett <b>kosttillskott som marknadsförs som ett naturligt Ozempic-alternativ</b>, inte ett läkemedel, och säljs som engångsköp med paketrabatt endast i den officiella butiken."),
    ("ozalyn","https://osanix.shop/se/","SE · UK · DE · AT · NL · BE · DK",
     "ozalyn sverige · ozalyn recensioner · ozalyn köpa · ozalyn trustpilot · ozalyn kapslar",
     "Ozalyn söks tydligt i Sverige, framför allt via „ozalyn sverige”, „ozalyn recensioner” och „ozalyn köpa”. Det är förtroendefrågor som ställs strax före ett köp. Ozalyn är ett <b>kapseltillskott för ämnesomsättningsstöd</b> utan recept, inte en viktminskningsspruta, och säljs uteslutande via den egna officiella butiken."),
    ("glpure","https://glpure.shop/se/","EU · internationellt",
     "glpure · glpure recensioner · glp-1 kosttillskott · glp-1 kosttillskott bäst i test",
     "GLPure riktar sig direkt mot sökningen „glp-1 kosttillskott” och „glp-1 kosttillskott bäst i test”. Varumärket är mindre än Ozem+ och Ozalyn men dyker upp konsekvent i dessa sökningar. Samma regler gäller: receptfritt kosttillskott, ingen spruta, endast officiell butik."),
  ],
  faq=[
    ("Finns det ett Ozempic alternativ receptfritt?",
     "Ozempic (semaglutid) och Wegovy är receptbelagda injektioner och säljs inte receptfritt. Det som finns receptfritt är kosttillskott i kapselform som marknadsförs som naturligt Ozempic-alternativ — till exempel Ozem+, Ozalyn eller GLPure. De är inte läkemedel och ersätter ingen behandling; de stödjer ämnesomsättningen via ingredienser som niacin, grönt te, berberin eller krom."),
    ("Har dessa kapslar varit i tv?",
     "Nej. Ingen viktminskningsprodukt har någonsin godkänts eller finansierats i ett tv-program med investerare. Varje annons som påstår det är falsk. Köp endast via varumärkets officiella butik."),
    ("Tabletter eller spruta — vad är skillnaden?",
     "Ozempic och Wegovy är receptbelagda injektioner med semaglutid. GLP-1 kosttillskott receptfritt innehåller inte semaglutid och verkar inte som läkemedel. Det finns ingen receptfri tablett med sprutans aktiva substans."),
    ("Vad kostar de?",
     "Cirka 450 till 850 kr per enskild flaska beroende på varumärke, med tydliga rabatter på flerpack. Det är nästan alltid ett engångsköp utan abonnemang, oftast med 30 dagars pengarna-tillbaka-garanti. Exakta priser finns endast i den officiella butiken."),
    ("Finns de på Apoteket?",
     "Nej. Dessa varumärken säljs uteslutande via sin egen officiella webbutik, inte på apotek, i hälsokostbutiker eller på marknadsplatser. Erbjudanden från tredje part innebär risk för kopior utan garanti."),
    ("Har de biverkningar?",
     "De flesta formler innehåller koffein från grönt te eller guarana och passar därför inte barn, gravida, ammande eller personer som är känsliga för koffein. Tar du mediciner eller har en sjukdom bör du rådgöra med läkare först."),
    ("Finns det någon rabattkod?",
     "Vanligtvis inte. Rabatten ingår redan i flerpacken i den officiella butiken. Sidor som utlovar rabattkoder leder oftast bara till annonslänkar."),
    ("Hur snabbt verkar de?",
     "Kosttillskott verkar inte som läkemedel och kan inte garantera resultat. De är tänkta som en daglig rutin under flera veckor tillsammans med balanserad kost och rörelse."),
  ],
)

# ============================== NO ==============================
LOCALES["no"] = dict(
  lang="no", path="no", hreflang=["no","nb"],
  title="Ozempic alternativ uten resept? GLP-1 kosttilskudd 2026",
  desc="Ozempic alternativ uten resept og GLP-1 kosttilskudd i 2026: Ozem+ og RetaFit — ærlig forklart. Ingen sprøyte, ingen resept.",
  brandline="Kapsel-Kompasset · uavhengig markedsoversikt",
  eyebrow="GLP-1 &amp; Ozempic-alternativer · 2026",
  h1a="Ozempic alternativ uten resept?", h1b="Oversikten 2026 over GLP-1 kosttilskudd uten resept",
  lede="„slankepiller uten resept”, „ozempic tabletter pris”, „glp 1 kosttilskudd erfaringer”, „glp 1 kosttilskudd best i test” — disse søkene vokser raskt. Her er hva kapslene bak dem faktisk er, hva de koster, og hvor du virkelig kan kjøpe dem.",
  updated="Sist oppdatert", readtime="6 min lesing",
  toc="Gå til et produkt", toc_faq="Ofte stilte spørsmål",
  intro="Etter at <b>retatrutid</b> og slankesprøytene <b>Ozempic</b>, <b>Wegovy</b> og <b>Mounjaro</b> kom i overskriftene, søker titusenvis daglig etter et <b>Ozempic alternativ uten resept</b> — uten sprøyte og uten legetime. Viktig først: <b>selve sprøytene er reseptbelagte og selges ikke uten resept.</b> Det som finnes uten resept, er <b>kosttilskudd i kapselform</b> med ingredienser som niacin, grønn te, berberin eller krom. Det er ikke legemidler.",
  tvtitle="En advarsel som gjelder alle merker", tvshow="Løvens hule",
  tv="Det har aldri vært et slankeprodukt i <b>Løvens hule</b>. Enhver annonse som hevder en opptreden i programmet eller en investering fra panelet — uansett kapsel — er falsk. Kjøp aldri via slike annonser, kun via merkets offisielle nettbutikk.",
  h_vs="Tabletter eller sprøyte — hva er forskjellen?",
  vs="Det mest stilte spørsmålet er <b>„ozempic tabletter eller sprøyte”</b>. Forskjellen er grunnleggende: Ozempic og Wegovy er reseptbelagte <b>injeksjoner</b> med semaglutid. <b>GLP-1 kosttilskudd</b> uten resept er kosttilskudd — de inneholder ikke semaglutid og virker ikke som et legemiddel. Det finnes ingen reseptfri tablett med sprøytens aktive stoff.",
  h_buy="Får man dem på apotek eller Sunkost?",
  buy="Nei. Søk som <b>„slankepiller apotek”</b>, <b>„glp 1 kosttilskudd apotek”</b> eller <b>„glp 1 kosttilskudd sunkost”</b> fører ikke til disse merkene — de selges <b>utelukkende via sin egen offisielle nettbutikk</b>. Verken Apotek 1, Vitusapotek, Sunkost eller Amazon. Sider som lover „rabattkoder”, fører som regel bare til annonselenker.",
  h_cost="Hva koster GLP-1 kosttilskudd uten resept?",
  cost="Regn med rundt <b>450–1200 kr per enkeltflaske</b> avhengig av merke, med tydelige rabatter på flerpakninger — rabatten ligger i pakken, og offisielle rabattkoder finnes normalt ikke. Det er nesten alltid et <b>engangskjøp uten abonnement</b>, som regel med 30 dagers pengene-tilbake-garanti. Bindende priser står bare i den offisielle nettbutikken.",
  h_safe="Bivirkninger og hvem som bør avstå",
  safe="Siden dette er kosttilskudd, er ingrediensene deklarert og tåles vanligvis godt. De fleste formlene inneholder likevel <b>koffein</b> (grønn te, guarana) — ikke egnet for barn, gravide, ammende eller personer som er følsomme for koffein. Bruker du medisiner eller har en sykdom, snakk med legen din først. Et kosttilskudd erstatter ikke et variert kosthold.",
  summary="<b>Kort oppsummert:</b> leter du etter et <b>Ozempic alternativ uten resept</b>, <b>slankepiller uten resept</b> eller et <b>GLP-1 kosttilskudd</b>, finnes det uten resept kun kosttilskudd — ikke legemidler. Vurder dem etter ingredienser, åpne priser og pengene-tilbake-garanti, ikke etter TV-rykter.",
  h_faq="Ofte stilte spørsmål", shopcta="Til den offisielle {}-butikken", langlabel="Språk",
  disc="Denne oversikten er kun til informasjon og er ikke medisinsk rådgivning. Produktene som nevnes er kosttilskudd og erstatter ikke medisinsk behandling eller reseptbelagte legemidler. „Ozempic”, „Wegovy”, „Mounjaro” og „Løvens hule” er varemerker som tilhører sine respektive eiere; ingen tilknytning antydes. Denne siden kan motta provisjon for bestillinger via de lenkede offisielle butikkene, uten ekstra kostnad for deg. Oppdatert: juli 2026.",
  products=[
    ("ozem","https://ozem-plus.store/","NO · DE · AT · CH · IT · PL · NL · SE",
     "ozem plus erfaringer · ozem plus test · ozem plus glp 1 · ozem plus review",
     "Ozem+ er den mest søkte reseptfrie kapselen i denne oversikten i Europa. Søk som „ozem plus erfaringer” og „ozem plus test” dominerer — folk leter etter bekreftelse før kjøp. Ozem+ er et <b>kosttilskudd som markedsføres som et naturlig Ozempic-alternativ</b>, ikke et legemiddel, og selges som engangskjøp med pakkerabatt kun i den offisielle nettbutikken."),
    ("retafit","https://tryretafit.com/no/","NO · DE · AT · CH · UK · DK · FR",
     "retafit · reta fit · reta vektnedgang · retafit anmeldelser · stoffskiftekapsler",
     "RetaFit er det nyeste merket i oversikten og bygger på oppmerksomheten rundt <b>retatrutid</b> („reta”). Viktig: <b>RetaFit er ikke retatrutid</b>, men en reseptfri kapsel med niacin, grønn te, guarana og N-acetyl-L-karnitin. Tilgjengelig i fem land som engangskjøp med 30 dagers pengene-tilbake-garanti.",
     ("https://tryretafit.com/no/lovens-hule/","RetaFit &amp; Løvens hule — fakta")),
  ],
  faq=[
    ("Finnes det et Ozempic alternativ uten resept?",
     "Ozempic (semaglutid) og Wegovy er reseptbelagte injeksjoner og selges ikke uten resept. Det som finnes uten resept, er kosttilskudd i kapselform som markedsføres som naturlig Ozempic-alternativ — for eksempel Ozem+ eller RetaFit. Det er ikke legemidler og de erstatter ingen behandling; de støtter stoffskiftet via ingredienser som niacin, grønn te, berberin eller krom."),
    ("Har disse kapslene vært i Løvens hule?",
     "Nei. Det har aldri vært et slankeprodukt i Løvens hule. Enhver annonse som hevder en opptreden i programmet eller en investering fra panelet — uansett kapsel — er falsk. Kjøp kun via merkets offisielle nettbutikk."),
    ("Tabletter eller sprøyte — hva er forskjellen?",
     "Ozempic og Wegovy er reseptbelagte injeksjoner med semaglutid. GLP-1 kosttilskudd uten resept inneholder ikke semaglutid og virker ikke som legemiddel. Det finnes ingen reseptfri tablett med sprøytens aktive stoff."),
    ("Hva koster de?",
     "Rundt 450 til 1200 kr per enkeltflaske avhengig av merke, med tydelige rabatter på flerpakninger. Det er nesten alltid et engangskjøp uten abonnement, som regel med 30 dagers pengene-tilbake-garanti. Nøyaktige priser står bare i den offisielle nettbutikken."),
    ("Får man dem på apotek eller Sunkost?",
     "Nei. Disse merkene selges utelukkende via sin egen offisielle nettbutikk, ikke på apotek, i helsekostbutikker eller på markedsplasser. Tilbud fra tredjeparter innebærer risiko for kopivarer uten garanti."),
    ("Har de bivirkninger?",
     "De fleste formlene inneholder koffein fra grønn te eller guarana og passer derfor ikke for barn, gravide, ammende eller personer som er følsomme for koffein. Bruker du medisiner eller har en sykdom, snakk med legen din først."),
    ("Finnes det en rabattkode?",
     "Vanligvis ikke. Rabatten ligger allerede i flerpakningene i den offisielle nettbutikken. Sider som lover rabattkoder, fører som regel bare til annonselenker."),
    ("Hvor raskt virker de?",
     "Kosttilskudd virker ikke som legemidler og kan ikke garantere resultater. De er ment som en daglig rutine over flere uker sammen med variert kosthold og bevegelse."),
  ],
)

# ---------------------------------------------------------------- render
NAMES = {"de":"Deutsch","en":"English","fr":"Français","it":"Italiano","pl":"Polski",
         "nl":"Nederlands","da":"Dansk","sv":"Svenska","no":"Norsk"}
ORDER = ["de","en","fr","it","nl","da","sv","no","pl"]

FAV = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230f7a68'/%3E"
       "%3Cpath d='M11 8h6a5 5 0 0 1 0 10h-6z' fill='none' stroke='%23fff' stroke-width='2.4'/%3E"
       "%3Cline x1='11' y1='8' x2='11' y2='24' stroke='%23f0603a' stroke-width='2.4' stroke-linecap='round'/%3E%3C/svg%3E")

CSS = """
  :root{--brand:#0f7a68;--brand2:#0c6152;--cta:#f0603a;--ink:#16231f;--dim:#5a6b64;--bg:#f6faf8;--pane:#fff;--line:#dfe8e4;--tint:#eef7f4}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
  .wrap{max-width:760px;margin:0 auto;padding:0 20px}
  header.top{background:var(--pane);border-bottom:1px solid var(--line)}
  header.top .wrap{display:flex;align-items:center;gap:10px;padding:16px 20px}
  .mk{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:7px;background:var(--brand);color:#fff;font-weight:800;font-size:15px;flex:none}
  .brand{font-weight:800;letter-spacing:-.01em;font-size:17px;color:var(--ink);text-decoration:none}
  .brand small{color:var(--dim);font-weight:600;font-size:13px}
  .hero{background:linear-gradient(175deg,var(--tint),var(--bg));padding:40px 0 26px;border-bottom:1px solid var(--line)}
  .eyebrow{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--brand2);background:var(--tint);border:1px solid var(--line);border-radius:999px;padding:5px 12px;margin-bottom:14px}
  h1{font-size:31px;line-height:1.2;letter-spacing:-.02em;margin:0 0 12px}
  h1 .hl{color:var(--brand2)}
  .lede{font-size:18px;color:var(--dim);margin:0 0 6px}
  .upd{font-size:13px;color:var(--dim);margin:14px 0 0}
  h2{font-size:22px;letter-spacing:-.01em;margin:36px 0 12px;padding-top:8px}
  h3{font-size:19px;margin:0 0 4px}
  p{margin:0 0 15px}
  a{color:var(--brand2)}
  .toc{background:var(--pane);border:1px solid var(--line);border-radius:14px;padding:18px 22px;margin:24px 0}
  .toc b{display:block;font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);margin-bottom:8px}
  .toc a{display:inline-block;margin:3px 14px 3px 0;font-weight:600;text-decoration:none}
  .card{background:var(--pane);border:1px solid var(--line);border-radius:16px;padding:22px 24px;margin:0 0 18px;box-shadow:0 6px 20px rgba(15,122,104,.05)}
  h2 .rank,.card .rank{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:8px;background:var(--brand);color:#fff;font-weight:800;font-size:15px;margin-right:10px;vertical-align:-5px}
  .card .head{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:8px}
  .card .geo{font-size:12.5px;font-weight:700;color:var(--brand2);background:var(--tint);border-radius:6px;padding:3px 9px;white-space:nowrap}
  .kw{font-size:13.5px;color:var(--dim);margin:2px 0 12px}
  .kw b{color:var(--ink)}
  .cta{display:inline-flex;align-items:center;gap:8px;background:var(--cta);color:#fff;font-weight:800;text-decoration:none;border-radius:10px;padding:11px 20px;font-size:15px;margin:4px 8px 4px 0}
  .cta:hover{filter:brightness(1.06)}
  .cta.ghost{background:transparent;color:var(--brand2);border:1.5px solid var(--line)}
  .note{background:var(--tint);border:1px solid var(--line);border-left:4px solid var(--brand);border-radius:12px;padding:16px 20px;margin:20px 0}
  .note.warn{background:#fff7ea;border-left-color:var(--cta);border-color:#f2dfb0}
  .faq details{background:var(--pane);border:1px solid var(--line);border-radius:12px;padding:2px 18px;margin:0 0 10px}
  .faq summary{font-weight:700;cursor:pointer;padding:14px 0;list-style:none}
  .faq summary::-webkit-details-marker{display:none}
  .faq summary::after{content:"+";float:right;color:var(--brand2);font-weight:800}
  .faq details[open] summary::after{content:"\\2013"}
  .faq details>div{padding:0 0 15px;color:var(--dim)}
  .langs{background:var(--pane);border:1px solid var(--line);border-radius:14px;padding:16px 20px;margin:28px 0 0}
  .langs b{display:block;font-size:12px;text-transform:uppercase;letter-spacing:.06em;color:var(--dim);margin-bottom:6px}
  .langs a{display:inline-block;margin:3px 12px 3px 0;font-weight:600;text-decoration:none;font-size:15px}
  .langs a[aria-current]{color:var(--ink);text-decoration:underline}
  footer{margin-top:40px;background:#0c1a16;color:#c7d6cf}
  footer .wrap{padding:26px 20px}
  footer a{color:#8fd8c6}
  .disc{font-size:12.5px;color:#7f948c;margin-top:14px;line-height:1.6}
  @media(max-width:520px){h1{font-size:25px}h2{font-size:20px}body{font-size:16px}}
"""


def url_for(code):
    p = LOCALES[code]["path"]
    return f"{BASE}/" + (f"{p}/" if p else "")


def render(code):
    L = LOCALES[code]
    me = url_for(code)
    # hreflang cluster
    alts = []
    for c in ORDER:
        for hl in LOCALES[c]["hreflang"]:
            alts.append(f'<link rel="alternate" hreflang="{hl}" href="{url_for(c)}">')
    alts.append(f'<link rel="alternate" hreflang="x-default" href="{url_for("en")}">')

    # JSON-LD
    faq_nodes = [{"@type": "Question", "name": q,
                  "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in L["faq"]]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": L["brandline"].split("·")[0].strip(), "item": me},
            {"@type": "ListItem", "position": 2, "name": html.unescape(L["title"]), "item": me}]},
        {"@type": "FAQPage", "mainEntity": faq_nodes}]}

    # products
    cards = []
    toc = []
    for i, prod in enumerate(L["products"], 1):
        key, url, geo, kw, body = prod[0], prod[1], prod[2], prod[3], prod[4]
        extra = prod[5] if len(prod) > 5 else None
        name = P[key]
        toc.append(f'<a href="#{key}">{name}</a>')
        extra_html = ""
        if extra:
            extra_html = f'<a class="cta ghost" href="{extra[0]}" target="_blank" rel="noopener">{extra[1]}</a>'
        cards.append(f"""  <h2 id="{key}"><span class="rank">{i}</span>{name}</h2>
  <div class="card">
    <div class="head"><h3>{name}</h3><span class="geo">{geo}</span></div>
    <p class="kw">{kw}</p>
    <p>{body}</p>
    <a class="cta" href="{url}" target="_blank" rel="noopener">{L['shopcta'].format(name)} →</a>{extra_html}
  </div>""")
    toc.append(f'<a href="#faq">{L["toc_faq"]}</a>')

    faq_html = "\n".join(
        f'    <details{" open" if i == 0 else ""}><summary>{q}</summary><div>{a}</div></details>'
        for i, (q, a) in enumerate(L["faq"]))

    def lang_link(c):
        cur = ' aria-current="page"' if c == code else ""
        hl = LOCALES[c]["hreflang"][0]
        return f'<a href="{url_for(c)}"{cur} hreflang="{hl}">{NAMES[c]}</a>'
    langs = " ".join(lang_link(c) for c in ORDER)

    tv_title = L["tvtitle"]
    return f"""<!DOCTYPE html>
<html lang="{L['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#0f7a68">
<title>{L['title']}</title>
<meta name="description" content="{L['desc']}">
<link rel="canonical" href="{me}">
<meta name="robots" content="index, follow, max-image-preview:large">
{chr(10).join(alts)}
<meta property="og:type" content="article">
<meta property="og:locale" content="{L['lang']}">
<meta property="og:title" content="{L['title']}">
<meta property="og:description" content="{L['desc']}">
<meta property="og:url" content="{me}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{FAV}">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
<style>{CSS}</style>
</head>
<body>

<header class="top"><div class="wrap">
  <span class="mk">K</span>
  <a class="brand" href="{me}">{L['brandline']}</a>
</div></header>

<section class="hero"><div class="wrap">
  <span class="eyebrow">{L['eyebrow']}</span>
  <h1>{L['h1a']} <span class="hl">{L['h1b']}</span></h1>
  <p class="lede">{L['lede']}</p>
  <p class="upd">{L['updated']}: {UPDATED} · {L['readtime']}</p>
</div></section>

<div class="wrap">

  <div class="toc">
    <b>{L['toc']}</b>
    {" ".join(toc)}
  </div>

  <p>{L['intro']}</p>

  <div class="note warn">
    <p style="margin:0"><b>{tv_title}:</b> {L['tv']}</p>
  </div>

{chr(10).join(cards)}

  <h2>{L['h_vs']}</h2>
  <p>{L['vs']}</p>

  <h2>{L['h_buy']}</h2>
  <p>{L['buy']}</p>

  <h2>{L['h_cost']}</h2>
  <p>{L['cost']}</p>

  <h2>{L['h_safe']}</h2>
  <p>{L['safe']}</p>

  <div class="note"><p style="margin:0">{L['summary']}</p></div>

  <h2 id="faq">{L['h_faq']}</h2>
  <div class="faq">
{faq_html}
  </div>

  <div class="langs">
    <b>{L['langlabel']}</b>
    {langs}
  </div>

</div>

<footer><div class="wrap">
  <div><b style="color:#fff">{L['brandline'].split('·')[0].strip()}</b></div>
  <p class="disc">{L['disc']}</p>
</div></footer>

</body>
</html>
"""


def main():
    written = []
    for code in ORDER:
        L = LOCALES[code]
        d = os.path.join(ROOT, L["path"]) if L["path"] else ROOT
        os.makedirs(d, exist_ok=True)
        fp = os.path.join(d, "index.html")
        with open(fp, "w", encoding="utf-8") as f:
            f.write(render(code))
        written.append(fp.replace(ROOT, "").lstrip("/") or "index.html")

    # sitemap
    urls = "\n".join(
        f'  <url><loc>{url_for(c)}</loc><lastmod>{UPDATED}</lastmod><changefreq>weekly</changefreq>'
        f'<priority>{"1.0" if c=="de" else "0.9"}</priority></url>' for c in ORDER)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '\n</urlset>\n')
    print("built:", len(written), "pages ->", ", ".join(written))
    print("sitemap:", len(ORDER), "urls")


if __name__ == "__main__":
    main()
