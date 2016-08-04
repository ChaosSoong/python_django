##注意坑
数据库采用的是sqlite3
1.数据验证命令:python manage.py check 
2.生成数据库表:python manage.py makemigrations models_name
3.同步模型到数据库的命令:python manage.py migrate
4.from books.models import Author //导入Author模型类
  a=Author(first_name='',last_name='',email='')  //创建模型类的实例
  a.save()//保存到数据库
  Author.objects.all() //取出数据库的信息，相当于执行了一条SQL `` SELECT`` 语句

