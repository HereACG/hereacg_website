"""
Some helper function for package auth
"""

class NoAPIKeyException(Exception):
    pass

class APIKeyNeedFunction(object):
    def __init__(egg,app):
        self._egg = egg
        self._app = app

    def apikey(self,r):
        apikey = r.args.get('apikey',None)
        if apikey != None:
            return apikey
        else:
            raise NoAPIKeyException()

    def __call__(self,*args,**kargs):
        try:
            self._egg(self.apikey(request),*args,**kargs)
        except NoAPIKeyException as e:
            self._app.logger.error("A ERROR Happened:"+e)



def apiv1_prefix(s):
    return '/api/v1' + s


def apikey_need(egg):
    pass
