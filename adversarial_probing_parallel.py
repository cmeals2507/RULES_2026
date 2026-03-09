import json
import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Segment replaced with placeholder to protect participant PII
# Note: As described in Meals & Waier RULES 2026, this script uses adversarial
# processes to minimize output drift and explore multiple qualitative lenses.
segment = """[Insert participant transcript segment here. Example: 'My time in marching band taught me a lot about life...']"""

def call_llm(system_prompt, user_prompt, model="gpt-4o"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

# --- ADVERSARIAL PROBING ---
print("--- Adversarial Probing ---")
probing_prompt_1 = f"""Analyze the following transcript segment. What underlying insecurities or anxieties about the transition to adulthood might this participant be masking by overemphasizing the pragmatic, resume-building 'tangible' benefits of marching band? Provide a critical reading.
Transcript Segment:
{segment}"""

probing_prompt_2 = f"""Analyze the following transcript segment. Could the participant's repeated references to leadership roles (section leader, drum major) be interpreted not as genuine personal growth, but rather as an internalization of a hierarchical, compliance-driven structure inherent in marching band culture? Provide a critical reading.
Transcript Segment:
{segment}"""

probing_prompt_3 = f"""Analyze the following transcript segment. In what ways might the participant's focus on structured activities and 'problem solving' reflect a reliance on rigid, external frameworks to cope with unstructured everyday life? Provide a critical reading.
Transcript Segment:
{segment}"""

print("Probing 1 (Masking Insecurities):")
print(call_llm("You are a critical discourse analyst.", probing_prompt_1))
print("\n" + "="*50 + "\n")

print("Probing 2 (Internalization of Hierarchy):")
print(call_llm("You are a critical discourse analyst.", probing_prompt_2))
print("\n" + "="*50 + "\n")

print("Probing 3 (Reliance on Rigidity):")
print(call_llm("You are a critical discourse analyst.", probing_prompt_3))
print("\n" + "="*50 + "\n")


# --- PARALLEL ANALYSIS ---
print("--- Parallel Analysis ---")
parallel_prompt_1 = f"""Analyze the following transcript segment through the lens of pure hermeneutic phenomenology. Focus strictly on the lived experience being described, staying as close to the participant's explicit meaning as possible without imposing external sociological frameworks. What does this reveal about what it *feels like* to experience leadership in this context?
Transcript Segment:
{segment}"""

parallel_prompt_2 = f"""Analyze the following transcript segment from the perspective of organizational socialization and identity development theory. How does the participant's trajectory through different roles contribute to their current professional identity and self-concept?
Transcript Segment:
{segment}"""

parallel_prompt_3 = f"""Analyze the following transcript segment focusing specifically on the language and rhetoric used. How does the participant construct the narrative of 'before and after' (youth vs. adulthood), and what do words like 'tangible' and 'benefits' reveal about their value system?
Transcript Segment:
{segment}"""

print("Parallel 1 (Hermeneutic Phenomenology):")
print(call_llm("You are a qualitative researcher.", parallel_prompt_1))
print("\n" + "="*50 + "\n")

print("Parallel 2 (Organizational Socialization):")
print(call_llm("You are a qualitative researcher.", parallel_prompt_2))
print("\n" + "="*50 + "\n")

print("Parallel 3 (Narrative/Rhetorical Analysis):")
print(call_llm("You are a qualitative researcher.", parallel_prompt_3))
print("\n" + "="*50 + "\n")
