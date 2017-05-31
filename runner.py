import elasticache
from settings import *
import consul
import logging


# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')
logger = logging.getLogger()

services = elasticache.collect_elasticache_information()

for key, value in services.iteritems():
    consul.register_external_service(CONSUL_URL, key, value['Address'], value['Port'])
