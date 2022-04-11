##!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Generate secret key 

from django.core.management import utils 

print(utils.get_random_secret_key())