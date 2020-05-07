# log config
import logging

logging.basicConfig(filename='../log/test.log', level=logging.DEBUG, filemode='w+', format='%(asctime)s %(levelname)-5s [%(module)s] %(message)s')
log = logging.getLogger(__name__)


# app config
from configparser import ConfigParser
configParser = ConfigParser()
configParser.read("../configuration/config.ini")
props = dict(configParser.items("DEFAULT"))
section = lambda sec, prop: configParser.items(sec, prop)
