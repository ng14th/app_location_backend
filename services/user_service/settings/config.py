# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path
try:
    import core
except ModuleNotFoundError:
    current_path = Path(os.getcwd())
    sys.path.append(str(current_path.parents[1]))

from typing import Optional
from core.settings.base_settings_mixin import BaseSettingMixin

env_path = os.path.join(os.path.dirname(__file__), '..', 'envs')
class AppEnvConfig(BaseSettingMixin):
    
    #-------- PROJECT ------------
    PROJECT_NAME : Optional[str] = ""
    SERVICE_PATH : Optional[str] = ""
    SERVICE_HOST : Optional[str] = ""
    SERVICE_PORT : int = 8888
    SECRET_KEY : str = "nguyennt63"
    SECURITY_ALGORITHM : str = 'HS256'
                    
    class Config:
        case_sensitive = True
        validate_assignment = True

settings = AppEnvConfig.set_up(env_path=env_path)    
if __name__ == "__main__":
    pass