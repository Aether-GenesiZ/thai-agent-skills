# Constructed teaching examples / ตัวอย่างเพื่อสอน

These examples are constructed, not quotations from native authors and not empirical
proof of quality. Select by audience and preserve the user's actual facts.

## Technical explanation

Brief: The system retries a failed request at most three times, then reports an error.

Awkward: `ระบบจะทำการดำเนินการลองคำขอซ้ำซึ่งล้มเหลวเป็นจำนวนสูงสุดสามครั้ง โดยหลังจากนั้นมันจะทำการรายงานข้อผิดพลาด`

Clear: `ถ้า request ล้มเหลว ระบบจะลองใหม่ไม่เกิน 3 ครั้ง หากยังไม่สำเร็จ จะแจ้งข้อผิดพลาด`

Meaning check: maximum stays three; an error is reported only after retries fail.

## Team message

Brief: Ask colleagues to review the attached draft by Friday; don't send it to clients yet.

Clear: `รบกวนตรวจร่างที่แนบมาภายในวันศุกร์ ฉบับนี้ยังเป็นร่าง กรุณาอย่าเพิ่งส่งให้ลูกค้า`

Meaning check: review deadline remains Friday; review is different from sending.

## Customer reply

Brief: Customer says a package is late. Ask for the order number; delivery date is unknown.

Clear: `ขออภัยที่พัสดุล่าช้า รบกวนแจ้งเลขคำสั่งซื้อเพื่อให้ตรวจสอบสถานะการจัดส่งได้`

Meaning check: no invented arrival date, refund or tracking result.

## Translation: preserve modality

Source: "You may cancel before Friday. You must keep the receipt."

Clear: `ยกเลิกได้ก่อนวันศุกร์ และต้องเก็บใบเสร็จไว้`

Meaning check: permission is not obligation; before Friday is not through Friday.

## UI states

Save: `บันทึก` · Saved: `บันทึกแล้ว` · Could not save: `บันทึกไม่ได้`
Permission denied: `ไม่มีสิทธิ์เข้าถึง` · Retry: `ลองอีกครั้ง`

## Tone pairs, same facts

Brief: The service is unavailable Saturday 22:00–23:00 for maintenance.

Team/chat: `คืนวันเสาร์ เวลา 22.00–23.00 น. ระบบจะปิดปรับปรุง ช่วงนี้จะใช้งานไม่ได้`

Business announcement: `แจ้งปิดปรับปรุงระบบในวันเสาร์ เวลา 22.00–23.00 น. ระหว่างดำเนินการจะไม่สามารถใช้งานระบบได้`

Do not add "security upgrade", "faster afterwards", or "data unaffected" without evidence.
