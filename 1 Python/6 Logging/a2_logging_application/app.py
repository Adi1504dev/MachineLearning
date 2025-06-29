from logger import logging

def add(x,y):
    logging.info("Performing addition operation")
    return x+y
logging.info("Addition operation completed")
logging.info(f"Output {add(4,5)}")
