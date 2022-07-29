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

"""
Routines for configuring cocoa
"""
import sys

from oslo_config import cfg
from oslo_db import options as db_options
from oslo_log import log as logging
from cocoa import version

LOG = logging.getLogger(__name__)

EXTRA_LOG_LEVEL_DEFAULTS = []

# Register the configuration options
# TODO

# Ensure that the control exchange is set correctly
_SQL_CONNECTION_DEFAULT = 'sqlite:///.cocoa.db'
# Update the default QueuePool parameters. These can be tweaked by the
# configuration variables - max_pool_size, max_overflow and pool_timeout
db_options.set_defaults(cfg.CONF, connection=_SQL_CONNECTION_DEFAULT,
                        max_pool_size=10, max_overflow=20, pool_timeout=10)


def register_cli_opts():
    logging.register_options(cfg.CONF)


def init(args, **kwargs):
    register_cli_opts()
    cfg.CONF(args=args, project='cocoa',
             version='%%prog %s' % version.version_info.release_string(),
             **kwargs)


def setup_logging(conf):
    """Sets up the logging options for a log with supplied name.

    :param conf: a cfg.ConfOpts object
    """
    logging.set_defaults(default_log_levels=logging.get_default_log_levels() +
                         EXTRA_LOG_LEVEL_DEFAULTS)
    product_name = "cocoa"
    logging.setup(conf, product_name)
    LOG.info("Logging enabled!")
    LOG.info("%(prog)s version %(version)s",
             {'prog': sys.argv[0],
              'version': version.version_info.release_string()})
    LOG.debug("command line: %s", " ".join(sys.argv))
