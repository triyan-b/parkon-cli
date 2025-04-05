from config import conf
from playwright.sync_api import sync_playwright
import time

def register(args):
    url = conf.url
    plates = conf.plates
    cantons = conf.cantons
    durations = conf.durations
    
    try:
        plate = plates[visitor := next(filter(lambda p: p.startswith(args.name.lower()), plates.keys()))]
    except:
        print(f"{args.name} is not a recognised visitor")
        print(f"Recognised visitors: {list(plates.keys())}")
        raise RuntimeError
    canton = c if (c := plate[:2]) in cantons else None
    duration = args.duration

    print(f"Registering {visitor} with plate {plate} for {duration} hours")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=args.headless)
        page = browser.new_page()
        page.goto(url)
        print(f"Navigated to {url}")
        time.sleep(1)
        
        # Focus form
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        
        # Select canton
        if canton:
            filtered_cantons = list(filter(lambda c: c.startswith(canton[0]), cantons))
            times_to_press_key = filtered_cantons.index(canton) + 1
            for i in range(times_to_press_key):
                page.keyboard.press(canton[0])
                time.sleep(0.2)
        else:
            page.keyboard.press("End")
        page.keyboard.press("Enter")

        # Enter number
        page.keyboard.press("Tab")
        page.keyboard.type(plate[2:] if canton else plate)

        # Enter duration
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")
        times_to_press_down_arrow = durations.index(duration) + 1
        for i in range(times_to_press_down_arrow):
            page.keyboard.press("ArrowDown")
            time.sleep(0.2)
        page.keyboard.press("Enter")

        # Enter email
        page.keyboard.press("Tab")
        if not args.noemail:
            page.keyboard.type(args.email)

        # Agree to T&C
        page.keyboard.press("Tab")
        page.keyboard.press("Enter")

        # Submit form
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        page.keyboard.press("Tab")
        if args.autosubmit or args.headless:
            page.keyboard.press("Enter")
            time.sleep(1)
        else:
            while True:
                try:
                    _ = page.title()
                    time.sleep(1)
                except Exception:
                    print("Browser closed")
                    break
        print("Done")
        