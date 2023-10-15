#!/usr/bin/python3
"""
Module for class user
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
