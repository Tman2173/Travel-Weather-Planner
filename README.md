# Travel-Weather-Planner
An interactive Python script that takes user input to recommend the best way to travel based on distance, weather, and available transportation.

## How It Works

The script collects five inputs from the user and runs them through a series of conditional checks:

### Decision Logic

- **≤ 1 mile + no rain** → Recommends walking
- **1–6 miles + bike + no rain** → Recommends biking
- **6+ miles + car or ride-share** → Recommends driving
- **Rain + no viable option** → Advises against traveling

## Usage

Run the script and answer the prompts:

```bash
python travel_planner.py
```
## What I Learned

- Converting string responses to booleans
- Python conditional logic (`if / elif / else`)
- Boolean expressions and compound conditions with `and` / `or`
- Using f-strings for personalized output

## Course

Built as a lab exercise from the [freeCodeCamp Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) course.
