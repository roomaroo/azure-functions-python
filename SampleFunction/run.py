import os
import sys

response = open(os.environ['res'], 'w')
response.write(sys.version)
response.close()