# -*- coding: utf-8 -*-
import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        f = open("taski.json")
        tasks_file = json.load(f)
        f.close()
        tasks_file = tasks
        f = open("taski.json", "w")
        json.dump(tasks_file, f, indent=4)
        f.close()

