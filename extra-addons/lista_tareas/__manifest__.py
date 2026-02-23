# -*- coding: utf-8 -*-
{
    'name': 'Lista de Tareas Profesionales',
    'summary': 'Gestión de tareas diarias con priorización automática.',
    'description': """
        Módulo de gestión de tareas desarrollado para la Práctica 3.
        Incluye:
        - Modelo de datos para tareas.
        - Cálculo automático de urgencia basado en prioridad.
        - (Mejora) Vistas optimizadas y campos adicionales.
    """,
    'author': 'Rafael Núñez Pedrosa',
    'website': 'https://github.com/rafaAuEs/Tere_practica_3_01.git',
    'category': 'Productivity',
    'version': '1.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}