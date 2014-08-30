#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyLastKernel
# ===========
# checks the lastest stable Linux kernel version
# warnings if new version appears
#
# psz, 2014, <pawel (at) szulczewski (dot) org>
# GNU/GPL v3+

import json
import urllib2
import os

__LASTVERFILE = os.path.expanduser("~") + "/.lastkernel"

def get_latest_ver_site ():
    kernel_json_file = urllib2.urlopen ('https://www.kernel.org/releases.json')
    kernel_json = kernel_json_file.read()

    json_data = json.loads (kernel_json)
    return json_data ['latest_stable']['version']

def get_latest_ver_file (_file):
    if os.path.isfile(_file):
        with open(_file, 'r') as f:
            last_ver = f.readline()
        f.close()
        return last_ver
    else:
         return ''

def write_latest_ver_file (_file, _ver):
    with open(_file, 'w') as f:
        f.write(_ver)
    f.close()

def main ():
    last_f_site = get_latest_ver_site()
    last_f_file = get_latest_ver_file(__LASTVERFILE)
    if (last_f_file != last_f_site):        
        print "\nBREAKING NEWS! New kernel: {0}\n".format(last_f_site)
        write_latest_ver_file(__LASTVERFILE, last_f_site)
    else:
        print "\nKernel: {0}\n".format(last_f_site)

if __name__ == "__main__" :
    main ()
