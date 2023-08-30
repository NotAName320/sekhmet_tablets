"""
Generates tablet infocards for the Sekhmet Legion
Copyright (C) 2023 Nota

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from enum import Enum
import json
import os
import sys


class Ranks(Enum):
    JONDI = 0x005600
    MOSAID = 0x00FF00
    RAID = 0x00FFFF
    LIWAA = 0x8BB8E7
    FARIQ = 0x3498DB
    DEPUTYMOSHIR = 0xE148FA
    MOSHIR = 0xE31C79


def generate_template():
    default_template = {
        'name': 'name',
        'title': 'the awesome title',
        'rank': 'jondi',
        'image': 'defaultimage.png'
    }


if __name__ == '__main__':
    print('Starting template...')
    if not os.path.isfile('template.json'):
        print('No template file found! Generating...', file=sys.stderr)
        generate_template()
        print('Tempalte generated! Fill it out now.', file=sys.stderr)
        exit(1)
