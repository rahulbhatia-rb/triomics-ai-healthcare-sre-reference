from dataclasses import dataclass
@dataclass(frozen=True)
class Workload:
 image_pinned: bool; tenant_isolated: bool; data_access_scoped: bool; backup_ready: bool; health_ratio: float
def admit(w:Workload)->tuple[bool,tuple[str,...]]:
 b=[]
 if not w.image_pinned:b.append('image-mutable')
 if not w.tenant_isolated:b.append('tenant-isolation-missing')
 if not w.data_access_scoped:b.append('data-access-unscoped')
 if not w.backup_ready:b.append('recovery-unready')
 if w.health_ratio<.99:b.append('workloads-unhealthy')
 return not b,tuple(b)
