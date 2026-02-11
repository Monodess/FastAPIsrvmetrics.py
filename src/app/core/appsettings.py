"""
Pagespeed configuration module
This script handles loading of .env variables
using Pydantic Settings
"""

from icecream import ic
from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pathlib import Path

#setting main root
__BASE_PATH__ = Path(__file__).resolve().parent.parent.parent
__ENV_PATH__ = __BASE_PATH__/".env"

class Configuration(BaseSettings):
    PAGESPEED_API_KEY: str
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=__ENV_PATH__,      #pydantic is case-insensitive
        env_file_encoding='utf-8',
        extra='ignore',             #other fields in .env ignored
    )

appsettings= Configuration()


if __name__ == '__main__':
    if os.path.exists(__ENV_PATH__):
        ic("file exists")
        ic(os.path.isfile(__ENV_PATH__))
    ic(appsettings.PAGESPEED_API_KEY)

    # PROB: putting settings in app created a problem:
# 1) data capturer seeks env_file in wrong dir what is not right (dir [env_file="../.env"])
# SOLV: implicit set base dir (projects root) and go from there to env
