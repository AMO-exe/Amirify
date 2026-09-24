<p align="center">
  <a href="https://graphify.com"><img src="https://raw.githubusercontent.com/Graphify-Labs/graphify/v8/docs/graphify-logo.png" width="480" height="252" alt="Amirify"/></a>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇺🇿 <a href="README.uz-UZ.md">Oʻzbekcha</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/Graphify-Labs/graphify/actions/workflows/ci.yml"><img src="https://github.com/Graphify-Labs/graphify/actions/workflows/ci.yml/badge.svg?branch=v8" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/company/graphify-labs"><img src="https://img.shields.io/badge/LinkedIn-Graphify%20Labs-0077B5?logo=linkedin" alt="LinkedIn"/></a>
</p>

**Sun'iy intellektga asoslangan kod yordamchilari uchun ko'nikma.** Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro yoki Google Antigravity da `/amirify` deb yozing — u sizning fayllaringizni o'qiydi, bilim grafini quradi va siz bilmagan tuzilmani sizga qaytaradi. Kod bazasini tezroq tushuning. Arxitektura qarorlari ortidagi "nima uchun" savoliga javob toping.

To'liq multimodal. Kod, PDF, markdown, ekran tasvirlari, diagrammalar, doska suratlari, boshqa tillardagi tasvirlar, video va audio fayllarni qo'shing — amirify ularning barchasidan tushuncha va aloqalarni chiqarib, bitta grafga birlashtiradi. Videolar Whisper yordamida mahalliy ravishda transkripsiya qilinadi, sizning korpusingizdan olingan domen-maxsus so'rov bilan. tree-sitter AST orqali 25 ta dasturlash tilini qo'llab-quvvatlaydi (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> Andrej Karpati maqolalar, tvitlar, ekran tasvirlari va eslatmalarni saqlaydigan `/raw` papkasini yuritadi. amirify ushbu muammoga javob — xom fayllarni o'qishga nisbatan har bir so'rov uchun **71,5 marta** kamroq token, sessiyalar orasida saqlanadi, topilgan va xulosa qilinganlar haqida halol.

```
/amirify .                        # istalgan papka bilan ishlaydi — kod, eslatmalar, maqolalar, hammasi
```

```
amirify-out/
├── graph.html       interaktiv graf — brauzerda oching, tugunlarni bosing, qidiring, filtrlang
├── GRAPH_REPORT.md  god-tugunlar, kutilmagan aloqalar, taklif qilingan savollar
├── graph.json       doimiy graf — haftalardan keyin qayta o'qimasdan so'rov qiling
└── cache/           SHA256-kesh — qayta ishga tushirish faqat o'zgargan fayllarni qayta ishlaydi
```

Papkalarni istisno qilish uchun `.amirifyignore` faylini qo'shing:

```
# .amirifyignore
vendor/
node_modules/
dist/
*.generated.py
```

Sintaksisi `.gitignore` ga o'xshash.

## Qanday ishlaydi

amirify uch bosqichda ishlaydi. Birinchi navbatda, deterministik AST bosqichi kod fayllaridan tuzilmani chiqaradi (klasslar, funksiyalar, importlar, chaqiruv graflari, docstring lar, sabab izohlari) — LLM ishtirokisiz. Keyin video va audio fayllar faster-whisper yordamida mahalliy ravishda transkripsiya qilinadi. Nihoyat, Claude subagentlari hujjatlar, maqolalar, tasvirlar va transkriptlar ustida parallel ishlab, tushunchalar, aloqalar va dizayn asoslarini chiqarib oladi. Natijalar NetworkX grafiga birlashtiriladi, Leiden hamjamiyat aniqlash algoritmi bilan klasterlanadi va interaktiv HTML, so'rov qilinadigan JSON hamda tabiiy tildagi audit hisoboti sifatida eksport qilinadi.

**Klasterlash graf topologiyasiga asoslangan — embedding ishlatilmaydi.** Leiden hamjamiyatlarni qirralar zichligi bo'yicha topadi. Claude tomonidan chiqarilgan semantik o'xshashlik qirralari (`semantically_similar_to`, INFERRED deb belgilangan) allaqachon grafda. Graf tuzilmasining o'zi o'xshashlik signali. Alohida embedding bosqichi yoki vektor ma'lumotlar bazasi shart emas.

Har bir aloqa `EXTRACTED` (manbada to'g'ridan-to'g'ri topilgan), `INFERRED` (ishonch bahosi bilan asoslangan xulosa) yoki `AMBIGUOUS` (tekshirish uchun belgilangan) deb teglanadi.

## O'rnatish

**Talablar:** Python 3.10+ va quyidagilardan biri: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes yoki [Google Antigravity](https://antigravity.google)

```bash
# Tavsiya etiladi — Mac va Linux da PATH ni sozlashsiz ishlaydi
uv tool install amirify && amirify install
# yoki pipx bilan
pipx install amirify && amirify install
# yoki oddiy pip
pip install amirify && amirify install
```

> **Rasmiy paket:** PyPI dagi paket nomi `amirify` (`pip install amirify` orqali o'rnatiladi). PyPI dagi boshqa `amirify*` nomli paketlar bu loyiha bilan bog'liq emas. Yagona rasmiy repozitoriy — [Graphify-Labs/amirify](https://github.com/Graphify-Labs/graphify).

### Platforma qo'llab-quvvatlash

| Platforma | O'rnatish buyrug'i |
|-----------|--------------------|
| Claude Code (Linux/Mac) | `amirify install` |
| Claude Code (Windows) | `amirify install` (avto-aniqlash) yoki `amirify install --platform windows` |
| Codex | `amirify install --platform codex` |
| OpenCode | `amirify install --platform opencode` |
| GitHub Copilot CLI | `amirify install --platform copilot` |
| VS Code Copilot Chat | `amirify vscode install` |
| Aider | `amirify install --platform aider` |
| OpenClaw | `amirify install --platform claw` |
| Factory Droid | `amirify install --platform droid` |
| Trae | `amirify install --platform trae` |
| Trae CN | `amirify install --platform trae-cn` |
| Gemini CLI | `amirify install --platform gemini` |
| Hermes | `amirify install --platform hermes` |
| Kiro IDE/CLI | `amirify kiro install` |
| Cursor | `amirify cursor install` |
| Google Antigravity | `amirify antigravity install` |

Keyin AI yordamchingizni oching va kiriting:

```
/amirify .
```

Eslatma: Codex ko'nikmalar uchun `/` o'rniga `$` ishlatadi, shuning uchun `$amirify .` deb kiriting.

### Yordamchini har doim grafdan foydalanishga majbur qilish (tavsiya etiladi)

Graf qurilgandan so'ng, loyihangizda buni bir marta bajaring:

| Platforma | Buyruq |
|-----------|--------|
| Claude Code | `amirify claude install` |
| Codex | `amirify codex install` |
| OpenCode | `amirify opencode install` |
| Cursor | `amirify cursor install` |
| Gemini CLI | `amirify gemini install` |
| Kiro IDE/CLI | `amirify kiro install` |
| Google Antigravity | `amirify antigravity install` |

## Foydalanish

```
/amirify                          # joriy katalog
/amirify ./raw                    # ma'lum bir papka
/amirify ./raw --mode deep        # INFERRED qirralarini agressivroq chiqarish
/amirify ./raw --update           # faqat o'zgargan fayllarni qayta chiqarish
/amirify ./raw --directed         # yo'naltirilgan graf
/amirify ./raw --cluster-only     # mavjud grafda klasterlashni qayta ishga tushirish
/amirify ./raw --no-viz           # HTML siz, faqat hisobot + JSON
/amirify ./raw --obsidian         # Obsidian vault yaratish (opsional)

/amirify add https://arxiv.org/abs/1706.03762   # maqolani olish
/amirify add <video-url>                         # audio yuklab olish, transkripsiya qilish va qo'shish
/amirify query "Attention ni optimallashtiruvchi bilan nima bog'laydi?"
/amirify path "DigestAuth" "Response"
/amirify explain "SwinTransformer"

amirify hook install              # Git ilgaklarini o'rnatish
amirify update ./src              # kod fayllarini qayta chiqarish, LLM siz
amirify watch ./src               # grafni avtomatik yangilash
```

## Nima olasiz

**God-tugunlar** — eng yuqori darajadagi tushunchalar (hamma narsa ular orqali o'tadi)

**Kutilmagan aloqalar** — qo'shma ball bo'yicha tartiblangan. Kod-maqola qirralari yuqoriroq baholanadi. Har bir natijada tabiiy tildagi "nima uchun" tushuntirishi bor.

**Taklif qilingan savollar** — graf alohida javob bera oladigan 4-5 ta savol

**"Nima uchun"** — docstring lar, ichki izohlar (`# NOTE:`, `# IMPORTANT:`, `# HACK:`, `# WHY:`) va hujjatlardagi dizayn asoslari `rationale_for` tugunlari sifatida chiqariladi.

**Ishonch ballari** — har bir INFERRED qirrasida `confidence_score` (0,0-1,0) mavjud.

**Token benchmark** — har bir ishga tushirishdan keyin avtomatik chiqariladi. Aralash korpusda: so'rov uchun **71,5 marta** kamroq token, xom fayllarga nisbatan.

**Avto-sinxronlash** (`--watch`) — kod o'zgarganida grafni avtomatik yangilaydi.

**Git ilgaklari** (`amirify hook install`) — post-commit va post-checkout ilgaklarini o'rnatadi.

## Maxfiylik

amirify hujjatlar, maqolalar va tasvirlardan semantik chiqarish uchun fayl mazmunini AI yordamchingizning model API siga yuboradi. Kod fayllari tree-sitter AST orqali mahalliy ravishda qayta ishlanadi. Video va audio fayllar faster-whisper bilan mahalliy ravishda transkripsiya qilinadi. Hech qanday telemetriya, foydalanishni kuzatish yo'q.

## Texnologiyalar to'plami

NetworkX + Leiden (graspologic) + tree-sitter + vis.js. Semantik chiqarish Claude, GPT-4 yoki sizning platformangiz modeli orqali. Video transkripsiyasi faster-whisper + yt-dlp orqali (opsional).

## amirify ustida qurilgan — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) — amirify ustidagi korporativ qatlam. amirify fayllar papkasini bilim grafiga aylantirganidek, Penpax o'sha yondashuvni butun ish hayotingizga uzluksiz qo'llaydi.

**Tez orada bepul sinov muddati.** [Kutish ro'yxatiga qo'shiling →](https://safishamsi.github.io/penpax.ai)

## Yulduzlar tarixi

[![Star History Chart](https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date)](https://star-history.com/#Graphify-Labs/graphify&Date)
