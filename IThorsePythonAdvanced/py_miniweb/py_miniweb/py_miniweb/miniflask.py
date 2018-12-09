# 不可变的资源做一个统一的处理,gif,png,jpg,mp3,mp4 不可变的资源我们进行处理的处理
# 直接 二进制 打开返回数据
# html网页的内容会随时发生变化,网页上的图片,gif,jpg这个不会进行变化
# html网页根据不同的地址进行不同的返回,不变的资源进行统一的处理


# 1.创建tcp服务器端
# 2. 循环接收客户端请求
# 3. 处理客户的请求
# 3.1 得到请求的路径
# 3.2 根据不同的路径返回不同的数据
# 4. 关闭
import re
import socket

import mini_web

# 协程版
import gevent

from gevent import monkey

monkey.patch_all()


class WebServer(object):
	def client_exec(self, client):
		# 1. 得到请求的数据
		# 2. 通过正则得到请求的地址
		# 3. 根据不同的地址返回不同的数据
		# 4. 关闭

		# 1. 得到请求的数据n
		data = client.recv(1024)

		if data:
			# 有数据n
			# 解析数据
			# GET /index.html HTTP/1.1
			# GET / HTTP/1.1
			# 请求数据得到
			recv_data = data.decode("utf-8")
			# 匹配的对象
			match = re.match("[^/]+(/[^ ]*)", recv_data)

			if match:
				# 说明匹配了数据
				file_path = match.group(1)
				# 如果你的地址是/那么定位到首页
				if file_path == "/":
					file_path = '/index.html'
			else:
				# 说明没有匹配数据n
				# 关闭客户端返回
				client.close()
				return

		else:
			# 没有数据
			# 关闭客户端返回
			client.close()
			return

		print("请求的路径:", file_path)

		# html单独处理,不可变资源进行统一处理
		if file_path.endswith(".html"):
			# 不同的地址返回不同的响应体


			# 根据不同的根据返回不同的数据,这个数据处理在mini_web进行处理
			response_line, response_head, response_body = mini_web.application(file_path)

			# 让我们的服务 器灵活性更高一点
			response_head += "server:oldyang\r\n"

			# 响应的格式
			response_content = response_line + response_head + "\r\n" + response_body

			# 发送数据
			client.send(response_content.encode("utf-8"))
		else:

			try:
				# 说明不可变的资源
				# 直接以二进制方式返回
				# 响应的格式
				# 响应行
				response_line = "HTTP/1.1 200 OK\r\n"
				# 响应头
				response_head = ""
				# 以二进制的方式打开不可变资源
				with open(".%s" % file_path, 'rb') as f:
					content = f.read()
				response_body = content

				# 响应的格式
				response_content_1 = response_line + response_head + '\r\n'

				response_content = response_content_1.encode("utf-8") + response_body

				# 发送数据
				client.send(response_content)
			except Exception as e:
				# 说明资源的路径不存在
				# 说明地址不存在,那么返回404
				# 响应行
				response_line = "HTTP/1.1 404 NOT FOUND\r\n"
				# 响应头
				response_head = ""
				# 响应体
				response_body = ""
				# 响应的格式
				response_content = response_line + response_head + "\r\n" + response_body

				# 发送数据
				client.send(response_content.encode("utf-8"))

		# 关闭
		client.close()

	# 开启服务
	def run_server(self):
		# 循环接收客户端请求
		while True:
			# 接收客户端
			client, address = self.tcp_server.accept()
			# 处理客户端请求
			# self.client_exec(client)

			gevent.spawn(self.client_exec, client)

		# 关闭
		self.tcp_server.close()

	def __init__(self):
		# 初始化套接字服务器
		# 1.创建套接字
		self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 2.绑定端口与复用端口
		self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.tcp_server.bind(("", 8080))
		# 3.被动模式
		self.tcp_server.listen(128)



