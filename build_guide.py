#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

IMGS = '/tmp/imgs'

# ── helpers ──────────────────────────────────────────────────────────────────

def rtl(para):
    pPr = para._p.get_or_add_pPr()
    b = OxmlElement('w:bidi'); pPr.append(b)
    jc = OxmlElement('w:jc'); jc.set(qn('w:val'), 'right'); pPr.append(jc)

def cs_font(run, name='Arial', size=None, bold=False, color=None, italic=False):
    run.font.name = name
    rPr = run._r.get_or_add_rPr()
    rf = OxmlElement('w:rFonts')
    rf.set(qn('w:ascii'), name); rf.set(qn('w:hAnsi'), name); rf.set(qn('w:cs'), name)
    rPr.append(rf)
    if size:   run.font.size = Pt(size)
    if bold:   run.font.bold = True
    if italic: run.font.italic = True
    if color:  run.font.color.rgb = RGBColor(*color)

def cell_bg(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color); tcPr.append(shd)

def no_borders(table):
    tbl = table._tbl
    tblPr = tbl.find(qn('w:tblPr'))
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr'); tbl.insert(0, tblPr)
    tblBorders = OxmlElement('w:tblBorders')
    for side in ['top','left','bottom','right','insideH','insideV']:
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'), 'none')
        tblBorders.append(el)
    tblPr.append(tblBorders)

def cell_border_color(cell, color='1A569A'):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for side in ['top','left','bottom','right']:
        el = OxmlElement(f'w:{side}')
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '6')
        el.set(qn('w:color'), color)
        tcBorders.append(el)
    tcPr.append(tcBorders)

def add_para(doc, text, size=14, bold=False, color=(0x22,0x22,0x22),
             align='right', space_before=0, space_after=4):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT if align=='right' else WD_ALIGN_PARAGRAPH.CENTER
    rtl(p)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    if text:
        r = p.add_run(text)
        cs_font(r, size=size, bold=bold, color=color)
    return p

def add_heading(doc, text, level=1):
    sizes   = {1:24, 2:18, 3:16}
    colors  = {1:(0x0A,0x3D,0x7A), 2:(0x0A,0x3D,0x7A), 3:(0x1A,0x56,0x9A)}
    p = add_para(doc, text, size=sizes.get(level,16), bold=True,
                 color=colors.get(level,(0,0,0)), space_before=8, space_after=4)
    # blue underline bar
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot = OxmlElement('w:bottom')
    bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '8')
    bot.set(qn('w:color'), '1A569A'); pBdr.append(bot); pPr.append(pBdr)
    return p

def page_break(doc):
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)

def add_screen(doc, img_file, title, bullets, img_width=Cm(5.5), note=None):
    """
    One row: [image | title + bullets]
    img_file: filename in IMGS dir
    bullets: list of (bold_label, description) or just strings
    """
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.RIGHT
    no_borders(tbl)

    img_col = tbl.columns[0]
    txt_col = tbl.columns[1]
    img_col.width = Cm(6)
    txt_col.width = Cm(11.5)

    ci = tbl.cell(0, 0)   # image cell (right in RTL → col 0 = right side visually)
    ct = tbl.cell(0, 1)   # text cell

    # image cell
    cell_bg(ci, 'EEF4FB')
    ci.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    pi = ci.paragraphs[0]
    pi.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pi.paragraph_format.space_before = Pt(6)
    pi.paragraph_format.space_after  = Pt(4)
    full_path = os.path.join(IMGS, img_file)
    if os.path.exists(full_path):
        pi.add_run().add_picture(full_path, width=img_width)
    else:
        r = pi.add_run(f'[صورة: {img_file}]')
        cs_font(r, size=10, color=(0x99,0x99,0x99))

    # text cell
    cell_bg(ct, 'FAFCFF')
    ct.vertical_alignment = WD_ALIGN_VERTICAL.TOP

    # title
    pt = ct.paragraphs[0]
    pt.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    rtl(pt)
    pt.paragraph_format.space_before = Pt(8)
    pt.paragraph_format.space_after  = Pt(6)
    rt = pt.add_run(title)
    cs_font(rt, size=16, bold=True, color=(0x0A,0x3D,0x7A))

    # bullets
    for item in bullets:
        pb = ct.add_paragraph()
        pb.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rtl(pb)
        pb.paragraph_format.space_before = Pt(2)
        pb.paragraph_format.space_after  = Pt(3)
        pb.paragraph_format.right_indent = Cm(0.3)

        if isinstance(item, tuple):
            label, desc = item
            # bullet dot
            rd = pb.add_run('◆  ')
            cs_font(rd, size=13, bold=True, color=(0x1A,0x56,0x9A))
            rl = pb.add_run(label + ':  ')
            cs_font(rl, size=14, bold=True, color=(0x0A,0x3D,0x7A))
            re = pb.add_run(desc)
            cs_font(re, size=14, color=(0x22,0x22,0x22))
        else:
            rd = pb.add_run('◆  ')
            cs_font(rd, size=13, bold=True, color=(0x1A,0x56,0x9A))
            re = pb.add_run(item)
            cs_font(re, size=14, color=(0x22,0x22,0x22))

    if note:
        pn = ct.add_paragraph()
        pn.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rtl(pn)
        pn.paragraph_format.space_before = Pt(6)
        pn.paragraph_format.space_after  = Pt(4)
        pn.paragraph_format.right_indent = Cm(0.3)
        cell_bg(ct, 'EEF4FB')  # note background
        rn = pn.add_run('⚠️  ' + note)
        cs_font(rn, size=13, italic=True, color=(0xB8,0x60,0x0B))

    # separator after table
    sep = doc.add_paragraph()
    sep.paragraph_format.space_after = Pt(6)
    pPr = sep._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bot = OxmlElement('w:bottom')
    bot.set(qn('w:val'), 'single'); bot.set(qn('w:sz'), '4')
    bot.set(qn('w:color'), 'CBD8E8'); pBdr.append(bot); pPr.append(pBdr)

# ── BUILD DOCUMENT ───────────────────────────────────────────────────────────

doc = Document()

section = doc.sections[0]
section.page_width   = Cm(21)
section.page_height  = Cm(29.7)
section.left_margin  = Cm(1.8)
section.right_margin = Cm(1.8)
section.top_margin   = Cm(2)
section.bottom_margin= Cm(2)

# RTL doc
settings = doc.settings.element
settings.append(OxmlElement('w:bidi'))

# ══════════════════════════════════════════════════════════════════════════════
# COVER
# ══════════════════════════════════════════════════════════════════════════════
add_para(doc, '', space_before=60)

# Logo icon
app_img = os.path.join(IMGS, 'الدخول للتاطبيق__صورة التطبيق.jpg')
if os.path.exists(app_img):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(app_img, width=Cm(4))

add_para(doc, 'دليل الضبط والإعداد', size=28, bold=True,
         color=(0x0A,0x3D,0x7A), align='center', space_before=10, space_after=4)
add_para(doc, 'تطبيق BARQ — نظام مراقبة الطاقة الشمسية', size=16,
         color=(0x44,0x44,0x44), align='center', space_after=4)
add_para(doc, 'شركة برق لحلول الطاقة النظيفة 🇸🇾', size=14,
         color=(0x77,0x77,0x77), align='center', space_after=40)

# ── فهرس سريع ──
toc = doc.add_table(rows=4, cols=2)
toc.alignment = WD_TABLE_ALIGNMENT.CENTER
no_borders(toc)
toc_items = [
    ('📱 الدخول للتطبيق',      'الاتصال بشبكة BARQ والدخول للتطبيق'),
    ('📡 ضبط المرسلة',         'إعداد WiFi وإعادة الضبط المصنعي'),
    ('❄️ ضبط البراد / المكيف', 'ضبط نسب التشغيل والإيقاف وأوقات التأخير'),
    ('🔥 ضبط السخان',           'ضبط نسبة التشغيل والحد الأعلى وهامش الاستمرار'),
]
for i, (t, d) in enumerate(toc_items):
    c0, c1 = toc.rows[i].cells[0], toc.rows[i].cells[1]
    cell_bg(c0, 'E8F0FA'); cell_bg(c1, 'F4F8FD')
    p0 = c0.paragraphs[0]; p0.alignment = WD_ALIGN_PARAGRAPH.RIGHT; rtl(p0)
    r0 = p0.add_run(t); cs_font(r0, size=14, bold=True, color=(0x0A,0x3D,0x7A))
    p1 = c1.paragraphs[0]; p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT; rtl(p1)
    r1 = p1.add_run(d); cs_font(r1, size=13, color=(0x44,0x44,0x44))
    for c in [c0, c1]:
        c.paragraphs[0].paragraph_format.space_before = Pt(5)
        c.paragraphs[0].paragraph_format.space_after  = Pt(5)

add_para(doc, '', space_before=10)
add_para(doc, 'ملاحظة: جميع صور الشاشات مأخوذة من التطبيق الفعلي', size=12,
         color=(0x88,0x88,0x88), align='center')

page_break(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — الدخول للتطبيق
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, '📱  أولاً — الدخول للتطبيق', level=1)
add_para(doc, 'بعد اقتران الجهاز مع المرسلة، اتبع الخطوات التالية للاتصال بالتطبيق وبدء الضبط:', size=14, space_after=8)

add_screen(doc,
    'الدخول للتاطبيق__البحث عن شبكة BARQ (1).jpg',
    'الخطوة 1 — البحث عن شبكة BARQ',
    [
        ('افتح إعدادات WiFi', 'في هاتفك من إعدادات الجهاز'),
        ('ابحث عن الشبكة', 'ستجد شبكة باسم BARQ في قائمة الشبكات المتوفرة'),
        ('اضغط عليها', 'للاتصال بها'),
    ]
)

add_screen(doc,
    'الدخول للتاطبيق__اسم الشبكة و كلمة سر الشبكة 1 ثمانية مرات.jpg',
    'الخطوة 2 — إدخال كلمة المرور',
    [
        ('اسم الشبكة', 'BARQ'),
        ('كلمة المرور', '11111111  (رقم 1 ثماني مرات)'),
        ('بعد الاتصال', 'سينقلك الهاتف تلقائياً للشبكة'),
    ],
    img_width=Cm(5.5)
)

add_screen(doc,
    'الدخول للتاطبيق__صورة داخل التطبيق  ضبط محلي او ضبط نت.jpg',
    'الخطوة 3 — فتح تطبيق BARQ',
    [
        ('ضبط محلي', 'للضبط المباشر بدون إنترنت — يستخدم عند التركيب'),
        ('ضبط إنترنت', 'للضبط عن بُعد — يحتاج المرسلة متصلة بالراوتر'),
        ('اختر الوضع', 'المناسب حسب الحاجة'),
    ],
    img_width=Cm(4)
)

page_break(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — ضبط المرسلة
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, '📡  ثانياً — ضبط المرسلة (الضبط المحلي)', level=1)
add_para(doc, 'بعد الاتصال بشبكة BARQ واختيار "ضبط محلي"، تظهر واجهة ضبط المرسلة:', size=14, space_after=8)

add_screen(doc,
    'واجهة المرسلة__واجهة الضبط المحلي للمرسلة .jpg',
    'واجهة ضبط المرسلة',
    [
        ('الرقم التسلسلي', 'رقم فريد للمرسلة — يُستخدم عند تسجيل الحساب على الإنترنت'),
        ('ضبط إعدادات WiFi', 'أدخل اسم شبكة الراوتر المنزلي وكلمة مروره لربط المرسلة بالإنترنت'),
        ('أسم الشبكة', 'اكتب اسم شبكة الراوتر المنزلي (تردد 2.4GHz)'),
        ('كلمة السر', 'كلمة مرور الراوتر المنزلي'),
        ('حفظ إعدادات WiFi', 'اضغط الزر الأزرق لحفظ البيانات وإرسالها للمرسلة'),
        ('إعادة ضبط مصنع', 'الزر الأحمر — يمسح جميع الأجهزة المقترنة (انتبه!)'),
    ],
    note='ربط الإنترنت اختياري — النظام يعمل بالكامل بدونه محلياً'
)

add_screen(doc,
    'واجهة المرسلة__خيار تاكيد لضبط المصنع .jpg',
    'تأكيد إعادة الضبط المصنعي',
    [
        ('رسالة تحذير', 'تظهر رسالة تأكيد قبل تنفيذ إعادة الضبط'),
        ('حسناً', 'للتأكيد وتنفيذ إعادة الضبط — سيتم حذف جميع الأجهزة المعرفة'),
        ('إلغاء', 'للرجوع دون تغيير'),
    ],
    note='إعادة الضبط المصنعي تحذف جميع أجهزة البراد والسخان المقترنة. يجب إعادة الاقتران من الصفر'
)

page_break(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — ضبط البراد / المكيف
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, '❄️  ثالثاً — ضبط جهاز البراد / المكيف', level=1)
add_para(doc, 'بعد الاتصال بشبكة BARQ لجهاز البراد واختيار "ضبط محلي"، تظهر واجهة ضبط البراد:', size=14, space_after=8)

add_screen(doc,
    'واجهة البراد__1.jpg',
    'واجهة ضبط البراد — الجزء الأول',
    [
        ('التشغيل عند نسبة شحن البطارية', 'يعمل البراد تلقائياً عند وصول البطارية لهذه النسبة  (مثال: 85%)'),
        ('الإطفاء عند نسبة شحن البطارية', 'يتوقف البراد عند انخفاض الشحن لهذه النسبة لحماية البطارية  (مثال: 70%)'),
        ('زمن التأخير الأول', 'تأخير الإقلاع بالدقائق — يمنع تشغيل أكثر من جهاز في نفس الوقت'),
        ('زمن التأخير الثاني', 'وقت الانتظار قبل محاولة الإقلاع مرة ثانية إذا فشلت الأولى'),
        ('زمن التأخير الثالث', 'وقت الانتظار قبل محاولة الإقلاع مرة ثالثة إذا فشلت الثانية'),
        ('زمن تأخير الإيقاف', 'بالثواني — يحمي الجهاز من الانطفاء المفاجئ عند انقطاع التيار (يُوصى بـ 30 ثانية)'),
    ]
)

add_screen(doc,
    'واجهة البراد__2.jpg',
    'واجهة ضبط البراد — الجزء الثاني',
    [
        ('حفظ الإعدادات', 'اضغط الزر الأزرق لحفظ جميع الإعدادات — عند النجاح يصدر الجهاز صوتاً مزدوجاً'),
        ('سلوك الجهاز عند عودة الكهرباء', 'خياران حسب رغبتك:'),
        ('تشغيل تلقائي عند عودة الكهرباء ✅', 'سيعود الجهاز للعمل فور وصول الكهرباء'),
        ('عدم التشغيل عند عودة الكهرباء 🔴', 'سيبقى الجهاز متوقفاً حتى تصدر له أوامر تشغيل'),
    ]
)

page_break(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 4 — ضبط السخان
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, '🔥  رابعاً — ضبط جهاز السخان', level=1)
add_para(doc, 'جهاز السخان يختلف عن البراد في طريقة التحكم — يعمل بنسبة جزئية من الطاقة (0% إلى 100%):', size=14, space_after=8)

add_screen(doc,
    'واجهة السخان__1.jpg',
    'واجهة ضبط السخان — الجزء الأول',
    [
        ('الحفاظ على التشغيل عند نسبة', 'نسبة شحن البطارية التي يبدأ عندها السخان بالعمل  (مثال: 85%)'),
        ('الحد الأعلى للتشغيل', 'أقصى طاقة يستهلكها السخان — من القائمة اختر 100% أو أقل حسب الحاجة'),
        ('حفظ النسبة والحد الأعلى', 'اضغط الزر الأزرق لحفظ هذين الإعدادين'),
        ('هامش الاستمرار 🎯', 'يسمح للسخان بالاستمرار في العمل حتى لو انخفضت النسبة بمقدار صغير عن الحد المضبوط'),
        ('1%', 'هامش ضيق — يوقف بسرعة عند الانخفاض'),
        ('2%', 'هامش متوسط (موصى به)'),
        ('3%', 'هامش أوسع — يمنح وقتاً أطول قبل الإيقاف'),
    ]
)

add_screen(doc,
    'واجهة السخان__2.jpg',
    'واجهة ضبط السخان — الجزء الثاني',
    [
        ('التشغيل حسب نسبة البطارية 📊', 'خياران:'),
        ('تشغيل حسب النسبة ✅', 'يعمل السخان عند بلوغ نسبة الشحن المضبوطة — الخيار الاعتيادي'),
        ('بدون النسبة 🔴', 'لا يأخذ نسبة البطارية بعين الاعتبار — للاستخدام الخاص'),
        ('التشغيل القسري عند عودة الكهرباء ⚡', 'خياران:'),
        ('تشغيل قسري مع الكهرباء ✅', 'يعمل فور وصول الكهرباء بغض النظر عن نسبة البطارية'),
        ('بدون التشغيل القسري 🔴', 'لا يشتغل بسبب الكهرباء وحدها — يعتمد على نسبة الشحن فقط'),
    ]
)

page_break(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SECTION 5 — المراقبة عبر الإنترنت
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, '🌐  خامساً — المراقبة عبر الإنترنت (ضبط إنترنت)', level=1)
add_para(doc, 'بعد ربط المرسلة بالراوتر المنزلي، يمكن مراقبة المنظومة وضبطها من أي مكان:', size=14, space_after=8)

add_screen(doc,
    'خاص بالنت__صفحة تسجيل الدخول للنت.jpg',
    'صفحة تسجيل الدخول',
    [
        ('الاسم', 'أدخل اسم المستخدم الذي سجّلته مسبقاً'),
        ('كلمة المرور', 'كلمة المرور الخاصة بحسابك'),
        ('دخول', 'اضغط للدخول لحسابك ومشاهدة منظومتك'),
        ('إنشاء حساب', 'إذا كانت المرة الأولى اضغط "إنشاء حساب" لتسجيل منظومتك'),
    ]
)

add_screen(doc,
    'خاص بالنت__انشاء حساب جديد .jpg',
    'إنشاء حساب جديد',
    [
        ('الاسم', 'اسمك الكامل'),
        ('رقم الهاتف', 'رقم هاتفك للتواصل'),
        ('الرقم التسلسلي للمرسلة', 'الرقم الموجود في واجهة الضبط المحلي (مثال: A8758188)'),
        ('كلمة المرور', 'اختر كلمة مرور لحسابك'),
        ('نوع المنظومة', 'اختر جهد المنظومة الكهربائية: 12V أو 24V أو 48V'),
        ('إنشاء الحساب', 'اضغط الزر الأزرق لإتمام التسجيل'),
    ]
)

add_screen(doc,
    'خاص بالنت__1782293776176.jpg',
    'شاشة المراقبة الرئيسية',
    [
        ('نسبة الشحن', 'نسبة شحن البطارية الحالية مع شريط بياني'),
        ('جهد البطارية', 'الجهد الفعلي للبطارية (مثال: 53.3V لمنظومة 48V)'),
        ('طاقة الألواح الشمسية', 'الطاقة المولّدة حالياً من الألواح الشمسية (بالواط)'),
        ('استهلاك الحمل', 'الطاقة التي تستهلكها الأجهزة الموصولة حالياً'),
        ('حرارة الإنفرتر', 'درجة حرارة الإنفرتر للكشف المبكر عن أي مشكلة'),
        ('مصدر الشحن', 'هل يشحن من الألواح الشمسية أم الكهرباء'),
    ]
)

add_screen(doc,
    'خاص بالنت__1782293776204.jpg',
    'شاشة حالة الأجهزة',
    [
        ('ساعات السخان 🔥', 'مجموع ساعات عمل السخان اليوم'),
        ('ساعات البراد ❄️', 'مجموع ساعات عمل البراد اليوم'),
        ('ساعات الكهرباء ⚡', 'مجموع ساعات توفر الكهرباء اليوم'),
        ('مخطط 24 ساعة', 'منحنى بياني يوضح تغير نسبة الشحن خلال الـ 24 ساعة الماضية'),
        ('أجهزة البراد', 'قائمة أجهزة البراد مع حالة كل جهاز (يعمل / متوقف)'),
        ('أجهزة السخان', 'قائمة أجهزة السخان مع حالة كل جهاز'),
    ]
)

# ── closing note ──────────────────────────────────────────────────────────────
add_para(doc, '', space_before=10)

info_tbl = doc.add_table(rows=1, cols=1)
no_borders(info_tbl)
c = info_tbl.cell(0, 0)
cell_bg(c, 'E8F0FA')
cell_border_color(c, '1A569A')
p = c.paragraphs[0]
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
rtl(p)
p.paragraph_format.space_before = Pt(8)
p.paragraph_format.space_after  = Pt(8)
r = p.add_run('🇸🇾  شركة برق لحلول الطاقة النظيفة — صناعة سورية  |  جميع الحقوق محفوظة')
cs_font(r, size=13, bold=True, color=(0x0A,0x3D,0x7A))

# ── save ──────────────────────────────────────────────────────────────────────
out = '/home/user/cataloc-for-barq-232/دليل_ضبط_تطبيق_BARQ.docx'
doc.save(out)
print(f'Saved: {out}')
