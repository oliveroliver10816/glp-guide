# glp-guide — GLP-1 category listicle (crawl-feeder for the money network)

**What:** A German category-overview page — "Ozempic-Alternative als Tablette? GLP-1 Kapseln 2026 im
Überblick" — that rides the huge category + brand search demand and links out to our 4 GLP-1 money
sites. Bob's idea (2026-07-22): a keyword-packed listicle of all our products, one paragraph each, that
gets crawled on the strength of fresh trending offer names → its outbound links get discovered/re-crawled.
This replaces the failed workers.dev crawl-bait (which Google never crawled — see linkspotter/indexer).

**LIVE:** https://oliveroliver10816.github.io/glp-guide/  (public, indexable)
- Isolated **clean** account `oliveroliver10816` (no money-site github.io CNAME; holds only deliverable/
  research pages). Money sites are on SEPARATE accounts → this is a one-directional feeder.
- Repo `oliveroliver10816/glp-guide`, Pages on `main` /. PAT in [[github-backup-accounts]].

## Why this works where the bait didn't (measured)
- **github.io >> workers.dev for crawl.** This page was **crawled at 2026-07-22T23:40:43Z — minutes
  after publish** (`urlInspection` = "Crawled - currently not indexed", the normal day-0 state). The
  workers.dev bait was NEVER crawled in 24h+. github.io is a high-authority, constantly-crawled domain.
- Mechanism: page gets crawled → Google follows its outbound links → our money-site pages
  (ozem-plus.store, osanix.shop, tryretafit.com/de/ + /de/reta-3/, glpure.shop) get discovered/re-crawled.

## Products & keyword targeting (grounded in real demand, not guesses)
Pulled `google.de/complete/search?client=chrome` + Everflow offer catalog before writing:
- **Ozem+** (#1) → ozem-plus.store. Strong DE brand demand (ozem plus erfahrungen/kaufen/fake oder
  echt/seriös) + our **best converter (8 conv lifetime)**. Geos DE/AT/CH/IT/PL/NL.
- **Ozalyn** (#2) → **osanix.shop** (the money site is Ozalyn-led). Target keyword = **"Ozalyn"**
  (ozalyn kapseln erfahrungen/kaufen/inhaltsstoffe) — NOT "Osanix", which is a **dead keyword**
  (autocompletes to "osanit", a baby teething product). Broad geo (UK/DE/NL/BE/DK/SE).
- **RetaFit** (#3) → tryretafit.com/de/. reta fit / reta 3 / reta abnehmen / retatrutide alternative.
  Also links the /de/reta-3/ explainer.
- **GLPure** (#4) → glpure.shop. Thin demand (glpure reviews / glp-1 supplement) → shorter paragraph.
- **Skipped:** Glowzi (verdict NO, 0 demand), Osanix-as-keyword (dead). Kept the set to ONE coherent
  category (GLP-1/weight-loss) so it can actually rank — did NOT mix in CoolJet/AC etc.

## Framing = safe (Bob's rules honoured)
- **NO review/rating markup** (per [[no-review-markup-or-framing]]). No stars, no "we rate X 4.7".
- **Category-education, not comparison-disparagement** (per [[affiliate-comparison-legal-limits]]).
  Every product is OURS (we're the affiliate), so no competitor content; framed as "which products are
  currently most-searched", ordered by demand, not "X worse than Y".
- Honest **Höhle-der-Löwen** note (rides ozem plus/glp-1 kapseln/abnehmtabletten + hdl autocomplete):
  no weight-loss product was ever on the show — applies to all of them. Sourced VZ/Mimikama.
- Full Impressum-style footer disclaimer (NEM not medicine, trademarks, affiliate commission).

## ⚠ Footprint tradeoff (flagged to Bob)
One page links all 4 money sites → a discoverable cluster tying them together. Mitigation: feeder is on
an isolated account with no other link to the money-site accounts, and the money sites don't link back
(one-directional). Accepted because Bob wants the funnel. See [[affiliate-footprint-isolation]].

## Verification / QA (all green, pre + post deploy)
- HTML well-formed, 1 JSON-LD @graph parses, 4 FAQ pairs visible⇄schema word-for-word, favicon (inline
  SVG data-URI, capsule mark), title 65ch, meta desc trimmed to ~150. Playwright: 0 console errors, no
  mobile overflow, 5 CTAs, all 4 shop hosts linked. All 5 outbound targets return 200.
- Fixed post-first-render: rank badge (1-4) was unstyled in `<h2>` (CSS scoped to `.card`) → added
  `h2 .rank`.
- **GSC-verified** as URL-prefix property (FILE method `google77a2c6704e5564a8.html`, SA
  gsc-reader@coolizi-gsc = owner) → added property (204) → **Indexing API accepted** + sitemap submitted
  (204) → **crawled within minutes**.

## Next / watch
- Re-inspect in ~2 days: does it go "Crawled → Indexed"? Does it start ranking for any category long-tail?
- If it earns crawl reliably, this is the repeatable pattern: **github.io category feeders**, one per
  vertical, GSC-verified + Indexing-API'd. Consider a UK/EN sibling (huge "ozempic pills / glp-1
  supplement uk" demand) and an IT/PL one (Ozem+ converts there, no content yet).
- Could add a few real backlinks (telegra.ph/rentry) as outbound links here too, so the crawl discovers
  them — turning this into the crawl-bait the workers.dev version failed to be.
- ⚠ github.io project-page robots.txt at the subpath is NOT read by crawlers (only domain root is);
  absent root robots = allow-all, so fine. Page-level `index,follow` meta governs.
