OnlineJudgeSite
请在这里做版本信息修改说明，注明修改人。
5.23    kitty:
	上传新版。
5.15.3 kitty:
	通过加Lock,实现不同人在同一时刻提交代码不会出现结果不正确的bug。
5.15.2 kitty:
	user 已经ok.
5.15.1 kitty:
	修正bug。

5.15 kitty:
	修正管理员进入myinfo出现错误的bug.
4.4.3 kitty:
	修正AC等计数bug
4.4.2 kitty:
	修正bug。
4.4.1 kitty:
	基本写好 Contest模块
	下一步：
		完善Contest 功能.
4.4 kitty:
	基本写好User模块，与系统整合较完美。
	加入修改密码功能。
	下一步：
		加入找回密码功能
		继续写Contest模块。
4.3 kitty :
	修改admin，将myadmin删除


4.3 icefish 阶段报告:
		现阶段主要围绕judge处理需求来设计
		admin仍用自带的admin操作，后期手动修改前台
		由于安全和权限管理问题，user需重新设计，方便admin管理
		判题进度在系统层面(内存,时间,安全监测)
	已知重要bug:
		判题结果还不能正确存储
		判题偶尔出现判题路径错误(原因不明,无规律,不知TCP是否仍存在)

4.3 icefish
	调整各个编译器编译参数
	client-server连接改为TCP协议
	调整judger.view结构
	现进度:
		judger服务处理顺序有待调整
		problem，user数据待更新(等待user重写)
		判题结束后代码文件归档(等待user重写)

3.31 icefish
	重写judge_server支持win/Linux下判题
	正常支持编译器选项
	判题结束后正常清理文件
	结构更科学
	暂存问题：
		判题数据导入方式存在问题，待修改
		代码文件在判题结束之后没有归属正确位置和命名
		判题结果不全面
		
3.24 大整合
3.20 kitty 增加contest模块，模板部分未完成。

3.15 icefish
	更改题目数据添加方法。
	更改题目数据所在位置
	添加多系统判断
	部分代码调整和优化

3.14 kitty
	能够实现开着服务器，则进行判题。
	已知bug，若同时交题，则会出现错误的情况。
3.13 kitty
	继续判题部分。有点bug，可以实现自动变换题号信息。
	加入队列部分。
3.12 kitty
	写判题部分。
	目前已知问题以及局限性：
		1、须在linux下运行。
		2、只能判断无输入的程序。
		3、返回结果只有 CE、WA、AC
		4、如今判什么题，都判./judger/tmp/1.cpp文件，以后会解决.

3.11 稍微改动界面。。
3.9 icefish
	对代码结构进行必要性的调整：
		防止代码冗余，对代码结果进行调整，删除requestQue模型。
			调整到judger.models中
		judger_server调整到工程根目录（暂定）。
	修改部分已知bug
	添加judge同步队列，但是目前还不能同步。

3.8.1 icefish
	修复判题返回结果保存中一个bug
	调整部分代码结构
	已知bug：(正在修复)
		提交代码后未对题目信息记录，判题结束后，对应题目结果也没有记录
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







	




