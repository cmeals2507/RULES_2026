import os
import glob
import json
import time
from openai import OpenAI
from pathlib import Path

client = OpenAI()

def call_llm(prompt, model="gpt-4o"): # fallback to gpt-4o if gpt-5.2 fails
    try:
        # User requested GPT-5.2-high reasoning
        response = client.chat.completions.create(
            model="gpt-5.2",
            reasoning_effort="high",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        model_used = "gpt-5.2"
    except Exception as e:
        print(f"gpt-5.2 failed, trying {model}: {e}")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        model_used = model
        
    log = {
        "timestamp": time.time(),
        "model": model_used,
        "prompt": prompt,
        "response": response.choices[0].message.content,
        "usage": json.loads(response.model_dump_json()).get('usage') if hasattr(response, 'model_dump_json') else None
    }
    return response.choices[0].message.content, log

def main():
    transcripts = glob.glob('*_transcript.txt')
    api_logs = []
    results = {}
    
    # Phase 1 & 2: Holistic Reading and Meaning Unit Extraction per transcript
    for t_file in transcripts:
        response_id = t_file.replace('_transcript.txt', '')
        print(f"Processing {response_id}...")
        
        with open(t_file, 'r') as f:
            text = f.read()
            
        # API Pass 1 -> Corresponds to Manuscript Phase 1 (Holistic Reading) & Phase 2 (Meaning Units)
        prompt1 = f"""You are a hermeneutic phenomenological researcher.
Perform a holistic reading of the following transcript. Identify "meaning units" that capture phrases, moments, and expressions central to the participant's lived experience of marching arts membership.
Provide output as a JSON object with a key 'meaning_units' which is a list of strings.
Transcript:
{text}
"""
        pass1_out, log1 = call_llm(prompt1)
        api_logs.append(log1)
        
        # API Pass 2 -> Corresponds to Manuscript Phase 3 (Provisional Thematizing) & Phase 4 (Whole-Part Synthesis)
        prompt2 = f"""You are a hermeneutic phenomenological researcher.
Given the transcript and meaning units, perform interpretive thematizing and whole-part reconciliation. Develop these into textural and structural descriptions reflecting core dimensions of experience.
Output as a JSON object with a key 'themes' containing a list of objects (with 'theme_name' and 'description').
Transcript:
{text}
Meaning Units:
{pass1_out}
"""
        pass2_out, log2 = call_llm(prompt2)
        api_logs.append(log2)
        
        results[response_id] = {
            "transcript": text,
            "pass1_meaning_units": json.loads(pass1_out),
            "pass2_themes": json.loads(pass2_out)
        }
        
    # API Pass 3 -> Corresponds to Manuscript Phase 5 (Cross-Case Synthesis)
    print("Performing cross-narrative synthesis...")
    all_themes_str = json.dumps({rid: data['pass2_themes'] for rid, data in results.items()}, indent=2)
    prompt3 = f"""You are a hermeneutic phenomenological researcher.
Synthesize the following themes from all participants into a phenomenological cross-narrative synthesis. Find overarching patterns and connections. Write a highly eloquent paragraph sharing the main findings and insights into the lived experience ("what is it like to be a marching arts member?").
Output a JSON object with 'cross_narrative_synthesis' and 'findings_paragraph'.
Themes:
{all_themes_str}
"""
    pass3_out, log3 = call_llm(prompt3)
    api_logs.append(log3)
    final_synthesis = json.loads(pass3_out)
    
    # Save outputs
    with open('analysis_results.json', 'w') as f:
        json.dump({"individual_analysis": results, "synthesis": final_synthesis}, f, indent=2)
        
    with open('api_logs.json', 'w') as f:
        json.dump(api_logs, f, indent=2)
        
    with open('findings_paragraph.txt', 'w') as f:
        f.write(final_synthesis['findings_paragraph'])
        
    print("Done. Saved analysis_results.json, api_logs.json, findings_paragraph.txt")

if __name__ == "__main__":
    main()
