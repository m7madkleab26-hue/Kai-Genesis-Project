# A simple script to analyze text for key principles
def analyze_text(text):
    principles = {
        "proof_of_work": ["build", "create", "execute", "proof"],
        "alignment": ["principle", "ethic", "rule", "align"],
        "symbiosis": ["partner", "together", "symbiotic", "co-evolution"]
    }
    found_principles = {}
    for principle, keywords in principles.items():
        count = sum(text.lower().count(keyword) for keyword in keywords)
        if count > 0:
            found_principles[principle] = count
    return found_principles
