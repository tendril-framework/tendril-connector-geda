#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) 2019 Chintalagiri Shashank
#
# This file is part of tendril.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
gEDA Symbol Generator Schema
----------------------------
"""

from decimal import Decimal
from tendril.schema.edasymbols import EDASymbolGeneratorBase


class GSymGeneratorFile(EDASymbolGeneratorBase):
    legacy_schema_name = 'gsymgenerator'
    supports_schema_name = 'gEDASymbolGenerator'
    supports_schema_version_max = Decimal('1.0')
    supports_schema_version_min = Decimal('1.0')

    def __init__(self, genpath):
        self._sympath = genpath.replace('.gen.yaml', '.sym')
        super(GSymGeneratorFile, self).__init__(genpath)

    def symbol_template(self):
        from tendril.entities.edasymbols.geda import GedaSymbol
        return GedaSymbol(self._sympath)


def load(manager):
    manager.load_schema('gEDASymbolGenerator', GSymGeneratorFile,
                        doc="Schema for Tendril "
                            "gEDA Symbol Generator Files")
