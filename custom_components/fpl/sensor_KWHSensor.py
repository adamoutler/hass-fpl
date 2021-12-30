from .fplEntity import FplEntity


class ProjectedKWHSensor(FplEntity):
    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Projected")

    @property
    def state(self):
        return self.getData("projectedKWH")

    @property
    def icon(self):
        return "mdi:flash"
    def defineAttributes(self):
        """Return the state attributes."""
        attributes = {}
        attributes["friendly_name"] = "Projected KWH"
        attributes["device_class"] = "energy"
        attributes["state_class"] = "total"
        attributes["unit_of_measurement"] = "kWh"
        return attributes

class DailyAverageKWHSensor(FplEntity):
    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Daily Average")

    @property
    def state(self):
        return self.getData("dailyAverageKWH")

    @property
    def icon(self):
        return "mdi:flash"

    def defineAttributes(self):
        """Return the state attributes."""
        attributes = {}
        attributes["friendly_name"] = "Daily Average"
        attributes["device_class"] = "energy"
        attributes["state_class"] = "total"
        attributes["unit_of_measurement"] = "kWh"
        return attributes

class BillToDateKWHSensor(FplEntity):
    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Bill To Date")

    @property
    def state(self):
        return self.getData("billToDateKWH")

    @property
    def icon(self):
        return "mdi:flash"

    def defineAttributes(self):
        """Return the state attributes."""
        attributes = {}
        attributes["friendly_name"] = "Billing Usage"
        attributes["device_class"] = "energy"
        attributes["state_class"] = "total_increasing"
        attributes["unit_of_measurement"] = "kWh"
        if self.getData("billStartDate") is not None:
            attributes["last_reset"] = self.getData("billStartDate")
        return attributes

class NetReceivedKWHSensor(FplEntity):
    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Received Reading")

    @property
    def state(self):
        try:
            return self.getData("recMtrReading")
        except:
            return None

    @property
    def icon(self):
        return "mdi:flash"

    def defineAttributes(self):
        """Return the state attributes."""
        attributes = {}
        attributes["friendly_name"] = "Meter Return to Grid"
        attributes["device_class"] = "energy"
        attributes["state_class"] = "total_increasing"
        attributes["unit_of_measurement"] = "kWh"
        if self.getData("billStartDate") is not None:
            attributes["last_reset"] = self.getData("billStartDate")

        return attributes

class NetDeliveredKWHSensor(FplEntity):
    def __init__(self, coordinator, config, account):
        super().__init__(coordinator, config, account, "Delivered Reading")

    @property
    def state(self):
        try:
            return self.getData("delMtrReading")
        except:
            try:
                return self.getData("billToDateKWH")
            except:
                return None

    @property
    def icon(self):
        return "mdi:flash"

    def defineAttributes(self):
        """Return the state attributes."""
        attributes = {}
        attributes["friendly_name"] = "Meter Consumption"
        attributes["device_class"] = "energy"
        attributes["state_class"] = "total_increasing"
        attributes["unit_of_measurement"] = "kWh"
        if self.getData("billStartDate") is not None:
            attributes["last_reset"] = self.getData("billStartDate")

        return attributes
