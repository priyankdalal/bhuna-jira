#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 23:10:42 2018

@author: priyank
"""
import sys
sys.path.insert(0, '/path/to/application/app/folder')
import loggging as log
import JiraHttp

class JiraRemoteHelper:
    def fetch_projects(self):
        path="/rest/api/2/project"