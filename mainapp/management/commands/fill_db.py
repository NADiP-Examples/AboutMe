from django.core.management.base import NoArgsCommand, BaseCommand
from mainapp.models import Work, Hobby, Study, Organization
from datetime import date


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        organizations = [
            {'name': 'Skyparkcdn', 'region': 'Пермь', 'tax_id': 123456, 'site': 'https://www.skyparkcdn.com/'},
            {'name': 'ООО Транио', 'region': 'москва', 'tax_id': 666122, 'site': 'https://www.tranio.ru/'},
            {'name': 'GeekBrains', 'region': 'Москва', 'tax_id': 123456, 'site': 'geekbrains.ru'},

        ]
        works = [
            {'organization': 'Skyparkcdn', 'position': 'Программист-разработчик',
             'duties': 'Разработка серверной(nodejs) и клиентской(angularJS) частей веб-сервисов.Написание '
                       'микро-сервисов для работы с MongoDB (REST архитектура).Верстка по предоставленным '
                       'макетам (Bootstrap)', 'period': 6},
            {'organization': 'ООО Транио', 'position': 'Программист Python',
             'duties': 'Доработка функциональности сайта. Backend разработка - Django,Frontend - javascript и '
                       'верстка по предоставленным шаблонам.', 'period': 4},
            {'organization': 'GeekBrains', 'position': 'teacher',
             'duties': 'Подготовка и преподавание курсов python/django', 'period': 12},
        ]
        hobbies = [
            {'name': 'tourism'},
            {'name': 'programming'},
        ]
        studies = [
            {'type': 'school', 'number': 36,
'study_from': date(1989, 9, 1), 'study_to': date(1997, 6, 1)},
            {'type': 'lyceum', 'number': 84,
'study_from': date(1997, 9, 1), 'study_to': date(2000, 6, 1)},
            {'type': 'university', 'number': 0,
'study_from': date(2000, 9, 1), 'study_to': date(2005, 8, 1)},
        ]
        for organization in organizations:
            organization = Organization(**organization)
            organization.save()

        for work in works:
            org_name = work["organization"]
            # Получаем организацию по имени
            organization = Organization.objects.get(name=org_name)
            # Заменяем название организации объектом
            work['organization'] = organization
            work = Work(**work)
            work.save()

        for hobby in hobbies:
            hobby = Hobby(**hobby)
            hobby.save()

        for study in studies:
            study = Study(**study)
            study.save()
