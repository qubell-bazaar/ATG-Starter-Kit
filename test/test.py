import os

from qubell.api.testing import *

@environment({
    "default": {},
    #"AmazonEC2_Centos_6.4": {
    #    "policies": [{
    #        "action": "provisionVms",
    #        "parameter": "imageId",
    #        "value": "us-east-1/ami-ee698586"
    #    }, {
    #        "action": "provisionVms",
    #        "parameter": "vmIdentity",
    #        "value": "root"
    #    }]
    #}
})
class ATGTestCase(BaseComponentTestCase):
    name = "ATG-Starter-Kit"
    meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml')) 
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name)),
        "settings": {"destroyInterval": 1000*60*60*2}
    }]
    @classmethod
    def timeout(cls):
        return 120
    @instance(byApplication=name)
    @values({"endpoints.atg-store-prod": "url"})
    def test_url(self, instance, url):
      import requests

      response = requests.get(url, timeout=60)
      assert response.status_code==200
    
