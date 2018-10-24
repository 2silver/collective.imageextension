# -*- coding: utf-8 -*-
# Standard Library
import logging

# Plone
from zope.annotation.interfaces import IAnnotations

# Package
from .utils import get_dominant_color
from .utils import get_ratio


logger = logging.getLogger(__name__)

KEY = 'collective.imageextension'


def add_image_attributes(obj, event):
    """Index the object when it is added/modified to the conversation.
    """
    annotations = IAnnotations(obj, None)
    if annotations is None:
        return None

    image = obj.image
    d = {
        'dominant_color': get_dominant_color(image),
        'ratio_percent': get_ratio(image)
    }

    annotations[KEY] = d


def remove_image_attributes(obj, event):
    """Unindex the object when it is removed from the conversation.
    """
    annotations = IAnnotations(obj, None)
    if annotations is None:
        return None

    if annotations.has_key(KEY):
        del annotations[KEY]
    return None


def update_image_attributes(obj, event):
    """Unindex the object when it is removed from the conversation.
    """
    annotations = IAnnotations(obj, None)
    if annotations is None:
        return None

    image = obj.image
    d = {
        'dominant_color': get_dominant_color(image),
        'ratio_percent': get_ratio(image)
    }

    annotations[KEY] = d
    return None
