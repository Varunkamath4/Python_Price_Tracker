import requests
from bs4 import BeautifulSoup

products_to_track =[
    {
        "product_url":"https://www.snapdeal.com/product/indus-valley-disposable-face-mask/638539148385",
        "name":"Disposable Face Mask",
        "target_price": 400
    },
    {
        "product_url":"https://www.snapdeal.com/product/campus-costa-pro-black-running/6917529697286127587",
        "name":"Campus COSTA PRO Blue Running Shoes",
        "target_price":6000
    },
    {
        "product_url":"https://www.snapdeal.com/product/campus-first-white-running-shoes/5188147417737615702",
        "name":"Campus white Running Shoes",
        "target_price":5000
    },
    {
        "product_url":"https://www.snapdeal.com/product/rickenbac-alfa05-white-mens-sports/661934824771#bcrumbLabelId:46105686",
        "name":"rick Alfa-05 White Men's Sports",
        "target_price":520
    },
    {
        "product_url":"https://www.snapdeal.com/product/asian-wonder13-gray-running-shoes/5188147411324396169#bcrumbLabelId:46105686",
        "name":"ASIAN Silver Men's Sports Running Shoes",
        "target_price":50000
    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find("span", {"class": "payBlkBig"})
    if (product_price == None):
        product_price = soup.find("span", {"class": "payBlkBig"})

    return product_price.getText()

result_file = open ('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + "-" + every_product.get("name"))


        my_product_price = product_price_returned[:]
        my_product_price = my_product_price.replace(',','')
        my_product_price = int(my_product_price)


        if my_product_price < every_product.get("target_price"):
            print("Availabel at your req price")
            result_file.write(every_product.get("name") + '- \t'+' Availabel at target price '+' current price - '+ str(my_product_price) + '\n')
        else:
            print("still at current price")

finally:
    result_file.close()








