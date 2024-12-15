from lib.bode import bode_plotter
from lib.utils import save_bode_json 

resistance = 1e3
other_component = 1e-8

# rc filter

rc_filter_type = "rc"
rc_filter_file = "./outputs/rc_filter.json"

rc_filter_results = bode_plotter(resistance, other_component, rc_filter_type, 1, 1e5, 5000)
save_bode_json(resistance, other_component, rc_filter_type, rc_filter_results, rc_filter_file)

# cr filter

cr_filter_type = "cr"
cr_filter_file = "./outputs/cr_filter.json"

cr_filter_results = bode_plotter(resistance, other_component, cr_filter_type, 1, 1e5, 5000)
save_bode_json(resistance, other_component, cr_filter_type, cr_filter_results, cr_filter_file)

# rl filter

rl_filter_type = "rl"
rl_filter_file = "./outputs/rl_filter.json"

rl_filter_results = bode_plotter(resistance, other_component, rl_filter_type, 1, 1e5, 5000)
save_bode_json(resistance, other_component, rl_filter_type, rl_filter_results, rl_filter_file)

# lr filter

lr_filter_type = "lr"
lr_filter_file = "./outputs/lr_filter.json"

lr_filter_results = bode_plotter(resistance, other_component, lr_filter_type, 1, 1e5, 5000)
save_bode_json(resistance, other_component, lr_filter_type, lr_filter_results, lr_filter_file)