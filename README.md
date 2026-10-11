# Thai Agent Skills

ชุด skill ภาษาไทยที่รวมและปรับปรุงจาก
[claude-thai-skills](https://github.com/Boom-Vitt/claude-thai-skills) และ
[kien-thai](https://github.com/chakrit/kien-thai) สำหรับ AI agent
มี plugin เดียว ประกอบด้วย 13 skills ใช้รูปแบบ `SKILL.md` พร้อม YAML frontmatter

`thai-language` เป็นแกนกลาง: อ่านคำขอภาษาไทย เขียน/แปล/แก้ภาษาไทย เลือกระดับภาษา
รักษาความหมาย ตัวเลข คำปฏิเสธและเงื่อนไข รองรับข้อความสั้นและไทยปนอังกฤษ
คำอธิบายเป็นอังกฤษคู่กับตัวอย่างไทย เพื่อให้โมเดลที่ใช้ไทยยังไม่คล่องทำตามได้
ไม่ต้องเรียกโมเดลอื่นหรือส่งข้อความไป API เพิ่ม

อีก 12 skills ครอบคลุมการแปล แคปชั่น ตอบลูกค้า เรซูเม่ คำอวยพร หนังสือราชการ
PDPA การประมวลผลข้อความ เลขบัตร/PromptPay วันที่ ที่อยู่ และใบกำกับภาษี
ดูข้อที่แก้และขอบเขตการ review ใน [docs/REVIEW.md](docs/REVIEW.md)

Skill เป็นคำแนะนำและตัวอย่าง ไม่ได้เพิ่มความรู้ภาษาไทยในน้ำหนักโมเดล ผลขึ้นกับโมเดล
และงานที่ทำ การผ่าน smoke test ไม่ได้พิสูจน์ว่าเขียนไทยได้ดีทุกประเภท

## ติดตั้ง

ต้องมี Python 3.9+ สำหรับ installer; การใช้ skill หลักไม่ต้องมี Python
Repo: [Aether-GenesiZ/thai-agent-skills](https://github.com/Aether-GenesiZ/thai-agent-skills)
Public repository; cloning and local installation require no GitHub account.

```bash
git clone https://github.com/Aether-GenesiZ/thai-agent-skills.git
cd thai-agent-skills
python3 scripts/install.py --harness all --dry-run
python3 scripts/install.py --harness all
python3 scripts/install.py --harness all --check
```

| Harness | Default skill directory |
| --- | --- |
| agy CLI | `~/.gemini/antigravity-cli/skills/` |
| Claude Code | `~/.claude/skills/` |
| Hermes | `~/.hermes/skills/` |
| Codex | `~/.codex/skills/` |

รองรับ `CLAUDE_CONFIG_DIR`, `HERMES_HOME`, `CODEX_HOME`
installer คัดลอกทั้งโฟลเดอร์ รวม references/scripts/templates/licenses
ตรวจทุกปลายทางก่อนเขียน ไม่ทับ skill ของคนอื่นหรือไฟล์ที่ผู้ใช้แก้
รันซ้ำได้และอัปเดตสำเนาที่ installer เป็นผู้ติดตั้งได้
โฟลเดอร์ปลายทางอาจได้สำเนาคนละเวอร์ชันหากเกิด disk failure ระหว่างติดตั้งหลาย harness;
ใช้ `--check` ตรวจและรัน installer ซ้ำหลังแก้สาเหตุ

สำหรับ IDE, โปรไฟล์ Hermes หรือ harness อื่นที่อ่าน Agent Skills:

```bash
python3 scripts/install.py --target ~/.gemini/antigravity/skills
python3 scripts/install.py --target /path/to/isolated-hermes-profile/skills
python3 scripts/install.py --target /path/to/harness/skills
```

ถ้าโปรไฟล์ Hermes ตั้ง `skills.external_dirs` ให้อ่านชุดหลักอยู่แล้ว ให้ติดตั้งที่ชุดหลักเท่านั้น
สำเนาชื่อเดียวกันในสองตำแหน่งทำให้ Hermes ปฏิเสธการโหลดเพราะชื่อชนกัน
ถอนการติดตั้งที่ installer เป็นเจ้าของได้ด้วย `--uninstall` (จะไม่ลบไฟล์ที่ถูกแก้)

หากต้องการเฉพาะภาษาไทย ให้ copy `skills/thai-language/` ทั้งโฟลเดอร์ไปยัง skill directory
ของ harness ไม่ควรติดตั้งแบบ copy และ plugin ซ้ำกันใน harness เดียว
เครื่องมือที่ไม่รองรับ Agent Skills ต้องใช้วิธีเพิ่ม instruction ของเครื่องมือนั้น
จึงไม่รับประกันว่าจะติดตั้งอัตโนมัติได้กับทุก harness ที่มีอยู่

Claude Code ติดตั้งทั้งชุดจาก GitHub ผ่าน plugin marketplace ได้
ผ่าน marketplace ของ repo นี้:

```text
/plugin marketplace add Aether-GenesiZ/thai-agent-skills
/plugin install thai-agent-skills@thai-agent-skills
```

หาก clone repo ไว้แล้ว ใช้ `/plugin marketplace add /absolute/path/to/thai-agent-skills`
เพื่อติดตั้งจากโฟลเดอร์ local ได้เช่นกัน

เปิด session ใหม่หลังติดตั้ง สำหรับ Hermes สามารถ preload ด้วย `hermes -s thai-language`
หรือพิมพ์ `ใช้ skill thai-language ช่วยแก้ข้อความนี้…` ใน harness ใดก็ได้
Codex เรียกแบบ `$thai-language` ได้ ใช้กับคำตอบปกติได้ ไม่จำกัดเฉพาะบทความยาว

## ตรวจสอบและทดสอบ

```bash
./scripts/test-all.sh
python3 scripts/smoke.py --harness claude codex hermes agy
```

คำสั่งแรกตรวจ frontmatter, manifest, utility self-tests และ regression tests
คำสั่งหลังรันโมเดลจริงในโฟลเดอร์ชั่วคราว อาจใช้โควตาหรือมีค่าใช้จ่ายของ provider
ใช้โมเดลที่ตั้งค่าอยู่ ไม่เปลี่ยน configuration ถาวร
ผลอยู่ใน `evals/results/` และตรวจว่าขอโหลด skill, รักษาความหมายพื้นฐานและตอบ UI ได้
ควรดู tool trace เพื่อยืนยันการโหลดจริง และอ่านงานตัวอย่างด้วยตนเองเพื่อประเมินความลื่นไหล
สร้าง zip สำหรับแจกหรือติดตั้งแบบ local plugin ได้ด้วย `python3 scripts/package.py`
ไฟล์อยู่ที่ `dist/thai-agent-skills-0.1.1.zip` และเก็บโครงสร้างสำหรับ `claude --plugin-dir`

ผลการตรวจเครื่องนี้อยู่ที่ [docs/VERIFICATION.md](docs/VERIFICATION.md)

## ที่มาและ license

MIT ทั้งสองต้นทาง เก็บ copyright และ license ใน `licenses/` และในแต่ละ skill ที่ติดตั้ง
commit ต้นทางอยู่ใน `sources.json` ไม่ดึง corpus บทความภายนอกหรือ excerpt collection
มาแจกเพิ่ม advanced references เป็นกฎและคำอธิบายของต้นทาง
`kien-thai`/`kode-thai` ถูกผสานเป็นแกนภาษาและการตรวจทานแบบจำกัดจำนวนรอบ
ไม่มี dependency ข้าม skill สองตัวหรือการเรียก Thai-native model อัตโนมัติ

## Contributing and support

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md),
[SECURITY.md](SECURITY.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md),
and [CHANGELOG.md](CHANGELOG.md). Code and skill instructions are MIT licensed;
see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for upstream attribution
and the province-data licensing exception.
