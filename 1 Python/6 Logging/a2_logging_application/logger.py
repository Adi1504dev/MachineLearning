import logging

## Setting logging level to DEBUG
logging.basicConfig(
    filename='application.log',
    filemode='w', # Can be w to overwrite and a to append
    level=logging.INFO,
    format='%(asctime)s -%(name)s - %(levelname)s - %(message)s',# Format Log
    datefmt= '%Y-%m-%d %H:%M:%S',# setting Date format
    force=True
)