import os, scenario_config
from common.args_parser import *
from common.common import get_test_result_metric, retrive_data
from common.env_config import Portal, LoginMethod
from common.playwright_helper import PlayWrightHelper
from common.log_utils import LogLevel, LogUtils
from common.common_page_operator import CommonPageOperator
from page_operator.bulk_power_operator import BulkPowerOperator

logger = LogUtils()
helperHandle = PlayWrightHelper()
device = "CPC-fredb-ZIIUE"


class TestBulkPowerOff:
    """Bulk Power Off Case"""

    def init_page_opr(self, env, certname):
        self.browser = helperHandle.get_browser(get_browserType())
        self.commonPageOperator = CommonPageOperator(env)
        self.BulkPowerOperator = BulkPowerOperator(self.browser)
        self.commonPageOperator.install_cert(certname)

    def step_01(self, user_name):
        msg = "Step_01: Login MEM Portal with bvt_admin account"
        logger.print(LogLevel.INFO, msg)
        self.commonPageOperator.login(self.browser, Portal.MEM, user_name)
        self.commonPageOperator.goto_blade(self.browser, "Devices", "All devices")

    def step_02(self):
        logger.print(LogLevel.INFO, "step_02: Confirm the Front cloud PC is Power On")
        self.BulkPowerOperator.confirm_device_power_off_state(
            device, expected_state="On"
        )

    def step_03(self):
        logger.print(LogLevel.INFO, "step_03: Bulk device actions - Power Off")
        self.BulkPowerOperator.bulk_device_power_on(device, expected_state="Off")

    def step_04(self):
        logger.print(LogLevel.INFO, "step_04: Verify the Front cloud PC is Power Off")
        self.BulkPowerOperator.verify_devices_power_state(device, expected_state="Off")

    def step_05(self):
        logger.print(LogLevel.INFO, "step_05: Power on the Front cloud PC")
        self.BulkPowerOperator.power_on_devices(device)

    def test_bulk_power_on(self):
        logger.print(LogLevel.INFO, "Start bulk power on test")
        try:
            data_set = retrive_data()
            user = data_set[0]
            self.user_passwd = user["Password"]
            test_result_metrics = get_test_result_metric(
                user["Environment"],
                user["ScaleUnit"],
                scenario_config.scenarioName,
                LoginMethod.CBA.value,
            )
            logUtils.print(
                LogLevel.INFO,
                f'Case:test_bulk_power_on login with CBA. Username={user["UserPrincipalName"]}, workflowId={os.environ.get("WORKFLOW_ID")}',
            )
            # Common Setting
            self.init_page_opr(user["Environment"], user["UserPrincipalName"])
            self.step_01(user["UserPrincipalName"])
            self.step_02()
            self.step_03()
            self.step_04()
            self.step_05()

            if test_result_metrics is not None:
                test_result_metrics.successed()
        except Exception as err:
            logger.print(LogLevel.ERROR, "Exception:{}".format(err), err)
            if test_result_metrics is not None:
                test_result_metrics.failed()
            self.commonPageOperator.save_screenshot(self.browser)
            assert False
        finally:
            helperHandle.quit_browser(self.browser)
            logger.print(LogLevel.INFO, "End【Bulk Power Off】test")
