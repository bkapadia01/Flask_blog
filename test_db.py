#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:43:27 2019

@author: clintoninnes
"""

from sqlalchemy import create_engine
import pandas as pd

SECRET_KEY='0b52813d81229b96c4623a337b016c55'
SQLALCHEMY_DATABASE_URI='sqlite:///site.db'



engine = create_engine(SQLALCHEMY_DATABASE_URI)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
engine.table_names()
df = pd.read_sql_query('SELECT * from post', engine)