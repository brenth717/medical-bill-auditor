#!/usr/bin/env python3
import json

def analyze_bill(text):
    # Simple analysis for demo
    return {
        "duplicate_charges": [{"code": "85025", "description": "CBC", "amount": 52.00}],
        "overcharges": [],
        "potential_savings": 52.00
    }

if __name__ == "__main__":
    print(json.dumps(analyze_bill("sample"), indent=2))
