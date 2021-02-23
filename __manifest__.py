# -*- coding: utf-8 -*-
{
    'name': "moduloprueba",

    'description': """
        Long description of module's purpose
    """,

    'author': "Monica",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
    ],
}