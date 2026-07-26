# خط إنتاج فيديوهات المنتجات ثلاثية الأبعاد (3D turntable)

يحوّل نموذج GLB لأي جهاز برق إلى فيديو دوران احترافي 1080×1920.

## المتطلبات (يُعاد تجهيزها إن كانت الحاوية جديدة)
- three.js:  `npm pack three@0.160.0 && tar xf three-0.160.0.tgz`  (يُنتج مجلد package/)
- خطوط Cairo في `fonts/`  (من `@expo-google-fonts/cairo@0.2.3`)
- `grain.png` حبيبات فيلمية
- توليد `glbdata.js`:  base64 لملف الـ glb داخل `window.GLB_URI`

## الخطوات
1. ضع نموذج الجهاز باسم `mursila.glb` (أو عدّل المسار) وولّد `glbdata.js`.
2. شغّل خادم محلي:  `python3 -m http.server 8099`
3. `show.html` = مشهد الاستوديو + الدوران،  `endcard.html` = البطاقة الختامية.
4. `render_video.py` يعرض الإطارات عبر Playwright/Chromium (WebGL/SwiftShader) ويجمعها بـ ffmpeg.

WebGL يعمل headless عبر:  `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swapchain`
