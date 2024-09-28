from rest_framework import serializers 
from django.contrib.auth.models import User 
from django.db.models import Q

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input-type': 'password'}, write_only= True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

        extra_kwargs = {
            'password': {'write_only': True},
        }
    def save(self, *args, **kwargs):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        print(args, kwargs)

        if password != password2: 
            raise serializers.ValidationError({'Error':'Password mismatch'})
        
        if User.objects.filter(Q(username=self.validated_data['username']) | Q( email=self.validated_data['email'])).exists():
            raise serializers.ValidationError({'Error':'This user with this smae username or email already exists'})
        

        
        user = User.objects.create_user(username=self.validated_data['username'], email=self.validated_data['email'], password=password)
        return user
    