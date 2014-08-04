#!/usr/bin/python
# -*- coding: utf-8 -*-

# PARAMETERS
import yaml

class Parameters:
    def __init__(self):
        stream = open("/home/laurent/Stage_LIA/WAV2JOKE/PyJoke/parameters.yml", "r")
        docs = yaml.load_all(stream)
        for doc in docs:
            self.host = doc["database"]["host"]
            self.user = doc["database"]["user"]
            self.passwd = doc["database"]["passwd"]
            self.db = doc["database"]["db"]
            self.table = doc["database"]["table"]

            self.lang = doc["pyjoke"]["lang"]
            self.jokelen = doc["pyjoke"]["jokelen"]
            self.debug = doc["pyjoke"]["debug"]

            self.postag = doc["postag"]["active"]
            self.default = doc["postag"]["default"]
            self.adj = doc["postag"]["adj"]
            self.noun = doc["postag"]["noun"]
            self.verb = doc["postag"]["verb"]
            self.brute = doc["postag"]["brute"]

            self.conv = doc["conversation"]["level"]

            if self.debug:
                for k,v in doc.items():
                    print k, "->", v
                print "\n",
