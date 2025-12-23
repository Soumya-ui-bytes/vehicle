from vehicle import vehicle_details
def test_vehicle_details():
    expected_output = (
    
        "vehicle Name: mahindra\n"
        "vehicle ID: 101fb\n"
        "cost: 80000\n"
    
    )
    assert vehicle_details("mahindra","101fb",80000) == expected_output
