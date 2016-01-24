"""
Management command to import a CSV file into the database, which specifies what
city-state information each post has
"""

from __future__ import print_function

import csv
import datetime
import logging
import re
import traceback

from django.core.management.base import BaseCommand
from django.db import transaction

from ...models import Message


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('csv_files', nargs="+")

    def handle(self, *args, **options):
        for file_name in options['csv_files']:
            reader = csv.DictReader(open(file_name))
            for row in reader:
                self.import_row(row)

    @classmethod
    def clean_newlines(cls, row):
        " Remove newlines or literal backslash-N sequences from input "
        result = dict()
        for key in row:
            result[key] = re.sub(r'\\n|\n', '', row[key], flags=re.IGNORECASE)
        return result

    @classmethod
    def import_row(cls, row):
        " Import a single row into the database "
        row = cls.clean_newlines(row)
        try:
            with transaction.atomic():
                message, _ = Message.objects.get_or_create(guid=row["guid"])
                message.city_state = "%s, %s" % (row["city"], row["state"])
                message.clean()
                message.save()

                logger.info("Imported message %s", row.get("guid"))
        except:
            logger.error("Failed to import message %s: %s",
                         row.get("guid"), traceback.format_exc())
            raise
