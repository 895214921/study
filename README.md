## README.md
-项目的说明文件
-怎么使用的
-怎么安装，怎么部署
-每个包，每个模块都是干什么的，有什么功能，有什么函数，每个函数都是干什么的

## 快速开始
'''bash
python run.py
'''

## 安装步骤
-1.安装python
-2.安装pip包
-3.浏览器和驱动

## 结构说明（面试题）
1.框架是怎么搭建的？
2.自动化脚本怎么设计的？
3.怎么做web自动化？
-自动化代码用例

## APIS 应用程序可编程接口（函数的说明）


##进行测试的流程 （面试题）
-需求分析 （看需求） 
-测试计划 （时间节点，哪些做自动化哪些不做，如果使用自动化，需要用到什么技术框架，selenium，unittest，pytest，python/java）
-编写用例 （）
-评审
-测试执行 （写代码）
-输出报告

##什么样的功能和项目适合做自动化测试 （面试题）
-需求稳定，不会频繁变更的需求
-项目周期比较长的
-复用性高的，可以跨系统，跨平台使用的
-流程规范的功能（文档）

##自动化测试用例的流程
1.进行用例的手工测试 （为什么可以手工测试还要写自动化代码呢，可以回归测试）
   （就把要定位的元素的表达式先准备好）
2.形成测试步骤
3.转化成代码版的步骤（封装po操作）
4.可以写自动化测试代码测试用例了

##web自动化会不会有数据库校验  
-如果有接口测试，在web中还要不要做数据库校验？
接口测试测的是什么 ，后端提供的接口返回的数据是不是有问题 包含整个后端逻辑，而web是测的前端页面是否显示正常、或者交互有没有问题，所以web不需要数据库校验
-如果没有接口测试，web就有可能需要做数据库校验

##浏览器的基础操作
-close
-refresh 刷新
-back 后退
-forward 前进
-最大化 
-最小化
-设置窗口大小

## pytest vs unittest
-pytest 功能很强,比unittest强。
-unittest 标准库，python内置库。

##面试题：为什么用pytest，pytest的特性
pytest优点：
-可以自动收集用例
-用python标准关键字assert去断言
-pytest 支持上千种插件，有自己的插件系统
-pytest 有用例筛选功能，有失败重运行功能
-pytest 有非常灵活的测试夹具(fixture)，相当于setup,tearDown    
-pytest和unittest是兼容的
pytest缺点：
-要安装pip install pytest  有可能和python版本不兼容


## web自动化测试
缺点：
-稳定性，
    -图形界面（浏览器）， 要去渲染图形，比较耗计算能力，cpu占满后就容易崩溃
    -页面加载时快时慢。每次跑代码会有时通过有时不通过，是没有等待够时间，查找元素的问题
    -后端服务。（接口）没有获取到后端数据就会出现一些异常状况。 加载一些静态页面（css，js文件），可能从第三方库直接调过来，如果库是谷歌的就会访问不了，造成稳定性不行

## web自动化
- 一般不会像接口那样过于要求测试覆盖率
- 主流程，冒烟（跑一下全部流程），回归测试
- 对用例进行筛选
- 用例失败重运行

## pytest名称规范：
- 文件，模块,test_开头，或者以test.py结尾
- 用例名称，test_开头
- 测试类类名：最好以Test开头

##pytest 运行
-1.右击（pytest）
-2.命令行的形式（自动收集在当前目下符合条件的用例）
-3.python指令运行

import pytest
#当以python脚本运行该文件的时候，执行下面的代码
if__name__=='__main__':
    pytest.mian()  收集当前目录下所有测试用例

##用例筛选  
指定测试模块： pytest test_demo.py   
指定测试目录： pytest tests/
通过节点id来运行测试：py模块名::类名::函数名  或者 py模块名::函数名   pytest test_login.py::test_ok
在需要运行的用例上加上标签名tag  如：@pytest.mark.自己定义的名字    运行： pytest -m 自己定义的名字
##一个用例可以加多个标签
##能不能支持多个标签，可以但是要加双引号
pytest -m "tag1 and tag2"  pytest -m "tag1 or tag2"  pytest -m "tag1 and not tag2"  包含tag1不包含tag2    pytest -m "not tag2"  不包含tag2

##skip,跳过用例
-同事写的用例，最好不要删，可以跳过
-页面改动，改了用例，可以把原来的用例不要删除，可以跳过
--skipif 跳过条件,如果是windows系统就跳过，苹果是'darwin' 也可以用linux
@pytest.mark.skipif(sys.platform=='win32'，reason='window系统'') 
def test_demo(self):
    pass
    
## 用例执行顺序
-在unittest 用例顺序是根据 ascii编码，用例名称
-pytest 是从上到下。

##pytest 断言
-如果继承了 unittest.TestCase, aseert, self.assertEqual 都是可以用的
-但是如果没有继承，只能用assert关键字

#测试报告
pip install pytest-html
pytest --html=report.html

## 数据驱动 parametrize
@pytest.mark.parametrize("自己起的名字",add_data)
def test_add(自己起的名字):
    print(自己起的名字)
#pytest test_add.py -s
#-s可以截获print信息

##Toast 弹窗

##TODO:
##每次用例都需要去开关浏览器
##一个类用一次浏览器，会有什么问题？ 如果不重新打开浏览器，测试数据会不重置 ，数据会错误

##web自动化测试本身就是本稳定的
要提高稳定性（第一性）
如果提升效率会造成稳定性受影响，就先不要提高效率
web运行效率不高

##验证码
-开发关掉
-如果要测试验证码，让开发设置万能验证码
-去买aip服务，人工打码平台
--通过图像识别，技术 滑动，字母（库）

##复杂用例的执行。（主逻辑）
-投资功能。
步骤：
一.登录页面前置：打开浏览器，登录，（）
     1，有标
     2.标有钱
     3.有余额可以投资
     前置条件一定得通过自动化去实现吗？
     如果是，一定要通过web自动化去实现吗？
     不是，只是一个条件，手工也行，只要达到条件即可

二.在首页上，点击可以投的标  class= btn btn-special
三.在投标详情页，输入投标金额：xpath= form-control invest-unit-investinput
四.定位按钮 xpath=btn btn-special height_style

#basepage
只是一种封装手段 (通用的代码)

page Object 
页面当中的逻辑--> 封装成对象  （登录页面逻辑）（投资页面逻辑）
每个页面的行为是独特的，登录和投资页面的逻辑不一样

页面当中有没有通用的逻辑，是否具有每个页面都是一样的操作
不以业务发生变化而变化 find_element(locate) 三种显性等待
这些共有的都可以放在 通用逻辑放到通用类里 commonpage,也可以把所有的页面都具备的逻辑放在basepage
basepage里面不会有具体的元素,继承思想，把所有的通用逻辑写好，要用直接继承，如果要加其他的逻辑可以重写或者使用super().__init__()
还有哪些操作是通用的，可以封装到basepage
如果js可以实现的浏览器操作，如果selenium没有支持，就可以放到basepage
selenium不支持元素属性设置


def refresh(self):
    """刷新"""
    self.brower.refresh()
    
def get(self):
    """访问"""
    self.browser.get()
    
def set_attr
    '''设置属性''''
    
框架以后可以怎么优化？（面试题）
元素定位可读性不是很强，封装一个类使用描述符进行元素定位
