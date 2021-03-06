#!/usr/bin/env python
# -*- coding: utf-8 -*-

from girder import events


API_VERSION = '1.1'


class PluginSettings:
    CULLING_PERIOD = 'ythub.culling_period'
    CULLING_FREQUENCY = 'ythub.culling_frequency'
    TMPNB_URL = 'ythub.tmpnb_internal_url'
    REDIRECT_URL = 'ythub.tmpnb_redirect_url'
    HUB_PRIV_KEY = 'ythub.priv_key'
    HUB_PUB_KEY = 'ythub.pub_key'


# Constants representing the setting keys for this plugin
class NotebookStatus(object):
    STARTING = 0
    RUNNING = 1
    ERROR = 2

    @staticmethod
    def isValid(status):
        event = events.trigger('notebook.status.validate', info=status)

        if event.defaultPrevented and len(event.responses):
            return event.responses[-1]

        return status in (NotebookStatus.STARTING, NotebookStatus.RUNNING,
                          NotebookStatus.ERROR)
