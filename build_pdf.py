#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate PDF catalog using weasyprint"""

import base64
import os
from weasyprint import HTML, CSS

IMAGES_DIR = "/tmp/docx_extracted/word/media"

def img_b64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            data = base64.b64encode(f.read()).decode()
        ext = path.rsplit('.', 1)[-1].lower()
        mime = 'jpeg' if ext in ('jpg','jpeg') else 'png'
        return f"data:image/{mime};base64,{data}"
    return ""

img1 = img_b64(f"{IMAGES_DIR}/image1.jpeg")
img2 = img_b64(f"{IMAGES_DIR}/image2.png")
img3 = img_b64(f"{IMAGES_DIR}/image3.png")
img4 = img_b64(f"{IMAGES_DIR}/image4.png")
img5 = img_b64(f"{IMAGES_DIR}/image5.png")
img6 = img_b64(f"{IMAGES_DIR}/image6.jpeg")
img7 = img_b64(f"{IMAGES_DIR}/image7.png")
img8 = img_b64(f"{IMAGES_DIR}/image8.png")

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap');

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: 'Tajawal', 'Arial', sans-serif;
    direction: rtl;
    color: #222;
    background: white;
    font-size: 12pt;
    line-height: 1.6;
  }}

  .page {{
    width: 210mm;
    min-height: 297mm;
    padding: 20mm 20mm 20mm 20mm;
    page-break-after: always;
    position: relative;
  }}

  /* ===== COVER ===== */
  .cover {{
    background: #0A1628;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    min-height: 297mm;
    padding: 30mm 20mm;
  }}

  .cover-brand {{
    font-size: 64pt;
    font-weight: 900;
    color: #4A8FD4;
    margin-bottom: 8pt;
    letter-spacing: -2pt;
  }}

  .cover-brand span {{ color: white; }}

  .cover-en {{
    font-size: 16pt;
    color: #8AABCC;
    margin-bottom: 20pt;
    letter-spacing: 3pt;
    font-weight: 300;
  }}

  .cover-line {{
    width: 80pt;
    height: 3pt;
    background: #4A8FD4;
    margin: 0 auto 20pt;
    border-radius: 2pt;
  }}

  .cover-images {{
    display: flex;
    gap: 15pt;
    justify-content: center;
    align-items: center;
    margin: 20pt 0;
  }}

  .cover-images img {{
    max-width: 120pt;
    max-height: 140pt;
    border-radius: 10pt;
    border: 1pt solid rgba(74,143,212,0.4);
    object-fit: contain;
  }}

  .cover-tagline {{
    font-size: 16pt;
    color: #CCDDEE;
    margin-top: 20pt;
    line-height: 1.8;
  }}

  .cover-subtitle {{
    font-size: 14pt;
    color: #8AABCC;
    margin-top: 30pt;
    padding-top: 20pt;
    border-top: 1pt solid rgba(74,143,212,0.3);
    width: 100%;
  }}

  /* ===== PAGE HEADER ===== */
  .page-header {{
    background: #0A1628;
    color: white;
    padding: 12pt 0;
    margin: -20mm -20mm 16pt -20mm;
    padding-left: 20mm;
    padding-right: 20mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .page-header-title {{
    font-size: 10pt;
    color: #8AABCC;
    letter-spacing: 2pt;
  }}

  .page-header-num {{
    font-size: 10pt;
    color: #4A8FD4;
    font-weight: 700;
  }}

  /* ===== HEADINGS ===== */
  h1 {{
    font-size: 26pt;
    font-weight: 800;
    color: #1A4E8A;
    margin-bottom: 4pt;
    margin-top: 0;
  }}

  h2 {{
    font-size: 18pt;
    font-weight: 700;
    color: #1A4E8A;
    margin-top: 14pt;
    margin-bottom: 6pt;
  }}

  h3 {{
    font-size: 14pt;
    font-weight: 600;
    color: #1A4E8A;
    margin-top: 10pt;
    margin-bottom: 4pt;
  }}

  .divider {{
    height: 3pt;
    width: 50pt;
    background: #1A4E8A;
    border-radius: 2pt;
    margin-bottom: 12pt;
  }}

  /* ===== BODY TEXT ===== */
  p.body {{
    font-size: 12pt;
    color: #333;
    margin-bottom: 8pt;
    line-height: 1.8;
  }}

  /* ===== INFO BOX ===== */
  .info-box {{
    background: #EEF4FB;
    border: 2pt solid #1A4E8A;
    border-radius: 8pt;
    padding: 10pt 14pt;
    margin-bottom: 8pt;
  }}

  .info-box.green {{
    background: #EEFAF3;
    border-color: #1A7A4E;
  }}

  .info-box.gold {{
    background: #FDF8EE;
    border-color: #B8860B;
  }}

  .info-box-title {{
    font-size: 13pt;
    font-weight: 700;
    color: #1A4E8A;
    margin-bottom: 4pt;
  }}

  .info-box.green .info-box-title {{ color: #1A7A4E; }}
  .info-box.gold .info-box-title {{ color: #B8860B; }}

  .info-box-text {{
    font-size: 11pt;
    color: #444;
    line-height: 1.7;
  }}

  /* ===== FLOW DIAGRAM ===== */
  .flow {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6pt;
    margin: 12pt 0;
    flex-wrap: wrap;
  }}

  .flow-box {{
    background: #EEF4FB;
    border: 1.5pt solid #4A8FD4;
    border-radius: 8pt;
    padding: 8pt 12pt;
    text-align: center;
    min-width: 70pt;
  }}

  .flow-icon {{ font-size: 18pt; }}
  .flow-name {{ font-size: 11pt; font-weight: 700; color: #1A4E8A; }}
  .flow-sub {{ font-size: 8pt; color: #666; }}

  .flow-arrow {{
    font-size: 18pt;
    color: #4A8FD4;
    font-weight: 700;
  }}

  /* ===== STEP BOX ===== */
  .step-box {{
    display: flex;
    margin-bottom: 8pt;
    border-radius: 8pt;
    overflow: hidden;
    border: 1pt solid #CBD8E8;
  }}

  .step-num {{
    background: #1A4E8A;
    color: white;
    font-size: 20pt;
    font-weight: 900;
    min-width: 40pt;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8pt;
  }}

  .step-content {{
    background: #F4F8FD;
    padding: 10pt 14pt;
    flex: 1;
  }}

  .step-title {{
    font-size: 13pt;
    font-weight: 700;
    color: #1A4E8A;
    margin-bottom: 4pt;
  }}

  .step-text {{
    font-size: 11pt;
    color: #444;
    line-height: 1.7;
    white-space: pre-line;
  }}

  /* ===== TABLES ===== */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 10pt;
    font-size: 11pt;
  }}

  table.specs th {{
    background: #1A4E8A;
    color: white;
    padding: 7pt 10pt;
    text-align: right;
    font-weight: 700;
  }}

  table.specs td {{
    padding: 6pt 10pt;
    text-align: right;
    border-bottom: 1pt solid #DDE8F4;
  }}

  table.specs tr:nth-child(even) td {{
    background: #F4F8FD;
  }}

  table.specs tr:nth-child(odd) td {{
    background: #FAFCFE;
  }}

  /* ===== IMAGES ===== */
  .img-center {{
    text-align: center;
    margin: 10pt 0;
  }}

  .img-center img {{
    max-width: 150pt;
    max-height: 150pt;
    border-radius: 8pt;
    border: 1pt solid #CBD8E8;
    object-fit: contain;
  }}

  .img-caption {{
    font-size: 9pt;
    color: #666;
    margin-top: 4pt;
  }}

  .img-row {{
    display: flex;
    gap: 15pt;
    justify-content: center;
    margin: 10pt 0;
  }}

  .img-row > div {{
    text-align: center;
    flex: 1;
  }}

  .img-row img {{
    max-width: 130pt;
    max-height: 150pt;
    border-radius: 8pt;
    border: 1pt solid #CBD8E8;
    object-fit: contain;
  }}

  /* ===== BULLETS ===== */
  ul.bullets {{
    list-style: none;
    padding: 0;
    margin: 8pt 0;
  }}

  ul.bullets li {{
    padding: 3pt 16pt 3pt 0;
    position: relative;
    font-size: 11pt;
    color: #333;
    line-height: 1.6;
  }}

  ul.bullets li::before {{
    content: '●';
    color: #1A4E8A;
    position: absolute;
    right: 0;
    font-size: 8pt;
    top: 5pt;
  }}

  /* ===== FEATURE GRID ===== */
  .feature-grid {{
    display: flex;
    flex-wrap: wrap;
    gap: 8pt;
    margin: 8pt 0;
  }}

  .feature-card {{
    flex: 1;
    min-width: 45%;
    background: #EEF4FB;
    border: 1pt solid #CBD8E8;
    border-radius: 8pt;
    padding: 10pt;
  }}

  .feature-card-title {{
    font-size: 12pt;
    font-weight: 700;
    color: #1A4E8A;
    margin-bottom: 4pt;
  }}

  .feature-card-text {{
    font-size: 10pt;
    color: #555;
    line-height: 1.6;
  }}

  /* ===== FOOTER ===== */
  .page-footer {{
    position: fixed;
    bottom: 10mm;
    left: 20mm;
    right: 20mm;
    text-align: center;
    font-size: 9pt;
    color: #888;
    border-top: 1pt solid #DDE;
    padding-top: 4pt;
  }}

  @page {{
    size: A4;
    margin: 0;
  }}

  @media print {{
    .page {{ page-break-after: always; }}
  }}
</style>
</head>
<body>

<!-- ===== COVER PAGE ===== -->
<div class="page cover">
  <div class="cover-brand">ب<span>ر</span>ق</div>
  <div class="cover-en">BARQ — Smart Energy Management</div>
  <div class="cover-line"></div>

  <div class="cover-images">
    {'<img src="' + img1 + '" alt="BARQ Device">' if img1 else ''}
    {'<img src="' + img6 + '" alt="BARQ System">' if img6 else ''}
  </div>

  <div class="cover-tagline">
    نظام ذكي لمراقبة وإدارة منظومات الطاقة الشمسية<br>
    <strong style="color:#4A8FD4">راقب • تحكم • وفّر</strong>
  </div>

  <div class="cover-subtitle">
    كتالوج الأجهزة ودليل التركيب والإعداد<br>
    <span style="font-size:12pt;color:#6699BB">شركة برق لحلول الطاقة النظيفة — صناعة سورية 🇸🇾</span>
  </div>
</div>

<!-- ===== PAGE 2: ما هو نظام برق؟ ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">نظام مراقبة الطاقة الشمسية</div>
    <div class="page-header-num">02</div>
  </div>

  <h1>ما هو نظام <span style="color:#4A8FD4">برق</span>؟</h1>
  <div class="divider"></div>

  <p class="body">
    برق هو نظام ذكي لمراقبة وإدارة منظومات الطاقة الشمسية المنزلية. يرتبط مباشرة بجهاز الإنفرتر ويقرأ بياناته الفعلية لحظة بلحظة، مما يتيح لك معرفة حالة بطاريتك ومصدر الطاقة في أي وقت — سواء كنت في المنزل أو على بُعد آلاف الكيلومترات.
  </p>

  <h2>كيف يعمل النظام؟</h2>
  <div class="flow">
    <div class="flow-box">
      <div class="flow-icon">⚡</div>
      <div class="flow-name">الإنفرتر</div>
      <div class="flow-sub">Voltronic / Growatt</div>
    </div>
    <div class="flow-arrow">←</div>
    <div class="flow-box" style="border-color:#1A4E8A;background:#D8E8F6">
      <div class="flow-icon">📡</div>
      <div class="flow-name">المرسلة</div>
      <div class="flow-sub">RS-232 / RJ45</div>
    </div>
    <div class="flow-arrow">←</div>
    <div class="flow-box">
      <div class="flow-icon">❄️🔥</div>
      <div class="flow-name">البراد / السخان</div>
      <div class="flow-sub">ESP-NOW لاسلكي</div>
    </div>
    <div class="flow-arrow">←</div>
    <div class="flow-box">
      <div class="flow-icon">📱</div>
      <div class="flow-name">التطبيق</div>
      <div class="flow-sub">WiFi / إنترنت</div>
    </div>
  </div>

  <h2>مميزات النظام</h2>
  <div class="feature-grid">
    <div class="feature-card">
      <div class="feature-card-title">🔍 مراقبة فورية</div>
      <div class="feature-card-text">اعرف نسبة شحن بطاريتك وجهدها وطاقة الألواح الشمسية واستهلاك الأحمال — كل ذلك في الوقت الفعلي من أي مكان.</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-title">🎛️ تحكم ذكي</div>
      <div class="feature-card-text">اضبط متى يشتغل البراد أو السخان بناءً على نسبة الشحن، وحدد الأولويات لتحافظ على عمر بطاريتك.</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-title">📊 تحليل الطاقة</div>
      <div class="feature-card-text">مخطط بياني لآخر 24 ساعة يوضح سلوك البطارية، وساعات تشغيل كل جهاز خلال اليوم.</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-title">🌐 يعمل بدون إنترنت</div>
      <div class="feature-card-text">يعمل النظام محلياً حتى بدون إنترنت. الإنترنت يضيف إمكانية المراقبة عن بُعد فقط.</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-title">🔋 حماية البطارية</div>
      <div class="feature-card-text">إيقاف تلقائي للأجهزة عند انخفاض الشحن لمستوى محدد، مما يطيل عمر البطارية.</div>
    </div>
    <div class="feature-card">
      <div class="feature-card-title">🇸🇾 صناعة سورية</div>
      <div class="feature-card-text">جميع الأجهزة مصنوعة ومطورة محلياً في سوريا مع دعم فني مباشر من الفريق المصنّع.</div>
    </div>
  </div>
</div>

<!-- ===== PAGE 3: المرسلة ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">مكونات النظام</div>
    <div class="page-header-num">03</div>
  </div>

  <h1>أولاً: المرسلة — <span style="color:#4A8FD4">قلب النظام</span></h1>
  <div class="divider"></div>

  <p class="body">تتصل مباشرة بالإنفرتر عبر كابل RJ45 على مخرج COMM، وتقرأ بيانات البطارية والطاقة الشمسية، ثم تبثها لاسلكياً للأجهزة وترفعها للإنترنت.</p>

  <div class="img-row">
    <div>
      {'<img src="' + img2 + '" alt="المرسلة">' if img2 else ''}
      <div class="img-caption">جهاز المرسلة BARQ — الواجهة الأمامية</div>
    </div>
    <div>
      {'<img src="' + img3 + '" alt="خلفية المرسلة">' if img3 else ''}
      <div class="img-caption">الخلفية: مدخل DC 12V + منفذ RJ45</div>
    </div>
    <div>
      {'<img src="' + img4 + '" alt="زر الضبط">' if img4 else ''}
      <div class="img-caption">الجانب: زر الضبط الأبيض</div>
    </div>
  </div>

  <h2>مواصفات المرسلة</h2>
  <table class="specs">
    <tr><th>المواصفة</th><th>القيمة</th></tr>
    <tr><td>المتحكم</td><td>ESP8266 / ESP-12E</td></tr>
    <tr><td>الاتصال بالإنفرتر</td><td>RS-232 / RJ45 (مخرج COMM)</td></tr>
    <tr><td>الاتصال اللاسلكي</td><td>ESP-NOW — مدى يصل 200 متر</td></tr>
    <tr><td>الاتصال بالإنترنت</td><td>WiFi 2.4GHz</td></tr>
    <tr><td>التغذية</td><td>DC 12V</td></tr>
    <tr><td>دورة رفع البيانات</td><td>كل دقيقتين تلقائياً</td></tr>
    <tr><td>الأنفرترات المدعومة</td><td>Voltronic / Growatt وما يدعم RS-232</td></tr>
  </table>

  <h2>وظائف زر الضبط</h2>
  <table class="specs">
    <tr><th>طريقة الضغط</th><th>الوظيفة</th></tr>
    <tr><td>ضغطة واحدة</td><td>وضع WiFi — يبث شبكة BARQ للضبط</td></tr>
    <tr><td>ضغطتان متتاليتان</td><td>وضع الاقتران مع المستقبلات</td></tr>
    <tr><td>ضغط مستمر 10 ثوانٍ</td><td>إعادة الضبط للإعدادات المصنعية</td></tr>
  </table>
</div>

<!-- ===== PAGE 4: البراد والمكيف ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">مكونات النظام</div>
    <div class="page-header-num">04</div>
  </div>

  <h1>ثانياً: جهاز البراد / <span style="color:#4A8FD4">المكيف</span></h1>
  <div class="divider"></div>

  <p class="body">يتحكم في تشغيل وإيقاف الثلاجة، الفريزر، الكولر، أو المكيف بشكل تلقائي بناءً على نسبة شحن البطارية التي تحددها أنت.</p>

  <div class="img-row">
    <div>
      {'<img src="' + img5 + '" alt="جهاز البراد">' if img5 else ''}
      <div class="img-caption">جهاز البراد — فيشة كهربائية</div>
    </div>
    <div>
      {'<img src="' + img7 + '" alt="جهاز المكيف">' if img7 else ''}
      <div class="img-caption">جهاز المكيف — ترمينالات</div>
    </div>
  </div>

  <div style="display:flex;gap:10pt;margin:10pt 0;">
    <div style="flex:1">
      <h2>مواصفات جهاز البراد</h2>
      <table class="specs">
        <tr><th>المواصفة</th><th>القيمة</th></tr>
        <tr><td>المتحكم</td><td>ESP8266 / ESP-12E</td></tr>
        <tr><td>الاتصال</td><td>ESP-NOW لاسلكي</td></tr>
        <tr><td>عنصر التحكم</td><td>ريلي — 10A / 240V AC</td></tr>
        <tr><td>الاستجابة</td><td>خلال 3 ثوانٍ</td></tr>
        <tr><td>التوصيل</td><td>فيشة كهربائية عادية</td></tr>
      </table>
    </div>
    <div style="flex:1">
      <h2>مواصفات جهاز المكيف</h2>
      <table class="specs">
        <tr><th>المواصفة</th><th>القيمة</th></tr>
        <tr><td>المتحكم</td><td>ESP8266 / ESP-12E</td></tr>
        <tr><td>الاتصال</td><td>ESP-NOW لاسلكي</td></tr>
        <tr><td>عنصر التحكم</td><td>ريلي — 30A / 240V AC</td></tr>
        <tr><td>التركيب</td><td>ترمينالات ثابتة</td></tr>
        <tr><td>مناسب لـ</td><td>مكيفات، غسالات، أحمال كبيرة</td></tr>
      </table>
    </div>
  </div>

  <h2>مميزات مشتركة</h2>
  <ul class="bullets">
    <li>يشتغل تلقائياً عند بلوغ نسبة الشحن المضبوطة</li>
    <li>يوقف تلقائياً لحماية البطارية من الإفراغ الزائد</li>
    <li>3 أوقات تأخير إقلاع لحماية الكمبروسر من الصدمات الكهربائية المتكررة</li>
    <li>خيار التشغيل الفوري عند عودة التيار الكهربائي</li>
    <li>زمن تأخير إيقاف قابل للضبط (موصى به: 30 ثانية) لحماية الأجهزة</li>
  </ul>
</div>

<!-- ===== PAGE 5: السخان ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">مكونات النظام</div>
    <div class="page-header-num">05</div>
  </div>

  <h1>ثالثاً: جهاز <span style="color:#4A8FD4">السخان</span></h1>
  <div class="divider"></div>

  <p class="body">يتحكم في سخان الماء بشكل تدريجي (0% إلى 100%) بناءً على الطاقة المتاحة من الألواح الشمسية، مما يعظّم استهلاك الطاقة الشمسية الفائضة بدلاً من هدرها.</p>

  {'<div class="img-center"><img src="' + img8 + '" alt="جهاز السخان" style="max-width:160pt;max-height:160pt"><div class="img-caption">جهاز السخان BARQ — يعرض الجهد والتيار</div></div>' if img8 else ''}

  <h2>مواصفات جهاز السخان</h2>
  <table class="specs">
    <tr><th>المواصفة</th><th>القيمة</th></tr>
    <tr><td>المتحكم</td><td>ESP8266 / ESP-12E</td></tr>
    <tr><td>الاتصال</td><td>ESP-NOW لاسلكي</td></tr>
    <tr><td>عنصر التحكم</td><td>ترياك BTA40</td></tr>
    <tr><td>نطاق التحكم</td><td>0% إلى 100% بخطوات 1%</td></tr>
    <tr><td>الحماية</td><td>إيقاف فوري عند انخفاض الشحن</td></tr>
    <tr><td>الشاشة</td><td>رقمية — تعرض الجهد والتيار</td></tr>
    <tr><td>التوصيل</td><td>فاز + نتر مدخل، فاز مخرج للسخان</td></tr>
  </table>

  <div class="info-box gold">
    <div class="info-box-title">🔥 ميزة التحكم التدريجي</div>
    <div class="info-box-text">
      على عكس البراد الذي يعمل أو لا يعمل فقط، يمكن للسخان أن يعمل بنسبة جزئية من الطاقة.<br>
      مثال: عند وجود 2 كيلوواط فائض من الألواح الشمسية → يشغّل السخان بـ 40% فقط.<br>
      هذا يحقق أقصى استفادة من الطاقة الشمسية الفائضة دون إهدار أو إفراط.
    </div>
  </div>
</div>

<!-- ===== PAGE 6: دليل التوصيل ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">دليل التركيب</div>
    <div class="page-header-num">06</div>
  </div>

  <h1>دليل التوصيل <span style="color:#4A8FD4">الكهربائي</span></h1>
  <div class="divider"></div>

  <h2>توصيل المرسلة</h2>

  <div class="step-box">
    <div class="step-num">1</div>
    <div class="step-content">
      <div class="step-title">توصيل كابل الشبكة بالإنفرتر</div>
      <div class="step-text">نوصّل كابل شبكة عادي (RJ45 — كابل الكمبيوتر العادي) بين مخرج الإنفرتر (COMM) وجهاز المرسلة.
بعد التوصيل مباشرة يبدأ الجهاز بالوميض دلالةً على أنه يعمل ويقرأ البيانات.</div>
    </div>
  </div>

  <div class="step-box">
    <div class="step-num">2</div>
    <div class="step-content">
      <div class="step-title">تغذية الكهرباء (إذا لزم)</div>
      <div class="step-text">معظم الأنفرترات تغذي المرسلة تلقائياً عبر كابل COMM.
وقد يحتاج بعض أنواع الأنفرترات إلى توصيل مدخل DC 12V منفصل (غالباً لا يحتاج).</div>
    </div>
  </div>

  <div class="step-box">
    <div class="step-num">3</div>
    <div class="step-content">
      <div class="step-title">التحقق من التشغيل</div>
      <div class="step-text">عند التشغيل الصحيح يبدأ الليد بالوميض بشكل منتظم.
إذا لم يضيء الليد → تحقق من اتجاه كابل RJ45 أو جرب توصيل DC 12V.</div>
    </div>
  </div>

  <h2>توصيل المستقبلات</h2>

  <div class="info-box">
    <div class="info-box-title">🔌 جهاز البراد</div>
    <div class="info-box-text">التوصيل بسيط جداً — ضع الجهاز في أي مأخذ كهربائي عادي ثم صِل البراد/الفريزر بالفيشة الخارجة من الجهاز. لا يحتاج أي تمديدات.</div>
  </div>

  <div class="info-box">
    <div class="info-box-title">🏠 جهاز المكيف</div>
    <div class="info-box-text">له ترمينالات للتركيب الثابت:
• مدخل فاز: من مصدر الكهرباء
• مدخل نتر مشترك: لتغذية الجهاز
• مخرج فاز: موصول بالمكيف</div>
  </div>

  <div class="info-box">
    <div class="info-box-title">🔥 جهاز السخان</div>
    <div class="info-box-text">نفس طريقة المكيف بترمينالات:
• مدخل فاز: من مصدر الكهرباء
• مدخل نتر مشترك: لتغذية الجهاز
• مخرج فاز: موصول بالسخان</div>
  </div>
</div>

<!-- ===== PAGE 7: خطوات الاقتران ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">دليل الإعداد</div>
    <div class="page-header-num">07</div>
  </div>

  <h1>خطوات الاقتران <span style="color:#4A8FD4">بين الأجهزة</span></h1>
  <div class="divider"></div>
  <p class="body">بعد توصيل المرسلة والمستقبل (براد أو سخان أو مكيف)، اتبع الخطوات التالية:</p>

  <div class="step-box">
    <div class="step-num">1</div>
    <div class="step-content">
      <div class="step-title">تفعيل وضع الاقتران في المرسلة</div>
      <div class="step-text">انقر زر المرسلة مرتين متتاليتين بسرعة.
✅ الليد الأخضر يضيء مرتين ثم يبقى مضيئاً.
🔴 الليد الأحمر يبقى في وضع الوميض.
⟹ المرسلة الآن جاهزة لاستقبال الاقتران.</div>
    </div>
  </div>

  <div class="step-box">
    <div class="step-num">2</div>
    <div class="step-content">
      <div class="step-title">تفعيل وضع الاقتران في المستقبل</div>
      <div class="step-text">انتقل للمستقبل (البراد مثلاً) وانقر زره مرتين متتاليتين.
ستلاحظ التسلسل التالي:
🔊 صوت مرة واحدة
🔴🟢 الليد الأحمر والأخضر يومضان معاً ثم ينطفئان
🔊🔊🔊 صوت ثلاث مرات
🔴🟢 يعودان للوميض معاً
🔊 صوت مرة ← ثم صوتان = ✅ تم الاقتران بنجاح!
(العملية كلها تتم في أقل من 30 ثانية)</div>
    </div>
  </div>

  <div class="step-box">
    <div class="step-num">3</div>
    <div class="step-content">
      <div class="step-title">دخول وضع الضبط</div>
      <div class="step-text">بعد الاقتران الناجح، انقر زر المستقبل نقرة واحدة.
⟹ يبدأ الوميض المتعاكس والسريع (أحمر ثم أخضر بسرعة).
⟹ الجهاز الآن يبث شبكة WiFi باسم BARQ.</div>
    </div>
  </div>

  <div class="step-box">
    <div class="step-num">4</div>
    <div class="step-content">
      <div class="step-title">الاتصال بشبكة BARQ</div>
      <div class="step-text">افتح إعدادات WiFi في هاتفك وابحث عن شبكة: BARQ
كلمة المرور (أول مرة): 11111111 (رقم 1 ثماني مرات)
بعد الاتصال → افتح تطبيق BARQ لبدء الضبط.</div>
    </div>
  </div>
</div>

<!-- ===== PAGE 8: الضبط عبر التطبيق ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">دليل الإعداد</div>
    <div class="page-header-num">08</div>
  </div>

  <h1>الضبط عبر تطبيق <span style="color:#4A8FD4">BARQ</span></h1>
  <div class="divider"></div>

  <p class="body">بعد الاتصال بشبكة BARQ، افتح التطبيق. ستجد خيارين في الشاشة الرئيسية:</p>

  <div style="display:flex;gap:10pt;margin:8pt 0 14pt;">
    <div class="info-box" style="flex:1;margin-bottom:0">
      <div class="info-box-title">📱 الضبط المحلي</div>
      <div class="info-box-text">للضبط المباشر عبر WiFi الجهاز. لا يحتاج إنترنت. مناسب للضبط الأولي أثناء التركيب.</div>
    </div>
    <div class="info-box" style="flex:1;margin-bottom:0">
      <div class="info-box-title">🌐 ضبط الإنترنت</div>
      <div class="info-box-text">للضبط عن بُعد من أي مكان. يحتاج المرسلة متصلة بالإنترنت.</div>
    </div>
  </div>

  <h2>حقول الضبط المحلي</h2>
  <p class="body" style="margin-bottom:6pt;">ادخل "الضبط المحلي" وأكمل الحقول التالية ثم اضغط حفظ:</p>

  <table class="specs">
    <tr><th>الحقل</th><th>الوصف</th><th>مثال</th></tr>
    <tr>
      <td><strong>الاسم</strong></td>
      <td>اسم تعريفي للجهاز</td>
      <td>براد المطبخ</td>
    </tr>
    <tr>
      <td><strong>الهدف</strong></td>
      <td>نوع الجهاز الموصول</td>
      <td>ثلاجة / مكيف / سخان</td>
    </tr>
    <tr>
      <td><strong>نسبة التشغيل (%)</strong></td>
      <td>نسبة شحن البطارية التي يبدأ عندها الجهاز بالعمل</td>
      <td>70%</td>
    </tr>
    <tr>
      <td><strong>نسبة الإيقاف (%)</strong></td>
      <td>نسبة شحن البطارية التي يتوقف عندها الجهاز حمايةً لها</td>
      <td>40%</td>
    </tr>
    <tr>
      <td><strong>زمن التأخير الأول (ث)</strong></td>
      <td>تأخير إقلاع الجهاز — مفيد لمنع تشغيل أكثر من جهاز في نفس الوقت</td>
      <td>30 ثانية</td>
    </tr>
    <tr>
      <td><strong>زمن التأخير الثاني (ث)</strong></td>
      <td>وقت الانتظار قبل محاولة الإقلاع الثانية عند فشل الأولى</td>
      <td>60 ثانية</td>
    </tr>
    <tr>
      <td><strong>زمن التأخير الثالث (ث)</strong></td>
      <td>وقت الانتظار قبل محاولة الإقلاع الثالثة عند فشل الثانية</td>
      <td>120 ثانية</td>
    </tr>
    <tr>
      <td><strong>زمن تأخير الإيقاف (ث)</strong></td>
      <td>وقت الانتظار قبل الإيقاف عند انقطاع التيار — يحمي الأجهزة من الانطفاء المفاجئ</td>
      <td>30 ثانية ✓</td>
    </tr>
    <tr>
      <td><strong>عند قدوم الكهرباء</strong></td>
      <td>هل يعمل الجهاز فوراً عند عودة التيار؟</td>
      <td>حسب الرغبة</td>
    </tr>
  </table>

  <div class="info-box green">
    <div class="info-box-title">✅ تأكيد الحفظ</div>
    <div class="info-box-text">بعد تعبئة جميع الحقول، اضغط زر "حفظ".<br>
    عند الحفظ الناجح: يصدر الجهاز <strong>صوتاً مزدوجاً</strong> تأكيداً لحفظ المعلومات بنجاح.</div>
  </div>
</div>

<!-- ===== PAGE 9: الإنترنت والتطبيق ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">التطبيق والمراقبة</div>
    <div class="page-header-num">09</div>
  </div>

  <h1>ربط المرسلة <span style="color:#4A8FD4">بالإنترنت</span></h1>
  <div class="divider"></div>
  <p class="body">هذه الخطوة اختيارية — النظام يعمل بالكامل محلياً بدونها. ولكن عند الاتصال بالإنترنت تتاح إمكانية المراقبة عن بُعد من أي مكان في العالم.</p>

  <div class="step-box">
    <div class="step-num">1</div>
    <div class="step-content">
      <div class="step-title">تفعيل وضع WiFi في المرسلة</div>
      <div class="step-text">انقر زر المرسلة مرة واحدة فقط.
⟹ تبدأ المرسلة ببث شبكة WiFi باسم BARQ.</div>
    </div>
  </div>

  <div class="step-box">
    <div class="step-num">2</div>
    <div class="step-content">
      <div class="step-title">الاتصال بشبكة BARQ من هاتفك</div>
      <div class="step-text">افتح WiFi في هاتفك واتصل بشبكة: BARQ
كلمة المرور: 11111111</div>
    </div>
  </div>

  <div class="step-box">
    <div class="step-num">3</div>
    <div class="step-content">
      <div class="step-title">إدخال بيانات الراوتر المنزلي</div>
      <div class="step-text">افتح التطبيق ← إعدادات WiFi.
أدخل: اسم شبكة الراوتر المنزلي + كلمة المرور.
⚠️ مهم: تأكد أن الراوتر على تردد 2.4 GHz (وليس 5 GHz).</div>
    </div>
  </div>

  <div class="step-box">
    <div class="step-num">4</div>
    <div class="step-content">
      <div class="step-title">التحقق من الاتصال</div>
      <div class="step-text">بعد الحفظ، تعود المرسلة للعمل وتتصل بالراوتر تلقائياً.
يمكنك الآن متابعة نظامك من أي مكان عبر التطبيق.</div>
    </div>
  </div>

  <h2>مقارنة وضعي العمل</h2>
  <div style="display:flex;gap:10pt;margin-top:8pt">
    <div class="info-box green" style="flex:1;margin-bottom:0">
      <div class="info-box-title">✅ مع الإنترنت</div>
      <div class="info-box-text">
        <ul class="bullets" style="margin:0">
          <li>مراقبة من أي مكان في العالم</li>
          <li>ضبط الإعدادات عن بُعد</li>
          <li>مخططات بيانية محفوظة</li>
          <li>إشعارات فورية على الهاتف</li>
        </ul>
      </div>
    </div>
    <div class="info-box" style="flex:1;margin-bottom:0">
      <div class="info-box-title">🔒 بدون إنترنت</div>
      <div class="info-box-text">
        <ul class="bullets" style="margin:0">
          <li>التحكم الكامل بالأجهزة محلياً</li>
          <li>آمن وخاص — يعمل 24/7</li>
          <li>الضبط عبر هاتفك مباشرة</li>
          <li>لا حاجة لاشتراك خارجي</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- ===== PAGE 10: المواصفات الفنية ===== -->
<div class="page">
  <div class="page-header">
    <div class="page-header-title">المواصفات الفنية</div>
    <div class="page-header-num">10</div>
  </div>

  <h1>المواصفات <span style="color:#4A8FD4">الفنية الكاملة</span></h1>
  <div class="divider"></div>

  <h2>📡 المرسلة</h2>
  <table class="specs">
    <tr><th>المواصفة</th><th>القيمة</th></tr>
    <tr><td>المتحكم</td><td>ESP8266 / ESP-12E</td></tr>
    <tr><td>الاتصال بالإنفرتر</td><td>RS-232 / RJ45 (مخرج COMM)</td></tr>
    <tr><td>الاتصال اللاسلكي</td><td>ESP-NOW — مدى يصل 200 متر</td></tr>
    <tr><td>الاتصال بالإنترنت</td><td>WiFi 2.4GHz</td></tr>
    <tr><td>التغذية</td><td>DC 12V</td></tr>
    <tr><td>دورة رفع البيانات</td><td>كل دقيقتين تلقائياً</td></tr>
  </table>

  <div style="display:flex;gap:10pt;margin-top:6pt">
    <div style="flex:1">
      <h2>❄️ جهاز البراد</h2>
      <table class="specs">
        <tr><th>المواصفة</th><th>القيمة</th></tr>
        <tr><td>المتحكم</td><td>ESP8266 / ESP-12E</td></tr>
        <tr><td>الاتصال</td><td>ESP-NOW لاسلكي</td></tr>
        <tr><td>عنصر التحكم</td><td>ريلي — 10A / 240V AC</td></tr>
        <tr><td>الاستجابة</td><td>خلال 3 ثوانٍ</td></tr>
        <tr><td>التغذية</td><td>DC 12V</td></tr>
      </table>

      <h2>🏠 جهاز المكيف</h2>
      <table class="specs">
        <tr><th>المواصفة</th><th>القيمة</th></tr>
        <tr><td>المتحكم</td><td>ESP8266 / ESP-12E</td></tr>
        <tr><td>الاتصال</td><td>ESP-NOW لاسلكي</td></tr>
        <tr><td>عنصر التحكم</td><td>ريلي — 30A / 240V AC</td></tr>
        <tr><td>التركيب</td><td>ترمينالات ثابتة</td></tr>
      </table>
    </div>
    <div style="flex:1">
      <h2>🔥 جهاز السخان</h2>
      <table class="specs">
        <tr><th>المواصفة</th><th>القيمة</th></tr>
        <tr><td>المتحكم</td><td>ESP8266 / ESP-12E</td></tr>
        <tr><td>الاتصال</td><td>ESP-NOW لاسلكي</td></tr>
        <tr><td>عنصر التحكم</td><td>ترياك BTA40</td></tr>
        <tr><td>نطاق التحكم</td><td>0% — 100% (خطوات 1%)</td></tr>
        <tr><td>الحماية</td><td>إيقاف فوري عند انخفاض الشحن</td></tr>
        <tr><td>الشاشة</td><td>رقمية — جهد وتيار</td></tr>
      </table>
    </div>
  </div>

  <div class="info-box gold" style="margin-top:16pt">
    <div class="info-box-title">🇸🇾 صناعة سورية — شركة برق لحلول الطاقة النظيفة</div>
    <div class="info-box-text">جميع أجهزة نظام برق مصنوعة ومطورة محلياً في سوريا.<br>
    الدعم الفني متوفر مباشرة من الفريق المصنّع. جميع الحقوق محفوظة.</div>
  </div>
</div>

</body>
</html>"""

output_pdf = '/home/user/cataloc-for-barq-232/كتالوج_برق_BARQ.pdf'
HTML(string=html_content).write_pdf(output_pdf)
print(f"PDF saved: {output_pdf}")
