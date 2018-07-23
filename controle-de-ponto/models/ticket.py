import datetime

"""
>>> import rlcompleter, readline
>>> readline.parse_and_bind('tab:complete')
"""

class Ticket(object):

    created_at = datetime.datetime.utcnow(),
    empresa = '',
    local = '',
    pessoa = '',
    date = None,
    time = None,
    done = False

    def __init__(self, *args, **kwargs):
    	if kwargs:
    		self.__setattr__(key, value) for key,value in kwargs if key
