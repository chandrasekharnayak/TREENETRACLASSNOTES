from src.calculator import addition,substraction,multiplication,division,power
import pytest
import sys


@pytest.mark.skipif(sys.platform=='darwin',reason='its is not macos , so that this functionality not to be execute')
def test_addition():
    assert addition(2,3)==5
    assert addition(0,0)==0
    assert addition(-1,1)==1
    assert addition(-9,-9)==-18

@pytest.mark.regression
@pytest.mark.smoke
def test_substraction():
    assert substraction(1,1)==0
    assert substraction(2,2)==0

@pytest.mark.regression
@pytest.mark.smoke
def test_multiplication():
    assert multiplication(2,5)==10
    assert multiplication(10,2)==20

@pytest.mark.regression
def test_division():
    assert division(10,2)==10
    assert division(-10,2)==-5.0

@pytest.mark.xfail(reason='Hope best on end user data , may be its failed')
def test_power():
    assert power(2,3)==6
    assert power(3,3)==27



@pytest.mark.v4
@pytest.mark.v1
def test_f1():
    pass

@pytest.mark.v2
def test_f2():
    pass

@pytest.mark.v4
@pytest.mark.v2
def test_f3():
    pass

@pytest.mark.v3
def test_f4():
    pass

@pytest.mark.retesting
@pytest.mark.v1
def test_f5():
    pass

@pytest.mark.retesting
@pytest.mark.v3
def test_f6():
    pass

@pytest.mark.v1
def test_f7():
    pass

@pytest.mark.retesting
@pytest.mark.v3
def test_f8():
    pass