import miniflask
# 入口函数第一个函数必须简洁
# 像书的目录
# 一个函数一个功能
# 类是相关函数的集合
def main():
	# 初始化tcp
	server = miniflask.WebServer()

	# 开启服务
	server.run_server()


if __name__ == '__main__':
	main()



