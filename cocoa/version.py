# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pbr.version

COCOA_VENDOR = "OpenLAN Network Solutions"
COCOA_PRODUCT = "cocoa"

version_info = pbr.version.VersionInfo('cocoa')


def vendor_string():
    return COCOA_VENDOR


def product_string():
    return COCOA_PRODUCT


def version_string_with_package():
    return version_info.version_string()
