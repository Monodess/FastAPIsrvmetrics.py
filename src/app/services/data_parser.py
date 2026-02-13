"""
Reshapes input metrics for database storage

This service receives [data] from 'data_capturer' and reshape it for DB model
with engines from 'init_engine'
"""
import os

from dotenv import load_dotenv
from icecream import ic

"""TODO: ORM is already a way to operate data like objects with db integration
   That why parsing implies using those models (with no additional dto) 
"""
from src.app.models.models import Healthcheck, PageSpeed
from data_capturer import loop


def parse_health(data: dict):
    return Healthcheck(**data) #unpack dict (dict's keys should be = class fields names

def parse_pagespeed(data: dict):
    return PageSpeed(**data)

def parse_both(data: tuple):
    return tuple( {parse_health(data[0]), parse_pagespeed(data[1])} ) #this should return a tuple of 2 objects 


# pagespeed = parse_health(data[1])


