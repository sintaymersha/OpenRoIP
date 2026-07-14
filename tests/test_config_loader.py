from app.config.config_loader import ConfigLoader

loader = ConfigLoader()

print(loader.load("system.yaml"))
print(loader.load("network.yaml"))