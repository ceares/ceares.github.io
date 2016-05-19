---
title: Python 异常处理简介
tags: [Python,异常,raise,assert,with]
---

* TOC
{:toc}

Python 是面向对象的语言，所以程序抛出的异常也是类。

# 一、常见的异常类

- NameError：尝试访问一个没有申明的变量 
- ZeroDivisionError：除数为 0 
- SyntaxError：语法错误 
- IndexError：索引超出序列范围 
- KeyError：请求一个不存在的字典关键字 
- IOError：输入输出错误（比如你要读的文件不存在） 
- AttributeError：尝试访问未知的对象属性 
- TypeError：传给函数的参数类型不正确，比如给 int 函数传入字符型 


# 二、自定义异常类

尽管内建的异常类已经包括大部分情况，但如果需要创建自己的异常类，可以采用下面的方法：

```py
class CustomException(Exception): # Exception 为所有异常的基类
    # 处理异常的代码
````

# 三、捕获异常

```py
try:  
   # 需要进行捕获异常的代码，只有出现异常之前的代码被最终执行
except (Exception1,Exception2,...) as argument:  
   # 捕获到 (Exception1,Exception2,...) 里的异常才执行本段代码
   # argument 是一个异常类的实例，包含异常的具体信息
except:
   # 捕获到 (Exception1,Exception2,...) 以外的异常执行本段代码，用 sys 模块的 exc_info() 函数可以获取异常信息
else:  
   # 如果没有捕获到异常则执行本段代码
finally:  
   # 无论是否捕获到异常都执行本段代码
```
上述语句并不都是必须的，譬如 try...except...、try...finally... 或者 try...except...else... 语句都是可行的。我们还可以 [用 try...except...else... 代替 if...else...](http://www.cnblogs.com/Pandaman/p/C21.html#tips)。

# 四、抛出异常

如果我们想要在自己编写的程序中主动抛出异常，可以采用如下两种方法：

- `raise Exception(reason)`：Exception 必须是一个异常类的名称。可选项 reason 用来传递异常的信息；
- `assert expression[,reason]`：assert 是断言的关键字。当表达式 expression 为真则什么都不做，否则抛出 AssertionError 异常。reason 提供异常的信息。

# 五、上下文管理器

由于对象 File 支持上下文管理协议，因此可以采用下面的方法打开文件：
 
```py
with open('filename') as fp: 
   # 无论本段代码是否出现异常，文件对象 fp 均能正确关闭
```

# 六、Example

```py
import sys

def div(num, den): 
	print('_________________   (',num,',',den,')\n')
	try:
		ans = num/den
		assert den != num, 'Equal' # 断言：分子分母不相等
		den = 'Changed'            # 如果执行本语句之前未出现异常，改变 den 的值
		if num % 2:                # 如果分子为奇数，则抛出异常
			raise ValueError('Odd')
	except ZeroDivisionError as e:
		print('except ... as ...\n\t', e)
	except:
		print('except\n\t', sys.exc_info())
	else:
		print('else\n\t', ans)
	finally:
		print('finally\n\t', den)

div(1,0)	# 除数为零，为 ZeroDivisionError 异常类
div(1,1)	# 分子等于分母，断言为假，抛出异常
div(2,1)	# 无异常
div(3,1)	# 分子为奇数，通过 raise 抛出异常
div(3,'x')	# 不属于 ZeroDivisionError 的其他异常
```
---

```
_________________   ( 1 , 0 )

except ... as ...
	 division by zero
finally
	 0
_________________   ( 1 , 1 )

except
	 (<class 'AssertionError'>, AssertionError('Equal',), <traceback object at 0x00000000029B42C8>)
finally
	 1
_________________   ( 2 , 1 )

else
	 2.0
finally
	 Changed
_________________   ( 3 , 1 )

except
	 (<class 'ValueError'>, ValueError('Odd',), <traceback object at 0x00000000029B42C8>)
finally
	 Changed
_________________   ( 3 , x )

except
	 (<class 'TypeError'>, TypeError("unsupported operand type(s) for /: 'int' and 'str'",), <traceback object at 0x00000000029B42C8>)
finally
	 x
```
