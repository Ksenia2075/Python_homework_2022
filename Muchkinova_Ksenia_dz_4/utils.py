import requests


def currency_rates(code="",
                   url="http://www.cbr.ru/scripts/XML_daily.asp") -> float:
    global code_curr
    code = code.upper()
    response = requests.get(url)
    if response.ok:
        code_curr = response.text.split(code)
        if len(code_curr) == 1:
            return None
    value = code_curr[1].split('</Value>')[0].split('Value>')[1]
    value = float(value.replace(',', '.'))
    print(value)
