# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """  
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Htet Myat",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'hospital',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'product'],

    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
    ],
    'sequence': '-1',

}
