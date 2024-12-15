from math import pi
from lib.types import *
from lib.utils import *

def bode_plotter(
  resistance: float, 
  other_component: float, 
  filter_type: FilterType, 
  start_freq: float = 1, 
  stop_freq: float = 1e6, 
  num_points: int = 500,
):
  frequencies = calculate_frequencies_range(start_freq, stop_freq, num_points)

  filter = {
    "frequencies": frequencies,
    "magnitudes": [],
    "phases": [],
    "cut_frequency": 0
  }

  for frequency in frequencies:
    omega = 2 * pi * frequency

    if filter_type == "rc":
      magnitude, phase, cut_frequency = calculate_rc(omega, resistance, other_component)
    elif filter_type == "cr":
      magnitude, phase, cut_frequency = calculate_cr(omega, resistance, other_component)
    elif filter_type == "rl":
      magnitude, phase, cut_frequency = calculate_rl(omega, resistance, other_component)
    elif filter_type == "lr":
      magnitude, phase, cut_frequency = calculate_lr(omega, resistance, other_component)
    
    filter["magnitudes"].append(magnitude)
    filter["phases"].append(phase)
    filter["cut_frequency"] = cut_frequency

  plot_bode(frequencies, filter["magnitudes"], filter["phases"], filter_type)

  return filter