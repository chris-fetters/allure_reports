import allure
import pytest 
import random


@allure.feature("Pets")
class TestAnimals:
    @allure.description("This test will validate that the first charater of the test pet matches a random pet")
    @pytest.mark.parametrize("pet",["dog","cat","ferret","iguana"])
    def test_animals(self,pet)->None:
        with allure.step("Arrange"):
            allure.dynamic.title(f"Feature Test for pet {pet}")
            random_choices = ["snake","alligator","parrot","goat"]
        
        with allure.step("Execute"):
            choice = random.choice(random_choices)
            choice_char = choice[0]
            test_char = pet[0]
        with allure.step("Assert"):
            assert choice_char == test_char, f"First characters of the pets do not match: Random Pet: {choice} vs. Test Pet {pet}"

@allure.feature("BabyNames")
class TestVegetables:
    @allure.description("This test will validate that the first charater of the test baby name matches a random baby name")
    @pytest.mark.parametrize("name",["sophia","sam","scarlett","sebastian","stella"])
    def test_names(self,name)->None:
        with allure.step("Arrange"):
            allure.dynamic.title(f"Feature Test for name {name}")
            random_choices = ["samual","santiago","sophie","sadie","skylar"]
        
        with allure.step("Execute"):
            choice = random.choice(random_choices)
            choice_char = choice[0]
            test__char = name[0]
        with allure.step("Assert"):
            assert choice_char == test__char, f"First characters of the names do not match: Random Name: {choice} vs. Test Name {name}"