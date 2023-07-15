#!/usr/bin/python3
"""Imports"""


from models.base_model import BaseModel


"""Class Review"""


class Review(BaseModel):
    """Public class attributes"""
    place_id = ""
    user_id = ""
    text = ""
