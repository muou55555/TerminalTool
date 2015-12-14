#TerminalTool
##项目概述
>>基于python语言开发，表格式终端命令菜单，会在此菜单上添加嵌入式开发中经常用到的工具类方法。目前按业务控制功能、视图、通用包进行分类
##一、pytable
功能说明：表格类，支持按行增加内容；支持多列；支持缺省列时补空；运行是否显示表格标题
###1.1 使用方法 
1、初始化pytable
```python
a = Pytable("Table Title", 60, [10, 20, 30])
```
2、显示表标题
```python
a.add_table_header()
```
3、添加行数据
```python
a.add_row_data(["1 - Home", "2 - Telnet", "3 - SSH"])
```
4、显示表格
```python
a.show()
```
##二、pymenu
功能说明：表格菜单类，支持按行增加内容；支持多列；支持缺省列时补空；支持多级子菜单；支持退出确认机制；支持自定义菜单功能实现
###2.1 使用方法
1、初始化pymenu
```python
main_menu = Pymenu("Main Menu", [20, 20, 20], back_key = "q")
```
3、添加行数据
```python
main_menu.add_field("1", "Telnet", lambda:fun("Telnet"))
main_menu.add_field("4", "SSH", fun_test)
main_menu.add_field("b", "sub b", None)
```
4、显示菜单
```python
main_menu.show()
```
