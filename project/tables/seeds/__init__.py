"""This makes the seed_db function in main.py 
accessible by importing the seed folder
"""

'''
from tables.seeds import *
seed_db(<path_to_data>)
example:
seed_db('tables/seeds/datasets/')
# the trailing slash is very important
'''

from .main import seed_db