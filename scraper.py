from requests_html import HTMLSession
session = HTMLSession()
url = "https://thenurseswithoutborders.org/COVID-19/index.rinj"
r = session.get(url)

table = r.html.find('#myTable > tbody > tr')
malta = [tr.find("td") for tr in table if "Malta" in tr.text][0]
malta_text = [tr.text for tr in malta]
print("Country: {}\n Cases: {}\n Deaths: {}\n Recoveries: {}"
      .format(*malta_text))
