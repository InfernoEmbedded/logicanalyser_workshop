##
## This file is part of the libsigrokdecode project.
##
## Copyright (C) 2015 Uwe Hermann <uwe@hermann-uwe.de>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

from collections import OrderedDict

# OrderedDict which maps command IDs to their names and descriptions.
# Please keep this sorted by command ID.
# Don't forget to update 'Ann' in pd.py if you add/remove items here.
cmds = OrderedDict([
    (0x01, ('WRSR', 'Write status register')),
    (0x02, ('PP', 'Page program')),
    (0x03, ('READ', 'Read data')),
    (0x04, ('WRDI', 'Write disable')),
    (0x05, ('RDSR', 'Read status register')),
    (0x06, ('WREN', 'Write enable')),
    (0x0b, ('FAST/READ', 'Fast read data')),
    (0x20, ('SE', 'Sector erase')),
    (0x2b, ('RDSCUR', 'Read security register')),
    (0x2f, ('WRSCUR', 'Write security register')),
    (0x35, ('RDSR2', 'Read status register 2')),
    (0x60, ('CE', 'Chip erase')),
    (0x70, ('ESRY', 'Enable SO to output RY/BY#')),
    (0x80, ('DSRY', 'Disable SO to output RY/BY#')),
    (0x90, ('REMS', 'Read electronic manufacturer & device ID')),
    (0x9f, ('RDID', 'Read identification')),
    (0xab, ('RDP/RES', 'Release from deep powerdown / Read electronic ID')),
    (0xad, ('CP', 'Continuously program mode')),
    (0xb1, ('ENSO', 'Enter secured OTP')),
    (0xb9, ('DP', 'Deep power down')),
    (0xbb, ('2READ', '2x I/O read')), # a.k.a. "Fast read dual I/O".
    (0xc1, ('EXSO', 'Exit secured OTP')),
    (0xc7, ('CE2', 'Chip erase')), # Alternative command ID
    (0xd8, ('BE', 'Block erase')),
    (0xef, ('REMS2', 'Read ID for 2x I/O mode')),
])

device_name = {
    'fidelix': {
        0x15: 'FM25Q32',
    },
    'macronix': {
        0x14: 'MX25L1605D',
        0x15: 'MX25L3205D',
        0x16: 'MX25L6405D',
    },
}

chips = {
    # FIDELIX
    'fidelix_fm25q32': {
        'vendor': 'FIDELIX',
        'model': 'FM25Q32',
        'res_id': 0x15,
        'rems_id': 0xa115,
        'rems2_id': 0xa115,
        'rdid_id': 0xa14016,
        'page_size': 256,
        'sector_size': 4 * 1024,
        'block_size': 64 * 1024,
    },
    # Macronix
    'macronix_mx25l1605d': {
        'vendor': 'Macronix',
        'model': 'MX25L1605D',
        'res_id': 0x14,
        'rems_id': 0xc214,
        'rems2_id': 0xc214,
        'rdid_id': 0xc22015,
        'page_size': 256,
        'sector_size': 4 * 1024,
        'block_size': 64 * 1024,
    },
    'macronix_mx25l3205d': {
        'vendor': 'Macronix',
        'model': 'MX25L3205D',
        'res_id': 0x15,
        'rems_id': 0xc215,
        'rems2_id': 0xc215,
        'rdid_id': 0xc22016,
        'page_size': 256,
        'sector_size': 4 * 1024,
        'block_size': 64 * 1024,
    },
    'macronix_mx25l6405d': {
        'vendor': 'Macronix',
        'model': 'MX25L6405D',
        'res_id': 0x16,
        'rems_id': 0xc216,
        'rems2_id': 0xc216,
        'rdid_id': 0xc22017,
        'page_size': 256,
        'sector_size': 4 * 1024,
        'block_size': 64 * 1024,
    },
}
