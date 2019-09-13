from django.shortcuts import render
from .models import Destination, News

# Create your views here.

def index(request) :
    
#    dest1 = Destination()
#    dest1.name = 'Mumbai'
#    dest1.img = 'destination_1.jpg'
#    dest1.desc = "The city that never sleeps"
#    dest1.price = 800
#    dest1.offer = True
#    
#    dest2 = Destination()
#    dest2.name = 'Goa'
#    dest2.img = 'destination_3.jpg'
#    dest2.desc = "The perfect holiday destination"
#    dest2.price = 700
#    dest2.offer = False
#    
#    dest3 = Destination()
#    dest3.name = 'Udaipur'
#    dest3.img = 'destination_2.jpg'
#    dest3.desc = "The city of lakes"
#    dest3.price = 750
#    dest3.offer = False
#    
#    dests = [dest1, dest2, dest3]

    dests = Destination.objects.all()
    
    news1 = News()
    news1.img = 'news_1.jpg'
    news1.date = '16'
    news1.month = 'Feb'
    news1.headline = "Birthdate of Legend"
    news1.category = "Wishing"
    news1.desc = "This is the great day on which the legend named Ankush is born"
    
    news2 = News()
    news2.img = 'news_2.jpg'
    news2.date = '16'
    news2.month = 'Feb'
    news2.headline = "Birthdate of Legend"
    news2.category = "Wishing"
    news2.desc = "This is the great day on which the legend named Ankush is born"
    
    news3 = News()
    news3.img = 'news_3.jpg'
    news3.date = '16'
    news3.month = 'Feb'
    news3.headline = "Birthdate of Legend"
    news3.category = "Wishing"
    news3.desc = "This is the great day on which the legend named Ankush is born"
    
    news = [news1, news2, news3]
    
    return render(request, "index.html", {'dests' : dests, 'news' : news})