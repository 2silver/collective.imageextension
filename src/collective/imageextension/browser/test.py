# -*- coding: utf-8 -*-
from time import time
from App.class_init import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import interface
from plone import api
from Products.statusmessages.interfaces import IStatusMessage
from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.annotation.interfaces import IAnnotations

import logging
logger = logging.getLogger(__name__)


class Test(BrowserView):

    """ """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        annotations = IAnnotations(self.context, None)
        print annotations
        # return self.template()