from home.models import CustomUser


def context(request):
    user = CustomUser.objects.filter(is_superuser=True, is_staff=True).order_by('-date_joined').first()
    return {"admin_user": user}
