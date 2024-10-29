import logging 
import time

logging.basicConfig(level=logging.INFO, format= f'')

def exec_time(func):
    def wrapper(*args, **kwargs):
