from django.shortcuts import render
from bs4 import BeautifulSoup
from Kylym.models import Mentor, Statistic, Sponsor, Body
import requests


def name_representative(request):
    mentors = Mentor.objects.all()
    context = {
        'mentors':mentors,
        'statistics': Statistic.objects.all(),
        'sponsors': Sponsor.objects.all(),
        'bodies': Body.objects.all()
    }
    return render(request, 'index.html', context)

def save_html(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    with open(filename, "w", encoding='utf-8') as f:
        f.write(str(soup))

        
if __name__ == "__main__":
    url = "https://let-me-explain-43808461.hubspotpagebuilder.com/main"
    filename = "index.html"
    save_html(url, filename)



# def split_style(url, filename):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     with open(filename, "w", encoding='utf-8') as formatted:
#         formatted.find('style').text  
     
# if __name__ == "__main__":
#     url = "https://let-me-explain-43808461.hubspotpagebuilder.com/main"
#     filename = "style.html"
#     split_style(url, filename)   

