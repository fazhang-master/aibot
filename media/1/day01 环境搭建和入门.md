# day01 环境搭建和入门

今日概要：

- 文档和工具
- 环境搭建
- 基础入门



## 1.文档和工具

- markdown笔记 -> 语法 -> 格式笔记   md

  ```
  # 第一章 Python基础
  
  ## 1.1 环境搭建
  ```

  ```
  把大象转冰箱，步骤：
  - 打开
  - 放进去
  - 关闭
  ```

  ```
  ​```
  代码
  ​```
  ```

- 工具 typora

  ```
  下载安装，不要升级。
  ```

  

注意：

- 新建文件后，一定要先保存，不要直接写笔记。
- 配置图片保存路径【当前目录】+ 【相对路径优先】   -> 只配置一次

![image-20220711101255010](assets/image-20220711101255010.png)



## 2.环境搭建



### 2.1 Python解释器



https://www.python.org/downloads/release/python-377/





```python
# D:\code\v1.py
print(123)
print(666)
```

Python解释器作用：将代码文件解释器计算机能听懂语言。

Python解释器版本：

- 2.x

- 3.x 主流

  ```
  3.9.0版本，win10
  3.7.x版本，win7
  ```

  注意：安装位置。

#### 2.1.1 安装

![image-20220711105310831](assets/image-20220711105310831.png)



![image-20220711105440379](assets/image-20220711105440379.png)

![image-20220711105546187](assets/image-20220711105546187.png)

![image-20220711105602533](assets/image-20220711105602533.png)



#### 2.1.2 关于安装目录

```
C:\Python38
	- python.exe        解释器
	- Scripts
		- pip.exe
		- pip3.exe
		- pip3.8.exe    安装Python第三方模块    pip install requests   pip install django
	- Lib
		- random.py
		- re.py        内置功能
		- site-packages
			- requests
			- django
```



- 测试解释器  `c:\code.txt`

  ```
  print("hello world")
  ```

  ```
  C:\Python38\python.exe  c:\code.txt
  ```

  ![image-20220711110744889](assets/image-20220711110744889.png)

  注意：python代码文件一般都是以py为后缀。
  ![image-20220711111005835](assets/image-20220711111005835.png)

- 测试pip工具

  ```
  C:\Python38\Scripts\pip3.8.exe config set global.index-url https://pypi.douban.com/simple/
  ```

  ```
  C:\Python38\Scripts\pip3.8.exe install requests
  ```

  ![image-20220711111507869](assets/image-20220711111507869.png)

  注意：你运行的特别慢。

  

  ![image-20220711111750569](assets/image-20220711111750569.png)



#### 2.1.3 环境变量

```
C:\Python38\python.exe  c:\code.txt
```

```
C:\Python38\Scripts\pip3.8.exe install requests
```



系统环境变量中如果添加了。

```
C:\Python38\
C:\Python38\Scripts\
```

![image-20220711113404513](assets/image-20220711113404513.png)

```
python  c:\code.txt
pip3.8 install requests
```

注意事项：曾经安装过python同学。

![image-20220711113909016](assets/image-20220711113909016.png)

```
pip install flask
```







### 2.2 Pycharm

IDE，集成开发环境，编写Python代码 + 调用解释器运行代码。

- 社区版，免费（现阶段）
- 专业版，收费（后续）

```
https://www.jetbrains.com/pycharm/download/
```

![image-20220711115242756](assets/image-20220711115242756.png)

注意：安装过程，一路next即可。





![image-20220711115525647](assets/image-20220711115525647.png)

![image-20220711115602853](assets/image-20220711115602853.png)

![image-20220711115702278](assets/image-20220711115702278.png)

![image-20220711115927931](assets/image-20220711115927931.png)

![image-20220711115944144](assets/image-20220711115944144.png)



注意：代码的目录一定是任意的其他目录，不要放在解释器目录中。 `C:\Python38\`

![image-20220711120146118](assets/image-20220711120146118.png)

![image-20220711120205883](assets/image-20220711120205883.png)

![image-20220711120249757](assets/image-20220711120249757.png)



![image-20220711120314150](assets/image-20220711120314150.png)

![image-20220711120417778](assets/image-20220711120417778.png)

```
print("hello world")
```



## 3.语法

### 3.1 编码

“中国”文本本质上存储计算机 0101010101.

```
中国             010100101001010100010100101010111
```



对应关系（类似于密码本）

```
中    0101001010010101
国    1010010101011101
```

```
中    1111111110010101
国    0000000001011101
```

文件是以什么编码存储，以后就要用什么编码去打开。



编写Python代码：

- code.py

  ```python
  print("hello world")
  ```

- 运行code

  ```
  python c:\xxx\xxx\code.py
  
  # python解释器内部打开文件时候默认使用的就是  utf-8编码
  python3.9 /Users/wupeiqi/PycharmProjects/jx/day01/demo.py
  ```

![image-20220711141040565](assets/image-20220711141040565.png)







### 3.2 输出

显示程序运行的结果。

```python
print("欢迎大家使用联通xx系统")
print("1.用户登录  2.管理员平台  3.供应商")
```



```python
print("欢迎大家使用联通xx系统", end="")
print("1.用户登录  2.管理员平台  3.供应商")
```



### 3.3 数据类型

- 字母、数字、汉字、成语，基于基础知识编写作文   -> 老师批改。
- 文本、数字、真假、如果，基于基础知识编写代码  -> 解释器+计算机运行。



#### 3.3.1 整型（int）

表示生活中的数字，例如：19、170、189。

```python
19
170
189
```

```python
19 + 1
9000 * 0.5
170 - 100
```

```python
print(19)
print(170-100)
```



#### 3.3.2 字符串（str）

表示生活中的文本信息，例如："武沛齐"     "中国北京昌平区xxx露"

```python
# 单行文本
"武沛齐"
"中国北京昌平区xxx露"
'武沛齐'

# 多行文本
"""武
沛
齐
"""
'''武沛齐'''
```



字符串的拼接

```
"聊经侦" + "yyds"           -> "聊经侦yyds"
```



小练习

```python
print( 12+10 )            # 22
print( "wupeiqi" +"666" ) # "wupeiqi666"
print( "12" + "10" )      # "1210"
```



整型和字符串的转换

- 整型转换成字符串类型

  ```
  str(123)     -> "123"
  ```

- 字符串转换整型

  ```python
  int("999")   -> 999
  ```



小练习

```python
print( int("123") + int("22") )    # 145
print( str(100) + str(200) )       # 100200
```



#### 3.3.3 布尔类型（bool）

真True、假False

```python
1 > 2            -> False
1 == 2           -> False
"生长" == "长生"  -> False
```

```python
if 1 > 2:
    print("...")
else:
    print("...")
```



类型转换：

- 整型 -> 布尔类型

  ```python
  bool(1)  # True
  bool(2)  # True
  bool(-1) # True
  bool(0)  # False
  ```

- 字符串 -> 布尔值

  ```python
  bool("wupeiqi") # True
  bool("-10")     # True
  bool("   ")     # True
  bool("")        # False
  ```

```python
if 0:
    pass
else:
    pass
```



#### 练习题

```python
print( int("8") > 7 )
print( str(111) == 111 )
print( bool(-1) )
print( bool(0) )
print( bool("") )
print( bool("你好") )
print( True == True )
print( True == False )
print( bool("") == bool(0) )
```



### 3.4 变量

变量，给你的值起别名或外号。

```
变量名 = 值
```

```
addr = "中国上海宝山"

print(addr)
print(addr)
print(addr)
```

```python
age = 20
name = "邱晨"

my_age = age + 10
info = "中国上海" + name

print(my_age) # 30
print(info)   # "中国上海邱晨"
```

```python
data = 1 == 2   # data = False
print(data)
```



**变量名的规范**：

- 变量名中只能出现：字母、数字、下划线（任意n中）
- 数字不能开头。

- 不能是Python内置的关键字。

  ```
  [‘and’, ‘as’, ‘assert’, ‘break’, ‘class’, ‘continue’, ‘def’, ‘del’, ‘elif’, ‘else’, ‘except’, ‘exec’, ‘finally’, ‘for’, ‘from’, ‘global’, ‘if’, ‘import’, ‘in’, ‘is’, ‘lambda’, ‘not’, ‘or’, ‘pass’, ‘print’, ‘raise’, ‘return’, ‘try’, ‘while’, ‘with’, ‘yield’]
  ```



建议：

- 多个单词标识时，多个用下划线。

  ```python
  data_set = [111,222,22]
  user_age = 19
  ```

- 见名知意

  ```python
  v1 = 123
  v2 = 456
  ```

  ```python
  age = 19
  password = "sdfsdf"
  ```

  



#### 练习题

```python
1 name = "吉诺比利"
2 name0 = "帕克"
3 name_1 = "邓肯"
4 _coach = "波波维奇"
5 _ = "卡哇伊"
6 1_year = "1990"
7 year_1_ = "1990"
8 _1_year = "1990"
9 nba-team = "马刺" 
10 new*name = "伦纳德"
```



### 3.5 输入

```python
print(123)
print("hello")
print(100+1000)
```

```python
text = input("提示信息")
```

![image-20220711152618987](assets/image-20220711152618987.png)



```python
name = input("请输入姓名：")
age = input("请输入年龄：")
email = input("请输入邮箱：")

text = name + age + email
print(text)
```

```python
name = input("请输入姓名：")
age = input("请输入年龄：")
email = input("请输入邮箱：")

text = "我是" + name + "今年" + age + "岁，邮箱是" + email
print(text)
```

注意：input用户输入的内容永远是字符串。

```
v1 = input('请输入：')  # v1 = "123"
print(v1)
```



```python
v1 = input("请输入：")  # 10
v2 = input("请输入：")  # 20
result = v1 + v2
print(result) # "1020"
```

```python
v1 = input("请输入：")  # "10"
v2 = input("请输入：")  # "20"
result = int(v1) + int(v2)
print(result) # 30
```





```python
num = input("请输入幸运数字：")

if num == "123":
    print("恭喜中奖1000w")
else:
    print("未中奖")
```

```python
username = input("请输入用户名：")
password = input("请输入密码：")

if username == "root" and password == "xxx":
    print("登录成功")
else:
    print("登录失败")
```





