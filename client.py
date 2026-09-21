# -*- coding: utf-8 -*-
"""
==================================================
🔌 DISANARE+ SIMPLE CLIENT — เชื่อมต่อระบบภายนอก→ภายใน
✅ ใช้ง่ายมาก แค่ 3 ขั้นตอน: ติดตั้ง → ส่งรหัส → เรียกใช้
✅ รองรับ: ทุกภาษา / ทุกรูปแบบ / Master Token
🔐 รหัสผ่าน: AGI244 (#AGI244)
==================================================
"""
import requests

class DisanarePlusClient:
    def __init__(self, base_url: str = "http://localhost:8002"):
        """
        เริ่มต้นเชื่อมต่อระบบ
        :param base_url: ที่อยู่ระบบภายในของคุณ (เปลี่ยนถDeploy บนเซิร์ฟเวอร์)
        """
        self.base_url = base_url.rstrip("/")
        self.system_password = "AGI244"       # 🔐 รหัสผ่านระบบ #AGI244
        self.master_token = "DSR-GLOBAL-MASTER-ALL-7K-LANG-2026-9F8D7C6B4A"
        self.session = requests.Session()
        self.session.headers.update({
            "X-SYSTEM-PASSWORD": self.system_password,
            "X-API-TOKEN": self.master_token
        })
        print("✅ DISANARE+ Client พร้อมใช้งาน")
        print(f"🔐 เชื่อมต่อ: {self.base_url}")
        print(f"🔑 System Code: #AGI244\n")

    # ──────────────────────────────────────────────
    # 📋 1. ดูรายการภาษาทั้งหมด
    # ──────────────────────────────────────────────
    def get_languages(self):
        """ดึงรายการภาษาทั้งหมดในระบบ"""
        r = self.session.get(f"{self.base_url}/languages")
        return r.json()

    # ──────────────────────────────────────────────
    # 📖 2. ดึงข้อมูลพจนานุกรม (ทางลัด Master Token)
    # ──────────────────────────────────────────────
    def get_dict(self, src_lang: str, tgt_lang: str, asset_type: str = "all", limit: int = 10):
        """
        ดึงข้อมูลพจนานุกรม
        :param src_lang: ภาษาต้นทาง เช่น "TH"
        :param tgt_lang: ภาษาเป้าหมาย เช่น "EN"
        :param asset_type: ประเภท "text" | "image" | "audio" | "all"
        :param limit: จำนวนคำที่ต้องการ
        """
        url = f"{self.base_url}/api/v1/global/{src_lang}/{tgt_lang}/{asset_type}"
        r = self.session.get(url, params={"limit": limit})
        return r.json()

    # ──────────────────────────────────────────────
    # 🔑 3. สร้าง Token ใหม่สำหรับผู้ใช้อื่น
    # ──────────────────────────────────────────────
    def create_user_token(self, src_lang: str, tgt_lang: str, owner: str, region: str = "TH", scope: str = "standard"):
        """สร้าง API Token ให้ผู้ใช้ภายนอก"""
        r = self.session.post(
            f"{self.base_url}/api/token/create",
            params={
                "src": src_lang,
                "tgt": tgt_lang,
                "owner": owner,
                "region": region,
                "scope": scope
            }
        )
        return r.json()

    # ──────────────────────────────────────────────
    # 📊 4. ตรวจสอบสถานะระบบ
    # ──────────────────────────────────────────────
    def status(self):
        """ตรวจสอบว่าระบบทำงานปกติหรือไม่"""
        try:
            r = self.session.get(f"{self.base_url}/api/system-status")
            return {"connected": True, "data": r.json()}
        except Exception as e:
            return {"connected": False, "error": str(e)}


# ══════════════════════════════════════════════════
# 🌟 วิธีใช้งาน: แค่คัดลอกส่วนนี้ไปเชื่อมกับระบบของคุณ
# ══════════════════════════════════════════════════
"""
from client import DisanarePlusClient

# 1. เชื่อมต่อ
dsr = DisanarePlusClient(base_url="http://localhost:8002")

# 2. ตรวจสอบสถานะ
print(dsr.status())

# 3. ดึงพจนานุกรม
data = dsr.get_dict("TH", "EN", "all", limit=5)
print(data)
"""
