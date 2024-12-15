import json
from lib.types import *
import matplotlib.pyplot as plt
from math import sqrt, atan, degrees, pi

def calculate_rc(omega: float, resistance: float, capacitor: float):
  """transfer function: H(jω)| = 1 / √(1 + (ωRC)²)"""
  multiplication = omega * resistance * capacitor
  magnitude = 1 / sqrt(1 + pow(multiplication, 2))
  phase = degrees(-atan(multiplication))
  cut_frequency = 1 / (2 * pi * resistance * capacitor)
  return magnitude, phase, cut_frequency

def calculate_cr(omega: float, resistance: float, capacitor: float):
  """transfer function: H(jω) = (jωRC) / (1 + jωRC)"""
  multiplication = omega * resistance * capacitor
  magnitude = multiplication / sqrt(1 + pow(multiplication, 2))
  phase = degrees(180 - atan(multiplication))
  cut_frequency = 1 / (2 * pi * resistance * capacitor)
  return magnitude, phase, cut_frequency

def calculate_rl(omega: float, resistance: float, inductor: float):
  """transfer function: H(jω) = (jωL/R) / (1 + (jωL/R))"""
  division = omega * inductor / resistance
  magnitude = division / sqrt(1 + pow(division, 2))
  phase = degrees(180 - atan(division))
  cut_frequency = resistance / (2 * pi * inductor)
  return magnitude, phase, cut_frequency

def calculate_lr(omega: float, resistance: float, inductor: float):
  """transfer function: H(jω) = 1 / (1 +(jωL/R))"""
  division = omega * inductor / resistance
  magnitude = 1 / sqrt(1 + pow(division, 2))
  phase = degrees(-atan(division))
  cut_frequency = resistance / (2 * pi * inductor)
  return magnitude, phase, cut_frequency

def calculate_frequencies_range(start_freq: float, stop_freq: float, num_points: int):
  return [start_freq + i * (stop_freq - start_freq) / num_points for i in range(num_points)]

def plot_bode(frequencies: list, magnitudes: list, phases: list, filter_type: str):
  _, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

  plt.get_current_fig_manager().set_window_title(f"Bode Plot - {filter_type.upper()} Filter")

  ax1.semilogx(frequencies, magnitudes)
  ax1.set_title(f"Bode Plot - {filter_type.upper()} Filter")
  ax1.set_xlabel("Frequency (Hz)")
  ax1.set_ylabel("Magnitude")
  ax1.grid(True)

  ax2.semilogx(frequencies, phases)
  ax2.set_xlabel("Frequency (Hz)")
  ax2.set_ylabel("Phase (Degrees)")
  ax2.grid(True)
  
  plt.tight_layout()
  plt.show()
  
def save_bode_json(
  resistance: float, 
  other_component: float, 
  filter_type: FilterType, 
  rc_filter_results: dict,
  rc_filter_file: str
):
  json_data = {
    "resistance": resistance,
    "other_component": other_component,
    "filter_type": filter_type,
    "cut_frequency": rc_filter_results["cut_frequency"],
    "data": []
  }

  for i in range(len(rc_filter_results["frequencies"])):
    json_data["data"].append({
      "frequency": rc_filter_results["frequencies"][i], 
      "magnitude": rc_filter_results["magnitudes"][i], 
      "phase": rc_filter_results["phases"][i]
    })

  with open(rc_filter_file, "w") as json_file:
    json.dump(json_data, json_file, indent=2)
    
  print(f"[SUCCESS] Data saved to {rc_filter_file}")