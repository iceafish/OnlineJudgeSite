OnlineJudgeSite
===============
请在这里做版本信息修改说明，注明修改人。
0.01 修改setting 加入users 模块 zny

2.10 修改user在admin下无法显示的问题
     修改user的csrf错误
     problem admin下添加默认排序，添加过滤器，信息添加完整
     problem 添加submit模板
     已知问题，user登陆后不能正确显示用户信息，无法登出
2.10.1
	解决 user登陆后不能正确显示用户信息，无法登出
2.10.2
	解决user bug
	修改problem_list 函数 的传参字典 改为 locals()
2.10.3
	myAdmin -->to myadmin
2.10.4
	修正 session 在html 中调用的问题。
	myadmin模块 未测试
	到目前为止 无已知问题.zny
	
2.12
	已知问题：
		1.当在problems问题列表下，点开任意一道题目，
		用户登录信息显示错误。已登录用户却显示登录框。
	已知逻辑错误，myadmin无法添加myadmin，造成永远没有办法登陆myadmin。
		临时解决办法，在admin中添加myadmin管理员账号的管理。
		（解决办法应该是当myadmin表为空时，提示用户注册界面。暂定）
		登录后不能登出。
	取消readme文件，繁琐，直接用github说明文件README.md，也就是此文件做更新记录。
2.12.1
	解决问题：
		解决在problem下，的一个题目会出现用户登录信息不能显示问题：
			原因：没有将request传参到题目的模板中，解决办法：使用locals()或者手动传参request

