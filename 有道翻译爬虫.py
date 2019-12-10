
import requests
import json
import time
import random
import hashlib




def getTime():
    return str(int(time.time() * 1000))
def md5(v):
	# Message Digest Algorithm 信息摘要算法第五版  为计算机安全领域广泛使用的一种散列函数 用以提供消息的完整性保护
	md5 = hashlib.md5()   # md5对象  md5不能反解  但是加密是固定的  就是关系意义对应  所以有缺陷 容易被对撞出来
	# update需要一个bytes格式参数
	md5.update(v.encode('utf-8'))
	value = md5.hexdigest()  # 得到加密字符串
	return value
def get_sign(key,salt):
	v = "fanyideskweb" + key + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
	sign = md5(v)
	return sign
def main():
	headers = {
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9",
		"Connection": "keep-alive",
		"Content-Length": "255",
		"Content-Type": 'application/x-www-form-urlencoded;charset=UTF-8',
		"Cookie": 'OUTFOX_SEARCH_USER_ID=727203793@10.108.160.18;OUTFOX_SEARCH_USER_ID_NCOO=2107317716.8406208; JSESSIONID=aaa35okFPMbvNc3YaeW7w; ___rl__test__cookies=1575986506553',
		"dnt": "1",
		"Host": "fanyi.youdao.com",
		"Origin": "http://fanyi.youdao.com",
		"Referer": "http://fanyi.youdao.com",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36",
		"X-Requested-With": "XMLHttpRequest"

	}
	url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
	word = "我爱你"
	ts = getTime()
	salt  = str(int(ts)+random.randint(0,9))
	sign = get_sign(word,salt)

	Form_data = {"i":word,
	"from": "AUTO",
	"to": "AUTO",
	"smartresult": "dict",
	"client": "fanyideskweb",
	"salt": salt,
	"sign": sign,
	"ts": ts,
	"bv": "f07c6164a4cf751f3f6b190b0aeb0d22",
	"doctype": "json",
	"version": '2.1',
	"keyfrom": "fanyi.web",
	"action": "FY_BY_CLICKBUTTION"}
	response = requests.post(url,data=Form_data,headers=headers)

	content = json.loads(response.text)
	print(content['translateResult'][0][0]['tgt'])








if __name__ == '__main__':
	main()