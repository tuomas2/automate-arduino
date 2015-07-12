# -*- coding: utf-8 -*-
# (c) 2015 Tuomas Airaksinen
#
# This file is part of automate-arduino.
#
# automate-arduino is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# automate-arduino is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with automate-arduino.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Tuomas Airaksinen"
__copyright__ = "Copyright 2015, Tuomas Airaksinen"
__credits__ = []
__license__ = "GPL"
__version__ = '0.9.2'
__maintainer__ = "Tuomas Airaksinen"
__email__ = "tuomas.airaksinen@gmail.com"
__status__ = "Beta"

from .arduino_service import ArduinoService
from .arduino_actuators import ArduinoDigitalActuator, ArduinoPWMActuator, ArduinoServoActuator, AbstractArduinoActuator
from .arduino_sensors import ArduinoAnalogSensor, ArduinoDigitalSensor, AbstractArduinoSensor

extension_classes = [ArduinoService, ArduinoDigitalActuator, ArduinoPWMActuator, ArduinoServoActuator, AbstractArduinoActuator,
                     ArduinoAnalogSensor, ArduinoDigitalSensor, AbstractArduinoSensor, ]
