from django.shortcuts import render
from .models import pictures
from django.conf import settings
import os


def home(request):
    return render(request, 'index.html', {})


def showgallery(request, gallery):
    # print(gallery)
    # img_list = os.listdir("C:/Users/N.TALEC-BERNARD/Desktop/test")
    data = dict()
    if not gallery == "all":
        img_list = os.listdir(settings.STATIC_ROOT + "/static/gallery/" + gallery)
        img_list_copy = img_list
        img_list_copy = ["../../static/gallery/" + gallery + "/" + e for e in img_list_copy]

        compteur = 0
        if not (pictures.objects.filter(IMG_URL=img_list_copy[0]).exists()):

            for e in img_list:
                print(img_list)
                e = e[:-4]
                IMG_NAME = e
                # print(IMG_NAME)
                CATEGORY = gallery
                # print(CATEGORY)
                IMG_URL = img_list_copy[compteur]
                ALL = "all"
                compteur = compteur + 1
                # print(IMG_URL)
                picture_data = pictures(IMG_NAME=IMG_NAME,
                                        CATEGORY=CATEGORY,
                                        IMG_URL=IMG_URL,
                                        ALL=ALL)
                picture_data.save()

                data['pics'] = pictures.objects.filter(CATEGORY=gallery)
            return render(request, 'gallery.html', data)
        else:
            data['pics'] = pictures.objects.filter(CATEGORY=gallery)
            return render(request, 'gallery.html', data)
    else:
        data['pics'] = pictures.objects.filter(ALL="all")
    return render(request, 'gallery_all.html', data)
