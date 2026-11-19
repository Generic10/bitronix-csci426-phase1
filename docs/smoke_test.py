"""Browser smoke tests. Uses in-memory assets because this sandbox restricts local navigation."""
from pathlib import Path
from playwright.sync_api import sync_playwright
import base64
ROOT=Path(__file__).resolve().parents[1]
ASSET=ROOT/'assets'

def load_app(page):
    urls={p.name:'data:image/svg+xml;base64,'+base64.b64encode(p.read_bytes()).decode() for p in (ASSET/'products').glob('*.svg')}
    urls['hero-tech.svg']='data:image/svg+xml;base64,'+base64.b64encode((ASSET/'hero-tech.svg').read_bytes()).decode()
    page.set_content('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head><body><div id="root"></div></body></html>')
    page.add_style_tag(content=(ASSET/'styles.css').read_text())
    page.add_script_tag(content=(ASSET/'vendor/react.production.min.js').read_text())
    page.add_script_tag(content=(ASSET/'vendor/react-dom.production.min.js').read_text())
    page.evaluate('''() => {const storage={};Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:(k)=>storage[k]===undefined?null:storage[k],setItem:(k,v)=>{storage[k]=String(v)},removeItem:(k)=>{delete storage[k]}}});}''')
    page.evaluate('(urls)=>{window.ASSET_URLS=urls;}',urls)
    js=(ASSET/'app.js').read_text()
    js=js.replace("return 'assets/products/' + p.image;","return window.ASSET_URLS[p.image];")
    for name in ['hero-tech.svg','orbit-laptop.svg','nova-phone.svg','pulse-headphones.svg']:
        js=js.replace('assets/'+('hero-tech.svg' if name=='hero-tech.svg' else 'products/'+name),urls[name])
    page.add_script_tag(content=js)
    page.wait_for_selector('h1',timeout=5000)
    page.evaluate("document.querySelectorAll('img').forEach(img => img.loading = 'eager')")

def visit(page,route):
    page.evaluate('(route)=>{window.location.hash="#"+route;}',route)
    page.wait_for_timeout(120)
    page.evaluate("document.querySelectorAll('img').forEach(img => img.loading = 'eager')")

def run():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'])
        desk=browser.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
        issues=[]
        desk.on('pageerror',lambda e:issues.append(str(e)))
        load_app(desk)
        assert 'Make room' in desk.locator('h1').inner_text()
        assert desk.locator('.product-card').count()==4
        desk.screenshot(path=str(ROOT/'screenshots/home-desktop.png'),full_page=True)
        print('PASS homepage; four featured products')
        visit(desk,'/shop')
        assert desk.locator('.product-card').count()==12
        desk.screenshot(path=str(ROOT/'screenshots/shop-desktop.png'),full_page=True)
        desk.get_by_role('searchbox').fill('OrbitBook')
        assert desk.locator('.product-card').count()==1
        desk.get_by_role('searchbox').fill('')
        desk.get_by_role('button',name='Audio',exact=True).click()
        assert desk.locator('.product-card').count()==3
        print('PASS shop search and category filtering')
        visit(desk,'/shop/nova-phone')
        assert 'Nova X Pro' in desk.locator('h1').inner_text()
        desk.get_by_role('button',name='Add to cart').click()
        visit(desk,'/cart')
        assert desk.locator('.cart-item').count()==1
        assert '$749' in desk.locator('.cart-summary').inner_text()
        desk.screenshot(path=str(ROOT/'screenshots/cart-desktop.png'),full_page=True)
        desk.get_by_role('button',name='Place demo order').click()
        assert 'Demo order created' in desk.locator('.order-success').inner_text()
        print('PASS dynamic product page, cart, demo checkout')
        visit(desk,'/track')
        desk.get_by_role('button',name='BTX-2048').click()
        assert 'Repair in progress' in desk.locator('.status-panel').inner_text()
        desk.screenshot(path=str(ROOT/'screenshots/repair-tracking.png'),full_page=True)
        desk.get_by_role('button',name='Create a demo ticket').click()
        desk.locator('.create-form input').nth(0).fill('Test User')
        desk.locator('.create-form input').nth(1).fill('Test laptop')
        desk.locator('.create-form textarea').fill('A demonstration issue')
        desk.get_by_role('button',name='Create demo ticket').click()
        assert 'Test laptop' in desk.locator('.status-panel').inner_text()
        assert desk.locator('.status-panel').inner_text().count('Request received')>=1
        print('PASS repair lookup and local ticket creation')
        visit(desk,'/services')
        assert desk.locator('.service-card').count()==4
        visit(desk,'/about')
        assert 'For the love' in desk.locator('h1').inner_text()
        visit(desk,'/contact')
        desk.locator('input[placeholder="Your name"]').fill('Demo Student')
        desk.locator('input[type="email"]').fill('student@example.com')
        desk.locator('textarea[placeholder="Tell us a little more..."]').fill('Testing the demo message form')
        desk.get_by_role('button',name='Save demo message').click()
        assert 'demo message is saved' in desk.locator('.contact-success').inner_text().lower()
        desk.screenshot(path=str(ROOT/'screenshots/contact-desktop.png'),full_page=True)
        print('PASS services, about, contact form')
        mobile=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1,is_mobile=True,has_touch=True)
        mobile_issues=[]
        mobile.on('pageerror',lambda e:mobile_issues.append(str(e)))
        load_app(mobile)
        mobile.screenshot(path=str(ROOT/'screenshots/home-mobile.png'),full_page=True)
        mobile.get_by_role('button',name='Open navigation').click()
        assert mobile.locator('.main-nav').is_visible()
        mobile.locator('.main-nav').get_by_role('link',name='Shop',exact=True).click()
        assert mobile.locator('.product-card').count()==12
        mobile.screenshot(path=str(ROOT/'screenshots/shop-mobile.png'),full_page=True)
        # no horizontal scrolling and no missing images
        width=mobile.evaluate('document.documentElement.scrollWidth')
        assert width<=390,f'Unexpected mobile horizontal overflow: {width}'
        mobile.wait_for_timeout(600)
        assert mobile.locator('img').first.evaluate('(img)=>img.complete && img.naturalWidth>0')
        print('PASS mobile navigation, layout width, loaded illustrations')
        if issues+mobile_issues:
            print('BROWSER ERRORS:',issues+mobile_issues)
            raise AssertionError('Browser errors found')
        print('ALL SMOKE TESTS PASSED')
        browser.close()

if __name__=='__main__':run()
