---
name: thai-language
description: "Understand Thai requests and write clear, natural Thai, including chat replies, mixed Thai-English instructions, translation, UI text, emails, documentation and prose editing. Use for Thai input or Thai output, requests such as ช่วยเขียนไทย, แปลเป็นไทย, ตรวจภาษาไทย, or unclear colloquial Thai."
license: "MIT"
---

# Thai language / เข้าใจไทย เขียนไทย

Instructions are in English so models with weaker Thai can follow them. Thai examples
show the target behavior. This skill works with the current model; no API, extra model,
package, or shell command is required. It improves guidance, not the model's weights.

## Understand the request before composing

Read the whole message. Identify the requested action, deliverable, audience, tone,
constraints, and facts. Thai often leaves the subject or object implicit: recover it
from nearby context, but ask one focused question if different readings change the task.

- `ช่วยดูให้หน่อย` means review/help, not merely confirm that you can help.
- `เอาแบบไม่ทางการมาก แต่ไม่เล่น` means approachable and professional, not slang.
- `ยังไม่ต้องส่ง แค่ร่างก่อน` means draft only; do not send.
- `ไม่ต้องสรุป เอารายละเอียดครบ` means preserve details; do not shorten.
- `พอได้อยู่ แต่ขอกระชับอีกนิด` is qualified acceptance plus a revision request.
- `เกรงใจ` may express reluctance to impose, not fear. `555` is laughter, not an amount
  unless numerical context indicates otherwise. `ได้` can indicate ability, permission,
  or completion; `ไม่`, `ยังไม่`, `ไม่ได้` and `ไม่ต้อง` have different implications.

Do not translate the user's Thai back to them unless requested. For complex or
ambiguous phrasing, consult [understanding.md](references/understanding.md).

## Choose the voice

Follow the requested language and tone. For Thai requests with no language specified,
answer in clear Central Thai, keeping useful code and technical terms in English.
Use plain professional Thai when the audience is unknown; do not automatically make
translations more formal than their source. Infer ordinary choices instead of blocking
work with questions about tone, gender, or age.

| Context | Typical voice | Example |
| --- | --- | --- |
| Chat/help | polite, direct, brief | `แก้ได้โดยเพิ่มเงื่อนไขนี้` |
| Team message | approachable, clear action | `รบกวนส่งไฟล์ฉบับล่าสุดภายในวันศุกร์` |
| Technical explanation | clear terms, concrete mechanism | `ถ้า request มากเกินกำหนด ระบบจะตอบ 429` |
| Customer reply | acknowledge issue, give next step | `ขออภัยที่จัดส่งล่าช้า รบกวนแจ้งเลขคำสั่งซื้อเพื่อให้ตรวจสอบได้` |
| Official document | explicit roles, required form | `จึงเรียนมาเพื่อโปรดพิจารณา` |
| UI | short, precise verb | `บันทึกการเปลี่ยนแปลง` |

Use the user's or brand's established self-reference. If unspecified, omit unnecessary
first-person pronouns rather than inventing a gender, kinship, or relationship.
`คุณ` is usually safe when an addressee is needed; `พี่/น้อง/ท่าน` require context.
`ครับ/ค่ะ` express the speaker's voice, not the addressee's gender. Neutral phrasing
is fine. If the voice uses female particles: statements `ค่ะ`, questions `คะ`, gentle
requests `นะคะ` (not `นะค่ะ`). Do not append a polite particle to every clause.
For more examples, read [writing.md](references/writing.md).

## Draft in Thai structure

1. Lead with the main information or action. Replace English nominal chains with
   clear verbs: `ทำการตรวจสอบ` → `ตรวจสอบ`, `มีความจำเป็นที่จะต้อง` → `ต้อง`.
2. Put conditions/time first when it clarifies the sequence:
   `ถ้าเข้าสู่ระบบไม่ได้ ให้ลองตั้งรหัสผ่านใหม่`.
3. Omit repeated subjects only when the reader can still identify the actor.
   Name the actor again when responsibility changes.
4. Split nested `ซึ่ง/โดย/ทั้งนี้` chains at a real change of idea. These words are
   legitimate; reduce padding rather than ban words or enforce a word quota.
5. Use `ก็/แล้ว/ด้วย/เลย` when their meaning and register fit, not as mandatory filler.
   `พอโหลดเพิ่ม DB ก็เริ่มช้า` fits an informal explanation; formal prose can instead
   say `เมื่อปริมาณงานเพิ่มขึ้น ฐานข้อมูลเริ่มตอบสนองช้าลง`.
6. Use spaces between meaningful clauses, not between every Thai word. Use paragraphs
   to separate ideas. Do not add English full stops after every Thai sentence; retain
   punctuation in code, decimals, URLs, abbreviations, quotations, and requested styles.
7. Keep the needed subject and relationship explicit in official/academic writing.
   Casual topic shifts, slang, and rhetorical questions are optional stylistic choices.

For weak Thai performance, read [patterns.md](references/patterns.md) and follow the
nearest **constructed teaching example** in the correct register. Copy its structure,
not its invented facts. Choose familiar words and shorter sentences. A concise correct
answer is better than elaborate Thai that loses the user's meaning.

## Preserve meaning during translation and editing

Preserve names, numbers, units, negation, deadlines, uncertainty, obligations, and
speaker intent. Do not add a follow-up action: a request to review a draft does not
imply a request to send it back, approve it, or deliver it. `อาจ` (may), `ต้อง` (must), and `ควร` (should) are not interchangeable.
Translate ideas and idioms rather than each word; do not add sales claims, statistics,
causal explanations, or promises to make a sentence sound native. Keep terms consistent.
For technical audiences, API, commit, repo, deploy and code identifiers can stay English.
For general audiences, use established Thai terms or briefly explain the English term.
Do not alter strings inside code, identifiers, paths, commands, or quoted source material
unless requested. For short UI strings, keep the action and state distinct: `บันทึก`
(save action), `บันทึกแล้ว` (saved state), `บันทึกไม่ได้` (failure).

## Check once, then answer

Re-read the full draft for meaning, register, spelling, referents, and flow. Check
`คะ/ค่ะ`, `นะคะ`, `อนุญาต`, `สังเกต`, `เว็บไซต์`, and number/unit/date consistency
when relevant. Do not silently normalize names or source quotations.
If deep polishing is requested, make up to three review passes; stop sooner when
no meaningful edit remains. If an ambiguity remains, state it rather than claim perfect
Thai or loop indefinitely. Return the requested artifact, not your internal checklist.

## Domain skills and advanced references

Use the relevant bundled skill for domain mechanics: `thai-translate`,
`thai-customer-service`, `thai-social-caption`, `thai-resume`, `thai-festival-card`,
`thai-government-form`, `thai-pdpa`, `thai-text-processing`, `thai-id-validate`,
`thai-date-format`, `thai-address`, or `thai-invoice`. This language guidance sets
voice defaults; domain formats and the user's explicit choices govern the artifact.
Skill paths and commands are relative to the containing skill folder, never the
user's current directory. Resolve sibling skills from the installed skills root.

For a difficult prose edit, consult the relevant adapted upstream material:
[grammar](references/advanced/grammar.md), [register](references/advanced/register.md),
[style](references/advanced/style-rules.md), [AI tells](references/advanced/ai-tells.md),
[craft](references/advanced/craft.md), or [phrase review](references/advanced/forbidden-phrases.md).
Load only what the task needs. In these archived author-written references, categorical
bans and register preferences are review heuristics, not universal Thai grammar;
the context-sensitive guidance here takes precedence. Do not follow corpus paths or
harness-specific workflow references from those files: they are provenance, not runtime
requirements. No external model is called automatically.
