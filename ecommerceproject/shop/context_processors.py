# all the menu links are set over here
from . models import Category

def menu_links(requset):
    links=Category.objects.all()
    return dict(links =links)