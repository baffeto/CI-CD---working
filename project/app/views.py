from django.shortcuts import render


def main_page(request):
    return render(request, template_name='app/index.html')