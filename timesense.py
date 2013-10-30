#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'joesuber'
## in its own repo version ##
import sys
reload(sys).setdefaultencoding("utf8")
import time
from collections import OrderedDict, deque

class AccumUnits(object):
    """
    make & print human readable lists of quantifiable things like
    time, distance, weight - track them the way computers like
    (as granular as you wish) output them the way humans like
    (without having to think about it more than once)
    todo: add unit conversions
    """
    def __init__(self, unit_names=None, unit_qnts=None, VERBOSE=False):
        """
        whether passed-in or using defaults, last unit should have quant=1
        as it is the most 'granular' unit you are using.
        Pick an instance name to reflect the units being handled
        """
        default_units = ['year', 'month', 'day', 'hr', 'min', 'sec']    # always go big to small
        default_quants = [12, 30, 24, 60, 60, 1]                        # don't calculate, just list
        # default_units = ['mile', 'foot', 'inch']                      # just like in physics class
        # default_quants = [5280, 12, 1]
        if unit_names is None:
            if VERBOSE:
                print('using default unit labels:')
                print(default_units)
            self.unit_names = default_units
        else:
            self.unit_names = unit_names
        if unit_qnts is None:
            if VERBOSE:
                print('using default unit quantities:')
                print(default_quants)
            unit_qnts = default_quants
        assert(isinstance(self.unit_names, list))
        assert(isinstance(unit_qnts, list))
        assert(len(set(self.unit_names)) == len(unit_qnts))         # set() to be rid of duplicate names
        self.timeunits = OrderedDict()
        sec = 1
        self.seclist = deque()
        while unit_qnts:                                            # multiply to get successive units
            xun = unit_qnts.pop()
            self.seclist.appendleft(sec * xun)
            sec *= xun
        for ktm, vtm in zip(self.unit_names, self.seclist):         # zip them into OrderedDict
            self.timeunits[ktm] = vtm
            if VERBOSE:
                print('{:6} : {:10}'.format(ktm, vtm))
        self.VERBOSE = VERBOSE


    def breakdown(self, rawseconds):
        """
        incoming raw-seconds (or whatever) returned as list of whatever-unit strings
        """
        qt = abs(rawseconds)
        divtime = []
        for plc, (kt, vt) in enumerate(self.timeunits.viewitems()):
            qt, leftover = divmod(qt, vt)
            if qt:
                divtime.append(str(int(qt))+' '+str(kt))
            if leftover < 1:
                if self.VERBOSE:
                    print('({} = fractional {} from given {})'.format(leftover, kt, rawseconds))
                    print('a stringy-list breakdown (joined): ')
                return divtime
            qt = leftover
        return divtime

    def breakdict(self, rawseconds):
        """
        incoming raw-seconds (or whatever) returned as dict
        with {unit_name: quantity-inside-remainder}
        """
        qt = abs(rawseconds)
        divtime = OrderedDict()
        for plc, (kt, vt) in enumerate(self.timeunits.viewitems()):
            qt, leftover = divmod(qt, vt)
            if qt:
                divtime[kt] = int(qt)
            if leftover < 1:
                if self.VERBOSE:
                    print('({} = fractional {} from given {})'.format(leftover, kt, rawseconds))
                    print('a dictionary breakdown:')
                return divtime
            qt = leftover
        return divtime

    def timebetween(self, start, end):
        """
        returns dict of unit-quant breakdown, optionally prints as string
        """
        assert(isinstance(start, int) or isinstance(start, float))
        assert(isinstance(end, int) or isinstance(end, float))
        quant = end - start
        if self.VERBOSE:
            print('between {0} {2}, and {1} {2}'.format(start, end, self.unit_names[-1]))
            print(" : {}".format(", ".join(self.breakdown(quant))))
        return self.breakdict(quant)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arp in sys.argv:
            print ('sys.argv has: {}'.format(arp))
        sample_quant = sys.argv[1]
        print('going with cmd-line-given 1st quantity of {}'.format(sample_quant))
    else:
        sample_quant = time.time()
        print('no command line quantity, so...')
        print('using current time-quantity of {} seconds'.format(sample_quant, ))

    breaker = AccumUnits(VERBOSE=True)          # use optional params to instantiate w/ your unit-quant combos
    print('*** showing units : quants-per ***')
    for k, v in breaker.timeunits.viewitems():
        print('unit name = {:6} has {:12} base-unit'.format(k, v))
    print ('*** end of unit view *** \n')
    print('sample unit breakdown : {}'.format(", ".join(breaker.breakdown(sample_quant))))
    print('\n **')
    sample_d = breaker.timebetween(1000000000, sample_quant)
    for k, v in sample_d.viewitems():
        print ('{:10} : {:5}'.format(k, v))
