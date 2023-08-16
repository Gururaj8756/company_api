from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("WORKED")
    li1=[
        'Guru',
        'Raj',
        'Hello'
    ]
    return JsonResponse (li1,safe=False)