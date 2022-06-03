from django.db import models


#1. 이미지필드를 사용해서 모델을 만든다
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='uploads/')
    #upload_to에 url을 'uploads/'라고 썼기 때문에 uploads폴더가 생겼다
    #imagefiled(height_field,width_field) 이런거 사용해서 이미지 크기 지정도 가능한것 같음

def __str__(self): #이건 원본 파일에 써서 쓴거임...
    return self.title


