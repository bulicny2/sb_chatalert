"""
Management command to import a CSV file into the database. Used to introduce
new data to the system to be labeled and displayed.
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
    def parse_date(cls, date_text):
        patterns = ["%m/%d/%y %H:%M",
                    "%Y-%m-%d %H:%M:%S",
                    "%m/%d/%Y %H:%M:%S",
                    "%m/%d/%Y %H:%M"]
        for pattern in patterns:
            try:
                return datetime.datetime.strptime(date_text, pattern)
            except ValueError:
                pass
        raise ValueError("Date text %r didn't match any of the patterns %s" %
                         (date_text, patterns))
                

    @classmethod
    def import_row(cls, row):
        " Import a single row into the database "
        row = cls.clean_newlines(row)
        try:
            with transaction.atomic():
                message, _ = Message.objects.get_or_create(guid=row["guid"])
                message.creation_datetime = \
                    cls.parse_date(row["creation_date"])
                message.message_type = row["type"]
                message.source = row["source"]
                message.url = row["url"]
                message.text = row["text"]
                message.author = row["author"]
                message.author_age = row["author_age"]
                message.city_state = row["city_state"]
                message.lat = row["lat"] or 0
                message.lng = row["lng"] or 0
                message.phone_number = row["phone_number"]
                message.post_id = row["post_id"]                
                message.label_user = row["label"] or -1
                message.clean()
                message.save()

                logger.info("Imported message %s", row.get("guid"))
        except:
            logger.error("Failed to import message %s: %s",
                         row.get("guid"), traceback.format_exc())
            raise
