#!/usr/bin/python3
"""
Module for class review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Declares Review class
    """
    place_id = ""
    user_id = ""
    text = ""
