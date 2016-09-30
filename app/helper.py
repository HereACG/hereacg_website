"""
Helper for all of app
"""

class Request(object):
    def __init__(self,*args,**kargs):
        pass

    def go(self,*args,**kargs):
        self.handle(*args,**kargs)

    def handle(self,*args,**kargs):
        pass

    def __enter__(self):
        return self.__onwith__()

    def __exit__(self,type,value,traceback):
        if (type,value,traceback) != (None,None,None):
            self.__onerror__(type,value,traceback)
        else:
            self.close()
        return True

    def __onwith__(self):
        pass

    def __onerror__(self,type,value,traceback):
        pass

    def close(self):
        pass
