import math
import pandas as pd

def calculate_wire_length(panel_width, panel_height, horizontal_spacing, vertical_spacing):
    num_horizontal_wires = math.ceil(panel_height / horizontal_spacing)
    num_vertical_wires = math.ceil(panel_width / vertical_spacing)

    total_horizontal_wire_length = num_horizontal_wires * panel_width
    total_vertical_wire_length = num_vertical_wires * panel_height

    total_wire_length = total_horizontal_wire_length + total_vertical_wire_length
    return math.ceil(total_wire_length)

def calculate_panel_cost(wire_length, wire_cost_per_meter):
    panel_cost = wire_length * wire_cost_per_meter
    return panel_cost

def calculate_fencing_cost(fencing_length, post_spacing, panel_width, panel_height, wire_cost_per_meter, labor_cost, coating_option, security_fencing_option, security_tech_option, color_option, bentop_option, entrance_control_option, facade_length, solar_lights_option):
    # Calculate component quantities
    num_posts = fencing_length / post_spacing
    num_post_cap = num_posts
    num_base_plates = num_posts
    num_anchor_plates = num_base_plates * 4
    num_clamps = num_posts * 6
    num_panels = fencing_length / panel_width
    #print(f"{num_posts}, {num_post_cap} , {num_base_plates} , {num_anchor_plates} , {num_clamps} , {num_panels}")

    # Calculate panel cost based on wire length
    horizontal_spacing = 0.0127  # meters
    vertical_spacing = 0.0762  # meters
    total_wire_length = calculate_wire_length(panel_width, panel_height, horizontal_spacing, vertical_spacing)
    panel_cost = calculate_panel_cost(total_wire_length, wire_cost_per_meter)


    # Calculate material costs
    post_cost = 1000  # Adjust as needed
    post_cap_cost = 50
    base_plate_cost = 500  # Adjust as needed
    anchor_bolt_cost = 50  # Adjust as needed
    clamp_cost = 10  # Adjust as needed

    # Calculate labor cost
    labor_rate = 15  # 15RS per meter
    labor_cost = fencing_length * labor_rate

    total_material_cost = (num_posts * post_cost) + (num_post_cap * post_cap_cost) + (
                num_base_plates * base_plate_cost) + (num_anchor_plates * anchor_bolt_cost) + (
                                      num_clamps * clamp_cost) + (num_panels * panel_cost)

    # Calculate additional costs based on customization options
    coating_cost = 0
    security_fencing_cost = 0
    security_tech_cost = 0
    color_cost = 0
    bentop_cost = 0
    entrance_control_cost = 0
    facade_cost = 0
    solar_lights_cost = 0

    # Coating cost
    match coating_option:
        case 1:
            print("Hot Dip Galvanized coating cost: Free")
        case 2:
            print("TPC coating cost: Free")
        case 3:
            print("PPC coating cost: Free")
        case _:
            print("Invalid coating option.")

    # Security fencing cost
    match security_fencing_option:
        case 1:
            security_fencing_cost = 10 * fencing_length  # Calculate per meter cost
            print("Electric Fencing cost: INR", security_fencing_cost)
        case 2:
            security_fencing_cost = 5 * fencing_length  # Calculate per meter cost
            print("Concertina Coil cost: INR", security_fencing_cost)
        case 3:
            security_fencing_cost = 7 * fencing_length  # Calculate per meter cost
            print("Wall Spikes cost: INR", security_fencing_cost)
        case _:
            print("Invalid security fencing option.")

    # Security technology cost
    match security_tech_option:
        case 1:
            num_intrusion_detectors = int(input("Enter the number of intrusion detectors required: "))
            security_tech_cost = 10000 * num_intrusion_detectors
            print("Intrusion Detection cost: INR 10000 per unit")
        case 2:
            num_cameras = int(input("Enter the number of cameras required: "))
            security_tech_cost = 8000 * num_cameras
            print("Camera cost: INR 8000 per unit")
        case _:
            print("Invalid security technology option.")

    # Color cost (free)
    match color_option:
        case 1:
            print("Green color is free")
        case 2:
            print("Red color is free")
        case 3:
            print("Yellow color is free")
        case 4:
            print("White color is free")
        case _:
            print("Invalid color option.")

    # Bentop cost
    if bentop_option:
        bentop_cost = 3 * fencing_length  # Calculate per meter cost
        print("Bentop cost: INR", bentop_cost)

    # Entrance control cost
    if entrance_control_option:
        entrance_control_cost = 15000
        print("Entrance Control cost: INR 15000")

    # Facade cost
    if facade_length > 0:
        facade_cost = facade_length * 20  # Adjust as needed
        print("Facade cost: INR 20/meter")

    # Solar lights cost
    if solar_lights_option:
        num_solar_lights = int(input("Enter the number of solar lights required: "))
        solar_lights_cost = 1000 * num_solar_lights
        print("Solar Lights cost: INR 1000 per unit")

    # Total cost
    print(f"\n\nTotal Cost without Customization : {total_material_cost }\n\n");
    print(f"\n\nTotal Cost without Customization : {total_material_cost+labor_cost}\n\n");
    total_cost = total_material_cost  + coating_cost + security_fencing_cost + security_tech_cost + color_cost + bentop_cost + entrance_control_cost + facade_cost + solar_lights_cost

    return total_cost, coating_cost, security_fencing_cost, security_tech_cost, bentop_cost, entrance_control_cost, facade_cost, solar_lights_cost

def main():
    # Get user input
    fencing_length = float(input("Enter fencing length (meters): "))
    post_spacing = 2.5
    panel_width = 2.5
    panel_height = 1.560
    wire_cost_per_meter = 2
    labor_cost = 0

    # Get customization options
    coating_option = int(input("Choose coating option (1: Hot Dip Galvanized, 2: TPC, 3: PPC): "))
    security_fencing_option = int(input("Choose security fencing option (1: Electric Fencing, 2: Concertina Coil, 3: Wall Spikes, 4: If None): "))
    security_tech_option = int(input("Choose security technology option (1: Intrusion Detection, 2: Camera, 3: If None): "))
    color_option = int(input("Choose color option (1: Green, 2: Red, 3: Yellow, 4: White): "))
    bentop_option = int(input("Include bentops? (1: Yes, 0: No): "))
    entrance_control_option = int(input("Include entrance control solutions? (1: Yes, 0: No): "))
    facade_length = float(input("Enter facade length (meters): "))
    solar_lights_option = int(input("Include solar lights? (1: Yes, 0: No): "))

    # Calculate total cost and individual customization costs
    total_cost, coating_cost, security_fencing_cost, security_tech_cost, bentop_cost, entrance_control_cost, facade_cost, solar_lights_cost = calculate_fencing_cost(
        fencing_length, post_spacing, panel_width, panel_height, wire_cost_per_meter, labor_cost, coating_option,
        security_fencing_option, security_tech_option, color_option, bentop_option, entrance_control_option, facade_length, solar_lights_option)

    # Display result

    # Create a table of customization options and costs
    data = {
        "Customization Option": ["Coating", "color","Security Fencing", "Security Technology", "Bentops", "Entrance Control", "Facade", "Solar Lights"],
        "Cost (INR)": [coating_cost, 0, security_fencing_cost, security_tech_cost, bentop_cost, entrance_control_cost, facade_cost, solar_lights_cost]
    }

    df = pd.DataFrame(data)
    print(df.to_string())  # Improved table formatting with to_string()
    print(f"\n\nTotal Cost with Customization :  {total_cost}\n\n")
    print("   Completed!   ")

if __name__ == "__main__":
    main()