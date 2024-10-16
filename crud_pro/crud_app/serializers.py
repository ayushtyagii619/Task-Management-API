from rest_framework import serializers
from .models import NewUser, Task
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from datetime import date

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True,
                                   validators = [UniqueValidator(queryset=NewUser.objects.all())])
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only = True,required = True)

    class Meta:
        model = NewUser
        fields = ['email','password','password2']
    
    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password didn't match"})
        return attrs
    def  create(self, validated_data):
        user = NewUser.objects.create(
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    class Meta:
        model = NewUser
        fields  = ['email','password']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','status','priority','due_date']

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def validate_status(self, value):
        current_instance = self.instance  # Get the existing task instance if updating
        if current_instance:
            # Ensure status follows logical progression (pending → in-progress → completed)
            if value == 'in-progress' and current_instance.status != 'pending':
                raise serializers.ValidationError("Status can only change to 'in-progress' from 'pending'.")
            if value == 'completed' and current_instance.status != 'in-progress':
                raise serializers.ValidationError("Status can only change to 'completed' from 'in-progress'.")
            if current_instance.status == 'completed':
                raise serializers.ValidationError("Task already completed.")
        return value