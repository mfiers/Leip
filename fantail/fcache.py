
import hashlib
import functools
import logging
import os
import pickle


from decorator import decorate
import dill

lgr = logging.getLogger(__name__)
#lgr.setLevel(logging.DEBUG)

def _get_key(func, *args, **kwargs):
    """Build a sha256 hash of function + arguments"""
    sha256 = hashlib.sha256()
    sha256.update(dill.dumps(func))
    
    for a in args:
        sha256.update(dill.dumps(a))
        
    for k in sorted(kwargs):
        sha256.update(dill.dumps(k))
        sha256.update(dill.dumps(kwargs[k]))

    rv = sha256.hexdigest()
    lgr.debug("cache key: %s", rv)
    return rv


def fcache(func):
    cache = func.cache = {}
    
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = _get_key(func, *args, **kwargs)
        cachedir = './fcache/c/{}'.format(key[:3])
        if not os.path.exists(cachedir):
            os.makedirs(cachedir)
            
        cachefile = os.path.join(cachedir, key)
        
        if os.path.exists(cachefile):
            lgr.debug("found cachefile: %s", cachefile)
            with open(cachefile, 'rb') as F:
                return pickle.load(F)

        lgr.debug("no cache - running function")
        rv = func(*args, **kwargs)
        with open(cachefile, 'wb') as F:
            pickle.dump(rv, F, protocol=pickle.HIGHEST_PROTOCOL)
        return rv
    
    return memoized_func
