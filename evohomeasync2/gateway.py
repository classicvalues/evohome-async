#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
"""Provide handling of a gateway."""
from .controlsystem import ControlSystem


class Gateway(object):
    """Provide handling of a gateway."""

    def __init__(self, client, location, data=None):
        """Initialise the class."""
        self.client = client
        self.location = location
        self._control_systems = []
        self.control_systems = {}

        if data is not None:
            self.__dict__.update(data["gatewayInfo"])

            for cs_data in data["temperatureControlSystems"]:
                control_system = ControlSystem(client, location, self, cs_data)
                self._control_systems.append(control_system)
                self.control_systems[control_system.systemId] = control_system
