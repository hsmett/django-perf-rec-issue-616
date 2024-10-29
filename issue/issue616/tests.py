import json
import django_perf_rec
from django.test import TestCase

from issue616.models import Entity


class TestIssue616(TestCase):
    def test_issue616(self):
        with django_perf_rec.record():
            Entity.objects.create(description=json.dumps({"foo": "bar"}))

        with django_perf_rec.record():
            Entity.objects.create(description=json.dumps({"foo": "bar\nbaz"}))
