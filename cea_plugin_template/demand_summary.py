"""
Creates a simple summary of the demand totals from the cea demand script.

NOTE: This is an example of how to structure a cea plugin script. It is intentionally simplistic to avoid distraction.
"""
from __future__ import division
from __future__ import print_function

import cea_plugin_template
import cea.config
import cea.inputlocator

__author__ = "Daren Thomas"
__copyright__ = "Copyright 2020, Architecture and Building Systems - ETH Zurich"
__credits__ = ["Daren Thomas"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Daren Thomas"
__email__ = "cea@arch.ethz.ch"
__status__ = "Production"


def summarize(total_demand_df):
    """
    Return only the following fields from the Total_demand.csv file:
    - Name (Unique building ID)
    - GFA_m2 (Gross floor area)
    - QC_sys_MWhyr (Total system cooling demand)
    - QH_sys_MWhyr (Total building heating demand)
    """
    return total_demand_df[["Name", "GFA_m2", "QC_sys_MWhyr", "QH_sys_MWhyr"]]


def main(config):
    """
    This is the main entry point to your script. Any parameters used by your script must be present in the ``config``
    parameter. The CLI will call this ``main`` function passing in a ``config`` object after adjusting the configuration
    to reflect parameters passed on the command line / user interface

    :param cea.config.Configuration config: The configuration for this script, restricted to the scripts parameters.
    :return: None
    """
    locator = cea.inputlocator.InputLocator(config.scenario, config.plugins)
    summary_df = summarize(locator.get_total_demand.read())
    locator.demand_summary.write(summary_df)


if __name__ == '__main__':
    main(cea.config.Configuration())
