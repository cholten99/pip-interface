#!/usr/bin/python

import yaml
f = open("test.yaml")
dataMap = yaml.safe_load(f)
f.close()

print dataMap

