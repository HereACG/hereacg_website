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
    # Finished (09/16/2016 Morning)@thislight
    # I'm crying...
    def init(self,mongo,dbname):
        self._db = mongo.db[dbname]
        return self
    
    @staticmethod
    def filter_val(val,egg):
        if egg(val):
            return val
        else:
            raise ModelFilterError(
                "value:%s could not pass filter function %s" % (val,repr(egg))
                )
    
    def load(self,**kargs):
        # TODO (09/14/2016 Night)@thislight: finish function 'load'
        # Finished (09/15/2016 Night)@thislight
        self._doc = self._db.find_one_or_404(kargs)
        return self
    
    def __getattr__(self, name):
        return self._doc[name]
    
    def __setattr__(self, name, value):
        self._doc[name] = value
        return self
    
    def __delattr__(self, name):
        del self._doc[name]
        return self
    
    def __bool__(self):
        if self._doc:
            return True
        else: return False
    
    def __len__(self):
        return len(self._doc)
    
    def __getitem__(self, key):
        return self.__getattr__(key)
    
    def __setitem__(self, key, value):
        return self.__setattr__(key,value)
    
    def __delitem__(self, name):
        return self.__delattr__(name)
    
    def __mod__(self, t):
        self.filter_val(self._doc[t[1]],t[2])
        return self
    
    def __or__(self, other):
        self._doc.extend(other)
        return self
        
    def __invert__(self):
        return self.clean()
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        if (type,value,traceback) is (None,None,None):
            self.save()
            ~self
        else:
            return True
    
    def save(self):
        doc = self._doc
        values = self.__dict__['values']
        for k in values:
            self.filter_val(doc[k],values[k])
        if doc['_id']:
            self._db.update({'_id':doc['_id']},doc)
        else:
            self._db.insert(doc)
    
    def clean(self):
        self._doc = None
    
    def __contains__(self, item):
        return item in self._doc



