import sum_recursion

def test_sum_add_1_up_to_10_times():
    # setup
    sum = 1
    counter = 10
    expected_result = 55

    # invoke
    actual_result = sum_recursion.sum(sum, counter)

    # analyze
    assert expected_result == actual_result