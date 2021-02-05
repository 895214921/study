"""测试登陆功能"""
import pytest
from data.login_data import login_data_error, login_data_uninvalid, login_data_success
from pages.login import LoginPage
from pages.index import IndexPage
class TestLogin():
    @pytest.mark.parametrize('data',login_data_error)
    def test_login_without_username(self,data,browser):
        expected=data['expected']
        actual=LoginPage(browser).get().login_fail(data['username'],data['pwd']).get_error_msg()
        assert expected==actual
    @pytest.mark.parametrize('data',login_data_uninvalid)
    def test_login_uninvalid_username(self,data,browser):
        expected=data['expected']
        actual=LoginPage(browser).get().login_fail(data['username'],data['pwd']).get_invalid_msg()
        assert expected==actual
        # def test_login_success(self,data,browser):
        #     expected=data['expected']
        #     actual=LoginPage(browser).login(data['username'],data['pwd']).get_invalid_msg()
        #     assert expected==actual
    @pytest.mark.parametrize('date',login_data_success)
    @pytest.mark.success
    def test_login_success(self,date,browser):
        expected=date['expected']
        actual=LoginPage(browser).get().login_success(date['username'], date['pwd']).get_user_info()
        assert expected in actual

