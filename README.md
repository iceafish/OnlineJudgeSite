OnlineJudgeSite
请在这里做版本信息修改说明，注明修改人。
3.8 icefish
	FAQ添加内容，复制POJ FAQ主体暂用。
	继续编写了judge
3.7 icefish
	judge 添加judge_server判题服务器，目前只能接收判题请求，无请求队列。
		判题前需运行judge_server服务器。
	judge 环境参数放在judger/setting.py中。
3.6 icefish
	数据库变更为sqlite3，默认管理员账号为
			admin，密码admin
	数据库文件放在网站根目录data.db
	暂时隐藏contest

3.4 kitty
	稍微改动下myadmin,用以增加对superuser 的增添与修改操作。

2.24.1 icefish
	主要对之前bug进行修复
		1.对于2.19.1中 1 问题解决。可以正常显示提交语言
		2.对status的排列顺序调整
		3.解决在无用户登录的情况下，仍可提交题目的bug

2.23 kitty
	续写myadmin
2.21 kitty 
	myadmin未完成
	
2.19.1 icefish
	实现status显示
	已知问题：
		1.status中语言不能从id正确转换成对应文字
		2.实际上judge 队列并没有实现，而是串行式的，这么设计是错误的
			目标设计应该是将提交的申请保存在requestQue中，然后显示status
			而后台对requestQue的id从上一个处理完的位置开始处理新的非new状态的request

2.19 icefish
	代码提交已经实现，能成功保存，上传文件放在/judger/tmp/中保存
	judger核心代码暂时以注释代替
	代码微调，删除一些因为重构而多余的文件

2.14.1 icefish
	2.14存在问题1已经解决
	添加request队列模型
	对其他代码一些微调

2.14 icefish
	添加代码提交功能
	针对代码提交部分，对原有站位代码进行重构。包括
		url响应原有位置（主urls中）不变
		对于响应代码，新添加app judger用于后天的代码处理。
		响应代码也由原来的主视函数中调整到judger中
	对于readme.md结构调整（顺序颠倒），最新的变动显示在最上面，更直观，易用。
	
	已知问题：
		1.submit处理逻辑存在问题，提交代码后转到status页面仍然显示submit/（id）的域名。
		2.submit还未添加处理队列，处理队列应该设计成一个借口，提供给整个程序中所有需要提交代码的位置使用。
		3.在点进problem里面后台提示警告，好像是与{% csrf_token %}有关
	
2.12.1
	解决问题：
		解决在problem下，的一个题目会出现用户登录信息不能显示问题：
			原因：没有将request传参到题目的模板中，解决办法：使用locals()或者手动传参request

2.12
	已知问题：
		1.当在problems问题列表下，点开任意一道题目，
		用户登录信息显示错误。已登录用户却显示登录框。
	已知逻辑错误，myadmin无法添加myadmin，造成永远没有办法登陆myadmin。
		临时解决办法，在admin中添加myadmin管理员账号的管理。
		（解决办法应该是当myadmin表为空时，提示用户注册界面。暂定）
		登录后不能登出。
	取消readme文件，繁琐，直接用github说明文件README.md，也就是此文件做更新记录。

2.10.4
	修正 session 在html 中调用的问题。
	myadmin模块 未测试
	到目前为止 无已知问题.zny

2.10.3
	myAdmin -->to myadmin

2.10.2
	解决user bug
	修改problem_list 函数 的传参字典 改为 locals()

2.10.1
	解决 user登陆后不能正确显示用户信息，无法登出
	
2.10 修改user在admin下无法显示的问题
     修改user的csrf错误
     problem admin下添加默认排序，添加过滤器，信息添加完整
     problem 添加submit模板
     已知问题，user登陆后不能正确显示用户信息，无法登出

0.01 修改setting 加入users 模块 zny







	



