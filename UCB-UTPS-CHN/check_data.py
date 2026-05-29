# check_data.py
import json
import glob

files = glob.glob("results/*.json")
for f in files:
    if "target5" in f and "past" in f:
        with open(f, 'r') as file:
            data = json.load(file)
            print(f"\n文件: {f}")
            print(f"final_effective_coverage: {data.get('final_effective_coverage', 'NOT FOUND')}")
            print(f"final_line_coverage: {data.get('final_line_coverage', 'NOT FOUND')}")
            print(f"final_condition_path_coverage: {data.get('final_condition_path_coverage', 'NOT FOUND')}")