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
        self.rekognition = self.setup_rekognition()
        self.log.info('Init done')

    def setup_rekognition(self):
        self.log.info('Setting up rekognition service for region: {}'.format(self.config.get('region')))
        return boto3.client('rekognition', self.config.get('region'),
                            aws_access_key_id=self.config.get('aws_access_key_id'),
                            aws_secret_access_key=self.config.get('aws_secret_access_key'))

    def setup_translate(self):
        pass



if __name__ == '__main__':
    bi = BotoInterface(config_file='config/basic_config.yml', loglevel='DEBUG')
    print(bi.config)