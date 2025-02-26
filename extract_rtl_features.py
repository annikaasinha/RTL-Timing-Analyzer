import os
import re
import pandas as pd
from collections import deque

def parse_rtl(file_path):
    """Extracts dependencies and computes fan-in & fan-out from RTL Verilog."""
    dependencies = {}
    fan_in = {}
    fan_out = {}

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if any(gate in line for gate in ['AND', 'OR', 'NAND', 'XOR', 'NOR', 'MUX', 'NOT']):
                parts = re.findall(r'\w+', line)
                if len(parts) >= 3:
                    output_signal = parts[1]  # ✅ Extract signal name
                    input_signals = parts[2:]

                    # Store dependencies signal-wise
                    dependencies[output_signal] = input_signals
                    fan_in[output_signal] = len(input_signals)
                    for signal in input_signals:
                        fan_out[signal] = fan_out.get(signal, 0) + 1

    return dependencies, fan_in, fan_out

def compute_logic_depth(dependencies):
    """Computes logic depth iteratively using Topological Sorting (No Recursion)."""
    in_degree = {node: 0 for node in dependencies}
    for inputs in dependencies.values():
        for inp in inputs:
            in_degree[inp] = in_degree.get(inp, 0) + 1  # Count incoming edges

    queue = deque([node for node in dependencies if in_degree[node] == 0])
    depth = {node: 1 for node in queue}  # Start depth from 1
    max_depth = 1

    while queue:
        node = queue.popleft()
        for neighbor in dependencies.get(node, []):
            depth[neighbor] = max(depth.get(neighbor, 1), depth[node] + 1)
            max_depth = max(max_depth, depth[neighbor])
            in_degree[neighbor] -= 1  # Remove edge
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return max_depth
def extract_features():
    """Extracts combinational logic features per signal from RTL files."""
    data = []

    for file in os.listdir("rtl_folder/Data_verilog files"):
        if file.endswith(".v") or file.endswith(".sv"):
            file_path = os.path.join("rtl_folder/Data_verilog files", file)
            dependencies, fan_in, fan_out = parse_rtl(file_path)

            for signal in dependencies.keys():
                logic_depth = compute_logic_depth({signal: dependencies[signal]})  # Compute for each signal

                data.append({
                    'rtl_file': file,
                    'signal': signal,  # ✅ Store signal-wise prediction
                    'logic_depth': logic_depth,
                    'fan_in': fan_in.get(signal, 0),
                    'fan_out': fan_out.get(signal, 0)
                })

    df = pd.DataFrame(data)
    df.to_csv("rtl_features_per_signal.csv", index=False)
    print(f"Dataset saved as rtl_features_per_signal.csv with {len(df)} signals analyzed.")

if __name__ == "__main__":
    extract_features()
