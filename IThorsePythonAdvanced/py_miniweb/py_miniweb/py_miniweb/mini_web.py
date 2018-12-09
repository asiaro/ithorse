# 根据不同的地址返回不同的数据n


# 写一个装饰器

# 创建一个空的字典
url_dict = dict()


def set_url(url):
	def set_fun(func):
		def call_fun(*args, **kwargs):
			return func(*args, **kwargs)

		# print("这个可以直接打印了", func)
		# print(url)
		# print(call_fun)
		# 直接添加到字典中
		# url_dict[url] = func      # func是装饰前的函数
		url_dict[url] = call_fun  # call_fun是装饰 后的函数

		return call_fun

	return set_fun


# 入口函数简洁
# 一个函数 一个功能
def application(file_path):
	# 响应行
	response_line = "HTTP/1.1 200 OK\r\n"
	# 响应头
	response_head = "content-type:text/html;charset=utf-8\r\n"

	try:
		# 根据不同的地址返回不同的响应体
		# 把地址跟响应体放在一个字典中
		# url_dict = {"/index.html": index, "/center.html": center,'/me.html':me}
		# print("字典:", url_dict)
		# 根据键进行取值
		fun = url_dict[file_path]

		# 返回响应体
		response_body = fun()

	except Exception as e:
		print("地址不存在")
		response_line = "HTTP/1.1 404 NOT FOUND\r\n"
		response_body = "亲页面不存在!"

	return response_line, response_head, response_body


##########################################################上面是框架#######################################

# 一个页面一个函数

@set_url("./登陆.html")
def denlu():
	print(mro(application))
	return 

#@set_url("/index.html")
#def index():
#	return "index page is show"
