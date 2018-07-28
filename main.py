import requests, json
def main():
    data = {"method":"do","login":{"password":"vWdR2dN43A0VbwK"}}
    sess = requests.Session()
    response = sess.post('http://124.16.85.115', data=json.dumps(data), headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '39',
        'Content-Type': 'application/json; charset=UTF-8',
        'Host': '124.16.85.115',
        'Origin': 'http://124.16.85.115',
        'Referer': 'http://124.16.85.115/',
        # 'content-type':'application/json',
    })
    stok = response.json()['stok']
    # print(response.json())
    ret = '{}<br>'.format(response.json())

    url = 'http://124.16.85.115/stok=%s/ds'%stok
    response = sess.post(url, data=json.dumps({"system":{"reboot":'null'},"method":"do"}))
    # print(response.text)
    return ret + response.text

if __name__ == '__main__':
    main()
