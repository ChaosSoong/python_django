##ע���
���ݿ���õ���sqlite3
**1.������֤����:python manage.py check
 
**2.�������ݿ��:python manage.py makemigrations models_name

**3.ͬ��ģ�͵����ݿ������:python manage.py migrate

**4.from books.models import Author //����Authorģ����

  a=Author(first_name='',last_name='',email='')  //����ģ�����ʵ��
  
  a.save()//���浽���ݿ�
  
  Author.objects.all() //ȡ�����ݿ����Ϣ���൱��ִ����һ��SQL `` SELECT`` ���

**5.���ݹ���:Author.objects.filter(name='')//���Դ��ݶ������  name__contains=''ģ��ƥ��,����һ����¼��

    ��ȡ��������Author.objects.get(name='') //�����ѯû�з��ؽ���ͻ��׳��쳣
	
	��������Author.objects.order_by('name')//'-name'���򣬲���Ҳ����Ϊ������ڶ����ֶλ��ڵ�һ���ֶε�ֵ��ͬ������±�ʹ�õ�
	
	��ģ����ָ��ȱʡ����ʽ��'''class Meta
									ordering =['name']'''
									
	���Ʒ��ص����ݣ������Ƭ�﷨������֧�ָ������������Ȳ�����������Ƭ

	ɾ������'''a=Author.objects.get(name='chaos')
				  p.delete()'''
				  
             '''Author.objects.all().delete()'''//�����all()



