# Lunar-Distance-py
 calculates and displays the Moon's closest (perigee) and farthest (apogee) distances from Earth for a given year using Two-pass algorithm:
First pass uses a coarser 6-hour interval to identify approximate locations of extremes
Second pass zooms in with 5-minute intervals around these approximate times
 <br><br>
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
<br>

## ✨ Features
- **Astronomical Accuracy**: Uses `ephem` for precise lunar position calculations.
- **Two-Phase Search**:
  - **Coarse Search**: 6-hour intervals to approximate events.
  - **Refined Search**: 5-minute intervals near extremes for precision.
- **Colorful CLI**: Terminal output with emojis and colored text.
- **Tabular Display**: Neatly formatted tables using `tabulate`.

---

## 📥 Installation
1. Clone the repository:

   ```bash
    git clone https://github.com/siddhivinayaksonkar/Lunar-Distance-py
   
2.   Install dependencies:

    pip install ephem colorama tabulate
    
##  📝 Notes

  - Time Zones: All times are in UTC.

  - Accuracy: Results may vary slightly from other sources due to algorithmic differences.

  - Search Window: Refinement uses a 24-hour window (12 hours before/after the coarse estimate).

    
 ## 🙏 Acknowledgments
- [`ephem`](https://rhodesmill.org/pyephem/) for providing the astronomical calculations.
- `colorama` and `tabulate` for enhancing terminal output readability.

