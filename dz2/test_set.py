def test_a_tuple(fixture_return_set):
    if fixture_return_set == 'Cucumber':
        assert fixture_return_set == 'Cucumber'
    elif fixture_return_set == '10':
        assert fixture_return_set == '10'
    elif fixture_return_set == 'string':
        assert fixture_return_set == 'string'
    elif fixture_return_set == 'False':
        assert fixture_return_set == 'False'
    elif fixture_return_set == 'Pen':
        assert fixture_return_set == 'Pen'

