from unittest import TestCase

from wifi.scan import Cell
from wifi import subprocess_compat as subprocess
from mock import patch
from test_parsing import IWLIST_SCAN_WEP, IWLIST_SCAN_WPA2


expected_output = '\n'.join([IWLIST_SCAN_WEP, IWLIST_SCAN_WPA2])

class ScanTest(TestCase):
    def test_all_calls_check_output_with_good_args(self):
        args = ['/sbin/iwlist', 'interface', 'scan']
        kwargs = {'stderr':subprocess.STDOUT}
        with patch.object(subprocess, 'check_output',
        return_value=expected_output):
	    Cell.all('interface')
            subprocess.check_output.assert_called_with(args, **kwargs)
            args.insert(0, 'sudo')
            Cell.all('interface', sudo=True)
            subprocess.check_output.assert_called_with(args, **kwargs)

