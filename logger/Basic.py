__author__ = 'Joseph'
import logging
import os
log_path = 'C:/Users/Joey/PycharmProjects/Joey_Logger/Basic.py'
log_file = 'basic'

#file_name = os.path.join(os.path.getcwd()+'\\log','Basic.log')                                                  '')
logging.basicConfig(ile_name = Basic.py, level=logging.INFO)
logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(loading information)")
log = logging.getLogger()

file_handler = logging.FileHandler("{0}/{1}.log".format(log_path, log_file))
file_handler.setFormatter(logFormatter)
log.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logFormatter)
log.addHandler(console_handler)