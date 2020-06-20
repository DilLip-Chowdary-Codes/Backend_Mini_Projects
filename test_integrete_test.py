def sum(num_1, num_2):
    result = num_1 + num_2
    return result

def test_sum_with_positive_integers(snapshot):
    return_value = sum(1, 2)
    # assert return_value == 2
    snapshot.assert_match(return_value, 'rgukt_response')

def test_sum_with_float_values(snapshot):
    return_value = sum(0.1, 0.2)
    snapshot.assert_match(return_value, 'sum_float_value')

def test_sum_with_negative_integers(snapshot):
    return_value = sum(-1, -2)
    snapshot.assert_match(return_value, 'sum_negative_value')
