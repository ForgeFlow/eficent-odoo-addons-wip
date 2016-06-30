# -*- coding: utf-8 -*-
# © 2014 Alexis de Lattre <alexis.delattre@akretion.com>
# © 2014 Lorenzo Battistini <lorenzo.battistini@agilebg.com>
# © 2016 Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Base Location Geonames Import',
    'version': '9.0.1.0.0',
    'category': 'Partner Management',
    'license': 'AGPL-3',
    'summary': 'Import better zip entries from Geonames',
    'author': 'Akretion,'
              'Agile Business Group,'
              'Antiun Ingeniería S.L.,'
              'Tecnativa,'
              'Odoo Community Association (OCA)',
              'Eficent Business and IT Consulting Services S.L.'
    'website': 'http://www.akretion.com',
    'depends': ['base_location'],
    'external_dependencies': {'python': ['requests', 'unicodecsv']},
    'data': [
        'wizard/geonames_import_view.xml',
        ],
    'installable': True,
}
