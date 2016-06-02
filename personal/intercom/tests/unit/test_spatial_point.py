# -*- coding: utf-8 -*-

import core
import unittest

from core.spatial_point import SpatialPoint
from nose.tools import istest

class SpatialPointTest(unittest.TestCase):

	@istest
	def it_creates_a_spatial_point(self):
		data = [
			(53.2451022, -6.238335, "Spatial Point")
		]

		for latitude, longitude, description in data:
			customer = CustomerSpatial(latitude, longitude, description)

			eq_(user_id, customer.user_id)
			eq_(name, customer.name)
			eq_(latitude, customer.latitude)
			eq_(longitude, customer.longitude)