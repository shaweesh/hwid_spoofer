# 🛠️ HWID Spoofer (Educational Project)

هذا المشروع التعليمي يهدف لفهم كيف تعتمد الألعاب والبرامج على **Hardware Identifiers (HWID)** مثل:
- MAC Address
- Volume Serial
- BIOS Serial
- System UUID

ويتيح تجربة تزوير هذه القيم (أو محاكاتها) بطريقة آمنة، قانونية، وغير مؤذية.

---

## ✅ ماذا يمكن لهذا المشروع فعله؟

| الوظيفة                        | مدعوم؟ | ملاحظات |
|-------------------------------|--------|----------|
| تزوير MAC Address             | ✅ نعم  | يتم عبر تعديل الـ Registry |
| تزوير Volume Serial           | ✅ نعم  | عبر أداة خارجية `volumeid.exe` |
| تزوير BIOS Serial (محاكاة)    | ✅ نعم  | كتابة في Registry فقط |
| تزوير UUID (محاكاة)           | ✅ نعم  | كتابة في Registry فقط |
| استعادة القيم الأصلية         | ✅ نعم  | عبر ملف `original_values.json` |
| واجهة رسومية (GUI)            | ✅ نعم  | مبنية بـ Tkinter |

---

## ❌ ماذا لا يمكن لهذا المشروع فعله؟

### على عكس أدوات مثل "Hydra Spoofer"، هذا المشروع لا يقوم بالتالي:

| الوظيفة                                      | مدعوم؟ | السبب |
|---------------------------------------------|--------|--------|
| تزوير BIOS / Motherboard / CPU بشكل فعلي    | ❌ لا   | يتطلب Kernel Driver |
| تزوير UUID من SMBIOS                         | ❌ لا   | لا يمكن بدون تعديل منخفض المستوى |
| تزوير Drive Serial الحقيقي (physical)       | ❌ لا   | يحتاج firmware-level access |
| تجاوز Anti-Cheat (مثل Riot Vanguard / EAC)  | ❌ لا   | غير قانوني، وهذا مشروع تعليمي |

---

## ⚠️ تنويه مهم:

> ❗ هذا المشروع لا يُستخدم لتجاوز الحظر، الغش في الألعاب، أو خداع أنظمة الحماية.
> 
> ✅ هدفه فقط تعليم كيفية قراءة وتزوير القيم من وجهة نظر تقنية، وبشكل مؤقت وآمن ضمن User Mode.
> 
> ❌ لا يحتوي أي driver أو كود منخفض المستوى.
> 
> 💡 لا يُغيّر أي قيمة دائمة في BIOS أو Hardware فعلي.

---

## 🔧 طريقة الاستخدام

### 1. تجهيز المشروع:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
````

### 2. تشغيل الواجهة الرسومية:

```bash
python gui.py
```

---

## 📚 روابط مفيدة

* [Download VolumeID.exe (Sysinternals)](https://learn.microsoft.com/en-us/sysinternals/downloads/volumeid)
* [WMI Command Reference](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)
* [UUID Specification](https://datatracker.ietf.org/doc/html/rfc4122)

---

## 📂 هيكل المشروع

```
hwid_spoofer/
│
├── gui.py                     # الواجهة الرسومية
├── mac_spoofer.py             # تزوير MAC Address
├── volume_spoofer.py          # تزوير Volume Serial
├── bios_spoofer.py            # محاكاة BIOS Serial
├── uuid_spoofer.py            # محاكاة UUID
├── original_values.json       # ملف تخزين القيم الأصلية
├── utils/
│   ├── registry_tools.py      # دوال قراءة/كتابة من Registry
│   └── storage.py             # تخزين واسترجاع القيم الأصلية
└── requirements.txt
```

---

## 🧠 تم تطويره لأغراض تعليمية فقط.

إذا كنت مطور أو باحث أمني وبدك تفهم كيف تقرأ وتتعامل مع HWID على مستوى نظام التشغيل بدون خرق قوانين أو تعدي على الخصوصية، هذا المشروع نقطة انطلاق ممتازة.

---

```
🔧 Developed by Majd Shawish – 2025
```
