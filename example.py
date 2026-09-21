# -*- coding: utf-8 -*-
"""
==================================================
🎯 ตัวอย่าง: วิธีเชื่อมระบบภายนอกกับ DISANARE+
รันไฟล์นี้ได้เลย: python example.py
==================================================
"""
from client import DisanarePlusClient

print("="*60)
print("🔌 DISANARE+ — ตัวอย่างเชื่อมต่อระบบภายนอก")
print("="*60)

# ═══ ขั้นที่ 1: เชื่อมต่อระบบ ═══
# ถ้า Deploy บนเซิร์ฟเวอร์ เปลี่ยนเป็น: "https://your-domain.com"
dsr = DisanarePlusClient(base_url="http://localhost:8002")

# ═══ ขั้นที่ 2: ตรวจสอบการเชื่อมต่อ ═══
print("\n📡 1. ตรวจสอบสถานะระบบ:")
status = dsr.status()
if status["connected"]:
    print("✅ เชื่อมต่อสำเร็จ!")
    print(status["data"])
else:
    print("❌ ไม่สามารถเชื่อมต่อระบบ ตรวจสอบว่ารันระบบหลักแล้วหรือไม่")
    exit()

# ═══ ขั้นที่ 3: ดูรายการภาษา ═══
print("\n🌍 2. รายการภาษาที่มีในระบบ:")
langs = dsr.get_languages()
print(langs)

# ═══ ขั้นที่ 4: ดึงพจนานุกรม ไทย→อังกฤษ ═══
print("\n📖 3. พจนานุกรม ไทย → อังกฤษ:")
data = dsr.get_dict("TH", "EN", "all", limit=5)
if "data" in data:
    for item in data["data"]:
        print(f"  • {item['word']} — ({item['pron']}) → {item['trans']}")

# ═══ ขั้นที่ 5: ดึงเฉพาะข้อความ ญี่ปุ่น→ไทย ═══
print("\n🇯🇵🇹🇭 4. ญี่ปุ่น → ไทย (เฉพาะข้อความ):")
data2 = dsr.get_dict("JP", "TH", "text", limit=3)
if "data" in data2:
    for item in data2["data"]:
        print(f"  • {item['word']} — {item['trans']}")

# ═══ ขั้นที่ 6: สร้าง Token ให้ผู้ใช้อื่น ═══
print("\n🔑 5. สร้าง Token ให้ผู้ใช้ใหม่:")
new_token = dsr.create_user_token("TH", "EN", owner="MyExternalApp", region="TH", scope="TH_EDU")
print(new_token)

print("\n✅ ทุกอย่างทำงานสมบูรณ์! เชื่อมต่อระบบภายในสำเร็จ")
print("\n💡 คำแนะนำ: นำโค้ดในไฟล์ client.py ไปรวมกับระบบของคุณได้เลยครับ")
