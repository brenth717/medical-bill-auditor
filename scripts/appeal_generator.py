#!/usr/bin/env python3
from datetime import datetime

def generate_appeal(patient, bill_info, analysis):
    # Simple template
    letter = datetime.now().strftime('%B %d, %Y') + "\n\n"
    letter += bill_info.get('hospital', 'Hospital') + "\n\n"
    letter += "RE: Billing Correction Request\n\n"
    letter += "To Whom It May Concern:\n\n"
    letter += "I found a duplicate charge on my bill.\n\n"
    letter += "Sincerely,\n"
    letter += patient.get('name', 'Patient')
    return letter

if __name__ == "__main__":
    print(generate_appeal(
        {"name": "John Doe"}, 
        {"hospital": "Memorial Hospital"}, 
        {"duplicate_charges": []}
    ))
