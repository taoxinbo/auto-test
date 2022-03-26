import re
import traceback
import unittest
from ter_Oracle import Case
from unittest import TestLoader, TestSuite
from ter_Oracle.CasesFilter import getCases


class TestSuites(object):
    pass


def getCasesFromSuite(suite):
    cases = []
    for item in suite._tests:
        if isinstance(item, TestSuite):
            cases += getCasesFromSuite(item)
        else:
            cases.append(item)
    return cases


def getSuite():
    suite = unittest.TestSuite()
    suite.addTests(TestLoader().discover(getCases(), pattern='Test*.py'))
    return suite


# getCaseDoc = lambda case: case._testMethodDoc
for item in getCasesFromSuite(getSuite()):
    doc = (lambda case: case._testMethodDoc)(item)
    if doc is None: continue
    results = re.findall(':\w*:.*', doc)
    result = {}
    for item in results:
        _, key, *value = item.split(':')
        value = ':'.join(value).lstrip()
        if key not in result: result[key] = []
        result[key].append(value)
    try:
        case = Case()
        case.title = result.get('title')[0],
        case.precondition = ','.join(result.get('premise')),
        case.desc = ','.join(result.get('step')),
        case.result = ','.join(result.get('result'))
    except Exception as error:
        msg = traceback.format_exc()