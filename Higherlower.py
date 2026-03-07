import random
#sorry has to keep it all here because using only single repo 
data = [
    {"name": "Without oxygen 🫁", "description": "before brain damage begins", "value": 0.08},
    {"name": "Holding breath underwater 🌊", "description": "average untrained human", "value": 0.03},
    {"name": "Without blood circulation ❤️", "description": "before fatal organ failure", "value": 0.1},
    {"name": "In freezing water 🧊", "description": "before hypothermia becomes fatal", "value": 0.9},
    {"name": "Without shelter in extreme cold ❄️", "description": "exposure survival", "value": 4},
    {"name": "Without sleep 😴", "description": "recorded extreme sleep deprivation", "value": 263},
    {"name": "Without water 💧", "description": "average dehydration survival", "value": 73},
    {"name": "Without food 🍽️", "description": "with water available", "value": 719},
    {"name": "Without sunlight ☀️", "description": "before serious vitamin D deficiency", "value": 2161},
    {"name": "Without gravity (space exposure) 🚀", "description": "without protection", "value": 0.02},
    {"name": "Without bathroom (urination) 🚻", "description": "before bladder danger", "value": 25},
    {"name": "Without blinking 👁️", "description": "before eye damage occurs", "value": 1.1},
    {"name": "Without body heat regulation 🌡️", "description": "severe heatstroke scenario", "value": 6.4},
    {"name": "Without salt intake 🧂", "description": "severe electrolyte imbalance", "value": 722},
    {"name": "Without sugar intake 🍬", "description": "extreme hypoglycemia risk", "value": 46},
    {"name": "Without movement 🛌", "description": "complete immobilization complications", "value": 335},
    {"name": "Without swallowing 🥤", "description": "severe dehydration risk", "value": 49},
    {"name": "Without blinking during screen use 💻", "description": "eye strain limit", "value": 0.6},
    {"name": "Without shade in extreme heat 🌞", "description": "desert exposure survival", "value": 5.3},
    {"name": "Without any sensory input 🧠", "description": "severe sensory deprivation tolerance", "value": 81},
    {"name": "Without clean drinking water in extreme heat 🏜️", "description": "rapid dehydration scenario", "value": 37},
    {"name": "Without shade in a desert at noon 🔥", "description": "heatstroke risk", "value": 5.8},
    {"name": "Trapped in a hot car 🚗", "description": "dangerous heat buildup", "value": 2.7},
    {"name": "Floating in cold ocean water 🌊", "description": "hypothermia survival time", "value": 3.6},
    {"name": "Buried under snow ⛄", "description": "air pocket survival estimate", "value": 1.7},
    {"name": "Trapped in an airtight small room 🏠", "description": "oxygen depletion", "value": 6.9},
    {"name": "Lost in a forest with water but no food 🌲", "description": "starvation timeline", "value": 601},
    {"name": "Lost at sea without fresh water 🌊", "description": "dehydration from salt exposure", "value": 47},
    {"name": "Extreme dehydration during intense exercise 🏃", "description": "collapse risk", "value": 9.2},
    {"name": "Exposed to freezing rain without shelter 🌧️", "description": "hypothermia development", "value": 7.6},
    {"name": "Trapped underground with limited oxygen ⛏️", "description": "oxygen depletion risk", "value": 8.4},
    {"name": "Stranded on a mountain without shelter 🏔️", "description": "cold exposure survival", "value": 13},
    {"name": "Extreme heat without hydration 🔥", "description": "heatstroke survival", "value": 8.9},
    {"name": "Locked in a sealed vehicle 🚘", "description": "oxygen and heat buildup", "value": 7.2},
    {"name": "Severe sleep deprivation during stress 😵", "description": "functional collapse limit", "value": 199},
    {"name": "Extreme fasting with minimal nutrients 🍽️", "description": "starvation scenario", "value": 801},
    {"name": "Total darkness confinement 🌑", "description": "psychological tolerance estimate", "value": 95},
    {"name": "Extreme cold wind exposure 🌬️", "description": "wind chill hypothermia", "value": 5.1},
    {"name": "No fluid intake during heavy heatwave 🌡️", "description": "dehydration limit", "value": 41},
    {"name": "Trapped in debris with limited airflow 🧱", "description": "oxygen availability", "value": 7.9}
]
def select(data):
    return random.randrange(0,len(data))
def compare(val1,val2):
    if val1 > val2:
        return "a"
    return "b"
    
def main(data,first, score):
    print("\n*20")
    print(r''' 
 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |     _____    | || |    ______    | || |  ____  ____  | |
| | |_   ||   _| | || |    |_   _|   | || |  .' ___  |   | || | |_   ||   _| | |
| |   | |__| |   | || |      | |     | || | / .'   \_|   | || |   | |__| |   | |
| |   |  __  |   | || |      | |     | || | | |    ____  | || |   |  __  |   | |
| |  _| |  | |_  | || |     _| |_    | || | \ `.___]  _| | || |  _| |  | |_  | |
| | |____||____| | || |    |_____|   | || |  `._____.'   | || | |____||____| | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
     .----------------.  .----------------.                                     
    | .--------------. || .--------------. |                                    
    | |     ____     | || |  _______     | |                                    
    | |   .'    `.   | || | |_   __ \    | |                                    
    | |  /  .--.  \  | || |   | |__) |   | |                                    
    | |  | |    | |  | || |   |  __ /    | |                                    
    | |  \  `--'  /  | || |  _| |  \ \_  | |                                    
    | |   `.____.'   | || | |____| |___| | |                                    
    | |              | || |              | |                                    
    | '--------------' || '--------------' |                                    
     '----------------'  '----------------'                                     
         .----------------.  .----------------.  .----------------.             
        | .--------------. || .--------------. || .--------------. |            
        | |   _____      | || |     ____     | || | _____  _____ | |            
        | |  |_   _|     | || |   .'    `.   | || ||_   _||_   _|| |            
        | |    | |       | || |  /  .--.  \  | || |  | | /\ | |  | |            
        | |    | |   _   | || |  | |    | |  | || |  | |/  \| |  | |            
        | |   _| |__/ |  | || |  \  `--'  /  | || |  |   /\   |  | |            
        | |  |________|  | || |   `.____.'   | || |  |__/  \__|  | |            
        | |              | || |              | || |              | |            
        | '--------------' || '--------------' || '--------------' |            
         '----------------'  '----------------'  '----------------'  ''')
    second = select(data)
    while second == first:
        second = select(data)
    second_item = data[second]
    first_item = data[first]
    second_val = second_item["value"]
    first_val = first_item["value"]
    correct_answer = compare(first_val,second_val)
    print(f"Compare option A {first_item["name"]}: {first_item["description"]}")
    print(r'''            
            
            
            
▀█▄ ██▀▄██▀█
 ██▄██ ▀███▄
  ▀█▀ █▄▄██▀
            
            ''')
    print(f"to option B {second_item["name"]}: {second_item["description"]}")
    user_input = input("Enter your Answer 'A' or 'B' : ").lower()
    if user_input == correct_answer:
        score += 1
        print(f"correct answer Current Score  = {score}")
        main(data=data, first= second, score = score)
    else:
        print(f"Wrong Answer Your Score is {score} Better luck Next time")
val  = select(data)
main(data= data, first= val, score= 0)