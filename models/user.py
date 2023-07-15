#!/usr/bin/python3
"""Import"""


from models.base_model import BaseModel


"""Class User"""


class User(BaseModel):
    """Public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
