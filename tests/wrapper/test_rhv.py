import unittest
try:
    # Python3
    from unittest.mock import patch
except ImportError:
    # Python2
    from mock import patch

import virt_v2v_wrapper as wrapper


class TestRHV(unittest.TestCase):
    """ Test specific to RHV """

    @patch('os.path.isfile', new=lambda _: True)
    def test_tools_iso_ordering(self):
        self.assertEqual(
                b'virtio-win-123.iso',
                wrapper.filter_iso_names(b'/', [
                    b'a.iso',
                    b'virtio-win-123.iso',
                    b'b.iso',
                    ]))
        self.assertEqual(
                b'RHEV-toolsSetup_123.iso',
                wrapper.filter_iso_names(b'/', [
                    b'RHEV-toolsSetup_123.iso',
                    b'virtio-win-123.iso',
                    ]))
        self.assertEqual(
                b'RHEV-toolsSetup_123.iso',
                wrapper.filter_iso_names(b'/', [
                    b'virtio-win-123.iso',
                    b'RHEV-toolsSetup_123.iso',
                    ]))
        self.assertEqual(
                b'RHEV-toolsSetup_234.iso',
                wrapper.filter_iso_names(b'/', [
                    b'RHEV-toolsSetup_123.iso',
                    b'virtio-win-123.iso',
                    b'RHEV-toolsSetup_234.iso',
                    ]))
        self.assertEqual(
                b'RHEV-toolsSetup_234.iso',
                wrapper.filter_iso_names(b'/', [
                    b'RHEV-toolsSetup_234.iso',
                    b'virtio-win-123.iso',
                    b'RHEV-toolsSetup_123.iso',
                    ]))
