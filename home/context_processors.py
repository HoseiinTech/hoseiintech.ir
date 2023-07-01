from home.models import CustomUser, AboutMe


def context(request):
    user = CustomUser.objects.filter(is_superuser=True, is_staff=True).order_by('-date_joined').first()
    about = AboutMe.objects.filter(status=True).first()
    return {"admin_user": user, "icon_site": about}
