# python
phonebook2.py
  第一个小项目，虽然很简单但也填了不少坑。
  在python里类也属于对象，如果要将类实例化，则要在类名后面加（）
  list=[]，中括号里是可以空的
  往list里加元素，应该list.append(P())而不是list.append(P)

# 请求响应流程
当用户访问一个URL时，发生了以下事件：
1. 浏览器生成对应的HTTP请求，通过互联网发送到web服务器
2. web服务器接收到请求，通过WSGI将HTTP格式的数据转换成Flask能识别的python数据
3. Flask根据请求的URL执行对应的视图函数，获取返回值生成响应
4. 响应经过WSGI转换成HTTP响应，发送到web服务器
5. web服务器最终把响应发送给发起请求的客户端
## HTTP请求
URL的组成部分，以http://www.baidu.com/s?kd=flask 为例：
| 信息 | 说明 |
| ----| ---- |
| http: | 协议字符串，指定需要使用的协议 |
| www.baidu.com | 服务器的域名(IP) |
| /s?kd=flask | 要获取资源的路径(path)，类似与UNINX的文件目录结构 |
常见的HTTP方法
| 方法 | 说明 |
|---|---|
|GET|获取资源|
| POST | 传输数据 |
| PUT | 传输文件 |
| DELETE | 删除资源 |
| HEAD | 获取报文的首部 |
| OPTIONS | 查询支持的方法 |
### Request 对象
使用 request 的属性来获取URL：
| 属性       |             值                    |
| ---       | --                                |
| path      | 's'                               |
| full_path | 's?kd=flask'                      |
| host      | 'www.baidu.com'                   |
| host_url  | 'http://www.baidu.com/'           |
| base_url  | 'http://www.baidu.com/s'          |
| url       | 'http://www.baidu.com/s?kd=flask' |
| url_root  | 'http://www.baidu.com/'           |
使用request对象的属性或方法来获取请求报文中的信息：
| 属性/方法 | 说明 |
| ------- | ---- |
| args | Werkzeug的Immutableultiict对象。存储解析后的字符串，可以通过字典的方式获取键和值 |
| query_string | 获取未解析的原生查询字符串 |
| blueprint | 当前蓝本的名称 |
| cookies | 一个包含所有随请求提交的cookies字典 |
| data | 包含字符串形式的请求数据 |
| endpoint | 与当前请求匹配的端点值 |
| files | Werkzeug的Immutableultiict对象，包含所有上传文件，可以以字典的形式获取文件。使用的键为input标签中的name属性值，对应的值为Werkzeug中的FileStorage对象，可以调用save(path)方法来保存文件 |
| form | Werkzeug的Immutableultiict对象，与files类似，包含解析后的表单数据。表单字段通过input标签的name属性值作为键获取 |
| values | Werkzeug的CombinedMultiDict对象，结合了args和form的属性值 |
| get_data(cache=True, as_text=False, parse_form_data=False) | 获取请求中的数据，默认读取为字节字符串，将as_text设置为True后返回的是解码后的unicode字符串 |
| get_json(self, force=False, silent=False, cache=True) | 作为JSON解析返回数据，如果MIME类型不是JSON，返回None(除非force设为True)；解析出错则抛出Werkzeug提供的BadRequest异常（非调试模式下返回400错误响应），如果silent设为True则返回None；cache设置是否缓存解析后的JSON数据 |
| headers | 一个Werkzeug的EnvironHeaders对象，包含首部字段，以字典形式操作 |
| is_json | 通过MIME类型判断是否为JSON数据，返回布尔值 |
| json | 包含解析后的JSON数据，内部调用get_json()，可通过字典的方式获取键值 |
| method | 请求的HTTP方法 |
| referrer | 请求发起的源URL，即referer |
| scheme | 请求的URL模式(http或https) |
| user_agent | 用户代理，包含了客户端的一些信息 |
