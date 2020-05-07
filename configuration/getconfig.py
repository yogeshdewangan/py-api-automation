# log config
import argparse
import logging
# logging.config.fileConfig("../configuration/logging.ini")
# log = logging.getLogger(__name__)

logging.basicConfig(filename='../log/test.log', filemode='w', format='%(asctime)s %(levelname)-5s [%(module)s] %(message)s')
log = logging.getLogger(__name__)
# app config
from configparser import ConfigParser
configParser = ConfigParser()
configParser.read("../configuration/config.ini")
props = dict(configParser.items("DEFAULT"))
section = lambda sec, prop: configParser.items(sec, prop)
