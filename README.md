##ע���
���ݿ���õ���sqlite3
1.������֤����:python manage.py check 
2.�������ݿ��:python manage.py makemigrations models_name
3.ͬ��ģ�͵����ݿ������:python manage.py migrate
4.from books.models import Author //����Authorģ����
  a=Author(first_name='',last_name='',email='')  //����ģ�����ʵ��
  a.save()//���浽���ݿ�
  Author.objects.all() //ȡ�����ݿ����Ϣ���൱��ִ����һ��SQL `` SELECT`` ���

