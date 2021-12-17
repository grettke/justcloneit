#!/usr/bin/env python
"""Clone and move an object"""

import inkex

class JustCloneIt(inkex.TextExtension):
    """To upper case"""
    def process_chardata(self, text):
        return text

if __name__ == '__main__':
    JustCloneIt().run()
