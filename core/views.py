from django.shortcuts import render


def about_us(request):
    return render(request=request, template_name="about.html")
