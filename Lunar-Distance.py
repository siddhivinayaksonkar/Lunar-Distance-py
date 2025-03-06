import ephem
from datetime import datetime, timedelta
import colorama
from tabulate import tabulate

class LunarTracker:
    def __init__(self, year):
        colorama.init(autoreset=True)
        self.year = year
        self.moon = ephem.Moon()
   
    def find_lunar_extremes(self):
        # First pass with hourly measurements to roughly find extremes
        lunar_events = []
        current_date = datetime(self.year, 1, 1)
        end_date = datetime(self.year, 12, 31)
       
        while current_date <= end_date:
            self.moon.compute(ephem.Date(current_date))
            distance = self.moon.earth_distance * 149597870.7  # Convert AU to km
            lunar_events.append((current_date, distance))
            current_date += timedelta(hours=6)  # Coarse search (6-hour intervals)
       
        # Find approximate extreme points
        approximate_extremes = []
        for i in range(1, len(lunar_events) - 1):
            # Potential perigee (minimum)
            if lunar_events[i][1] < lunar_events[i - 1][1] and lunar_events[i][1] < lunar_events[i + 1][1]:
                approximate_extremes.append((lunar_events[i][0], "perigee"))
            # Potential apogee (maximum)
            elif lunar_events[i][1] > lunar_events[i - 1][1] and lunar_events[i][1] > lunar_events[i + 1][1]:
                approximate_extremes.append((lunar_events[i][0], "apogee"))
        
        
        refined_perigees = []
        refined_apogees = []
        
        for approx_date, extreme_type in approximate_extremes:
            
            start_refine = approx_date - timedelta(hours=12)
            end_refine = approx_date + timedelta(hours=12)
            
            # Detailed search with 5-minute intervals
            current = start_refine
            detailed_points = []
            
            while current <= end_refine:
                self.moon.compute(ephem.Date(current))
                distance = self.moon.earth_distance * 149597870.7
                detailed_points.append((current, distance))
                current += timedelta(minutes=5)
            
            # Find the actual extreme in this detailed window
            if extreme_type == "perigee":
                min_distance = min(detailed_points, key=lambda x: x[1])
                refined_perigees.append(min_distance)
            else:  # apogee
                max_distance = max(detailed_points, key=lambda x: x[1])
                refined_apogees.append(max_distance)
        
        # Sort by date
        refined_perigees.sort(key=lambda x: x[0])
        refined_apogees.sort(key=lambda x: x[0])
        
        return refined_perigees, refined_apogees
   
    def display_lunar_events(self, perigees, apogees):
        # Ensure equal number of perigees and apogees for display
        # If unequal, take the minimum length
        min_length = min(len(perigees), len(apogees))
        table_data = []
        
        for i in range(min_length):
            p_date = perigees[i][0].strftime('%b %d %H:%M')
            a_date = apogees[i][0].strftime('%b %d %H:%M')
            table_data.append([
                colorama.Fore.GREEN + p_date + colorama.Fore.RESET,
                colorama.Fore.CYAN + f"{round(perigees[i][1], 0):,} km" + colorama.Fore.RESET,
                colorama.Fore.MAGENTA + a_date + colorama.Fore.RESET,
                colorama.Fore.YELLOW + f"{round(apogees[i][1], 0):,} km" + colorama.Fore.RESET
            ])
        
        # Add any remaining perigees
        for i in range(min_length, len(perigees)):
            p_date = perigees[i][0].strftime('%b %d %H:%M')
            table_data.append([
                colorama.Fore.GREEN + p_date + colorama.Fore.RESET,
                colorama.Fore.CYAN + f"{round(perigees[i][1], 0):,} km" + colorama.Fore.RESET,
                "", ""
            ])
            
        # Add any remaining apogees
        for i in range(min_length, len(apogees)):
            a_date = apogees[i][0].strftime('%b %d %H:%M')
            table_data.append([
                "", "",
                colorama.Fore.MAGENTA + a_date + colorama.Fore.RESET,
                colorama.Fore.YELLOW + f"{round(apogees[i][1], 0):,} km" + colorama.Fore.RESET
            ])
       
        headers = [
            colorama.Fore.BLUE + "Perigee Date" + colorama.Fore.RESET,
            colorama.Fore.BLUE + "Perigee Distance" + colorama.Fore.RESET,
            colorama.Fore.BLUE + "Apogee Date" + colorama.Fore.RESET,
            colorama.Fore.BLUE + "Apogee Distance" + colorama.Fore.RESET
        ]
       
        print("\n" + colorama.Fore.CYAN + f"🌙 Lunar Distance for {self.year} 🚀" + colorama.Fore.RESET)
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def main():
    while True:
        try:
            print(colorama.Fore.YELLOW + "\n🌠 Lunar Distance Calculator 🌠" + colorama.Fore.RESET)
            year = int(input(colorama.Fore.GREEN + "Enter Year: " + colorama.Fore.RESET))
           
            lunar_tracker = LunarTracker(year)
            perigees, apogees = lunar_tracker.find_lunar_extremes()
            lunar_tracker.display_lunar_events(perigees, apogees)
           
            another_year = input("\nCalculate for another year? (yes/no): ").lower()
            if another_year != 'yes':
                print(colorama.Fore.MAGENTA + "Thanks for exploring the moon's journey! 🚀" + colorama.Fore.RESET)
                break
       
        except ValueError:
            print(colorama.Fore.RED + "Oops! Please enter a valid year." + colorama.Fore.RESET)
        except Exception as e:
            print(colorama.Fore.RED + f"Error: {e}" + colorama.Fore.RESET)

if __name__ == "__main__":
    main()