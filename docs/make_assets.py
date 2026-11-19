"""Generate original SVG mock product illustrations for the academic demo."""
from pathlib import Path
import html
root=Path(__file__).resolve().parents[1]
out=root/'assets'/'products'; out.mkdir(parents=True,exist_ok=True)
items=[
('nova-phone','phone','#94b8f2','#23365d'),('pixel-phone','phone','#ffbc9a','#9c4354'),
('orbit-laptop','laptop','#b0b6eb','#1e2444'),('arc-laptop','laptop','#c4ebde','#2e6f6a'),
('pulse-headphones','headphones','#e9d1a9','#836646'),('echo-earbuds','earbuds','#c9c0f2','#6b5a9e'),
('prism-monitor','monitor','#a2bbed','#243d72'),('spark-keyboard','keyboard','#ced9fa','#5b6aa0'),
('flux-mouse','mouse','#bfe8dc','#346c62'),('wave-speaker','speaker','#efd3b1','#9c6845'),
('slate-tablet','tablet','#c9d8ed','#526c8b'),('glow-watch','watch','#d4c9e9','#795ba0')]
base='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 440" role="img" aria-label="{label}"><defs>
<linearGradient id="device" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<linearGradient id="screen" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#151e35"/><stop offset=".5" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/></linearGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ffffff" stop-opacity=".26"/><stop offset="1" stop-color="#ffffff" stop-opacity=".02"/></linearGradient>
<filter id="shadow" x="-50%" y="-60%" width="200%" height="240%"><feGaussianBlur stdDeviation="16"/></filter></defs>
<ellipse cx="280" cy="370" rx="152" ry="24" fill="#172137" opacity=".18" filter="url(#shadow)"/>
{graphic}</svg>'''

def graphic(t):
 if t=='phone': return '''<g transform="translate(170 38) rotate(-8 100 168)"><rect x="0" y="0" width="205" height="345" rx="37" fill="#121b2e"/><rect x="8" y="8" width="189" height="329" rx="30" fill="url(#screen)"/><path d="M17 248 Q120 90 190 45 L190 318 Q100 306 17 248" fill="url(#glass)"/><path d="M17 274 Q108 212 196 138" stroke="#f4f7ff" stroke-opacity=".25" stroke-width="4" fill="none"/><rect x="70" y="15" width="63" height="17" rx="8.5" fill="#131a2b"/><circle cx="147" cy="23" r="4" fill="#556987"/><rect x="85" y="323" width="36" height="3" rx="1.5" fill="#e5f2ff" opacity=".45"/></g>'''
 if t=='laptop': return '''<g transform="translate(76 65)"><rect x="47" y="0" width="360" height="243" rx="15" fill="#263044"/><rect x="56" y="9" width="342" height="224" rx="8" fill="url(#screen)"/><path d="M68 222 Q190 54 380 26 L380 224 Z" fill="url(#glass)"/><circle cx="226" cy="6" r="2.6" fill="#8898bd"/><path d="M2 258 H452 L417 277 H37 Z" fill="url(#device)" stroke="#5b6678" stroke-opacity=".45"/><path d="M65 258 H387 L383 264 H69 Z" fill="#364158" opacity=".42"/><rect x="186" y="262" width="82" height="9" rx="4" fill="#8a99a8" opacity=".5"/></g>'''
 if t=='monitor': return '''<g transform="translate(76 32)"><rect x="14" y="25" width="428" height="258" rx="20" fill="#1b2433"/><rect x="23" y="34" width="410" height="239" rx="10" fill="url(#screen)"/><path d="M39 258 Q196 38 410 48 L410 260 Z" fill="url(#glass)"/><rect x="202" y="283" width="50" height="57" fill="#3d4b5b"/><path d="M142 353 Q227 340 313 353 L338 365 H116 Z" fill="url(#device)"/><circle cx="227" cy="278" r="3" fill="#8492a5"/></g>'''
 if t=='headphones': return '''<g transform="translate(126 40)"><path d="M56 226 V158 C56 40 253 40 253 158 V226" fill="none" stroke="#27313c" stroke-width="55" stroke-linecap="round"/><path d="M56 219 V147 C56 32 253 32 253 147 V219" fill="none" stroke="url(#device)" stroke-width="38" stroke-linecap="round"/><rect x="4" y="182" width="92" height="140" rx="39" fill="#232d3b"/><rect x="16" y="191" width="71" height="122" rx="33" fill="url(#device)"/><rect x="215" y="182" width="92" height="140" rx="39" fill="#232d3b"/><rect x="225" y="191" width="71" height="122" rx="33" fill="url(#device)"/><path d="M24 218 Q32 212 42 209" stroke="#fff" stroke-opacity=".38" stroke-width="6" stroke-linecap="round"/></g>'''
 if t=='earbuds': return '''<g transform="translate(116 72)"><rect x="35" y="158" width="260" height="158" rx="75" fill="#e9edf5" stroke="#cbd0e0" stroke-width="5"/><rect x="50" y="166" width="230" height="132" rx="65" fill="url(#device)"/><rect x="58" y="180" width="214" height="115" rx="60" fill="url(#glass)"/><path d="M54 217 H276" stroke="#e9edf5" stroke-opacity=".65" stroke-width="3"/><circle cx="166" cy="268" r="4.5" fill="#f4f7ff"/><g fill="#e9edf5" stroke="#cbd2df" stroke-width="3"><path d="M83 14 Q119 -6 146 29 Q154 65 123 79 L123 145 Q99 159 92 138 L88 82 Q53 64 67 32 Q70 20 83 14Z"/><path d="M222 14 Q258 -6 285 29 Q293 65 262 79 L262 145 Q238 159 231 138 L227 82 Q192 64 206 32 Q209 20 222 14Z"/></g></g>'''
 if t=='keyboard': return '''<g transform="translate(57 120) rotate(-7 225 130)"><path d="M25 45 H434 Q447 45 452 60 L477 216 Q481 235 460 238 H17 Q-2 238 3 219 L10 64 Q13 45 25 45Z" fill="#252f42"/><path d="M26 59 H430 L450 219 H20 Z" fill="url(#device)"/>{keys}</g>'''.replace('{keys}', ''.join(f'<rect x="{32+j*33}" y="{72+i*33}" width="26" height="23" rx="5" fill="#263246" opacity=".87"/>' for i in range(4) for j in range(12))+ '<rect x="143" y="204" width="205" height="12" rx="5" fill="#263246" opacity=".85"/>')
 if t=='mouse': return '''<g transform="translate(152 30) rotate(9 110 177)"><path d="M110 8 C31 8 22 100 20 202 Q17 335 110 349 Q204 335 201 202 C200 100 187 8 110 8Z" fill="#253342"/><path d="M110 18 C43 18 34 107 34 201 Q31 320 110 335 Q190 320 187 201 C186 107 177 18 110 18Z" fill="url(#device)"/><path d="M110 18 V146" stroke="#28374f" stroke-opacity=".6" stroke-width="4"/><rect x="101" y="70" width="18" height="57" rx="9" fill="#253342"/><path d="M45 257 Q74 299 150 284" fill="none" stroke="#fff" stroke-opacity=".18" stroke-width="8"/></g>'''
 if t=='speaker': return '''<g transform="translate(158 32) rotate(-8 120 170)"><rect x="10" y="12" width="220" height="343" rx="56" fill="#29303e"/><rect x="19" y="20" width="202" height="327" rx="51" fill="url(#device)"/><circle cx="120" cy="116" r="73" fill="#222c3a"/><circle cx="120" cy="116" r="62" fill="#3b4755"/><circle cx="120" cy="116" r="31" fill="url(#device)"/><circle cx="120" cy="264" r="48" fill="#263343"/><circle cx="120" cy="264" r="23" fill="url(#device)"/><circle cx="120" cy="29" r="4" fill="#e9edf5"/></g>'''
 if t=='tablet': return '''<g transform="translate(108 25) rotate(-6 170 180)"><rect x="1" y="0" width="336" height="366" rx="31" fill="#212b3b"/><rect x="12" y="11" width="314" height="344" rx="22" fill="url(#screen)"/><path d="M18 298 Q110 55 323 74 L323 347 H18Z" fill="url(#glass)"/><circle cx="169" cy="6" r="2" fill="#c8d3e6"/></g>'''
 if t=='watch': return '''<g transform="translate(137 23)"><rect x="80" y="0" width="130" height="390" rx="36" fill="url(#device)"/><rect x="55" y="106" width="180" height="185" rx="50" fill="#263145"/><rect x="65" y="116" width="160" height="165" rx="43" fill="#111827"/><circle cx="145" cy="196" r="55" stroke="url(#device)" stroke-width="12" fill="none"/><path d="M145 154 V198 L177 213" stroke="#d8f3eb" stroke-linecap="round" stroke-width="9" fill="none"/><rect x="235" y="167" width="12" height="34" rx="6" fill="#5a6175"/><path d="M112 54 H178 M112 344 H178" stroke="#fff" stroke-opacity=".18" stroke-width="13" stroke-linecap="round"/></g>'''
 return ''
for name,t,c1,c2 in items:
 svg=base.format(label=html.escape(name.replace('-',' ').title()),c1=c1,c2=c2,graphic=graphic(t))
 (out/f'{name}.svg').write_text(svg)

hero='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 590"><defs>
<linearGradient id="lap" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#30404c"/><stop offset="1" stop-color="#0b1522"/></linearGradient>
<linearGradient id="glow" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#c7ff8a"/><stop offset=".45" stop-color="#8dc5c4"/><stop offset="1" stop-color="#35486a"/></linearGradient>
<linearGradient id="phone" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#b9d5ec"/><stop offset="1" stop-color="#253753"/></linearGradient>
<linearGradient id="shine" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#ffffff" stop-opacity=".22"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></linearGradient>
<filter id="blur"><feGaussianBlur stdDeviation="35"/></filter>
<filter id="shadow"><feGaussianBlur stdDeviation="16"/></filter></defs>
<ellipse cx="380" cy="525" rx="290" ry="35" fill="#000" opacity=".3" filter="url(#shadow)"/>
<circle cx="405" cy="252" r="205" fill="#b9f676" opacity=".15" filter="url(#blur)"/>
<g transform="translate(40 76) rotate(-6 340 260)"><rect x="80" y="50" width="500" height="350" rx="24" fill="#3c4c5d"/><rect x="92" y="62" width="476" height="327" rx="13" fill="#0e1825"/><rect x="105" y="75" width="450" height="301" rx="8" fill="url(#glow)"/><path d="M105 365 C165 220 273 160 556 103 L556 376 H105" fill="#151e32" opacity=".45"/><circle cx="340" cy="56" r="3" fill="#dce5ed" opacity=".8"/><path d="M7 405 H661 L620 437 H49Z" fill="url(#lap)"/><path d="M150 408 H523 L541 422 H125Z" fill="#4c6170" opacity=".7"/><rect x="292" y="425" width="94" height="6" rx="3" fill="#9bacb5" opacity=".55"/></g>
<g transform="translate(455 130) rotate(12 85 200)"><rect x="0" y="0" width="179" height="346" rx="36" fill="#101b2a" stroke="#a7b6be" stroke-width="5"/><rect x="9" y="8" width="161" height="329" rx="29" fill="url(#phone)"/><path d="M13 264 Q88 89 166 40 V330 H13Z" fill="#7cc4bb" opacity=".47"/><path d="M12 297 Q87 175 167 138" stroke="#fafafa" stroke-width="3" opacity=".28" fill="none"/><rect x="56" y="16" width="65" height="17" rx="9" fill="#142133"/></g>
<g transform="translate(130 395) rotate(-15 108 54)"><rect x="1" y="5" width="213" height="104" rx="52" fill="#ece8dd"/><path d="M20 36 Q100 7 195 34 V66 Q115 96 20 64Z" fill="#c2baa9" opacity=".28"/><path d="M15 54 H200" stroke="#c9c5bb" stroke-width="2"/><circle cx="108" cy="83" r="4" fill="#b2ada3"/></g>
<g opacity=".78"><circle cx="96" cy="178" r="5" fill="#d5faab"/><circle cx="677" cy="95" r="7" fill="#d5faab"/><path d="M685 314 l11 -11 m-11 0 l11 11" stroke="#d5faab" stroke-width="2"/></g></svg>'''
(root/'assets'/'hero-tech.svg').write_text(hero)
print('Created',len(items),'product SVGs and hero SVG')
