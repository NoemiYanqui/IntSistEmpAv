# -*- coding: utf-8 -*-
{
    'name': 'Facturacion',
    'version': '1.0',
    'summary': 'Modulo basico para Facturacion Peru',
    'description': """
Core mechanics for the accounting modules .To display the menuitems, install the module fgsgsdgsd account_invoicing.
""",
    'depends': [
        "account",
    ],
    'data': [
        'data/series.xml',
        'data/documentos.xml',
        'views/series_view.xml',
        'views/documentos_view.xml',  
        'views/account_invoice_view.xml',
        'views/res_partner_view.xml', 
    ]
}
