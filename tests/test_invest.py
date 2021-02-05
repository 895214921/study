from time import sleep
class TestInvest():
    def test_invest_success(self,login):
        invest_page = login
        actual = invest_page.click_invest_btn().fill_money(100).invest_click_invest_btn().get_success_pop_msg()
        exepected = '投标成功！'
        # sleep(1)
        assert exepected in actual


    # def test_invest_error(self,login):
        '''
        1.登录页面前置：打开浏览器，登录，（）
            1.有标
            2.标有钱
            3.有余额可以投资
        前置条件一定得通过自动化去实现吗？
        如果是，一定要通过web自动化去实现吗？
        不是，只是一个条件，手工也行，只要达到条件即可

        2、在首页上，点击可以投的标  class= btn btn-special
        3.在投标详情页，输入投标金额：xpath= form-control invest-unit-investinput
        4.定位按钮 xpath=btn btn-special height_style
        :return:
        '''
        # pass
        # invest_page.click_invest_btn().invest_error_NotCertified(10)
