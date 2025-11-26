from common.playwright_helper import PlayWrightHelper
from page_config.bulk_power_config import bulk_power_config
from common.common_page_config import MenuConf

helperHandle = PlayWrightHelper()


class BulkPowerOperator:
    def __init__(self, browser):
        self.browser = browser

    def get_page(self):
        return self.browser.pages[0]

    def confirm_device_power_off_state(self, device_list, expected_state="Off"):
        page = self.get_page()
        helperHandle.click(page, bulk_power_config["Windows 365"])
        helperHandle.click(page, MenuConf["All Cloud PCs"])

        for device in device_list:
            # Locate the device row and check its power state
            helperHandle.input_text(
                page, bulk_power_config["CPC Search inputbox"], device
            )
            page.wait_for_timeout(5000)  # Wait for search results to load
            helperHandle.click(page, bulk_power_config["CPC First device name"])
            page.wait_for_timeout(10000)
            power_state = helperHandle.get_element_attribute_value(
                page, bulk_power_config["Power Off"], "aria-disabled"
            )
            if power_state == "false" and expected_state == "Off":
                helperHandle.click(page, bulk_power_config["Power Off"])
                helperHandle.click(page, bulk_power_config["Confirm Power"])
            elif power_state == "true" and expected_state == "On":
                helperHandle.click(page, bulk_power_config["Power On"])
                helperHandle.click(page, bulk_power_config["Confirm Power"])
        page.wait_for_timeout(300000)
        page.reload()

    def confirm_device_power_state(self, device_list, expected_state="Off"):
        page = self.get_page()
        for device in device_list:
            # Locate the device row and check its power state
            helperHandle.input_text(page, bulk_power_config["Search Box"], device)
            page.wait_for_timeout(10000)  # Wait for search results to load
            helperHandle.click(page, bulk_power_config["First Box"])
            page.wait_for_timeout(15000)
            power_state = helperHandle.get_element_attribute_value(
                page, bulk_power_config["Power Off"], "aria-disabled"
            )
            if power_state == "false" and expected_state == "Off":
                helperHandle.click(page, bulk_power_config["Power Off"])
                helperHandle.click(page, bulk_power_config["Confirm Power"])
            elif power_state == "true" and expected_state == "On":
                helperHandle.click(page, bulk_power_config["Power On"])
                helperHandle.click(page, bulk_power_config["Confirm Power"])
        page.wait_for_timeout(300000)
        page.reload()

    def bulk_device_power_on(self, device_list, expected_state):
        page = self.get_page()
        helperHandle.click(page, MenuConf["Devices"])
        helperHandle.click(page, MenuConf["All devices"])
        page.wait_for_timeout(5000)
        helperHandle.click(page, bulk_power_config["Bulk device actions"])
        page.wait_for_timeout(2000)
        helperHandle.click(page, bulk_power_config["Select OS"])
        helperHandle.click(page, bulk_power_config["Select OS Option"])
        helperHandle.click(page, bulk_power_config["Select device type"])
        helperHandle.click(page, bulk_power_config["Select device type Option"])
        helperHandle.click(page, bulk_power_config["Select device action"])
        if expected_state == "On":
            helperHandle.click(page, bulk_power_config["Select device action Power On"])
        else:
            helperHandle.click(
                page, bulk_power_config["Select device action Power Off"]
            )
        helperHandle.click(page, bulk_power_config["Next"])
        helperHandle.click(page, bulk_power_config["Select one"])
        helperHandle.click(page, bulk_power_config["Select one Option"])
        helperHandle.click(page, bulk_power_config["Add devices"])
        page.wait_for_timeout(5000)
        for item in device_list:
            helperHandle.input_text(page, bulk_power_config["Select devices"], item)
            page.wait_for_timeout(5000)
            helperHandle.click(page, bulk_power_config["Select one device layer1"])
            page.wait_for_timeout(5000)
            helperHandle.click(page, bulk_power_config["Select one device layer2"])
        page.wait_for_timeout(5000)
        helperHandle.click(page, bulk_power_config["Select"])
        page.wait_for_timeout(5000)
        helperHandle.click(page, bulk_power_config["Next"])
        page.wait_for_timeout(10000)
        helperHandle.click(page, bulk_power_config["Create"])
        page.wait_for_timeout(300000)
        page.reload()

    def verify_devices_power_state(self, device_list, expected_state="On"):
        page = self.get_page()
        helperHandle.click(page, MenuConf["Devices"])
        helperHandle.click(page, MenuConf["All devices"])
        page.wait_for_timeout(5000)
        for device in device_list:
            helperHandle.input_text(page, bulk_power_config["Search Box"], device)
            page.wait_for_timeout(5000)
            helperHandle.click(page, bulk_power_config["First Box"])
            page.wait_for_timeout(15000)
            power_state = helperHandle.get_element_attribute_value(
                page, bulk_power_config["Power Off"], "aria-disabled"
            )
            if power_state == "false" and expected_state == "Off":
                raise Exception(f"Device {device} is expected to be Off but is On.")
            elif power_state == "true" and expected_state == "On":
                raise Exception(f"Device {device} is expected to be On but is Off.")

    def power_on_devices(self, device_list):
        page = self.get_page()
        helperHandle.click(page, MenuConf["Devices"])
        helperHandle.click(page, MenuConf["All devices"])
        page.wait_for_timeout(5000)
        for device in device_list:
            helperHandle.input_text(page, bulk_power_config["Search Box"], device)
            page.wait_for_timeout(5000)
            helperHandle.click(page, bulk_power_config["First Box"])
            page.wait_for_timeout(15000)
            power_state = helperHandle.get_element_attribute_value(
                page, bulk_power_config["Power Off"], "aria-disabled"
            )
            if power_state == "true":
                helperHandle.click(page, bulk_power_config["Power On"])
                helperHandle.click(page, bulk_power_config["Confirm Power"])
        page.wait_for_timeout(300000)
        page.reload()
