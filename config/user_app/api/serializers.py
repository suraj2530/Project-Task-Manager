
from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(style = {'input_type': 'password'} ,  write_only=True)
  class Meta:
    model = User
    fields = ['username','email', 'password', 'password2']  #  this uses [] not () in fields
    extra_kwargs = {
      'password' : {'write_only': True}, 
    }
  
  def save(self):
    password = self.validated_data['password']
    password2 = self.validated_data['password2']
    if (password != password2):
      raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})
    
    if User.objects.filter(email = self.validated_data['email']).exists(): 
      #  don't use like email = self.validated_data['email']))
      raise serializers.ValidationError({'error': 'Email already exists!'})
     
    account = User(email = self.validated_data['email'], username = self.validated_data['username'])
    account.set_password(password)
    account.save()
    return account
    

