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


def parse_health(data: tuple |dict):
    return Healthcheck(**data) #unpack dict (dict's keys should be = class fields names

def parse_pagespeed(data: tuple | dict):
    return PageSpeed(**data)

ic(data[0])
ic(data[1])
health = parse_health(data[0])
ic(health)
# pagespeed = parse_health(data[1])


