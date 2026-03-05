"""
Reshapes input metrics for database storage

This service receives [data] from 'data_capturer' and reshape it for DB model
with engines from 'init_engine'
"""

"""TODO: ORM is already a way to operate data like objects with DB integration
   That why parsing implies using those models (with no additional dto) 
"""
from src.app.models.models import Healthcheck, PageSpeed


def parse_health(data: dict):
    return Healthcheck(**data) #unpack dict (dict's keys should be = class fields names

def parse_pagespeed(data: dict):
    return PageSpeed(**data)

def parse_both(data: tuple):
    return tuple( {parse_health(data[0]), parse_pagespeed(data[1])} ) #this should return a tuple of 2 objects 




