import os,sys
sys.path.append(os.path.dirname(__file__))
from app import JsonpDataProxy
app_file = os.path.join('/usr/lib/ckan/default/src/dataproxy/dataproxy/app.py')
execfile(app_file,dict(__file__=app_file))

application = JsonpDataProxy(3000000)
