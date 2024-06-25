import allure
import pytest 
import random

@allure.feature("Fruits")
class TestFruit:
    @allure.description("This test will validate that the first charater of the test fruit matches a random fruit")
    @pytest.mark.parametrize("fruit",["apple","orange","pear","peach"])
    def test_fruit(self,fruit)->None:
        with allure.step("Arrange"):
            allure.dynamic.title(f"Feature 1 Test 1 for fruit {fruit}")
            my_fruits = ["apple","pear","peach","kiwi"]
        
        with allure.step("Execute"):
            my_fruit = random.choice(my_fruits)
            my_fruit_char = my_fruit[0]
            test_fruit_char = fruit[0]
        with allure.step("Assert"):
            assert my_fruit_char == test_fruit_char, f"First characters of the fruits do not match: Random Fruit: {my_fruit} vs. Test Fruit {fruit}"

@allure.feature("Vegetables")
class TestVegetables:
    @allure.description("This test will validate that the first charater of the test vegtable matches a random vegtable")
    @pytest.mark.parametrize("vegetable",["beans","corn","peas","cauliflower","carrots"])
    def test_veggies(self,vegetable)->None:
        with allure.step("Arrange"):
            allure.dynamic.title(f"Feature 1 Test 1 for fruit {vegetable}")
            my_vegetables = ["corn","carrots","cauliflower","beats","peppers"]
        
        with allure.step("Execute"):
            my_vegetable = random.choice(my_vegetables)
            my_vegetable_char = my_vegetable[0]
            test_vegetables_char = vegetable[0]
        with allure.step("Assert"):
            assert my_vegetable_char == test_vegetables_char, f"First characters of the fruits do not match: Random Fruit: {my_vegetable} vs. Test Fruit {vegetable}"