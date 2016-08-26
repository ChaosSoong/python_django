##注意坑
###数据库采用的是sqlite3

- 数据验证命令:python manage.py check
 
- 生成数据库表:python manage.py makemigrations models_name

- 同步模型到数据库的命令:python manage.py migrate

- from books.models import Author //导入Author模型类

  	a=Author(first_name='',last_name='',email='')  //创建模型类的实例
  
 	 a.save()//保存到数据库
  
  	Author.objects.all() //取出数据库的信息，相当于执行了一条SQL `` SELECT`` 语句

- 数据过滤:Author.objects.filter(name='')//可以传递多个参数  	name__contains=''模糊匹配,返回一个记录集

	获取单个对象：Author.objects.get(name='') //如果查询没有返回结果就会抛出异常
	
	数据排序：Author.objects.order_by('name')//'-name'逆序，参数也可以为多个，第二个字段会在第一个字段的值相同的情况下被使用到
	
	在模型中指定缺省排序方式：class Meta
								ordering =['name']
									
	限制返回的数据：遵从切片语法，但不支持负索引，并非先查找所有再切片

	删除对象：a=Author.objects.get(name='chaos')
			 p.delete()
				  
             Author.objects.all().delete()  //必须加all()

- 设置字段可选:email = models.EmailField(**blank=True,null=True** )

- 设置中文字段标签：email = models.EmailField(blank=True, verbose_name='电子邮件')  另：**coding：utf-8**

- 改进表单的时候,''/search-form/''指向的是表单,更改之后
**< form action="" method="get">**action=""后指向本页面,而''/search-form/''没有任何修改,应该为''/search/''

- 有关csrf验证问题:[点这里](http://blog.csdn.net/tr1ue/article/details/20654943)