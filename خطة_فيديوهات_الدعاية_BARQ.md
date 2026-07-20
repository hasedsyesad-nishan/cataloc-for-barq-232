# خطة إنتاج فيديوهات الدعاية لنظام برق BARQ

خطة عملية لإنتاج **3 فيديوهات يومياً** (فيديو من كل منصة مجانية) باستخدام صور المنتج الموجودة في مجلد `Advertising campaign of barq`، مع مكتبة برومبتات جاهزة للنسخ تغطي أسبوعاً كاملاً بدون تكرار.

---

## 1) المنصات الثلاث المعتمدة يومياً

| # | المنصة | الرابط | الكريدت المجاني | علامة مائية؟ |
|---|--------|--------|-----------------|---------------|
| 1 | ImagineArt | https://www.imagine.art/ | 100 كريدت يتجدد يومياً | ❌ بدون |
| 2 | Pika | https://pika.art/ | ~150 كريدت شهرياً | ❌ بدون |
| 3 | Kling AI | https://klingai.com/ | ~66 كريدت يومياً | ✅ يوجد |
| احتياط | Google Flow (Veo 3.1) | https://labs.google/fx/tools/flow | حصة يومية | ✅ "Made with Veo" |

**قاعدة التشغيل اليومي:** كل يوم تدخل على المنصات الثلاث الأولى، ترفع صورة واحدة، تلصق برومبت اليوم من الجدول في القسم 5، وتولّد مقطع 5–10 ثوانٍ من كل منصة. الكريدت يتجدد فتكرر العملية في اليوم التالي ببرومبت جديد.

**إعدادات مهمة عند التوليد:**
- اختر النسبة **9:16 (عمودي)** إذا كان الهدف واتساب/فيسبوك ريلز/تيك توك، أو **16:9** ليوتيوب.
- مدة المقطع: 5–10 ثوانٍ، وبعدين تدمج المقاطع في CapCut.
- ولّد الفيديو **بدون أي نص على الشاشة** — النص العربي يضاف لاحقاً في CapCut (المولدات تكتب العربي بشكل خاطئ).

---

## 2) الصور الجاهزة في المستودع — مجلد `صور_الدعاية/`

استخرجت صور المنتج الحقيقية من الكتالوج ونظمتها في مجلد `صور_الدعاية/` داخل هذا المستودع، جاهزة للتحميل والرفع مباشرة على منصات التوليد:

| الملف | المحتوى | تصلح للبرومبتات |
|-------|---------|------------------|
| `المرسلة_3_زوايا.png` | المرسلة السوداء: الزر الأبيض الجانبي، الواجهة (DC 12V IN / RS-232 / ليد أحمر)، منفذ RJ45 | A1, A2, B2, B5 والمشاهد التعليمية |
| `جهاز_البراد_3_زوايا.jpeg` | جهاز البراد الأسود بالفيشة والزر الذهبي وشعار BARQ | مشاهد البراد |
| `جهاز_المكيف_3_زوايا.png` | جهاز المكيف أبيض/أسود بترمينالات (خرج/نتر/دخل) والزر الأحمر | مشاهد المكيف |
| `جهاز_السخان_مجموعة.png` | جهاز السخان بالواجهة الذهبية والشاشة الرقمية (فولت/أمبير) | A4 ومشاهد السخان |
| `سكرين_لوحة_التحكم.jpg` | الشاشة الرئيسية: ساعات السخان/البراد/الكهرباء، مخطط 24 ساعة، حالة الأجهزة | A3, B4 |
| `سكرين_انشاء_حساب.jpg` | شاشة إنشاء الحساب (48V/24V/12V) | مشهد إنشاء الحساب |
| `سكرين_ضبط_السخان.jpg` | خيارات التشغيل حسب النسبة والتشغيل القسري | مشاهد ضبط السخان |

**صور ما زلت تحتاج تصويرها بنفسك** (غير موجودة في الكتالوج):
1. صورة الألواح الشمسية على السطح وقت الظهر أو الغروب.
2. صورة الإنفرتر الحقيقي موصولاً بالمرسلة بكابل الشبكة (مهمة جداً للمشاهد التعليمية).

> نصيحة: الصورة النظيفة بخلفية بسيطة تعطي نتيجة أفضل بكثير من الصورة المزدحمة.

---

## 2.5) أوصاف الأجهزة الحقيقية بالإنجليزي — الصقها مع أي برومبت

عند رفع صورة الجهاز مع البرومبت، أضف السطر المناسب في نهاية البرومبت حتى لا يغيّر المولّد شكل الجهاز:

**المرسلة:**
```
Use the attached image of the black BARQ transmitter device exactly as shown — a small matte-black rectangular box with a blue-and-silver BARQ lightning logo, a red LED, labels "DC 12V IN" and "RS-232", a round white side button, an RJ45 port and DC jack on its side. Do not alter its shape, logo, ports, or color.
```

**جهاز البراد:**
```
Use the attached image of the black BARQ fridge controller exactly as shown — a slim black plug-through device with a European wall plug on its back, a power outlet on its side, silver corner screws, a blue BARQ lightning logo and a round golden button. Do not alter its shape, logo, or color.
```

**جهاز المكيف:**
```
Use the attached image of the BARQ air-conditioner controller exactly as shown — a rectangular wall-mounted box with a white front panel reading "BARQ" and Arabic text, black side casing, terminal connectors on top labeled in Arabic (input / neutral / output), and a small red button at the bottom. Do not alter its shape, labels, or colors.
```

**جهاز السخان:**
```
Use the attached image of the BARQ water heater controller exactly as shown — a wall-mounted box with a shiny gold front panel, BARQ lightning logo, a small digital display showing voltage and amperage readings, white terminal connectors on top and a silver heatsink on its back. Do not alter its shape, logo, display, or colors.
```

---

## 3) مكتبة البرومبتات — فيديوهات تعريفية بالمنتج

انسخ البرومبت كما هو بالإنجليزي. لكل برومبت نسخة طويلة ونسخة قصيرة (لو المنصة تحدد عدد الكلمات).

### برومبت A1 — الإعلان الرئيسي السريع (الصورة: المرسلة)

```
Fast-paced, energetic commercial for a smart solar power controller. Quick dynamic cuts: sunlight flashing across solar panels, close-up on a sleek matte-black smart device with a glowing blue lightning logo and a blinking red LED light, a hand tapping a smartphone screen showing a live dashboard with battery percentage climbing, a refrigerator light switching on instantly, warm home lighting turning on during a blackout. Snappy camera movement — quick zooms, whip pans, rhythmic cuts synced to an upbeat beat. Bright vibrant color grading, golden-hour sunlight, clean modern tech aesthetic, ultra-realistic, 4K, commercial advertisement style, no on-screen text.
```

نسخة قصيرة:

```
Energetic solar-tech commercial, quick dynamic cuts between solar panels, a glowing smart controller device, a phone dashboard with rising battery stats, and a fridge light switching on. Fast snappy camera movement, vibrant golden-hour lighting, modern cinematic style, 4K, no text.
```

### برومبت A2 — كيف يعمل النظام (الصورة: المرسلة موصولة بالإنفرتر)

```
Clean modern product commercial showing a smart home energy system coming to life. The camera slowly orbits a small matte-black smart device with a blue lightning logo, connected to a solar inverter with a network cable, its LED blinking rhythmically. Glowing data particles flow wirelessly from the device through the air toward a refrigerator and a water heater across the room, then up to a smartphone. Soft depth of field, cool blue and warm gold lighting, futuristic but realistic smart-home atmosphere, cinematic lighting, 4K, commercial style, no on-screen text.
```

نسخة قصيرة:

```
Cinematic smart-home commercial: a black smart controller with a blue lightning logo connected to a solar inverter blinks, glowing wireless signals flow to a fridge, water heater and a smartphone. Cool blue and gold lighting, realistic, 4K, no text.
```

### برومبت A3 — لوحة التحكم والمراقبة عن بعد (الصورة: سكرين شوت الداشبورد)

```
Sleek technology commercial focused on a smartphone screen displaying a live solar energy dashboard: battery percentage rising, power graphs animating smoothly, device toggles switching on. The phone is held in a hand, city lights blurred in the background at dusk. Camera pushes in slowly on the glowing screen, subtle reflections, premium fintech-style aesthetic, crisp UI animations, cinematic shallow depth of field, 4K, commercial advertisement, no on-screen text.
```

نسخة قصيرة:

```
Premium tech ad: close-up of a smartphone showing a live solar battery dashboard with rising stats and smooth animated graphs, held in hand at dusk, cinematic depth of field, 4K, no text.
```

### برومبت A4 — السخان والاستفادة من فائض الشمس (الصورة: جهاز السخان)

```
Bright optimistic commercial about solar water heating. Golden sunlight pours over rooftop solar panels, energy visualized as warm glowing streams flowing into a smart controller device with a digital display, then into a water heater. Steam gently rises from a hot shower head, a family home glows warmly. Smooth cinematic camera moves, warm golden color palette, ultra-realistic, 4K, advertisement style, no on-screen text.
```

نسخة قصيرة:

```
Warm cinematic ad: golden sunlight over solar panels, glowing energy flows into a smart controller then a water heater, steam rises from a hot shower. Golden color palette, realistic, 4K, no text.
```

---

## 4) مكتبة البرومبتات — فيديوهات الإقناع (الخسارة مقابل التوفير)

هذه الفيديوهات هدفها إقناع العميل أنه **بدون برق يخسر طاقة ومال وعمر بطاريته**، ومعه **يوفر ويرتاح**.

### برومبت B1 — معاناة انقطاع الكهرباء (بدون المنتج)

```
Dramatic emotional scene: a dark home during a power blackout at night, a worried man holding his phone flashlight, opening a refrigerator with warm spoiled food inside, a dead battery indicator, candles flickering on a table. Desaturated cold blue color grading, slow tense camera movement, cinematic realism, 4K, commercial storytelling style, no on-screen text. Then a sudden transition: warm light floods the home as power returns, hopeful atmosphere.
```

نسخة قصيرة:

```
Cinematic story ad: dark home in a blackout, worried man, fridge with spoiled food, dead battery icon, candles — then warm light suddenly returns and the home glows with hope. Realistic, 4K, no text.
```

### برومبت B2 — البطارية تموت ببطء (الخوف من الخسارة)

```
Dramatic close-up commercial: a home battery indicator draining from 80% down to 10%, red warning glow, lights in the house dimming one by one, a refrigerator light fading out. Tense atmosphere, dark moody lighting with red accents. Then a small black smart device with a blue lightning logo blinks to life, the drain stops, the percentage stabilizes and slowly climbs, lights return warm and steady. Cinematic contrast between cold red danger and warm safe light, ultra-realistic, 4K, ad style, no on-screen text.
```

نسخة قصيرة:

```
Dramatic ad: home battery draining fast with red warning glow and dimming lights — a black smart device blinks on, the drain stops, battery climbs, warm light returns. Cinematic, 4K, no text.
```

### برومبت B3 — المال المهدور (فاتورة وطاقة ضائعة)

```
Symbolic commercial about wasted energy and money: banknotes and coins dissolving into thin air above a rooftop at noon while bright sunlight hits solar panels unused, an electricity meter spinning fast. Then a smart controller device activates with a green LED, the dissolving money reverses back into a savings jar filling up, sunlight now flowing as golden energy into the home. Clever visual metaphor, vibrant realistic style, smooth transitions, 4K, advertisement, no on-screen text.
```

نسخة قصيرة:

```
Visual metaphor ad: money dissolving into air over unused solar panels and a fast-spinning electricity meter — a smart device activates, money flows back into a filling savings jar, golden energy enters the home. 4K, no text.
```

### برومبت B4 — الراحة والسيطرة وأنت بعيد (السفر/العمل)

```
Lifestyle commercial: a man sitting relaxed in a cafe far from home, checking his phone showing a solar dashboard — battery healthy, fridge running, all green. Split-scene feeling: his home appears calm and well-lit, refrigerator humming, water heater ready. He smiles and puts the phone away with total peace of mind. Warm natural lighting, modern lifestyle cinematography, shallow depth of field, 4K, commercial style, no on-screen text.
```

نسخة قصيرة:

```
Lifestyle ad: a relaxed man in a cafe checks a solar dashboard on his phone — battery healthy, home safe and lit — he smiles with peace of mind. Warm cinematic look, 4K, no text.
```

### برومبت B5 — قبل / بعد (المقارنة الصريحة)

```
Split-screen style commercial comparing two homes at night during a city blackout. Left: dark windows, candles, a frustrated family, food spoiling. Right: warm glowing windows, refrigerator running, kids doing homework under bright light, a small black smart device with a blue lightning logo blinking calmly near the inverter. Camera slowly pushes toward the bright home. High contrast cinematic grading, emotional storytelling, ultra-realistic, 4K, advertisement, no on-screen text.
```

نسخة قصيرة:

```
Split-screen ad: two homes in a blackout — one dark with candles and frustration, one warm and bright with a blinking smart controller. Camera pushes toward the bright home. Cinematic, 4K, no text.
```

---

## 5) جدول الإنتاج الأسبوعي — 3 فيديوهات يومياً

كل يوم: نفس البرومبت على المنصات الثلاث (تحصل على 3 نتائج مختلفة وتختار الأفضل)، أو برومبت مختلف لكل منصة حسب الجدول:

| اليوم | ImagineArt | Pika | Kling AI | الصورة المرفوعة |
|-------|-----------|------|----------|------------------|
| 1 | A1 الإعلان الرئيسي | A1 | A1 | المرسلة |
| 2 | B1 معاناة الانقطاع | B5 قبل/بعد | B1 | صورة منزل/الألواح |
| 3 | A3 الداشبورد | A3 | B4 وأنت بعيد | سكرين شوت اللوحة |
| 4 | B2 البطارية تموت | B2 | A2 كيف يعمل | المرسلة + الإنفرتر |
| 5 | B3 المال المهدور | B3 | B3 | الألواح الشمسية |
| 6 | A4 السخان | A4 | A4 | جهاز السخان |
| 7 | أعد توليد أفضل برومبتين بنتائج ضعيفة | — | — | حسب الحاجة |

بنهاية الأسبوع يكون عندك **15–20 مقطعاً** تختار منها الأفضل وتدمجها في CapCut لإنتاج:
- إعلان تعريفي 30 ثانية (A1 + A2 + A3).
- إعلان إقناعي عاطفي 30–40 ثانية (B1 أو B5 + B2 + B4 + لقطة ختامية من A1).

---

## 6) النصوص العربية للإضافة في CapCut

بعد توليد الفيديو، أضف الشعار واسم Barq وهذه النصوص في CapCut:

**للفيديوهات التعريفية:**
- «برق — نظام ذكي لمراقبة وإدارة الطاقة الشمسية»
- «راقب بطاريتك من أي مكان في العالم»
- «يعمل حتى بدون إنترنت»
- «صناعة سورية 🇸🇾 — دعم فني مباشر»

**لفيديوهات الإقناع (الخطاف Hook في أول ثانيتين):**
- «كم مرة خرب أكلك بالبراد بسبب انقطاع الكهرباء؟»
- «بطاريتك عم تموت وأنت ما بتعرف!»
- «شمس مجانية فوق سطحك… وأنت عم تدفع مصاري؟!»
- «مع برق: البراد شغال، البطارية محمية، والمصاري بجيبتك»

**دعوة لاتخاذ إجراء (آخر الفيديو) — بدون ذكر أي سعر:**

السياسة: لا يُذكر السعر في أي فيديو إطلاقاً. الهدف دفع العميل للاتصال برقم الشركة.

- «للطلب والاستفسار، اتصل الآن: 0936177050»
- «راسلنا واتساب على: 0936177050 — والتركيب بسيط»
- «برق… وفّر طاقتك، طوّل عمر بطاريتك. اتصل: 0936177050»
- «الكمية محدودة — احجز جهازك الآن: 0936177050»

> يفضّل إبقاء الرقم 0936177050 ظاهراً في آخر 3 ثوانٍ من الفيديو بخط كبير مع أيقونة اتصال/واتساب.

**ملاحظة التعليق الصوتي:** مولدات الفيديو (Veo وغيرها) لا تنطق العربية الفصحى بدقة موثوقة. ولّد المشاهد صامتة، وسجّل التعليق الصوتي منفصلاً — بصوتك أو بأداة تحويل نص لكلام تدعم العربية بجودة عالية (مثل ElevenLabs) — ثم ركّبه فوق الفيديو في CapCut.

---

## 7) ملاحظات تشغيلية

1. **ابدأ بـ ImagineArt وPika** — بدون علامة مائية على المجاني.
2. نتيجة Kling ذات العلامة المائية تصلح للتجربة واختيار الحركة، وممكن قص العلامة في CapCut إذا كانت في الزاوية.
3. إذا خرجت النتيجة غير مقنعة، أعد التوليد بنفس البرومبت — كل توليدة تعطي نتيجة مختلفة، والكريدت اليومي يكفي لـ 2–3 محاولات.
4. لا تكتب أي نص عربي داخل البرومبت — النص كله يضاف في CapCut.
5. احفظ كل المقاطع الناتجة في مجلد واحد باسم اليوم والبرومبت (مثال: `Day2-B1-Pika.mp4`) حتى يسهل المونتاج لاحقاً.

---

## 8) طريقة الإنتاج الداخلية (للجلسات القادمة)

الفيديوهات تُنتج بالكامل داخل بيئة العمل بدون منصات خارجية:
1. تصميم كل مشهد كصفحة HTML/CSS احترافية (خط Cairo، تدرجات، بطاقات، توهجات) بمقاس 1350×2400.
2. تصويرها بـ Chromium عبر Playwright (`executable_path=/opt/pw-browsers/chromium`).
3. تحريكها بـ ffmpeg (`pip install imageio-ffmpeg`): zoompan (تقريب/إبعاد 1.12) + fade، ثم دمج المقاطع concat بمخرج 1080×1920@24fps.
4. الخطوط: `npm pack @expo-google-fonts/cairo@0.2.3` (نسخة 0.2.3 تحديداً — تحتوي ملفات ttf).
5. التحقق البصري من عدة إطارات إلزامي قبل التسليم (الانتباه لقصّ النصوص عند حواف التقريب).
6. الناتج يُحفظ مرقّماً في `فيديوهات_جاهزة/` ويُرسل للمستخدم.
7. **العلم السوري:** يُمنع استخدام إيموجي 🇸🇾 (يعرض العلم القديم). يُرسم العلم الجديد دائماً كـ SVG: ثلاثة أشرطة أفقية — أخضر ‎#007A3D‎ فوق، أبيض بالوسط، أسود تحت، وثلاث نجوم خماسية حمراء ‎#CE1126‎ في الشريط الأبيض.
