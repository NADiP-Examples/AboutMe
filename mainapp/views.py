import datetime
from .models import Work
from django.shortcuts import render, render_to_response, Http404, \
    get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


def main(request):
    name = "евгений"
    surname = "юрченко"
    middlename = "витальевич"
    return render(request, "index.html",
                  {"name": name, "surname": surname, 'middlename': middlename})


def works(request):
    _works = Work.objects.all()
    # _works = [{"header": "Skyparkcdn", "post": "Программист-разработчик",
    #            "desc": "Разработка серверной(nodejs) и клиентской(angularJS) частей веб-сервисов. "
    #                    "Написание микро-сервисов для работы с MongoDB (REST архитектура). "
    #                    "Верстка по предоставленным макетам (Bootstrap)"},
    #           {"header": "tranio.ru", "post": "Программист Python",
    #            "desc": "Доработка функциональности сайта. Backend разработка - Django, "
    #                    "Frontend - javascript и верстка по предоставленным шаблонам."},
    #           {"header": "Новосибирская Академия Дизайна и Программирования, НУДО", "post":
    #               "Преподаватель: программирование и веб-дизайн",
    #            "desc": "Обучение детей 7-11 класс программированию на языке Python, верстка (HTML5, CSS). "
    #                    "Разработка лекций, учебных и методических материалов."},
    #           {"header": "ОАО 'НижневартовскНефтеГеоФизика'", "post": "Инженер-геофизик",
    #            "desc": "Констроль процесса бурения на нефтяных платформах"},
    #           ]
    # Контекст "page": request.path[1:] нужен, для отображения активной закладки в меню
    return render(request, "works.html", {"works": _works, "page": request.path[1:]})


def work(request, id):
    # try:
    #     cur_work = Work.objects.get(id=id)
    # except ObjectDoesNotExist:
    #     raise Http404'
    get_object_or_404(Work, id=id)
    # print("id  ", id)
    return render(request, 'work_card.html', {})

def learn(request):
    study_places = [
        {"date_from": datetime.date(1990, 9, 1), "date_to": datetime.date(1997, 6, 1),
         "place": "Общеобразовательная школа"},
        {"date_from": datetime.date(1997, 9, 1), "date_to": datetime.date(2000, 6, 1),
         "place": "Лицей"},
        {"date_from": datetime.date(2000, 9, 1), "date_to": datetime.date(2006, 7, 1),
         "place": "СибГИУ"},

    ]
    return render_to_response("learn.html", {"study_places": study_places, "page": request.path[1:]})
