import sys
from factory import Factory


if __name__ == "__main__":
    if len(sys.argv)==1:
        sys.exit()

    factory = Factory.getFactory(sys.argv[1])

    asahi = factory.createLink("asahi newspaper", "http://wwww.asahi.com")
    yomiuri = factory.createLink("yomiuri newspaper", "http://wwww.yomiuri.co.jp")
    us_yahoo = factory.createLink("Yahoo!", "http://wwww.yahoo.com")

    jp_yahoo = factory.createLink("Yahoo!Japan", "http://wwww.yahoo.co.jp")
    excite = factory.createLink("Excite", "http://wwww.excite.com")
    google = factory.createLink("Google", "http://wwww.google.com")

    tray_news = factory.createTray("Newspaper")
    tray_news.add(asahi)
    tray_news.add(yomiuri)

    tray_yahoo = factory.createTray("Yahoo!")
    tray_yahoo.add(us_yahoo)
    tray_yahoo.add(jp_yahoo)

    tray_search = factory.createTray("Search engine")
    tray_search.add(tray_yahoo)
    tray_search.add(excite)
    tray_search.add(google)

    page = factory.createPage("LinkPage", "yujikawa")
    page.add(tray_news)
    page.add(tray_search)
    page.output()








