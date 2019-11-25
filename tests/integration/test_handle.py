# vim:ts=4:sw=4:et:
# Copyright 2019-present Microsoft Corporation.
# Licensed under the Apache License, Version 2.0

from __future__ import absolute_import, division, print_function

import os
import sys

import WatchmanTestCase


@WatchmanTestCase.expand_matrix
class TestHandles(WatchmanTestCase.WatchmanTestCase):
    def checkOSApplicability(self):
        if sys.platform != "win32":
            self.skipTest("N/A unless Windows")

    def test_handles(self):

        root = self.mkdtemp()
        self.watchmanCommand("watch", root)
        self.touchRelative(root, "file")
        self.watchmanCommand("watch-del", root)
        os.rmdir(root)
        self.assertFalse(os.path.isdir("root"))