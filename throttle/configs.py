import os

# path
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]
DATA_ROOT = os.path.join(CURRENT_PATH, 'data')

# web
PORT_CHOICES = (6050, 7050, 8050, 9050, 10050,)
