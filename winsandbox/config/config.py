from dataclasses import dataclass
from typing import Optional, List

@dataclass
class SandboxConfig:
    folder_mappers: Optional[List] = None
    networking: bool = True
    logon_script: Optional[str] = None
    virtual_gpu: bool = True
    memory_mb: Optional[int] = None
