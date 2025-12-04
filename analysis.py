# This Marimo notebook demonstrates interactive data analysis
# Author: 23f1001452@ds.study.iitm.ac.in

import marimo

app = marimo.App()

# ---- Cell 1: Imports and slider widget ----
# Exposes: slider
@app.cell
def __(mo):
    # Slider controls the scaling factor
    slider = mo.ui.slider(start=1, stop=10, step=1, value=5, label="Scaling Factor")
    slider
    return slider, 

# ---- Cell 2: Data creation depending on slider ----
# Depends on: slider
# Exposes: scaled_data
@app.cell
def __(slider):
    import numpy as np

    base_data = np.arange(1, 11)  # 1 to 10
    scaled_data = base_data * slider.value  # Dependency on slider value

    scaled_data
    return scaled_data,

# ---- Cell 3: Dynamic markdown based on computed data ----
# Depends on: scaled_data, slider
@app.cell
def __(scaled_data, slider, mo):
    mo.md(f"""
    ### Interactive Analysis Output

    **Current slider value:** `{slider.value}`  
    **Scaled dataset:** `{list(scaled_data)}`

    The data is multiplied by the slider value, demonstrating  
    a simple variable dependency within this interactive notebook.
    """)
    return ()

# ---- Run app ----
if __name__ == "__main__":
    app.run()
