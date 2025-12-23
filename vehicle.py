def vehicle_details(vname, vid, cost):
    result = (
        f"vehicle Name: {vname}\n"
        f"vehicle ID: {vid}\n"
        f"cost: {cost}\n"
    
    )
    return result

if __name__ == "__main__":
    vname = "mahindra"   
    vid = "101fb"
    cost = 80000
    print(vehicle_details(vname, vid, cost))