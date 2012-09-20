# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tempfile

import pytest
import dawg_python

from .utils import data_path

def test_c_dawg_contains():
    dawg = pytest.importorskip("dawg") #import dawg
    bin_dawg = dawg.IntDAWG({'foo': 1, 'bar': 2, 'foobar': 3})

    d = dawg_python.Dictionary()

    fd, path = tempfile.mkstemp()
    bin_dawg.save(path)

    with open(path, 'rb') as f:
        d.read(f)

    assert d.contains(b'foo')
    assert not d.contains(b'x')
    assert d.contains(b'foobar')
    assert d.contains(b'bar')

#class TestIntDAWG(object):
#
#    def dawg(self):
#        payload = {'foo': 1, 'bar': 5, 'foobar': 3}
#        d = dawg.IntDAWG(payload)
#        return payload, d
#
#    def test_getitem(self):
#        payload, d = self.dawg()
#        for key in payload:
#            assert d[key] == payload[key]
#
#        with pytest.raises(KeyError):
#            d['fo']
#
#
#    def test_dumps_loads(self):
#        payload, d = self.dawg()
#        data = d.tobytes()
#
#        d2 = dawg.IntDAWG()
#        d2.frombytes(data)
#        for key, value in payload.items():
#            assert key in d2
#            assert d2[key] == value
#
#    def test_dump_load(self):
#        payload, _ = self.dawg()
#
#        buf = BytesIO()
#        dawg.IntDAWG(payload).write(buf)
#        buf.seek(0)
#
#        d = dawg.IntDAWG()
#        d.read(buf)
#
#        for key, value in payload.items():
#            assert key in d
#            assert d[key] == value
#
#    def test_pickling(self):
#        payload, d = self.dawg()
#
#        data = pickle.dumps(d)
#        d2 = pickle.loads(data)
#
#        for key, value in payload.items():
#            assert key in d2
#            assert d[key] == value
#
#    def test_int_value_ranges(self):
#        for val in [0, 5, 2**16-1, 2**31-1]:
#            d = dawg.IntDAWG({'f': val})
#            assert d['f'] == val
#
#        with pytest.raises(ValueError):
#            dawg.IntDAWG({'f': -1})
#
#        with pytest.raises(OverflowError):
#            dawg.IntDAWG({'f': 2**32-1})
#
#
#class TestCompletionDAWG(object):
#    keys = ['f', 'bar', 'foo', 'foobar']
#
#    def dawg(self):
#        return dawg.CompletionDAWG(self.keys)
#
#    def test_completion(self):
#        keys, d = self.keys, self.dawg()
#        for key in keys:
#            assert key in d
#
#        assert d.keys('foo') == ['foo', 'foobar']
#        assert d.keys('b') == ['bar']
#        assert d.keys('z') == []
#
#    def test_completion_dawg_saveload(self):
#        buf = BytesIO()
#        dawg.CompletionDAWG(self.keys).write(buf)
#        buf.seek(0)
#
#        d = dawg.CompletionDAWG()
#        d.read(buf)
#
#        for key in self.keys:
#            assert key in d
#
#        assert d.keys('foo') == ['foo', 'foobar']
#        assert d.keys('b') == ['bar']
#        assert d.keys('z') == []
#
#    def test_no_segfaults_on_invalid_file(self):
#        d = self.dawg()
#        fd, path = tempfile.mkstemp()
#        with open(path, 'w') as f:
#            f.write('foo')
#
#        with pytest.raises(IOError) as e:
#            d.load(path)
#            assert "can't load _dawg.Dictionary" in e.args[0]
#
