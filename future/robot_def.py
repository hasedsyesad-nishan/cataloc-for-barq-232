# -*- coding: utf-8 -*-
"""
تعريف روبوت المستقبل (2225) — SVG معدني هولوغرافي.
كروم + زجاج + عين فايزر سماوية #5fd0ff + نواة طاقة + hover glow.
يُستخدم في فيديوهات حملة برق (الأسلوب المستقبلي — فيديو 22 وما بعده).

الاستخدام:  html = ROBOT.format(w=340)
مواصفات الأنيميشن (CSS تُضاف في المشهد نفسه):
  .floatbot  -> طفو عام لجسم الروبوت
  .armL/.armR -> تأرجح الأذرع
  .visor     -> نبض العين
  .hoverpad  -> توسّع وسادة الطفو
  .corebolt  -> وميض النواة
"""

ROBOT = r'''
<svg class="floatbot" width="{w}" viewBox="0 0 340 440" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="0.35" stop-color="#e9eef4"/>
      <stop offset="0.72" stop-color="#b9c3cf"/>
      <stop offset="1" stop-color="#8a97a6"/>
    </linearGradient>
    <linearGradient id="chrome2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#f4f7fb"/>
      <stop offset="0.5" stop-color="#c4ccd6"/>
      <stop offset="1" stop-color="#9aa6b4"/>
    </linearGradient>
    <radialGradient id="glass" cx="0.5" cy="0.4" r="0.75">
      <stop offset="0" stop-color="#0a2b45"/>
      <stop offset="0.6" stop-color="#061726"/>
      <stop offset="1" stop-color="#02080f"/>
    </radialGradient>
    <radialGradient id="coreGrad" cx="0.5" cy="0.5" r="0.6">
      <stop offset="0" stop-color="#8fe6ff"/>
      <stop offset="0.45" stop-color="#2aa6e6"/>
      <stop offset="1" stop-color="#0a3a63"/>
    </radialGradient>
    <linearGradient id="visorGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#1d6f9e" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#8fe9ff"/>
      <stop offset="1" stop-color="#1d6f9e" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="7" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softglow" x="-120%" y="-120%" width="340%" height="340%">
      <feGaussianBlur stdDeviation="12"/>
    </filter>
  </defs>

  <!-- وسادة الطفو المتوهجة -->
  <ellipse class="hoverpad" cx="170" cy="410" rx="88" ry="17" fill="#37c6ff" opacity="0.55" filter="url(#softglow)"/>
  <ellipse cx="170" cy="410" rx="60" ry="10" fill="#aef0ff" opacity="0.7" filter="url(#softglow)"/>

  <!-- الأذرع الطافية -->
  <g class="armL">
    <ellipse cx="86" cy="250" rx="27" ry="24" fill="url(#chrome2)"/>
    <ellipse cx="72" cy="300" rx="22" ry="20" fill="url(#chrome2)"/>
  </g>
  <g class="armR">
    <ellipse cx="254" cy="250" rx="27" ry="24" fill="url(#chrome2)"/>
    <ellipse cx="268" cy="300" rx="22" ry="20" fill="url(#chrome2)"/>
  </g>

  <!-- الجسم -->
  <path d="M108 210 L232 210 L242 250 Q246 258 240 268 L240 340 Q240 372 208 378 L132 378 Q100 372 100 340 L100 268 Q94 258 98 250 Z"
        fill="url(#chrome)" stroke="#eef3f8" stroke-width="2"/>
  <!-- لوحة النواة الداكنة -->
  <rect x="132" y="258" width="76" height="104" rx="16" fill="url(#glass)" stroke="#123a55" stroke-width="1.5"/>
  <!-- شرائط ضوء جانبية -->
  <rect x="121" y="272" width="7" height="74" rx="3.5" fill="#42c7ff" opacity="0.85" filter="url(#glow)"/>
  <rect x="212" y="272" width="7" height="74" rx="3.5" fill="#42c7ff" opacity="0.85" filter="url(#glow)"/>
  <!-- النواة + البرق -->
  <circle class="corebolt" cx="170" cy="310" r="30" fill="url(#coreGrad)" filter="url(#glow)"/>
  <path d="M176 290 L156 314 L168 314 L164 332 L184 306 L172 306 Z" fill="#ffffff"/>

  <!-- الرأس -->
  <!-- هوائي -->
  <rect x="164" y="60" width="12" height="16" rx="6" fill="#7fdcff" filter="url(#glow)"/>
  <!-- أذنان جانبيتان -->
  <rect x="86" y="128" width="20" height="46" rx="10" fill="url(#chrome2)"/>
  <rect x="234" y="128" width="20" height="46" rx="10" fill="url(#chrome2)"/>
  <rect x="92" y="140" width="7" height="22" rx="3.5" fill="#42c7ff" opacity="0.8" filter="url(#glow)"/>
  <rect x="241" y="140" width="7" height="22" rx="3.5" fill="#42c7ff" opacity="0.8" filter="url(#glow)"/>
  <!-- قبة الرأس -->
  <path d="M100 168 Q100 74 170 74 Q240 74 240 168 Q240 196 210 200 L130 200 Q100 196 100 168 Z"
        fill="url(#chrome)" stroke="#f2f6fb" stroke-width="2"/>
  <!-- زجاج الوجه -->
  <ellipse cx="170" cy="150" rx="66" ry="52" fill="url(#glass)" stroke="#0f3350" stroke-width="2"/>
  <!-- عين الفايزر -->
  <rect class="visor" x="112" y="142" width="116" height="15" rx="7.5" fill="url(#visorGrad)" filter="url(#glow)"/>
  <circle class="visor" cx="170" cy="149.5" r="8" fill="#ffffff" filter="url(#glow)"/>
</svg>
'''

# العلم السوري الجديد (SVG) — يُستخدم في شاشة الختام
FLAG_SVG = '''<svg width="66" height="44" viewBox="0 0 90 60"><rect width="90" height="20" fill="#007A3D"/><rect width="90" height="20" y="20" fill="#fff"/><rect width="90" height="20" y="40" fill="#000"/>
<polygon points="24,23.5 25.53,28.2 30.47,28.2 26.47,31.1 28,35.8 24,32.9 20,35.8 21.53,31.1 17.53,28.2 22.47,28.2" fill="#CE1126"/>
<polygon points="45,23.5 46.53,28.2 51.47,28.2 47.47,31.1 49,35.8 45,32.9 41,35.8 42.53,31.1 38.53,28.2 43.47,28.2" fill="#CE1126"/>
<polygon points="66,23.5 67.53,28.2 72.47,28.2 68.47,31.1 70,35.8 66,32.9 62,35.8 63.53,31.1 59.53,28.2 64.47,28.2" fill="#CE1126"/></svg>'''
