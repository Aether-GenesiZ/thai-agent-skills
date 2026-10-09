# Reading colloquial and mixed Thai

Thai text often omits subjects, punctuation, or spaces. Read clauses as a whole.
Do not split text on spaces to identify words; if programming segmentation, use
thai-text-processing. Normalize Thai numerals for calculation, retaining the original
form for quotations. Do not strip combining marks or replace visually similar letters.

| User phrase | Intended constraint or nuance |
| --- | --- |
| `ยังไม่ต้องแก้ ขอ review ก่อน` | Review now; edits are not yet requested |
| `แก้ได้เลย แต่ห้ามเปลี่ยน API` | Editing authorized; preserve the API |
| `ไม่ใช่ว่าทำไม่ได้ แค่ยังไม่อยากทำ` | Possible, but currently unwanted |
| `ส่งพรุ่งนี้ได้ไหม` | Request about tomorrow's delivery; not confirmed delivery |
| `ส่งพรุ่งนี้ได้` | Can deliver tomorrow; context determines promise vs capability |
| `ได้ส่งแล้ว` | Has sent; completion, not ability |
| `พอไหว` | Manageable/tolerable, not enthusiastic endorsement |
| `ไม่ค่อยโอเค` | Negative judgment softened for politeness |
| `เดี๋ยวขอดูก่อน` | Wants time to review; not approval |
| `เอาอันเดิม แต่ปรับให้ลื่น` | Preserve previous content; improve flow |
| `ไม่เอาแปลตรงตัว` | Translate meaning into natural Thai |
| `ช่วย clone แล้ว fork ให้หน่อย` | Requested actions; common mixed-language phrasing |

Treat a typo as a likely typo only when context strongly supports the reading.
For a material ambiguity, ask specifically: `หมายถึงให้ยกเลิกรายการนี้ หรือแค่เลื่อนวันส่ง?`
Do not invent an object when multiple files, people, or tasks are plausible.
Relative dates such as `วันศุกร์หน้า` can be ambiguous. Resolve from known current
date/timezone, or ask for a calendar date when the deadline matters. Explicit พ.ศ.
and ค.ศ. override numerical heuristics. Never double-convert a BE year.

Scope negation carefully: `ไม่ต้องส่งทุกไฟล์` might mean "not every file is needed"
or "do not send any files" in context. Clarify before a consequential action.
Sarcasm such as `ดีมาก ล่มอีกแล้ว` is frustration, not praise of an outage.
Regional language or specialized royal vocabulary may need reference lookup; do not
pretend Central Thai examples establish the correct dialect or rank-specific term.
