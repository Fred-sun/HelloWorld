import os, pytest, sys
import scenario_config

if scenario_config.is_local:
    sys.path.append(os.path.join(os.getcwd(), "CMD-Test-Shared/community/Modules"))

from common.common import *
from common.log_utils import LogLevel, LogUtils
from common.args_parser import *


if __name__ == "__main__":
    logUtils = LogUtils()
    logUtils.print(
        LogLevel.INFO, f'>>> Run this case with "{get_browserType()}" browser'
    )

    test_case_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "test_case"
    )
    if scenario_config.is_local:
        test_case_file = os.path.join(test_case_DIR, "test-bulk-power-off.py")
    else:
        test_case_file = os.path.join(test_case_DIR, "test-" + get_case_name() + ".py")

    pytest.main([test_case_file])
