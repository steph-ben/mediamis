from itertools import chain
#from querysetjoin import QuerySetJoin

class FilteredQuerySetJoin(object):
   def filter(self, **kwargs):
        """ Apply filter on all querysets et return results """
        filtered_querysets = [qs.filter(**kwargs) for qs in self.querysets]
        return chain(*filtered_querysets)