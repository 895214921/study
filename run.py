'''搜集用例，生成报告之类的。程序入口'''
import pytest

if __name__=='__main__':
    pytest.main(['--alluredir=report'])
