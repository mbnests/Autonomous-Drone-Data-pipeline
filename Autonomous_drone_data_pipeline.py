import pandas as pd

class DroneFleetPipeline:
    
    def __init__(self):

        #Table 1: Raw drone data 
        raw_fleet = {
            "drone_id": ["D-001", "D-002", "D-003", "D-004"],
            "model_type": ["Scout", "Hauler", "Scout", "Hauler"],
            "battery_pct": [85, 12, 90, 45],
            "flight_hours": [120.0, 300.0, None, 150.0] 
        }
        self.fleet_df = pd.DataFrame(raw_fleet)

        #Table 2: Separate maintenance records
        raw_maintenance = {
            "drone_id": ["D-001", "D-002", "D-003", "D-004"],
            "repair_cost_usd": [50.0, 400.0, 0.0, 120.0]
        }
        self.maintenance_df = pd.DataFrame(raw_maintenance)

    def process_data(self):
        print("--- 0. ORIGINAL DATAFRAME ---")
        print(self.fleet_df)
        
        #Slicing & Boolean Masking
        low_battery_df = self.fleet_df[ self.fleet_df["battery_pct"] < 50 ]
        
        print("\n--- 1. SLICING (Battery < 50%) ---")
        print(low_battery_df)

        #Handling Missing Data
        clean_df = self.fleet_df.fillna(0.0)
        
        print("\n--- 2. CLEANING (Filled NaN) ---")
        print(clean_df)

        #Relational Merging
        merged_df = pd.merge(clean_df, self.maintenance_df, on="drone_id")
        
        print("\n--- 3. MERGING (Added Repair Costs) ---")
        print(merged_df)

        #Grouping & Feature Engineering
        merged_df["cost_per_hour"] = merged_df["repair_cost_usd"] / (merged_df["flight_hours"] + 1)
        
        # Grouping: Shrink the table to find the average cost-per-hour by model
        model_summary = merged_df.groupby("model_type")["cost_per_hour"].mean()
        
        print("\n--- 4. GROUPING (Average Cost per Hour by Model) ---")
        print(model_summary)

if __name__ == "__main__":
    pipeline = DroneFleetPipeline()
    pipeline.process_data()