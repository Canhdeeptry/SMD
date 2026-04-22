from pathlib import Path

from smd.app_injector.sls import SLSManager
from smd.steam_client import SteamInfoProvider


def test_add_id():
    # Steam path only used in DLC Checking
    sls = SLSManager(Path(r"C:\GAMES\Steam"), SteamInfoProvider())
    sls.add_ids([123])
