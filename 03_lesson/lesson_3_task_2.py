from smartphone import Smartphone

catalog = [
    Smartphone ("XiaoMi", "RedMi3", "+79578445145"),
    Smartphone ("iPhone", "11", "+76542584567"),
    Smartphone ("Sumsung", "A54", "+75412368265"),
    Smartphone ("Honor", "400", "+75145864572"),
    Smartphone ("GooglePixel", "8", "+79965465823")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")