# -*- coding: utf-8 -*-
import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        f = open("taski.json")
        taski = json.load(f)
        f.close()
        return taski


    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.read_tasks()

f = open("taski.json")
taski = json.load(f)
f.close()
print(taski)