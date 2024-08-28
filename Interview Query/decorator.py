import logging.config
import time
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s " )
def execution_decorator(func):
    def wrapper( *args, **kwargs):
        start = time.time()
        result = func(*args)
        end = time.time()
        executionTime = end - start
        logging.info(f'my execution time is {executionTime} and result is {result}')
        return result
    return wrapper




@execution_decorator
def addit(a,b):
    time.sleep(0.5)
    return a+b

print(addit(5,4))