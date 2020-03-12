Feature: gestionar actividades

   Background:
     Given Estoy en la Url del API

  Scenario: consultar todas las actividades
    When Consulto todas las actividades
    Then Trae todas las actividades

  Scenario: Consultar una actividad
    When Consulto una actividad con codigo "Id"
    Then Trae la informacion de esa actividad