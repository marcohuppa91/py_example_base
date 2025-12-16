from hydra import initialize, compose
from hydra.core.global_hydra import GlobalHydra
from omegaconf import open_dict
from pathlib import Path
import os

initialize(config_path="../test_config/", version_base=None)
config = compose(config_name="config")
GlobalHydra.instance().clear()

root = str(Path(__file__).resolve().parent.parent.parent) + os.sep
with open_dict(config):
    config["root"] = root
