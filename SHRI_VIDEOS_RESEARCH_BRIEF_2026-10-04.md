# Shri Videos: what Master AI holds, where the project stands, and a first-phase plan for Krupali

Prepared 2026-10-04 by Claude Code for Dr. Shah and Yash. Research only: nothing in Master AI, Drive, Gmail or the Shri files was changed, and nothing was downloaded except Internet Archive *metadata* (file lists and sizes).

---

## 1. Short answer

**Yes. Acquiring a large body of source material first is the recorded plan.** Master AI does not name a person for it yet.

- The project is in **Phase 0B, Research Foundation**. No production footage is to be made until the research and canon gates pass (`00_MASTER_GUIDE.md`, "Current Phase").
- On 2026-09-21 a decision was added to `SHREEJI_PRODUCTION_SYSTEM`: stop redundant AI-tool research, but "do **not** reduce Shrinathji/Pushtimarg historical and devotional source acquisition." Before story lock, run an audit: **what we have → what is missing → what to acquire → what is sufficient.**
- On 2026-09-16 you told Gemini you plan to download "another 300 GB of information on religious subject to make movie" (Master AI finding GEMINI-G-16). Your 2 TB Google plan covers that.

**The record also says to do it in controlled steps, not as one blind bulk download.** All three canonical files agree on the order (`TECH_04_SOURCE_ACQUISITION_ENGINE_RESEARCH_SPEC` §10–12, Master Guide, CHANGELOG 2026-09-14):

1. List what is available.
2. Make a rights-checked download list (the "manifest").
3. Run a 1 GB proof.
4. Grow to 10 GB, then 50 GB, then 200 GB, measuring quality at each gate.

**Nothing has been downloaded yet:**
- The source registry has 0 rows.
- The acquisition queue has not changed since 2026-09-13.
- Every evidence folder in Drive is empty.
- The Internet Archive inventory script was never run.

**The first target is ready and larger than recorded** (section 5). The Internet Archive "Pushtimarg" upload holds 2,456 books and PDFs: 66 GB in total, about 51 GB after exact duplicates are removed. That one source covers the 50 GB gate.

**Where the real work is:** downloading 51 GB takes hours. Logging, de-duplicating, rights-tagging and OCR-ing it takes weeks. That cataloguing is what makes the material usable and citable, and it is the right core job for Krupali.

**Krupali appears in no record.** Gmail, Calendar, WhatsApp, Drive, Dropbox, Master AI, and the ChatGPT, Gemini and DeepSeek archives were all searched. Their name, email, start date and language skills need to be added (section 9).

---

## 2. Where everything lives

The Shri project folder is **`G:\My Drive\MASTER_AI\01_COMMERCIAL_VENTURES\`**.
- It is the old `G:\My Drive\Shri Videos` folder, renamed on 2026-09-20 during a Gemini-guided folder move (Master AI findings SHRI-DRIVE-FILING-20260920, GEMINI-F-02/F-03).
- Drive folder ID: `1roi3Sm3waglNqSwWhhwkaRbrs0BBZylr`.
- It is a **Drive-live** folder: it is not frozen, and the nightly C:→Drive copy does not touch it (`C:\MASTER_AI\config\drive_mirror_filters.txt`).

| File | What it is | State |
|---|---|---|
| `00_MASTER_GUIDE.md` | Project constitution: mission, rules, phase, next steps | Updated 2026-09-15 |
| `CHANGELOG.md` | Decision history | Last entry 2026-09-15 |
| `00_GOVERNANCE/RIGHTS_ACCESS_AND_SACRED_MATERIAL_POLICY.md` | Rights and sacred-status rules | v0.1 |
| `01_RESEARCH_FRAMEWORK.md` | Source tiers A–E, claim labels, quality gate | Done |
| `02_VALLABHACHARYAJI_SHRINATHJI_CHRONOLOGY.md` | Working chronology | v0.1, many open questions |
| `03_SHRINATHJI_PRAKATYA_AND_BRAHMSAMBANDHA.md` | Source-controlled dossier | v0.1 |
| `04_THEOLOGY_AND_SEVA_GLOSSARY.md` | Terminology guide | v0.1 |
| `TECHNICAL_ARCHITECTURE/TECH_01`, `TECH_02` | Knowledge-vault design and data schema | Design only |
| `TECHNICAL_ARCHITECTURE/TECH_03` | AI film/VFX production research | Research only |
| `TECHNICAL_ARCHITECTURE/TECH_04_..._SPEC` (Google Doc) | **The canonical acquisition specification** | Authorizes bounded manual batches; no background crawler |
| `SHRI_SOURCE_REGISTRY` (Google Sheet, ID `1cSChrs88unreXBFb0tO7blofUAIRkplLt0UM-ny5fRk`) | Master list of every acquired source | **Header row only, 0 sources** |
| `SHRI_ACQUISITION_QUEUE` (Google Sheet, ID `1mS78P-62noNkbuluXA4eGgLspNz0fk8PlK5_FLqpDhM`) | 12 target repositories (AQ-0001 to AQ-0012) | All still pre-acquisition |
| `SHRI_VIDEOS_RESEARCH_LEDGER` (Google Doc) | Research loop log; current P0 question is "Visual Canon and continuity" | Updated 2026-09-21 |
| `40_PRODUCTION/SHREEJI_PRODUCTION_SYSTEM`, `30_STORY_DEVELOPMENT/.../SHREEJI_STORY_EPISODES` | Production pipeline; story rules and Episode 1 concept (not canonical) | — |
| `10_RESEARCH_LIBRARY/` (7 subfolders), `99_SYSTEM_INDEX/` (7 subfolders), `20_`–`80_` | Where originals, extracted text, manifests and hashes go | **All empty** apart from 3 AI-film screenshots |
| `90_ARCHIVE/IMPLEMENTATION_STARTERS/SHRI_SOURCE_ACQUISITION_STARTER.zip` | `shri_ia_inventory.py`, an Internet Archive metadata-inventory script | Never run; has a bug (section 5) |

Outside that folder:
- **Loop 2 agent prompt.** `Shri Videos — Loop 2_ Source Acquisition & Corpus Processing Agent.md` is now only in `Dropbox\PC Downloads` and Drive "PC Downloads" (ID `1u4S_5VzQpxj6x0o5ErMYXLGY8QRdgHMJ`). Its general method is good, but it is aimed at film and VFX sources and describes a continuous crawler, which TECH_04 forbids. TECH_04 takes precedence.
- **Master AI registry.** Shri is system **SYS-053**, recorded as "Always separate. Only the 52-video religious project." Its home file has not been chosen (`MASTER_SYSTEM_REGISTRY.md` B1 row 31).
- **The only Shri email to Yash** is "Shri Videos – Computer Setup Plan" (2026-10-03). It says: don't buy a computer yet; first choose an office desktop spec of about ₹60–90k (32 GB RAM, 1 TB SSD, NVIDIA GPU) and check Indian prices; Google Drive is permanent storage. The thread has no reply yet.

---

## 3. The project in one page (from the canon)

- **Mission:** a cinematic, spiritually respectful Shreeji/Pushtimarg storytelling universe for global audiences.
  - Quality comes before cost.
  - Story first, emotion second, beauty third.
- **Format:**
  - Flagship: about **52 weekly episodes of 12–15 minutes** in chronological order.
  - Also 30–60 second shorts and about 3-minute stories.
  - Possible Gujarati and Hindi versions.
- **First milestone:** a 45–60 second, 8–12-shot "cinematic proof". There is **no target date**, and gates are never weakened to meet a deadline.
- **Three approval gates:**
  1. historical/religious;
  2. cinematic/creative;
  3. technical/continuity.
- **"AI is never the religious authority."**
  - Keep documented history separate from devotional tradition. Every claim is labelled HISTORY, TRADITION, THEOLOGY, DRAMATIZATION, VISUAL-INFERENCE or OPEN.
  - Sacred mantras are not to be published or put into scripts without authority review.
- **Team plan as written** (Master Guide, "Team Strategy"): Dr. Shah plus AI first. "After the production method is proven, consider training 1–2 India-based team members:
  1. AI video operator/editor;
  2. research/religious-accuracy assistant.

  They should execute a documented system rather than inventing a new workflow."
  - Krupali fits role 2.
  - Hiring now is earlier than written, so record it as a decision (section 9).
- **Delegation:** Master AI records Yash as "human executive coordinator" who "can assign and supervise India workers". That supports Krupali reporting to Yash.

---

## 4. What exists versus what is missing

**Done (design and early research):**
- Rights and sacred-material policy.
- Research framework with source tiers.
- Chronology, prakatya/Brahmasambandha dossier and glossary (all v0.1).
- Knowledge-vault schema with ID formats such as `SHR-SRC-000001`.
- 12-row acquisition queue and registry template.
- A metadata inventory script.
- Production-research notes.

**Not done:**
- **Zero sources acquired or registered.**
- AQ-0001 inventory and rights manifest: not started. Today's metadata snapshot (section 5) is a head start, not the approved manifest.
- Multilingual OCR benchmark (TECH_02 §14) and the **1 GB end-to-end proof**.
- `05_EIGHT_DARSHAN_REFERENCE_TABLE.md`: named as the next content step since 2026-09-12, never created.
- 3–5 named scholar or Vaishnav reviewers: none named.
- The daily ChatGPT "Shri Research Loop" automation was **turned off** on 2026-09-14 and ran once.

**Primary texts that research files 02–04 say must be acquired** (to settle open questions such as the 1493 encounter date, Gokul vs. Jharkhand, and the Damodardas "heard but did not understand" passage):
- an authoritative *Siddhanta Rahasya* edition;
- the Damodardas Harsani section of *Chaurasi Vaishnavan ki Varta*;
- *Shrinathji (Govardhannathji) Prakatya Varta* attributed to Hariray;
- *Nij Varta*;
- *Baithak Charitra*;
- *Pushti-pravaha-maryada-bheda* and *Seva-phala* with commentary;
- *Shodash Granth*;
- named scholarship: Entwistle, *Braj*; F. M. Smith 2009; Pauwels & Bachrach 2018; Bachrach 2022; Bennett; Parekh; Barz; Dasgupta Vol. IV.

---

## 5. New today: the first target, measured

I read the Internet Archive's public metadata. These numbers are measured, not estimated. The full file list is in **`AQ-0001_IA_Pushtimarg_metadata_snapshot_2026-10-04.csv`** in this folder.

**What it is:** `archive.org/details/Pushtimarg` is **a single upload, not a collection.**
- Uploaded 2017 by a community account (`pushtirassagar@mail.com`).
- Described as "Online Library of rare Pushtimargiya ebooks…".
- **No license is stated.**

**Size:**

| Measure | Value |
|---|---|
| Original PDF/EPUB files | 2,456 files, 66.2 GB |
| After removing exact duplicates (same MD5) | 1,692 files, about 51.1 GB (567 duplicate groups, about 15 GB of waste) |
| Scanned PDFs needing OCR | 999 of the 1,692 unique files, about 44.9 GB |
| Archive.org's own derived files | 198 GB. Not needed: download originals only |

The queue's estimate was "1,000+ books / ~20+ GB". The real total is about 2.5 times that. Many further near-duplicates have different file names, for example "252 Vaishnav Vaartaji…" and "252VaishnavVaartaji…".

**Languages** (guessed from file names): Gujarati about 650, Hindi about 610, English about 175, Sanskrit about 165, Vraj Bhasha about 57, unmarked about 790.

**Key primary texts it contains** (matched by file name; still to be checked by opening the files):

| Text | Unique files | Example |
|---|---|---|
| Siddhanta Rahasya | 8 | `Siddhant-Rahasya-Darshan-1-1729.pdf` |
| Shreenathji Prakatya Varta | 5 | `Shreenathji Prakatya Vaarta Vraj Bhasha 1956 (Vaarta Sahitya).pdf` |
| Nij Varta | 1 | `Nijvarta Gahruvarta Tatha Courashi Vaishnavanki Varta Vraj Bhasha 1959` |
| 84 Vaishnav Varta | 17 | incl. an illustrated 1883 edition, about 1.09 GB |
| Shodash Granth | 24 | `16WorksOfShriVallabhacharya…`, `NibandhWithShodashgranth…` |
| Pushti-pravaha-maryada / Seva-phala | 7 | `SevaPhalamWith-14-Comment…` |
| Also | — | Subodhini (116 files, 6.3 GB), Anubhashya (44), 252 Vaishnav Varta (49), Hariray (32), Gusainji (20), Kirtans (76), 84 Baithak (8) |

The core primary texts come to **61 unique files, about 2.5 GB**, or about 1.4 GB without the 1.09 GB 1883 edition. That makes a natural **1 GB proof batch**: it is exactly what files 02–04 are waiting on.

**Script bug to fix before use:** `shri_ia_inventory.py` searches `collection:Pushtimarg` by default, which returns **0 results**. It must be run with `--query identifier:Pushtimarg`. It also:
- never computes SHA-256 (it imports `hashlib` but doesn't use it);
- restarts its summary counts after `--resume`;
- can write duplicate rows if interrupted.

**More beyond AQ-0001:** a wider archive.org search (pushtimarg OR pushti OR vallabhacharya OR shrinathji OR nathdwara) finds **1,008 items**: 649 texts, 227 audio, 96 image and 32 video. They total about 1.1 TB *including* archive.org's derived files, so the originals are much smaller. These are good AQ-0001b candidates once the main item is done.

**Rights position.** This is my reading of the policy; Dr. Shah decides.
- The Shri policy allows a **private research copy** of lawfully reachable material.
- With no stated license, every file starts as `RIGHTS_UNKNOWN`. Older editions such as 1883, 1903 and 1927 may be public domain in India; modern editions such as 1988 and 2005 probably are not.
- Archiving is fine. Quoting, filming or publishing needs a per-title rights decision.

---

## 6. Rules Krupali must follow

Condensed from the rights policy, research framework and TECH_02/TECH_04:

1. **Lawful access only.** Never bypass logins, paywalls or DRM. "Publicly downloadable" does not mean public domain.
2. **Having a file is not permission to use it.** Record copyright status, sacred/cultural status and allowed uses as separate fields. Never infer one permission from another.
3. **Originals are permanent evidence.** Never edit or overwrite them. OCR text, Markdown and translations are separate "derivative" files.
4. **Every file gets the full record:**
   - a Source ID (`SHR-SRC-000001` style);
   - a SHA-256 hash;
   - a registry row with URL, access date and method, language and script, edition/year, size, and rights and sacred status.
   - No row means not acquired.
5. **De-duplicate by hash, but keep different editions.** A 1927 and a 1968 edition are different sources.
6. **Native text first.** OCR only scanned pages, using local tools. Never put whole books through paid AI.
7. **Handwritten manuscripts are a separate, slower lane.** Keep the page image. Every transcription needs qualified human review before anyone relies on it.
8. **Tag every visual reference with its period.** Later Nathdwara art is not evidence for 15th/16th-century Braj.
9. **Sacred mantras or ritual formulas** never go into scripts, prompts or public material without authority review.
10. **Checkpoint every batch to Drive** so work can restart from Drive, not from memory.

---

## 7. Proposed first-phase plan for Krupali (under Yash)

**This is a proposal for Dr. Shah's approval.** Nothing below has been started.

| Step | Work | Output | Gate |
|---|---|---|---|
| 0. Setup | Decide access (section 9). Krupali gets the Shri folder only, never the MASTER_AI root, which holds unrelated private records. Local working folder; Python; about 150 GB free disk | Access confirmed | Dr. Shah |
| 1. Read-in (1–2 days) | Master Guide, rights policy, research framework, glossary, this brief | Questions list to Yash | Yash |
| 2. AQ-0001 manifest | Start from the snapshot CSV:<br>• pick one copy per duplicate group<br>• normalize title, language, edition year<br>• flag near-duplicates<br>• assign a first rights label<br>• mark the core-text batch | Approved download manifest | Dr. Shah/Yash approve |
| 3. 1 GB proof | Download the core primary texts:<br>• check each file's MD5 against archive.org<br>• compute SHA-256<br>• assign Source IDs<br>• fill registry rows<br>• store originals in `10_RESEARCH_LIBRARY/01_ORIGINAL_SOURCES` | Registry rows + measured results: duplicates, failures, time | Dr. Shah reviews before scaling |
| 4. 10 GB → 50 GB | The rest of the AQ-0001 unique files, in batches, same procedure | Weekly status from Yash: counts, GB, duplicates, failures, rights flags | Each gate approved |
| 5. Small, high-value parallel lane | Met Museum open-access Shrinathji/Nathdwara/pichwai images (AQ-0003, CC0), with period tags | Visual reference set | Yash |
| 6. Source-library audit | Have / missing / acquire / sufficient, checked against the open questions in files 02–04 | Audit table that drives the next downloads (DLI, HathiTrust, Google Books, IGNCA) | Dr. Shah |

**OCR comes after the proof, not during.**
- About 45 GB of the material is scanned and needs OCR.
- TECH_02 §14 requires a small multilingual test first: 30–60 pages of Gujarati, Hindi, Sanskrit and handwritten material, measuring accuracy. That test picks the tool.
- Krupali's reading ability in Gujarati, Hindi and Vraj Bhasha is valuable here, for checking OCR and naming editions correctly.

**Krupali's role does not include:** religious or historical judgments, choosing story content, or contacting temples, havelis, ACK or rights holders. All of these stay with Dr. Shah and the reviewers the framework calls for.

---

## 8. Small fixes needed before downloading starts

1. **Registry columns.**
   - Add what TECH_04 §5 and the rights policy require but the sheet lacks: acquisition method, script, sacred/cultural status, per-use permissions (archive, internal research, public display, film use, model training), reviewer/verification, and duplicate group.
   - Pick **one** status vocabulary. The rights policy's list and TECH_01/02's list differ; I recommend the policy's.
2. **Inventory script.** Fix the query (`identifier:Pushtimarg`), add SHA-256 on download, and fix the resume counters.
3. **Computer.** The Oct 3 plan (office desktop, 1 TB SSD) is enough for this phase. About 51 GB of originals, plus OCR output, plus working space fits easily. OCR speed is the only real hardware question, and the benchmark will answer it.
4. **Stale Master AI paths.** SYS-053 and MASTER_INVENTORY still point to `G:\My Drive\Shri Videos` and a Downloads copy of the Loop 2 file. Neither exists any more.

---

## 9. Decisions only Dr. Shah can make

1. **Krupali's role.** Confirm it is "research/acquisition assistant under Yash", and record in the Master Guide that India staffing starts now, ahead of the "after the method is proven" rule.
   - Also needed: Krupali's full name, email, start date, hours, and languages (Gujarati / Hindi / Sanskrit / Vraj Bhasha).
2. **Access (Master AI DEC-016, open).** Choose one:
   - (a) share only the Shri folder with Krupali and Yash; or
   - (b) Master AI's current recommendation, "task-scoped copies only", e.g. a separate shared intake folder that you or Yash move into the canon.

   Either way, never share the MASTER_AI root. It holds tax, legal, medical-practice and credential-bearing files. One of Yash's to-do files contains a portal login.
3. **Project home and name.** Master AI row B1-31 asks where Shri's home file lives, and whether to rename `01_COMMERCIAL_VENTURES` back to "Shri Videos". This empty `VS Shri videos` folder could become the working-code home, with Drive staying the archive.
4. **Pace.** Recommended: keep the staged gates but move fast (1 GB proof in the first week, then 10 GB and 50 GB). The alternative, pulling all 51 GB at once, makes the download easy and the catalogue hard.
5. **Rights stance on the archive.org upload.** Private research archive allowed, every file `RIGHTS_UNKNOWN` until reviewed, no public or film use without a per-title decision?
6. **Episode format conflict.**
   - The canon says about 52 episodes × 12–15 minutes, plus a 45–60 s proof first.
   - The Oct 3 email to Yash says "about one 30-minute video per week".
   - Which is current?
7. **Size expectation.** The Master Guide says not to record the earlier "≈2 TB" figure. Master AI separately records your own projection of "a couple of terabytes". The measured core source today is about 51 GB unique, plus the wider related material on archive.org. Treat 2 TB as a ceiling, not a target.

---

## 10. Other inconsistencies found (for the next Shri sync)

- **ID formats:** files 03/04 use `SHR-SRC-PRK-001` / `SHR-SRC-GLS-001`; TECH_02 mandates `SHR-SRC-000001`.
- **Status lists:** source lifecycle DISCOVERED → ACQUIRED → PROCESSED → RESEARCHED appears in the CHANGELOG and TECH_04 but not in the TECH_02 schema.
- **Author conflict:** *Religious Reading and Everyday Lives in Devotional Hinduism* is credited to Emilia Bachrach in file 03 and to "Hanna H. Kim" in file 04. It needs checking.
- **Stale dates:** the chronology (file 02) still shows "c. 1493/1494"; file 03 says not to inherit 1492/93/94 until a calendar conversion is done.
- **TECH_03 problems:**
  - TECH_02 points the OCR benchmark at a "new TECH_03_INGESTION_BENCHMARK.md", but TECH_03 is now the film-research file.
  - TECH_03 has two sections numbered §24.
- **Loop 2 file vs. TECH_04:** the Loop 2 prompt (continuous, film/VFX-focused) conflicts with TECH_04 (bounded batches, Pushtimarg-focused). TECH_04 governs.
- **Boundary leaks:**
  - Arizona Land Intelligence files appear in the Shri ChatGPT project's file store.
  - Ramayana titles appear as format examples in the research ledger.
  - Shri is meant to stay separate.

---

## Sources used

- **Shri canon:** `G:\My Drive\MASTER_AI\01_COMMERCIAL_VENTURES\` (all `.md` files, plus the 6 Google Docs/Sheets read through the Drive connector).
- **Master AI:** `C:\MASTER_AI\00_INVENTORY\MASTER_GAPS.md` (GAP-B05, GAP-B12, SHRI-DRIVE-FILING-20260920, GEMINI-F-02/F-03/G-16, DEC-016), `MASTER_SYSTEM_REGISTRY.md` (SYS-053, B1 row 31), `MASTER_INVENTORY.md`, `OPEN_ACTIONS.md` (MA-012 step 4), `config\drive_mirror_filters.txt`, `WORKER_REGISTRY.md`.
- **Gmail:** "Shri Videos – Computer Setup Plan" (2026-10-03, Dr. Shah → Yash). Earlier Yash threads, for how work is delegated.
- **AI chat archives:**
  - ChatGPT export of 2026-09-21: 9 Shri-related chats; none covers acquisition or Krupali.
  - Gemini chats 8dee926895055e52 (2026-09-16, the 300 GB plan) and 5e66a599b9b4a2ec (2026-09-20, folder move).
- **Internet Archive:** public metadata API, read 2026-10-05 UTC (`archive.org/metadata/Pushtimarg`; advanced search).
