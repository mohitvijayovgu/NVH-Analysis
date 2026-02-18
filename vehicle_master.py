"""
NVH (Noise, Vibration, and Harshness) Synthetic Dataset Generator
Generates realistic automotive NVH data for Power BI analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
NUM_VEHICLES = 60
NUM_MEASUREMENTS = 800
NUM_FEEDBACK = 600

# ============================================================================
# TABLE 1: Vehicle Master Data
# ============================================================================

def generate_vehicle_master():
    """Generate vehicle master data table"""
    
    vehicle_models = [
    'Commuter Bike A1', 'Commuter Bike A2', 'Cruiser B1', 'Cruiser B2',
    'Sport Bike C1', 'Naked Bike D1', 'Adventure Bike E1',
    'Superbike F1', 'Electric Bike G1', 'Hybrid Bike H1'
]

    
    manufacturers = ['AutoCorp', 'VehicleTech', 'MotorWorks', 'DriveMax']
    engine_types = ['Gasoline', 'Diesel', 'Electric', 'Hybrid']
    
    vehicles = []
    for i in range(1, NUM_VEHICLES + 1):
        model = random.choice(vehicle_models)
        
        # Determine engine type based on model
        if 'Electric' in model:
            engine = 'Electric'
        elif 'Hybrid' in model:
            engine = 'Hybrid'
        else:
            engine = random.choice(['Gasoline', 'Diesel'])
        
        vehicle = {
            'Vehicle ID': f'VEH{i:04d}',
            'Vehicle Model': model if random.random() > 0.05 else None,  # 5% null
            'Manufacturer': random.choice(manufacturers) if random.random() > 0.08 else None,  # 8% null
            'Engine Type': engine if random.random() > 0.06 else None,  # 6% null
            'Manufacturing Date': (datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1460))).strftime('%Y-%m-%d') if random.random() > 0.07 else None,  # 7% null
        }
        vehicles.append(vehicle)
    
    # Add some duplicate rows (approximately 10% duplicates)
    num_duplicates = int(NUM_VEHICLES * 0.10)
    for _ in range(num_duplicates):
        # Randomly select an existing vehicle to duplicate
        duplicate = random.choice(vehicles).copy()
        vehicles.append(duplicate)
    
    df_vehicles = pd.DataFrame(vehicles)
    return df_vehicles


# ============================================================================
# TABLE 2: NVH Measurements
# ============================================================================

def generate_nvh_measurements(df_vehicles):
    """Generate NVH measurement data table"""
    
    test_conditions = ['City Driving', 'Highway Driving', 'Rough Road', 'Smooth Road', 'Acceleration', 'Braking', 'Idling']
    road_surfaces = ['Asphalt', 'Concrete', 'Gravel', 'Cobblestone', 'Test Track']
    
    measurements = []
    measurement_date_start = datetime(2023, 1, 1)
    
    for i in range(NUM_MEASUREMENTS):
        vehicle = df_vehicles.sample(1).iloc[0]
        test_condition = random.choice(test_conditions)
        road_surface = random.choice(road_surfaces)
        
        # Base noise levels with variations based on conditions
        base_noise = 60
        if test_condition == 'City Driving':
            base_noise = random.uniform(65, 75)
        elif test_condition == 'Highway Driving':
            base_noise = random.uniform(70, 80)
        elif test_condition == 'Rough Road':
            base_noise = random.uniform(75, 90)
        elif test_condition == 'Acceleration':
            base_noise = random.uniform(80, 95)
        elif test_condition == 'Idling':
            base_noise = random.uniform(40, 55)
        
        # Road surface affects vibration frequency
        base_vib_freq = 50
        if road_surface in ['Gravel', 'Cobblestone']:
            base_vib_freq = random.uniform(80, 200)
        elif road_surface == 'Asphalt':
            base_vib_freq = random.uniform(30, 80)
        else:
            base_vib_freq = random.uniform(40, 120)
        
        # Speed affects measurements
        speed = random.randint(15, 120) if test_condition != 'Idling' else 0
        
        # Harshness score correlates with noise and road surface
        harshness = 5.0
        if road_surface in ['Gravel', 'Cobblestone']:
            harshness = random.uniform(6, 9)
        elif base_noise > 80:
            harshness = random.uniform(6, 8)
        else:
            harshness = random.uniform(2, 6)
        
        # Generate measurement date with 1% inconsistency
        if random.random() < 0.01:  # 1% inconsistent dates
            # Create inconsistent date strings
            inconsistent_type = random.choice(['future_year', 'far_future_year'])
            if inconsistent_type == 'future_year':
                # Near future year like 2029
                measurement_date = f"2029-{random.randint(1, 12):02d}-{random.randint(1, 28):02d} {random.randint(0, 23):02d}:{random.randint(0, 59):02d}:00"
            else:
                # Far future year like 2080
                measurement_date = f"{random.choice([2080, 2090, 2099])}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d} {random.randint(0, 23):02d}:{random.randint(0, 59):02d}:00"
        else:
            # Normal date
            measurement_date = (measurement_date_start + timedelta(days=random.randint(0, 730), hours=random.randint(0, 23))).strftime('%Y-%m-%d %H:%M:%S') if random.random() > 0.03 else None
        
        measurement = {
            'Measurement ID': f'MEAS{i+1:05d}',
            'Vehicle ID': vehicle['Vehicle ID'],
            'Measurement Date': measurement_date,
            'Road Surface': road_surface if random.random() > 0.06 else None,  # 10% null
            'Speed (KMH)': speed if random.random() > 0.05 else None,  # 12% null
            'Noise Level (dB)': round(base_noise + random.uniform(-3, 3), 2) if random.random() > 0.03 else None,  # 9% null
            'Vibration Frequency (Hz)': round(base_vib_freq, 2) if random.random() > 0.01 else None,  # 11% null
            'Harshness Score': round(harshness, 1) if random.random() > 0.01 else None,  # 8% null
        }
        measurements.append(measurement)
    
    df_measurements = pd.DataFrame(measurements)
    # Don't sort by date since some dates are intentionally invalid
    return df_measurements


# ============================================================================
# TABLE 3: Customer Feedback
# ============================================================================

def generate_customer_feedback(df_vehicles):
    """Generate customer feedback data table"""
    
    comments_positive = [
        'Very smooth and quiet ride, excellent NVH performance',
        'Minimal cabin noise even at highway speeds',
        'Comfortable ride with well-damped suspension',
        'Engine operates quietly and smoothly',
        'Excellent noise insulation throughout the cabin',
        'Ride quality is impressive with minimal vibrations',
        'Very pleased with the overall refinement',
        'Smooth operation with excellent sound dampening'
    ]
    
    comments_neutral = [
        'Acceptable noise levels for the price range',
        'Ride comfort is adequate for daily commuting',
        'Some road noise on rough surfaces but manageable',
        'Average NVH performance compared to competitors',
        'Satisfactory overall, minor vibrations at idle'
    ]
    
    comments_negative = [
        'Excessive engine noise during acceleration',
        'Uncomfortable vibrations felt through steering wheel',
        'Road noise is too loud on highway',
        'Harsh ride over bumps and rough roads',
        'Engine vibrations noticeable in the cabin',
        'Wind noise at high speeds is intrusive',
        'Dashboard rattles over rough surfaces',
        'Seat vibrations make long drives uncomfortable',
        'Poor noise insulation, tire noise is excessive',
        'Steering wheel vibrates excessively'
    ]
    
    comfort_levels = ['Very Poor', 'Poor', 'Fair', 'Good', 'Very Good', 'Excellent']
    
    feedbacks = []
    feedback_date_start = datetime(2023, 6, 1)
    
    for i in range(NUM_FEEDBACK):
        vehicle = df_vehicles.sample(1).iloc[0]
        
        # Randomly assign comfort level
        comfort_level = random.choice(comfort_levels)
        
        # Select comment based on comfort level
        if comfort_level in ['Excellent', 'Very Good']:
            comment = random.choice(comments_positive)
        elif comfort_level in ['Good', 'Fair']:
            comment = random.choice(comments_neutral)
        else:
            comment = random.choice(comments_negative)
        
        feedback = {
            'Feedback ID': f'FB{i+1:05d}',
            'Vehicle ID': vehicle['Vehicle ID'],
            'Comfort Level': comfort_level if random.random() > 0.15 else None,  # 15% null
            'Comment': comment if random.random() > 0.10 else None,  # 10% null
        }
        feedbacks.append(feedback)
    
    df_feedback = pd.DataFrame(feedbacks)
    return df_feedback


# ============================================================================
# Main Execution
# ============================================================================

def main():
    """Generate all tables and save to CSV files"""
    
    print("=" * 70)
    print("NVH Dataset Generator for Power BI Dashboard")
    print("=" * 70)
    
    # Generate Table 1: Vehicle Master Data
    print("\n[1/3] Generating Vehicle Master Data...")
    df_vehicles = generate_vehicle_master()
    df_vehicles.to_excel('Vehicle.xlsx', index=False)
    print(f"✓ Generated {len(df_vehicles)} vehicle records")
    print(f"  Saved to: Vehicle.xlsx")

    # Generate Table 2: NVH Measurements
    print("\n[2/3] Generating NVH Measurements...")
    df_measurements = generate_nvh_measurements(df_vehicles)
    df_measurements.to_excel('NVH_Measurements.xlsx', index=False)
    print(f"✓ Generated {len(df_measurements)} measurement records")
    print(f"  Saved to: NVH_Measurements.xlsx")

    # Generate Table 3: Customer Feedback
    print("\n[3/3] Generating Customer Feedback...")
    df_feedback = generate_customer_feedback(df_vehicles)
    df_feedback.to_excel('Customer_Feedback.xlsx', index=False)
    print(f"✓ Generated {len(df_feedback)} feedback records")
    print(f"  Saved to: Customer_Feedback.xlsx")

    # Summary statistics
    print("\n" + "=" * 70)
    print("DATASET SUMMARY")
    print("=" * 70)
    
    print("\n📊 Vehicle Master Data:")
    print(f"   - Total Vehicles: {len(df_vehicles)}")
    print(f"   - Unique VehicleIDs: {df_vehicles['Vehicle ID'].nunique()}")
    print(f"   - Duplicate Rows: {len(df_vehicles) - df_vehicles.drop_duplicates().shape[0]}")
    print(f"   - Unique Models: {df_vehicles['Vehicle Model'].nunique()}")
    print(f"   - Engine Types: {', '.join(str(x) for x in df_vehicles['Engine Type'].dropna().unique())}")
    print(f"   - Null Values: Model({df_vehicles['Vehicle Model'].isna().sum()}), Manufacturer({df_vehicles['Manufacturer'].isna().sum()}), Engine Type({df_vehicles['Engine Type'].isna().sum()}), Manufacturing Date({df_vehicles['Manufacturing Date'].isna().sum()})")

    print("\n📊 NVH Measurements:")
    print(f"   - Total Measurements: {len(df_measurements)}")
    print(f"   - Date Range: {df_measurements['Measurement Date'].dropna().min()} to {df_measurements['Measurement Date'].dropna().max()}")
    print(f"   - Avg Noise Level: {df_measurements['Noise Level(dB)'].mean():.2f} dB")
    print(f"   - Avg Vibration Frequency: {df_measurements['Vibration Frequency(Hz)'].mean():.2f} Hz")
    print(f"   - Avg Harshness Score: {df_measurements['Harshness Score'].mean():.2f}/10")
    print(f"   - Null Values: Measurement Date({df_measurements['Measurement Date'].isna().sum()}), Road Surface({df_measurements['Road Surface'].isna().sum()}), Speed(km/h)({df_measurements['Speed(km/h)'].isna().sum()}), Noise Level(dB)({df_measurements['Noise Level(dB)'].isna().sum()}), Vibration Frequency(Hz)({df_measurements['Vibration Frequency(Hz)'].isna().sum()}), Harshness Score({df_measurements['Harshness Score'].isna().sum()})")
    
    print("\n📊 Customer Feedback:")
    print(f"   - Total Feedbacks: {len(df_feedback)}")
    print(f"   - Comfort Level Distribution:")
    for level in df_feedback['Comfort Level'].value_counts().sort_index().items():
        print(f"      • {level[0]}: {level[1]} ({level[1]/len(df_feedback)*100:.1f}%)")
    print(f"   - Null Values: Comfort Level({df_feedback['Comfort Level'].isna().sum()}), Comment({df_feedback['Comment'].isna().sum()})")
    
    print("\n" + "=" * 70)
    print("✓ All datasets generated successfully!")
    print("=" * 70)
    
    print("\n📝 NEXT STEPS:")
    print("   1. Import the three CSV files into Power BI")
    print("   2. Create relationships:")
    print("      - vehicle_master.VehicleID → nvh_measurements.VehicleID (Many-to-One)")
    print("      - vehicle_master.VehicleID → customer_feedback.VehicleID (Many-to-One)")
    print("   3. Start building your dashboard!")
    print("\n")


if __name__ == "__main__":
    main()
