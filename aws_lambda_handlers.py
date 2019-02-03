#!/usr/bin/env python

"""aws_lambda_handlers.py: docstring"""

__author__ = 'thomas'
__creation_date__ = '01.10.18'


def dummy_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'],
                                    event['last_name'])
    return {
        'message' : message
    }

