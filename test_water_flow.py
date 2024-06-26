from pytest import approx
import pytest

import water_flow



def test_water_column_height():
    A = water_flow.water_column_height(0.0, 0.0)
    print(f"{A}")

    B = water_flow.water_column_height(0.0, 10.0)
    print(f"{B}")

    C = water_flow.water_column_height(25.0, 0.0)
    print(f"{C}")

    D = water_flow.water_column_height(48.3, 12.8)
    print(f"{D}")


def test_pressure_gain_from_water_height():
    A = water_flow.pressure_gain_from_water_height(0.0)

    print(f"{A}")

    B = water_flow.pressure_gain_from_water_height(30.2)

    print(f"{B}")

    C = water_flow.pressure_gain_from_water_height(50.0)

    print(f"{C}")


def test_pressure_loss_from_pipe():

    A = water_flow.pressure_lost_from_pipe(0.048692, 0.00, 0.018, 1.75)
    print(f"{A}")

    B = water_flow.pressure_lost_from_pipe(0.048692, 200.0, 0.0, 1.75)
    print(f"{B}")

    C = water_flow.pressure_lost_from_pipe(0.048692, 200.0, 0.018, 0.0)
    print(f"{C}")

    D = water_flow.pressure_lost_from_pipe(0.048692, 200.0, 0.018, 1.75)
    print(f"{D}")

    E = water_flow.pressure_lost_from_pipe(0.048692, 200.0, 0.018, 1.65)
    print(f"{E}")

    F = water_flow.pressure_lost_from_pipe(0.286870, 1000.0, 0.013, 1.65)
    print(f"{F}")

    G = water_flow.pressure_lost_from_pipe(0.286870, 1800.75, 0.013, 1.65)
    print(f"{G}")
    


test_water_column_height()
test_pressure_gain_from_water_height()
test_pressure_loss_from_pipe()

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])