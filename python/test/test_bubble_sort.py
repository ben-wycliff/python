from .. algorithms.bubble_sort import bubble_sort

class TestBubbleSort:
    def assertion(self, list_in, list_out):
        assert bubble_sort(list_in) == list_out

    def test_sorting_integer_array(self):
        list_in = [34,12,0,3,1,2,5,4,6]
        list_out = [0,1,2,3,4,5,6,12,34]
        self.assertion(list_in, list_out)

    def test_sorting_string_array(self):
        list_in = ["Walaga","Kitta","Wamala","Mugalu", "Weikama", "Bwowe"]
        list_out = ["Bwowe", "Kitta", "Mugalu", "Walaga", "Wamala", "Weikama"]
        self.assertion(list_in, list_out)

    def test_sorting_float_array(self):
        list_in = [0.1, 0.0, 2.1, 2.4, 2.2, 3.0, 2.9]
        list_out = [0.0, 0.1, 2.1, 2.2, 2.4, 2.9, 3.0]
        self.assertion(list_in, list_out)
