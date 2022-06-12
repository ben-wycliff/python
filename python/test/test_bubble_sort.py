from .. algorithms.bubble_sort import bubble_sort

class TestBubbleSort:
    def test_one(self):
        assert bubble_sort([34,12,0,3,1,2,5,4,6]) == [0,1,2,3,4,5,6,12,34]

    def test_two(self):
        assert bubble_sort(["Walaga",
                            "Kitta",
                            "Wamala",
                            "Mugalu", 
                            "Weikama", 
                            "Bwowe"]) == ["Bwowe", "Kitta", "Mugalu", "Walaga", "Wamala", "Weikama"]

    def test_three(self):
        assert bubble_sort([0.1, 0.0, 2.1, 2.4, 2.2, 3.0, 2.9]) == [0.0, 0.1, 2.1, 2.2, 2.4, 2.9, 3.0]