import requests
import pandas as pd

cookies = {
    "SCF": "AjkAtUGXsleTsqaMGv0YefkKt_VBA2hPuyyPFQpZ82ZxQbAnGoEzGIakhe4ssFzGbTdSHyX4-_LMceHnYmkYJ9A.",
    "SINAGLOBAL": "6027523846707.496.1742952231239",
    "ULV": "1742952231255:1:1:1:6027523846707.496.1742952231239:",
    "XSRF-TOKEN": "LOtrfZTYMkZztYsURU9zeaTH",
    "PC_TOKEN": "fa9ce08836",
    "SUB": "_2AkMfSVaff8NxqwFRmfATym7gZIhwzgDEieKpFadEJRMxHRl-yj9yqkEEtRB6NMl4cEuoiABMTQU1JH5K6agzjCoFMC4R",
    "SUBP": "0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFR4_WbMJgEuCxKPmS3l520",
    "WBPSESS": "fhlE7lUFBip5iXsQIeNCGGENvIuPuMQyNHpEPIO_-_P6X-zn6U7Jf6SmHTdLGV0g4rKLpQjujPKCmeqqemEjndq35hlIb4QuNiBcThS5xozywiGtynnL5Mt20lcuF92_"
}
url = "https://weibo.com/ajax/feed/hottimeline"
params = {
    "since_id": "0",
    "group_id": "1028039999",
    "containerid": "102803_ctg1_9999_-_ctg1_9999_home",
    "extparam": "discover|new_feed",
    "max_id": "0",
    "count": "10"
}
response = requests.get(url, cookies=cookies, params=params)

json_data = response.json()
# print(json_data)

pd1 = pd.DataFrame(json_data,columns=['ok','statuses'])
print(pd1)
pd1.to_excel('ok.xlsx')