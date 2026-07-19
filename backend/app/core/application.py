from app.services.service_manager import ServiceManager
from app.events.event_bus import EventBus


service_manager = ServiceManager()

event_bus = EventBus()

initialized = False