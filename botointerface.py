#!/usr/bin/env python

"""botointerface.py: docstring"""

__author__ = 'thomas'
__creation_date__ = '23.09.18'

import boto3

import python_general.library.configreader


class BotoInterface(python_general.library.configreader.ConfigReader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = self.config.get('botointerface')
        self.rekognition = self.setup_service('rekognition')
        self.translate = self.setup_service('translate')
        self.log.info('Init done')

    def setup_service(self, service_name=None):
        if not service_name:
            raise NameError('Service name must be given')
        self.log.info('Setting up {} service for region: {}'.format(service_name, self.config.get('region')))
        return boto3.client('{}'.format(service_name), self.config.get('region'),
                            aws_access_key_id=self.config.get('aws_access_key_id'),
                            aws_secret_access_key=self.config.get('aws_secret_access_key'))


if __name__ == '__main__':
    bi = BotoInterface(config_file='config/basic_config.yml', loglevel='DEBUG')
    print(bi.config)