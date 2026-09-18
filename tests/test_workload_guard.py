import unittest
from src.workload_guard import Workload,admit
class T(unittest.TestCase):
 def w(self,**k):
  d=dict(image_pinned=True,tenant_isolated=True,data_access_scoped=True,backup_ready=True,health_ratio=1);d.update(k);return Workload(**d)
 def test_allow(self):self.assertTrue(admit(self.w())[0])
 def test_block_tenant(self):self.assertIn('tenant-isolation-missing',admit(self.w(tenant_isolated=False))[1])
 def test_block_data(self):self.assertFalse(admit(self.w(data_access_scoped=False))[0])
