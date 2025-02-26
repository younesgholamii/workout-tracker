from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, phone_number, password=None, **kwargs):
        if not first_name:
            raise ValueError('user must have an first_name')
        if not last_name:
            raise ValueError('user must have an last_name')
        if not username:
            raise ValueError('user must have an username')
        if not email:
            raise ValueError('user must have an email')
        if not phone_number:
            raise ValueError('user must have an phone_number')
        
        user = self.model(first_name=first_name, last_name=last_name, username=username, email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, phone_number, password=None, **kwargs):
        user = self.create_user(first_name, last_name, username, email, phone_number, password)
        user.is_admin = True
        user.save()
        return user

