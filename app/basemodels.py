# TODO (09/14/2016 Night)@thislight: move it to file 'basemodel.py'
# Finished (09/15/2016 Night)@thislight 

class ModelException(Exception):
    pass

class ModelFilterException(ModelException):
    pass


class Filters(object):
    # TODO (09/14/2016 Night)@thislight: add more filter function
    # example: stringonly...
    
    @staticmethod
    def any(val):
        return True
    
    @staticmethod
    def notempty(val):
        return not val is None
    
    @staticmethod
    def numberonly(val):
        if val is int:
            return True
        elif (val is str) and val.isnumeric():
            return True
        else:
            return False
    


class Model(object):
    # TODO (09/14/2016 Night)@thislight: finish class 'Model'
    def init(self,mongo):
        self._mongo = mongo
    
    @staticmethod
    def filter_val(val,egg):
        if egg(val):
            return val
        else:
            raise ModelFilterError(
                "value:%s could not pass filter function %s" % (val,repr(egg))
                )
        
    def load(**kargs):
        # TODO (09/14/2016 Night)@thislight: finish function 'load'
        pass



