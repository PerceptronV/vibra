from __future__ import absolute_import, division, print_function, unicode_literals
import numpy as np
import os
import time
import tensorflow as tf
from tensorflow import keras

class file(object):
    def __init__ (self,filename,src,encoding='utf-8'):
        self.src=src
        self.filename=filename
        self.chars=None
        self.encoding = encoding
        self.file = keras.utils.get_file(self.filename, self.src)
        self.text = open(self.file, 'rb').read().decode(encoding=self.encoding)
        self.chars = sorted(set(self.text))
        self.char2idx={u:i for i, u in enumerate(self.chars)}
        self.idx2char=np.array(self.chars)
        self.text_as_int = np.array([self.char2idx[c] for c in self.text])
        self.len=len(self.text)
        self.char_size=len(self.chars)

    def text(self):
        return (self.text)

    def chars(self):
        return (self.chars)

    def char2idx(self):
        return (self.char2idx)

    def idx2char(self):
        return (self.idx2char)

    def text_as_int(self):
        return (self.text_as_int)

    def len(self):
        return (self.len)

    def char_size(self):
        return (self.char_size)