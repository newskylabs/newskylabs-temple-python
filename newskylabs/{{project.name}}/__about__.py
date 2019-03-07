## =========================================================
## {{ copyright }}
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##      http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## ---------------------------------------------------------

## =========================================================
## Package metadata
## ---------------------------------------------------------

__all__ = [
    '__package_name__',
    '__version__',
    '__status__',
    '__description__',
    '__author__',
    '__authors__',
    '__maintainer__',
    '__email__',
    '__contact__',
    '__copyright__',
    '__url__',
    '__license__',
    '__date__',
]

__package_name__ = '{{ project.name }}'
__version__      = '{{ version }}'
__status__       = '{{ status }}'
__description__  = '{{ company }} {{ project.language }} project {}'.format(__package_name__)
__author__       = '{{ author.name }}'
__authors__      = [__author__]
__maintainer__   = __author__
__email__        = '{{ author.email }}'
__contact__      = __email__
__copyright__    = 'Copyright {{ datetime.year }} {}'.format(__author__)
__url__          = 'http://newskylabs.net/python/packages/{}'.format(__package_name__)
__license__      = '{{ license }}'
__date__         = '{{ date }}'

## =========================================================
## =========================================================

## fin.
