# -*- coding: utf-8 -*-
import os, math, subprocess
from playwright.sync_api import sync_playwright
import imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe()
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
W,H,FPS=1080,1920,24
BASE='http://localhost:8099'
os.makedirs(HERE+'/vframes/turn',exist_ok=True)
os.makedirs(HERE+'/vframes/end',exist_ok=True)
os.makedirs(HERE+'/vclips',exist_ok=True)

TURN_SEC=11.0
END_SEC=5.4
Nturn=int(TURN_SEC*FPS)
Nend=int(END_SEC*FPS)

with sync_playwright() as p:
    br=p.chromium.launch(executable_path='/opt/pw-browsers/chromium',
        args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swapchain','--ignore-gpu-blocklist'])
    pg=br.new_page(viewport={'width':W,'height':H},device_scale_factor=1)
    # --- turntable ---
    pg.goto(BASE+'/show.html')
    pg.wait_for_function("window.__ready===true || window.__error", timeout=45000)
    if pg.evaluate("()=>window.__error"): raise SystemExit('load err '+str(pg.evaluate("()=>window.__error")))
    HOLD=3.8  # after this, text fully settled
    for i in range(Nturn):
        t=i/FPS
        cst=min(t, HOLD)*1000.0
        # ease the rotation start (slow-in) then constant
        prog=i/Nturn
        angle= -2*math.pi*prog  # one full turn, natural direction
        pg.evaluate("(cst)=>{document.getAnimations().forEach(a=>{try{a.pause();a.currentTime=cst;}catch(e){}});}", cst)
        pg.evaluate("(a)=>window.renderAt(a)", angle)
        pg.screenshot(path=HERE+'/vframes/turn/f%04d.png'%i)
        if i%40==0: print('turn',i,'/',Nturn,flush=True)
    out=HERE+'/vclips/turn.mp4'
    subprocess.run([FF,'-y','-loglevel','error','-framerate',str(FPS),'-i',HERE+'/vframes/turn/f%04d.png',
        '-vf','fade=t=in:st=0:d=0.5,fade=t=out:st=%.2f:d=0.5,format=yuv420p'%(TURN_SEC-0.5),
        '-c:v','libx264','-preset','medium','-crf','18','-r',str(FPS),out],check=True)
    print('turn clip done',flush=True)
    # --- end card ---
    pg.goto(BASE+'/endcard.html')
    pg.wait_for_timeout(400)
    for i in range(Nend):
        cst=i/FPS*1000.0
        pg.evaluate("(cst)=>{document.getAnimations().forEach(a=>{try{a.pause();a.currentTime=cst;}catch(e){}});}", cst)
        pg.screenshot(path=HERE+'/vframes/end/f%04d.png'%i)
    out=HERE+'/vclips/end.mp4'
    subprocess.run([FF,'-y','-loglevel','error','-framerate',str(FPS),'-i',HERE+'/vframes/end/f%04d.png',
        '-vf','fade=t=in:st=0:d=0.4,fade=t=out:st=%.2f:d=0.4,format=yuv420p'%(END_SEC-0.4),
        '-c:v','libx264','-preset','medium','-crf','18','-r',str(FPS),out],check=True)
    print('end clip done',flush=True)
    br.close()

with open(HERE+'/vconcat.txt','w') as f:
    f.write("file '%s'\n"%(HERE+'/vclips/turn.mp4'))
    f.write("file '%s'\n"%(HERE+'/vclips/end.mp4'))
out=ROOT+'/فيديوهات_جاهزة/فيديو_المرسلة_ثلاثي_الأبعاد.mp4'
subprocess.run([FF,'-y','-loglevel','error','-f','concat','-safe','0','-i',HERE+'/vconcat.txt',
    '-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r',str(FPS),out],check=True)
print('FINAL',out,flush=True)
