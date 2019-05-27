import allure
import pytest


class Test_01:

    @allure.step(title="这是一个测试步骤01")
    def test_01_1(self):
        print("--->test_01_1")
        allure.attach("标题", "具体内容")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_01_2(self):
        print("--->test_01_2")
        assert True