from behave import *
from mi_proyecto.tests.test_activities import ApiRequestsActivities

test = ApiRequestsActivities()


@given(u'Estoy en la Url del API')
def step_impl(context):
    pass


@when(u'Consulto todas las actividades')
def step_impl(context):
    test.test_get_all_activites()


@then(u'Trae todas las actividades')
def step_impl(context):
    test.test_validate_status_code(200)




@when(u'Consulto una actividad con codigo "Id"')
def step_impl(context):
    pass


@then(u'Trae la informacion de esa actividad')
def step_impl(context):
    pass
