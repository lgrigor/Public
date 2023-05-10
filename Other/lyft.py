import requests


class Lyft:
    URL = "https://api.lyft.com/v1/phoneauth"

    def __init__(self, __phone_number):
        try:
            response = requests.post(url=self.URL,
                                     headers=self.generate_headers(),
                                     json=self.generate_body(__phone_number))

            print(response.content, response.status_code)

        except requests.exceptions.RequestException as e:
            print(f"Request exception occurred: {e}")

    @staticmethod
    def generate_headers():
        return {
            "Content-Type": "application/json",
            "Authority": "api.lyft.com",
            "Path": "/v1/phoneauth",
            "Scheme": "https",
            "Cookie": Lyft.generate_cookie(),
            "Lyft-Version": "2017-09-18",
            "Origin": "https://account.lyft.com",
            "Referer": "https://account.lyft.com/",
            "Sec-Ch-Ua": '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "X-Locale-Language": "en-US"
        }
    
    @staticmethod
    def generate_cookie():
        return 'sessId=cc185167-cab4-40d0-8875-53e70ace36f6L1683654952; ' \
               '_gcl_au=1.1.2102413292.1683654954; ' \
               'lyftAccessToken=Pn2v7dW1iqOjy2ewI9tGHmrjUYF94N2lBtYN+gnVwM2TGXgFDSJGM67M/j3Sq+ibj0XBWOJnUwMdle8XoM6pfk65Y5sdXs5LcNhBdETLGqI4JZettQ450sM=; ' \
               'stickyLyftBrowserId=95d_bCVG_FyPsh-ONdOT7P5w; ' \
               'OptanonConsent=isGpcEnabled=0&datestamp=Tue+May+09+2023+21%3A55%3A57+GMT%2B0400+(Armenia+Standard+Time)&' \
               'version=202211.2.0&' \
               'isIABGlobal=false&' \
               'hosts=&' \
               'consentId=6954a448-1aa1-4c1f-8c6d-97b6f0006a76&' \
               'interactionCount=0&' \
               'landingPath=https%3A%2F%2Faccount.lyft.com%2Fauth&' \
               'groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1; ' \
               '_gid=GA1.2.1295721917.1683654958; ' \
               '_ga=GA1.1.function(b){try{a&&b.set("dimension"+String(a),b.get("clientId"))}catch(c){console.log(c)}}; ' \
               '_scid=ed924789-bdac-4d0f-9e96-bd905510b66e; ' \
               '_scid_r=ed924789-bdac-4d0f-9e96-bd905510b66e; ' \
               '_fbp=fb.1.1683654958409.158645692; ' \
               '_tt_enable_cookie=1; ' \
               '_ttp=pELlfdq7MO8COdQF6f4D9dErMmb; ' \
               '_sctr=1%7C1683576000000; ' \
               '_uetsid=c1c898c0ee9211edb41dbfb9ac8d4baf; ' \
               '_uetvid=c1c90c00ee9211edb62031f8ed6b4828; ' \
               '_ga_EBV76KZYKH=GS1.1.1683654956.1.1.1683655156.0.0.0; ' \
               '_ga_LQ1KHS36LD=GS1.1.1683654957.1.1.1683655156.35.0.0'
    
    @staticmethod
    def generate_body(__phone_number):
        return {
            "phone_number": __phone_number,
            "extend_token_lifetime": True,
            "message_format": "sms_basic"
        }


if __name__ == "__main__":
  
    # https://receive-smss.com/sms/447538304679/
    Lyft("+447538304679")
