from pathlib import Path
import yaml


class ConfigLoader:

    def __init__(self):
        self.base_path = Path(__file__).resolve().parents[3] / "config"

    def load(self, filename):

        path = self.base_path / filename

        with open(path, "r") as file:
            return yaml.safe_load(file)