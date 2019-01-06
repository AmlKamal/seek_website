# -*- coding: utf-8 -*-
{
    'name': "seek website",

    'summary': """
       Job seeking Website""",

    'description': """
        
    """,

    'author': "Aml Kamal",
    'website': "amlbabikir@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website_form'],

    # always loaded
    'data': [
        
        'views/kanban.xml',
        'views/templates.xml',
        'data/config_data.xml',
       
    ],
    # only loaded in demonstration mode
    # 'demo': [
    # ],
}
