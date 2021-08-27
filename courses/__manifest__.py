# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Courses",
    'summary': "Allows to create Course detail",
    'description': """Allows to link forum on a course""",
    'version': '1.0',
    'depends': ['base', 'auth_totp', 'contacts'],

    'data': [
        
        'views/course_view.xml',
        'views/room_view.xml',
        'views/lesson_view.xml',
        'views/attendee_view.xml',
        'views/instructor_view.xml',
        'views/contact_view.xml',
        'report/course_report.xml',
        'report/course_report_templates.xml',
        'security/course_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'installable': True,
    'application': True
}
