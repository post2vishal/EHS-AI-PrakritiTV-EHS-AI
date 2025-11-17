import os
from grok_api import GrokClient  # xAI API (get key from x.ai/api)
# Assume AnantAI as custom class (add his knowledge here)
class AnantAI:
    def __init__(self):
        self.knowledge_base = "Infinite EHS sims: Vedic zero-waste + NEP compliance"
    def simulate_risk(self, scenario):
        return f"AnantAI: {scenario} → Sustainable fix: Circular economy loop."

# xAI Integration
grok = GrokClient(api_key=os.getenv('XAI_API_KEY'))

def ehs_query(query):
    anant = AnantAI()
    base_risk = anant.simulate_risk(query)
    grok_response = grok.chat(f"EHS Risk: {query}. Explain with SHAP: {base_risk}")
    return f"{base_risk}\nGrok Insight: {grok_response}"

if __name__ == "__main__":
    print(ehs_query("Factory chemical leak in Bihar farm"))
