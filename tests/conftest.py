import os
import pytest
import pytest_html
from utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def screenshot_tracker(request):
    request.node._screenshots = []
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        screenshots = getattr(item, "screenshots", [])

        if screenshots:
            report.extras = getattr(report, "extras", [])

            for screenshot in screenshots:
                report.extras.append(
                    pytest_html.extras.image(
                        screenshot,
                        mime_type="image/png"
                    )
                )

