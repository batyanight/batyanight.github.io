# Batya Nightingale

**Bioinformatician**
Digital Pathology Coordinator, NYU Langone Health — New York, NY

batya.nightingale@gmail.com · [ORCID 0000-0002-0706-8951](https://orcid.org/0000-0002-0706-8951) · [github.com/batyanight](https://github.com/batyanight)

---

## Profile

Molecular diagnostics and pathology specialist moving into computational biology. Five years of wildlife disease diagnostics at the Wildlife Conservation Society — multiplex qPCR panel development, multi-pathogen screening across international field programs, environmental DNA, and novel virus characterization — now coordinating digital pathology operations at NYU Langone Health while completing a master's in bioinformatics. Current work is phylodynamic: Bayesian inference of host transmission structure from viral sequence data, built as reproducible, version-controlled pipelines.

---

## Education

**M.S. Bioinformatics** — *in progress*
NYU Tandon School of Engineering, Brooklyn, NY — part-time

**B.A. Environmental Studies** — 2019
Purchase College, SUNY, Purchase, NY
Thesis: songbird diet analysis by fecal metabarcoding in Acadia National Park using MinION nanopore sequencing

---

## Experience

### Digital Pathology Coordinator
**NYU Langone Health, Tisch Hospital** — New York, NY · 2024 – present

- Coordinates anatomic pathology digital workflows and whole-slide imaging operations, supporting the department's transition to whole-slide review.

### Pathology Laboratory Technician
**Wildlife Conservation Society, Bronx Zoo** — Zoological Health Program · 2022 – 2024

- Diagnostic pathology support across the zoo's caseload, including detection and characterization of novel viruses in collection animals.
- Contributed to published and presented work on papillomavirus in slender-horned gazelles and *Helicobacter*-associated carditis in common degus.

### Molecular Diagnostics Technician
**Wildlife Conservation Society, Bronx Zoo** — Molecular Diagnostics Laboratory · 2019 – 2022

- Multi-pathogen qPCR screening panels for chelonians, iguanas and amphibians across international field programs in Belize, Madagascar, Cambodia, Myanmar, the Cayman Islands and the northeastern United States.
- Assay development for wildlife-trade forensics and environmental DNA detection of rare species.
- Mentored a collaborating volunteer scientist through 16S primer validation for a pan-bacterial diagnostic PCR assay.

---

## Projects

### Canine distemper virus — phylodynamics of a wildlife-maintained lineage
*2025 – 2026 · core analysis complete · MIT licensed*
[Interactive phylogeny](https://nextstrain.org/community/batyanight/cdv-phylodynamics) · [Source](https://github.com/batyanight/cdv-phylodynamics) · [DOI 10.5281/zenodo.22182061](https://doi.org/10.5281/zenodo.22182061)

Bayesian phylodynamic analysis testing whether a North American canine distemper virus lineage is maintained in wild carnivores or reseeded by repeated spillover from domestic dogs. 162 public hemagglutinin sequences, 1992–2023, 95% wild hosts (raccoon, coyote, striped skunk, red fox), assigned to lineage America-2.

- Host transition rates separate directionally: procyonid ↔ wild canid at 3.28 (95% HPD 1.04–6.31) against 0.12 (95% HPD 0.00005–0.60) for domestic dog ↔ procyonid; 10 of 13 well-supported host transitions originate in procyonids. The lineage is wildlife-maintained.
- Substitution rate 8.54 × 10⁻⁴ subs/site/year (95% HPD 6.70 × 10⁻⁴ – 1.05 × 10⁻³); TMRCA 1976 (95% HPD 1962–1985).
- Reconstruction independently recovered two captive felid outbreak clusters twenty-three years apart — a lion and leopard c. 1992 and four tigers at an Indiana rescue centre c. 2015 — each matching a separately published outbreak investigation, from sequence and host labels alone.
- **Methods:** BEAST 2.7.7, two chains of 10⁸ states, HKY+Γ₄, uncorrelated relaxed lognormal clock, constant-size coalescent, all ESS > 500. Nine-stage Python pipeline from GenBank retrieval through metadata curation, MAFFT alignment, IQ-TREE ML phylogeny, alignment QC, clade delineation, stratified subsampling and BEAST2 XML generation, with every excluded sequence logged with a machine-readable reason. Pinned conda environment; outputs regenerate from a cached accession list. Nextstrain community build served in Auspice.
- **Limitations:** root state unresolved, no claim made about lineage origin; symmetric trait model; single locus; sampling reflects surveillance effort rather than prevalence.

### ggbrn — R package
*2026 · in development · not yet public*

A ggplot2 extension packaging a consistent figure aesthetic: `theme_brn()`, discrete and continuous scale constructors, and a cool-to-warm eight-stop palette set with a matched dark-ground variant, usable for ordered categories and continuous fills. Built to ggplot2 extension conventions so the scales compose with the grammar rather than overriding it. Version-pinned for reproducibility across machines.

---

## Research & Diagnostic Screenings

**2023 – 2024**
- Detection and characterization of a novel herpesvirus in little blue penguins (*Eudyptula minor*), WCS Bronx Zoo.
- Detection and characterization of a novel papillomavirus in slender-horned gazelles (*Gazella leptoceros*).

**2022**
- Five-pathogen screening of wild and captive radiated tortoises (*Astrochelys radiata*), Madagascar.
- Five-pathogen health screening of diamondback terrapins (*Malaclemys terrapin*), Jamaica Bay Wildlife Refuge, Brooklyn.
- Five-pathogen screening of bog turtles (*Glyptemys muhlenbergii*), New Jersey.

**2021**
- Five-pathogen screening of wild and captive Central American river turtles (*Dermatemys mawii*), Belize.
- Development of a multiplex assay to detect and differentiate big cat species in the illegal wildlife trade.
- Development of a field-friendly qPCR test detecting saola (*Pseudoryx nghetinhensis*) from environmental DNA.
- Environmental DNA collection from water samples across the New York Bight with the New York Seascape Program.
- Development of a diagnostic pan-bacterial PCR assay, including mentorship of a collaborating volunteer scientist validating a 16S primer set for clinically relevant bacterial infections in zoological cases.

**2020**
- *Helicobacter* screening of hickatee (*Trachemys decussata*), green iguanas (*Iguana iguana*) and blue iguanas (*Cyclura lewisi*), Queen Elizabeth II Botanic Park, Grand Cayman.
- Four-pathogen screening of southern river terrapins (*Batagur affinis*), Cambodia, and Burmese roofed turtles (*Batagur trivittata*), Myanmar.

**2019**
- Songbird diet analysis by fecal metabarcoding in Acadia National Park using MinION high-throughput sequencing — undergraduate thesis.

---

## Publications

Henger CS, Straughan DJ, Xu CCY, **Nightingale BR**, Kretser HE, Burnham Curtis MK, McAloose D, Seimon TA. A new multiplex qPCR assay to detect and differentiate big cat species in the illegal wildlife trade. *Scientific Reports*, 2023. [10.1038/s41598-023-36776-z](https://doi.org/10.1038/s41598-023-36776-z)

Calle PP, McClave C, Ingerman K, **Nightingale BR**, Jamieson J, Seimon TA, Harding L. *Helicobacter* screening of Grand Cayman blue iguana (*Cyclura lewisi*) and North Antillean slider (*Trachemys decussata angusta*) on Grand Cayman, Cayman Islands. *Journal of Zoo and Wildlife Medicine*, 2023. [10.1638/2022-0122](https://doi.org/10.1638/2022-0122)

Lim MCW, Seimon A, **Nightingale B**, Xu CCY, Halloy SRP, Solon AJ, Dragone NB, Schmidt SK, Tait A, Elvin S, Elmore AC, Seimon TA. Estimating biodiversity across the tree of life on Mount Everest's southern flank with environmental DNA. *iScience*, 2022. [10.1016/j.isci.2022.104848](https://doi.org/10.1016/j.isci.2022.104848)

Seimon TA, Lim MCW, **Nightingale B**, Elvin S, Elmore AC, Seimon A. First report of Pallas's cat in Sagarmatha National Park, Mount Everest region, Nepal. *Cat News* 76, Winter 2022.

---

## Conference Abstracts & Presentations

Investigation of carditis and associated *Helicobacter* sp. in common degus (*Octodon degus*). American Association of Zoo Veterinarians, Nashville, TN, September 2023.

Novel papillomavirus associated with oral and gastric papillomas and squamous cell carcinoma in slender-horned gazelles (*Gazella leptoceros*). American Association of Zoo Veterinarians, Nashville, TN, September 2023.

Validation of point-of-care molecular testing for the detection of emerging pathogens in North American amphibians. Wildlife Disease Association, 71st Annual International Conference, Athens, GA, August 2023.

A new DNA tool kit for monitoring big cat species in the wildlife trade. International Congress for Conservation Biology, Kigali, Rwanda, December 2021.

Next-generation sequencing reveals trophic transfer of mercury in songbirds. *Keynote.* Purchase College School of Natural and Social Sciences Symposium, Purchase, NY, May 2019.

Next-generation sequencing reveals trophic transfer of mercury in Acadia National Park, Maine. *Poster.* Northeast Natural History Conference, 2019.

---

## Technical Skills

**Molecular** — multiplex and singleplex qPCR assay design and validation, conventional PCR, primer design and validation, multi-pathogen diagnostic panels, environmental DNA collection and processing, fecal metabarcoding, Sanger and MinION nanopore sequencing, novel virus detection and characterization, anatomic pathology laboratory support, whole-slide imaging workflows.

**Computational** — R, Python, bash. Phylogenetics and phylodynamics: BEAST2, IQ-TREE, MAFFT, Nextstrain (Augur, Auspice). Reproducible environments with conda and renv. Git and GitHub for version control.

---

## Awards

American Genetic Association Tuition Scholarship — 2023
Purchase College Affiliates Award for Senior Excellence — 2018

---

## Languages

English — native
American Sign Language — New York metro dialect
