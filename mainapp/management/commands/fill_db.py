from django.core.management.base import NoArgsCommand, CommandError
from mainapp.models import Work, Hobby, Study, Organization
from datetime import date


class Command(NoArgsCommand):
    help = 'Fill DB new data'

    def handle_noargs(self, **options):
        organizations = [
            {'name': 'ООО "СтройКопай"', 'region': 'Москва', 'tax_id': 123456, 'site': 'build_dig.com'},
            {'name': 'ИП "Иванушка"', 'region': 'Подмосковье', 'tax_id': 666122, 'site': ''},
            {'name': 'GeekBrains', 'region': 'Москва', 'tax_id': 123456, 'site': 'geekbrains.ru'},

        ]
        works = [
            {'organization': 'ООО "СтройКопай"', 'position': 'digger',
             'duties': 'В основном копал...', 'period': 6},
            {'organization': 'ИП "Иванушка"', 'position': 'assistant',
             'duties': '...', 'period': 4},
            {'organization': 'GeekBrains', 'position': 'teacher',
             'duties': 'Пдготовка и преподавание курсов python/django', 'period': 12},
        ]
        hobbies = [
            {'name': 'tourism'},
            {'name': 'programming'},
            {'name': 'digging -)'},
        ]
        studies = [
            {'type': 'school', 'number': 36, 'study_from': date(1990, 9, 1), 'study_to': date(1998, 6, 1)},
            {'type': 'lyceum', 'number': 66, 'study_from': date(1998, 9, 1), 'study_to': date(2001, 6, 1)},
            {'type': 'university', 'number': 0, 'study_from': date(2001, 9, 1), 'study_to': date(2006, 8, 1)},
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
