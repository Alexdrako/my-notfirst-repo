import requests
from docutils.parsers.rst.directives import body
from faker import Faker
from pytest_steps import test_steps

from test_goal_checks_homework2 import create_goal, get_goals, update_goal, get_updated_goal_response, delete_goal, \
    get_created_goal

# fake = Faker()

#
# def test_get_goals():
#     result = get_goals()
#     assert result.status_code == 200
#     print('test 1 passed')
#     print(result.json()["goals"][2]["name"])

# @test_steps("Create a new goal", "Verify created goal", "Delete created goal")
# def test_create_goal():
#     result = create_goal()
#     assert result.status_code == 200
#     print('test1 passed')
#     id = result.json()['goal']['id']
#     yield
#     get_result = get_created_goal(id)
#     assert get_result.status_code == 200
#     print('test2 passed')
#     assert get_result.json()['goal']['id'] == id
#     print('test3 passed')
#     yield
#     result = delete_goal(id)
#     assert result.status_code == 200
#     assert result.text == '{}'
#     print('test4 passed')
#     yield


# def test_update_goal():
#     result=create_goal()
#     assert result.status_code == 200
#     id = result.json()['goal']['id']
#     print(result.json()['goal']['name'])
#     update_goal(id)
#     assert result.status_code == 200
#     updated_result=get_updated_goal_response(id)
#     print(updated_result.json()['goal']['name'])
#     assert result.json()['goal']['name'] != updated_result.json()['goal']['name']
#     print('passed')
#     result = delete_goal(id)
#     assert result.status_code == 200
#     assert result.text == '{}'
#     print('goal confirmed as deleted')

# def test_delete_goal():
#     result=create_goal()
#     assert result.status_code == 200
#     id = result.json()['goal']['id']
#     print(result.json()['goal']['name'])
#     delete_result = delete_goal(id)
#     assert delete_result.status_code == 200
#     print(delete_result.text)
#     assert delete_result.text == '{}'
#     print('goal confirmed as deleted')