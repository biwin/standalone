# -*- coding: utf-8 -*-
"""
Copyright 2018 Biwin John Joseph

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import os
import django


def run(settings_module, path=None):
    if path:
        sys.path.append(path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    django.setup()
