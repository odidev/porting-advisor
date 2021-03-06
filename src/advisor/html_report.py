"""
Copyright 2017 Arm Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

SPDX-License-Identifier: Apache-2.0
"""

from jinja2 import Environment, PackageLoader
from .report import Report
import os


class HtmlReport(Report):
    """Generates an HTML report from a template."""

    def write_items(self, output_file, items):
        env = Environment(
            loader=PackageLoader('advisor', 'templates'),
            autoescape=True
        )
        template = env.get_template('advice.html')
        rendered = template.render(
            root_directory=self.root_directory,
            root_directory_basename=os.path.basename(self.root_directory),
            items=items)
        output_file.write(rendered)
