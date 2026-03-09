import os
import glob
from openai import OpenAI

client = OpenAI()

def call_gpt52(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-5.2",
            reasoning_effort="high",
            messages=[{"role": "system", "content": "You are a qualitative research assistant helping a human research team with phenomenological analysis."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling gpt-5.2: {e}")
        return str(e)

def main():
    # Replaced Qualtrics response IDs with generic placeholders
    transcripts_to_process = ['Participant_A', 'Participant_B', 'Participant_C']
    
    # Markdown headers aligned with the manuscript workflow
    phase2_content = "# Post-Phase 2 LLM Expansion (Processed via GPT-5.2)\n\n"
    phase4_content = "# Post-Phase 4 LLM Expansion (Processed via GPT-5.2)\n\n"
    
    for t_id in transcripts_to_process:
        with open(f"{t_id}_transcript.txt", "r") as f:
            text = f.read()
            
        print(f"Generating Post-Phase 2 Expansion for {t_id}...")
        prompt_p2 = f"""Review the following transcript and generate a candidate analytic memo and meaning units for it.
Format your output in Markdown with two sections:
### Candidate Analytic Memo
(Paragraph summarizing the holistic sense of the transcript)
### Candidate Meaning Units
(Numbered list of meaning units capturing phrases, moments, and expressions)

Transcript:
{text}
"""
        p2_res = call_gpt52(prompt_p2)
        phase2_content += f"## Transcript: {t_id}\n{p2_res}\n\n"
        
        print(f"Generating Post-Phase 4 Expansion for {t_id}...")
        prompt_p4 = f"""Review the following transcript and generate a provisional within-case summary and candidate thematic groupings for it.
Format your output in Markdown with two sections:
### Provisional Within-Case Summary
(Paragraph synthesizing the textural and structural meaning)
### Candidate Thematic Groupings
(List of themes with brief descriptions based on the transcript)

Transcript:
{text}
"""
        p4_res = call_gpt52(prompt_p4)
        phase4_content += f"## Transcript: {t_id}\n{p4_res}\n\n"
        
    with open("Post_Phase2_LLM_Expansion.md", "w") as f:
        f.write(phase2_content)
        
    with open("Post_Phase4_LLM_Expansion.md", "w") as f:
        f.write(phase4_content)
        
    print("Done generating new GPT-5.2 outputs.")

if __name__ == "__main__":
    main()
