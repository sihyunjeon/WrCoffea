import uproot
import os
import dask
from dask.diagnostics import ProgressBar

def save_histograms(all_histograms, filename):
    output_dir = "root_outputs"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, filename)

    with uproot.recreate(f"{filename}") as root_file:
        hists = []
        mass_tuples = []
        for sample, sample_info in all_histograms.items():
            mc = sample_info['mc']
            process = sample_info['process']
            hist_dict = sample_info['hist_dict']
            for region, hist_obj in hist_dict.items():
                if "vals" not in region:
                    channel, mll_range = region.split('_')
                    directory_path = f"{mc}/{process}/{channel}/{mll_range}/"
                    for hist_name, hist_data in hist_obj.__dict__.items():
                        if "cuts" not in hist_name:
                            hists.append((directory_path + hist_name, hist_data))

        print("\nComputing histograms...")
        with ProgressBar():
            (histograms,)= dask.compute(hists)

        for path, hist in histograms:
            root_file[path] = hist
            
    print(f"Histograms saved to {output_file}.\n")
