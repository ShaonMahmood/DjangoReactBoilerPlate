import os
import fileinput
import re

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Renames a Django Project'

    def add_arguments(self, parser):
        parser.add_argument('old_project_name', type=str, help='Old Project Name')
        parser.add_argument('new_project_name', type=str, help='New Project Name')

    def handle(self, *args, **options):
        new_project_name = options['new_project_name']
        old_project_name = options['old_project_name']

        files_to_rename = [
            f'{old_project_name}/settings/base.py',
            f'{old_project_name}/wsgi.py',
            'manage.py'
        ]

        folder_to_rename = old_project_name

        for filename in files_to_rename:
            with open(filename) as f:
                s = f.read()
            with open(filename, 'w') as f:
                s = s.replace(old_project_name,new_project_name)
                f.write(s)

        os.rename(folder_to_rename,new_project_name)
        self.stdout.write(self.style.SUCCESS(f'Project has been renamed from {old_project_name} to {new_project_name}'))