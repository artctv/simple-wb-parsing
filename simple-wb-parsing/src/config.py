

class URLS:
    # PRICE_URL = "https://card.wb.ru/cards/detail?" \
    #             "spp=0&" \
    #             "regions=80,64,38,4,115,83,33,68,70,69,30,86,40,1,66,48,110,22,31,111&" \
    #             "pricemarginCoeff=1.0&" \
    #             "reg=0&" \
    #             "appType=1&" \
    #             "emp=0&" \
    #             "locale=ru&" \
    #             "lang=ru&" \
    #             "curr=rub&" \
    #             "couponsGeo=2,12,7,3,6,13,21&" \
    #             "dest=-5803327&" \
    #             "nm=71906089"

    PRICE: str = "https://card.wb.ru/cards/detail?" \
                "appType=1&" \
                "locale=ru&" \
                "lang=ru&" \
                "curr=rub&" \
                "nm={vendor_code}"

    CATEGORY: str = "https://www.wildberries.ru/webapi/product/{vendor_code}/data?" \
                        "subject={subject_id}&" \
                        "kind={kind_id}&" \
                        "brand={brand_id}"

    SALE_QUANTITY: str = "https://product-order-qnt.wildberries.ru/by-nm/?nm={vendor_code}"

    PRICE_HISTORY: str = "https://basket-{server_n}.wb.ru/vol{vendor_code_first_three}/part{vendor_code_first_five}/{vendor_code}/info/price-history.json"
