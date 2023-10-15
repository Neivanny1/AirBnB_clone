#!/usr/bin/python3
"""
Module for city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City classinherits from BaseModel
    """
    state_id = ""
    name = ""
