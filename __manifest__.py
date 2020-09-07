# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Gestion de formation',
    'version': '0.1',
    'author': 'Nour',
    'category': 'premier module',
    'description': "Ceci est mon premier module du tp n_3",
    'depends': ['project'],
    'installable': True,
    'application': True,
    'data': [
             'security/ir.model.access.csv',
             'security/users.xml',
             'views/formateur.xml',
             'views/formation.xml',
             'wizard/wizard_attestation.xml',
             'views/session.xml',
             'views/salle.xml',
             'views/candidat.xml',
             'report/attestation_report.xml',
             'views/attestation.xml'
             ],
    
}
