# import the module
import example

def test_sum_2_5_is_7():
    # setup 
    num1 = 2
    num2 = 5
    expected_result = 7

    # invoke
    actual_result = example.sum(num1, num2)

    # analyze
    assert expected_result == actual_result