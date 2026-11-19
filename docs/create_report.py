"""Create the six-part PDF submission draft using verified browser screenshots."""
from pathlib import Path
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, Preformatted, KeepTogether, Flowable
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'CSCI426_Bitronix_Phase1_Report.pdf'
DPI=150
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DejaVu',FONT));pdfmetrics.registerFont(TTFont('DejaVuBold',BOLD))
DARK=colors.HexColor('#162820'); GREEN=colors.HexColor('#607f4f'); LIME=colors.HexColor('#c9f789'); MUTED=colors.HexColor('#687970'); BORDER=colors.HexColor('#e4ebe3'); LIGHT=colors.HexColor('#f3f8ef')
styles={
 'title':ParagraphStyle('title',fontName='DejaVuBold',fontSize=25,leading=31,textColor=DARK,spaceAfter=12),
 'heading':ParagraphStyle('heading',fontName='DejaVuBold',fontSize=20,leading=27,textColor=DARK,spaceAfter=10),
 'sub':ParagraphStyle('sub',fontName='DejaVuBold',fontSize=11.5,leading=17,textColor=DARK,spaceBefore=14,spaceAfter=8),
 'body':ParagraphStyle('body',fontName='DejaVu',fontSize=9.25,leading=15,textColor=colors.HexColor('#344339'),spaceAfter=9),
 'small':ParagraphStyle('small',fontName='DejaVu',fontSize=8.1,leading=13,textColor=MUTED,spaceAfter=6),
 'eyebrow':ParagraphStyle('eyebrow',fontName='DejaVuBold',fontSize=8,leading=13,textColor=GREEN,spaceAfter=10),
 'tablehead':ParagraphStyle('tablehead',fontName='DejaVuBold',fontSize=8.2,leading=12,textColor=DARK),
 'cell':ParagraphStyle('cell',fontName='DejaVu',fontSize=8,leading=12,textColor=colors.HexColor('#465449')),
 'code':ParagraphStyle('code',fontName='Courier',fontSize=7.4,leading=11,textColor=colors.HexColor('#d7f9dc')),
 'white':ParagraphStyle('white',fontName='DejaVu',fontSize=9.3,leading=16,textColor=colors.white),
 'cover-meta':ParagraphStyle('cover-meta',fontName='DejaVuBold',fontSize=9,leading=14,textColor=DARK),
}
W,H=A4
class CoverBanner(Flowable):
 def __init__(self):Flowable.__init__(self);self.width=510;self.height=235
 def draw(self):
  c=self.canv;c.setFillColor(DARK);c.roundRect(0,0,self.width,self.height,15,stroke=0,fill=1)
  c.setFillColor(LIME);c.setFont('DejaVuBold',9);c.drawString(31,200,'CSCI426 / ADVANCED WEB PROGRAMMING')
  c.setFillColor(colors.white);c.setFont('DejaVuBold',27);c.drawString(31,146,'BITRONIX')
  c.drawString(31,110,'Technology Store &')
  c.drawString(31,76,'Repair Portal')
  c.setFillColor(colors.HexColor('#b9d2bb'));c.setFont('DejaVu',10);c.drawString(32,35,'Project Phase 1  |  Responsive ReactJS Frontend')
  c.setFillColor(LIME);c.circle(self.width-49,self.height-49,12,stroke=0,fill=1)
  c.setFillColor(colors.HexColor('#76a45c'));c.circle(self.width-85,self.height-69,6,stroke=0,fill=1)

def frame(c,doc):
 c.saveState()
 if doc.page>1:
  c.setFillColor(DARK);c.rect(0,H-11,W,11,stroke=0,fill=1)
  c.setFont('DejaVuBold',7.2);c.setFillColor(GREEN);c.drawString(43,H-39,'BITRONIX / CSCI426 / PHASE 1')
 c.setStrokeColor(BORDER);c.line(43,42,W-43,42)
 c.setFont('DejaVu',7.2);c.setFillColor(MUTED);c.drawString(43,28,'Fall 2026 - Academic frontend demonstration')
 c.drawRightString(W-43,28,f'{doc.page}')
 c.restoreState()

def p(txt,style='body'):return Paragraph(txt,styles[style])
def head(k,t):return [p(k,'eyebrow'),p(t,'heading')]
def image_crop(name,box,wide=500):
 source=PILImage.open(ROOT/'screenshots'/name).convert('RGB');crop=source.crop(box)
 tmp=Path('/tmp')/('bitronix_report_crop_'+name)
 crop.save(tmp,quality=88,optimize=True)
 height=wide*crop.height/crop.width
 im=Image(str(tmp),width=wide,height=height)
 im.hAlign='CENTER';return im

def panel(rows,widths=None):
 cells=[[p(str(x),'tablehead' if i==0 else 'cell') for x in row] for i,row in enumerate(rows)]
 t=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([
  ('BACKGROUND',(0,0),(-1,0),LIGHT),('GRID',(0,0),(-1,-1),.45,BORDER),
  ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),11),('RIGHTPADDING',(0,0),(-1,-1),10),
  ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),
 ]))
 return t

def dark_snippet(code):
 t=Table([[Preformatted(code,styles['code'])]],colWidths=[510]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),DARK),('BOX',(0,0),(-1,-1),.5,DARK),('LEFTPADDING',(0,0),(-1,-1),15),('RIGHTPADDING',(0,0),(-1,-1),14),('TOPPADDING',(0,0),(-1,-1),13),('BOTTOMPADDING',(0,0),(-1,-1),12)]));return t

story=[]
# 1. Title page
story += [Spacer(1,36),CoverBanner(),Spacer(1,22),p('DEPARTMENT OF COMPUTER SCIENCE AND INFORMATION TECHNOLOGY','eyebrow'),p('Project report','title'),p('A working frontend prototype with responsive layouts, product exploration, local cart management, repair-ticket tracking, and a contact interface.','body'),Spacer(1,18)]
story.append(panel([
 ['Submission detail','To complete before classroom submission'],
 ['Student name / student ID','[Add your name and university ID]'],
 ['Course / term','CSCI426 Advanced Web Programming / Fall 2026'],
 ['GitHub repository','[Add your actual GitHub repository URL]'],
 ['Deployment URL','[Add your actual GitHub Pages / Netlify / Vercel URL]'],
],widths=[169,341]))
story.extend([Spacer(1,12),p('Custom project theme: instructor approval is required under the course brief. This PDF is a submission draft, not proof of live deployment.','small'),PageBreak()])
# 2. Abstract and requirements
story+=head('01 / PROJECT OVERVIEW','Abstract & Objectives')
story.append(p('Bitronix is a ReactJS frontend concept for a technology retail and device-service experience. It combines an organized product catalog, rich item details, a browser-local shopping cart, customer repair-status views and a simple contact workflow in one responsive website. The main aim is to demonstrate front-end usability and interaction while solving the real-world problem of fragmented store browsing and after-sales visibility.'))
story.append(p('The prototype deliberately avoids claims of a production commerce system: orders are demonstrations, sample repair references are fictional, and browser localStorage holds test information only. A real commercial deployment would require server-side validation, authentication, secure storage and payment integrations.'))
story.append(p('Alignment with learning objectives','sub'))
story.append(panel([
 ['Course requirement','Project implementation'],
 ['ReactJS frontend','React class components, JSX source, component state, event handlers'],
 ['Five or more pages','Home, Shop, dynamic Product, Services, dynamic Repair Tracker, About, Contact, Cart'],
 ['Responsive UI/UX','Custom CSS grid, fluid typography, mobile navigation, accessible forms'],
 ['Git version control','Included local repository with multiple documented commits'],
 ['Frontend hosting','Static GitHub Pages-ready assets; external publication required'],
 ['README & screenshots','README.md, run instructions, original screenshot assets'],
],widths=[180,330]))
story.extend([Spacer(1,18),p('Real-world problem','sub'),p('Customers benefit from discovering products, learning about service options, and checking repair progress without switching between disconnected interfaces. This Phase 1 demonstration illustrates those customer journeys through interactive frontend behaviors.'),p('Theme note','sub'),p('A technology store and repair service is a student-proposed theme, not one of the six sample themes in the assignment; the course document states custom themes need prior approval.'),PageBreak()])
# 3. system design
story+=head('02 / SYSTEM DESIGN','Architecture & Navigation')
story.append(p('The site is a client-side React app rendered by a browser. Navigation uses URL hash paths, enabling deployment to a static GitHub Pages directory without server rewrite rules. Components read example product and repair records from the frontend bundle; the cart and newly created demo tickets use localStorage.'))
story.append(p('Client-side architecture','sub'))
story.append(panel([
 ['Layer','Responsibility'],
 ['Presentation','React page components, reusable product cards, forms, timeline, responsive CSS'],
 ['Navigation','Hash routes: #/, #/shop, #/shop/:id, #/services, #/track, #/about, #/contact, #/cart'],
 ['State / interaction','React component state: search, filters, sorting, quantity, status lookup, form validation'],
 ['Data / persistence','Static JavaScript product catalog and sample tickets + browser localStorage'],
 ['Distribution','index.html with local React/ReactDOM, compiled assets/app.js, SVG graphics'],
],widths=[143,367]))
story.append(Spacer(1,18));story.append(p('Primary user journeys','sub'))
story.append(panel([
 ['Shop journey','Repair journey'],
 ['Home → Shop → Search/filter → Product details → Cart → Demo confirmation','Services → Track repair → Enter code → Status timeline → View update'],
 ['Search and quantity state update immediately in React.','Example tickets are preloaded; optional demo requests are saved locally.'],
],widths=[255,255]))
story.extend([Spacer(1,15),p('Data & privacy boundary','sub'),p('No user login, database, backend API, checkout gateway or email service is included in this academic phase. The demo does not transmit data. Local storage should not be used for sensitive customer information in a production website.'),PageBreak()])
# 4. screenshots and features
story+=head('03 / INTERFACE & FEATURES','Visual Design in Action')
story.append(p('The visual system uses a dark evergreen navigation-and-hero palette, lime highlights, clean product grids, gentle cards and original SVG device illustrations. Buttons, state feedback, filter pills and responsive forms provide clear interaction targets.'))
story.append(p('Homepage - hero, discovery and featured products','sub'))
story.append(image_crop('home-desktop.png',(0,0,1440,710),wide=495))
story.append(Spacer(1,16));story.append(p('Product discovery - searchable catalog and interactive filters','sub'))
story.append(image_crop('shop-desktop.png',(0,0,1440,640),wide=495))
story.append(PageBreak())
# 5. technology and snippets
story+=head('04 / TECHNOLOGY & IMPLEMENTATION','Technologies Used')
story.append(panel([
 ['Technology','Use in project'],
 ['ReactJS 16.0 (MIT)','Component rendering, declarative views, state and events; UMD bundles included locally'],
 ['JSX + TypeScript compiler','Human-readable JSX in src/app.jsx transpiled to assets/app.js'],
 ['HTML5 / CSS3','Semantic elements, responsive grid/flex layouts, media queries, validation styles'],
 ['JavaScript ES2018','Search, sorting, route parsing, event handling, conditional rendering'],
 ['localStorage','Persists example cart quantities, local repair tickets and demo messages'],
 ['Git / GitHub Pages','Version history; static deployment with relative URLs and hash navigation'],
],widths=[163,347]))
story.append(Spacer(1,15));story.append(p('Key code snippet 1 - live product filters','sub'))
story.append(dark_snippet("const visible = PRODUCTS.filter(p =>\n  (category === 'All' || p.category === category) &&\n  (p.name + ' ' + p.description).toLowerCase()\n    .includes(query.trim().toLowerCase())\n);"))
story.append(Spacer(1,12));story.append(p('Key code snippet 2 - local cart persistence','sub'))
story.append(dark_snippet("saveCart(cart) {\n  localStorage.setItem('bitronix_demo_cart',\n    JSON.stringify(cart));\n  this.setState({ cart });\n}"))
story.append(Spacer(1,12));story.append(p('The samples show the same techniques used in the JSX source. The actual shop filter also accounts for product category text and supports sorting; the provided snippets are shortened for clarity.','small'))
story.append(PageBreak())
# 6. test & deployment
story+=head('05 / VERIFICATION & SUBMISSION','Testing, Deployment & Limits')
story.append(p('Browser validation was performed with automated Chromium interactions at desktop and phone viewports. Tests checked homepage rendering, catalog search/category filtering, dynamic product details, cart and demo checkout, sample repair lookup, local ticket creation, contact form submission and mobile navigation.'))
story.append(panel([
 ['Test area','Expected outcome','Result'],
 ['Catalog','12 products; search and filters update results','Passed'],
 ['Product / cart','Selected item appears; subtotal recalculates','Passed'],
 ['Repair tracking','Sample code shows correct status timeline','Passed'],
 ['Demo ticket','New local code and received status generated','Passed'],
 ['Contact','Valid form gives local success confirmation','Passed'],
 ['Responsive','Mobile menu usable; no horizontal overflow','Passed'],
],widths=[137,305,68]))
story.extend([Spacer(1,13),p('Deployment steps','sub'),p('1. Publish the included Git repository to your own GitHub account.  2. In repository Settings → Pages, select Deploy from branch, main and root.  3. Open the published URL and verify every route.  4. Insert the actual GitHub link and student details above; submit this PDF with the repository URL in Google Classroom.'),p('Limitations and integrity','sub'),p('This frontend-only phase intentionally excludes backend storage, production inventory, payments, real tickets and live email delivery. Illustrations and demo dataset were created for this project; bundled React/ReactDOM are MIT-licensed and attributed. Review, adapt, and acknowledge AI assistance if required by institutional academic-integrity rules.'),Spacer(1,8),p('Submission checklist','sub'),p('React pages: complete   |   Responsive layout: complete   |   Git history: included   |   README/screenshots: included   |   PDF report: complete   |   Instructor theme approval, actual deployment and student identity: pending.','small')])

doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=43,leftMargin=43,topMargin=65,bottomMargin=59,title='CSCI426 - Bitronix Technology Store & Repair Portal - Project Phase 1',author='CSCI426 project draft',subject='Advanced Web Programming - ReactJS frontend project')
doc.build(story,onFirstPage=frame,onLaterPages=frame)
print(OUT)
