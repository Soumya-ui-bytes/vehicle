from vehicle import vehicle_details
def test_vehicle_details():
    expected_output = (
        " Name: Laptop\n"
        "vehicle Name: mahindra\n"
        "vehicle ID: 101fb\n"
        "cost: 80000\n"
    
    )
    assert vehicle_details("nahindra","101fb",80000) == expected_output