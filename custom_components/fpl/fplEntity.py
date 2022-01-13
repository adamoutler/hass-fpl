"""BlueprintEntity class"""
from homeassistant.components.sensor import SensorEntity, STATE_CLASS_MEASUREMENT
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from homeassistant.const import (
    CURRENCY_DOLLAR,
    DEVICE_CLASS_ENERGY,
    ENERGY_KILO_WATT_HOUR,
    DEVICE_CLASS_MONETARY,
    DEVICE_CLASS_TIMESTAMP,
)

from datetime import datetime, timedelta
from .const import DOMAIN, VERSION, ATTRIBUTION


class FplEntity(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, config_entry, account, sensorName):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.account = account
        self.sensorName = sensorName

    @property
    def unique_id(self):
        """Return the ID of this device."""
        id = "{}{}{}".format(
            DOMAIN, self.account, self.sensorName.lower().replace(" ", "")
        )
        return id

    @property
    def name(self):
        return f"{DOMAIN.upper()} {self.account} {self.sensorName}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.account)},
            "name": f"Account {self.account}",
            "model": VERSION,
            "manufacturer": "Florida Power & Light",
        }

    def defineAttributes(self):
        return {}

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        attributes = {
            "attribution": ATTRIBUTION,
            "integration": "FPL",
        }
        attributes.update(self.defineAttributes())
        return attributes

    def getData(self, field):
        return self.coordinator.data.get(self.account).get(field)


class FplEnergyEntity(FplEntity):
    def __init__(self, coordinator, config_entry, account, sensorName):
        super().__init__(coordinator, config_entry, account, sensorName)

    @property
    def state_class(self) -> str:
        """Return the state class of this entity, from STATE_CLASSES, if any."""

        return STATE_CLASS_MEASUREMENT

    @property
    def last_reset(self) -> datetime:
        """Return the time when the sensor was last reset, if any."""

        today = datetime.today()
        yesterday = today - timedelta(days=1)
        return datetime.combine(yesterday, datetime.min.time())

    @property
    def device_class(self) -> str:
        """Return the class of this device, from component DEVICE_CLASSES."""
        return DEVICE_CLASS_ENERGY

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement of this entity, if any."""
        return ENERGY_KILO_WATT_HOUR

    @property
    def icon(self):
        return "mdi:flash"


class FplMoneyEntity(FplEntity):
    def __init__(self, coordinator, config_entry, account, sensorName):
        super().__init__(coordinator, config_entry, account, sensorName)

    @property
    def icon(self):
        return "mdi:currency-usd"

    @property
    def device_class(self) -> str:
        """Return the class of this device, from component DEVICE_CLASSES."""
        return DEVICE_CLASS_MONETARY

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement of this entity, if any."""
        return CURRENCY_DOLLAR


class FplDateEntity(FplEntity):
    def __init__(self, coordinator, config_entry, account, sensorName):
        super().__init__(coordinator, config_entry, account, sensorName)

    # @property
    # def device_class(self) -> str:
    #    """Return the class of this device, from component DEVICE_CLASSES."""
    #    return DEVICE_CLASS_TIMESTAMP

    @property
    def icon(self):
        return "mdi:calendar"