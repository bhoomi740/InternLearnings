import json
import re
def substitutor():
    sen1 = "It is sunny outside."
    print(re.sub(r"sunny", "raining", sen1))
    sen2 = "This is Python Course"
    print(re.sub(r"Course", "Tutorial", sen2))
substitutor()