bulk_power_config = {
    "Search Box": {
        "name": "Search Box",
        "locator_type": "xpath",
        "value": "//div/input[@id='SearchBox5' and @role='searchbox']",
        "iframe": "//iframe[@name='AllManagedDevices.ReactView']",
    },
    "First Box": {
        "name": "First Box",
        "locator_type": "xpath",
        "value": "//div[@data-automation-key='deviceName']//a",
        "iframe": "//iframe[@name='AllManagedDevices.ReactView']",
    },
    "Power Off": {
        "name": "Power Off",
        "locator_type": "xpath",
        "value": '//div[@aria-label="Power off"]',
    },
    "Confirm Power": {
        "name": "Confirm Power",
        "locator_type": "xpath",
        "value": "//div[@role='button' and @title='Yes']",
    },
    "Power On": {
        "name": "Power On",
        "locator_type": "xpath",
        "value": '//div[@aria-label="Power on"]',
    },
    "Devices | All devices": {
        "name": "Devices | All devices",
        "locator_type": "xpath",
        "value": "//a[text()='Devices | All devices']",
    },
    "Bulk device actions": {
        "name": "Bulk device actions",
        "locator_type": "xpath",
        "value": '//span[text()="Bulk device actions"]//ancestor::button[@role="menuitem"]',
        "iframe": "//iframe[@name='AllManagedDevices.ReactView']",
    },
    "Select OS": {
        "name": "Select OS",
        "locator_type": "xpath",
        "value": "//div[text()='Select OS']/parent::div/following-sibling::span[@role='button']",
    },
    "Select OS Option": {
        "name": "Select OS Option",
        "locator_type": "xpath",
        "value": "//div[@role='treeitem' and @aria-posinset='8']",
    },
    "Select device type": {
        "name": "Select device type",
        "locator_type": "xpath",
        "value": "//div[text()='Select device type']/parent::div/following-sibling::span[@role='button']",
    },
    "Select device type Option": {
        "name": "Select device type Option",
        "locator_type": "xpath",
        "value": "//div[@role='treeitem' and @aria-posinset='1' and @aria-setsize='2']",
    },
    "Select device action": {
        "name": "Select device action",
        "locator_type": "xpath",
        "value": "//div[text()='Select device action']/parent::div/following-sibling::span[@role='button']",
    },
    "Select device action Power On": {
        "name": "Select device action Power On",
        "locator_type": "xpath",
        "value": "//div[@role='treeitem' and @aria-posinset='11']",
    },
    "Select device action Power Off": {
        "name": "Select device action Power Off",
        "locator_type": "xpath",
        "value": "//div[@role='treeitem' and @aria-posinset='12']",
    },
    "Next": {
        "name": "Next",
        "locator_type": "xpath",
        "value": "//div[@role='button' and @title='Next']",
    },
    "Select one": {
        "name": "Select one",
        "locator_type": "xpath",
        "value": "//div[text()='Select one']/parent::div/following-sibling::span[@role='button']",
    },
    "Select one Option": {
        "name": "Select one Option",
        "locator_type": "xpath",
        "value": "//span[text()='Select individual devices across your environment']/parent::div[@role='treeitem' and @aria-posinset='1']",
    },
    "Add devices": {
        "name": "Add devices",
        "locator_type": "xpath",
        "value": "//div[@title='Add devices' and @role='button']",
    },
    "Select devices": {
        "name": "Select devices",
        "locator_type": "xpath",
        "value": "//div[@class='ext-searchBoxWithInfoBalloon']//input[@type='text' and @aria-label='Search']",
    },
    "Select one device layer1": {
        "name": "Select one device layer1",
        "locator_type": "xpath",
        "value": "//div[@role='gridcell']/ancestor::div[@role='row']",
    },
    "Select one device layer2": {
        "name": "Select one device layer2",
        "locator_type": "xpath",
        "value": "//div[@role='gridcell']/ancestor::div[@role='row']/div/div[1]/div",
    },
    "Select": {
        "name": "Select",
        "locator_type": "xpath",
        "value": "//div[@role='button' and @title='Select']",
    },
    "Create": {
        "name": "Create",
        "locator_type": "xpath",
        "value": "//div[@class='ext-wizardNextButton fxc-base fxc-simplebutton']/div[@role='button' and @title='Create']",
    },
    "CPC Search inputbox": {
        "name": "CPC Search inputbox",
        "locator_type": "xpath",
        "value": "//input[@aria-label='Search']",
        "iframe": "//iframe[@name='LandingHomePage.ReactView']",
    },
    "CPC First device name": {
        "name": "CPC First device name",
        "locator_type": "xpath",
        "value": "//div[@data-automation-key='managedDeviceName']/button",
        "iframe": "//iframe[@name='LandingHomePage.ReactView']",
    },
    "Windows 365": {
        "name": "Windows 365",
        "locator_type": "xpath",
        "value": '(//div[@data-telemetryname="Menu-Cloud PC"])[1]',
    },
}
