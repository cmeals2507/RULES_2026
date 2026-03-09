import csv
import os
import re

def calculate_years(text):
    if not text:
        return 0
    # Find all year ranges like YYYY-YYYY or YYYY to YYYY
    total_years = 0
    matches = re.findall(r'(\d{4})\s*[-to]+\s*(\d{4})', text)
    for start, end in matches:
        total_years += (int(end) - int(start) + 1)
    return total_years

def process():
    csv_file = 'participant_responses.csv' # Replaced exact filename for privacy
    # Replaced Qualtrics response IDs with generic placeholders
    transcripts_to_process = ['Participant_A', 'Participant_B', 'Participant_C', 'Participant_D', 'Participant_E']
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            response_id = row['ResponseId']
            if response_id in transcripts_to_process:
                q5 = row.get('Q5', '')   # Gender
                q3 = row.get('Q3', '')   # Instrument
                q8 = row.get('Q8', '')   # Activities
                q9 = row.get('Q9', '')   # HS
                q10 = row.get('Q10', '') # College
                q11 = row.get('Q11', '') # DCI
                
                # Calculate years
                hs_years = calculate_years(q9)
                college_years = calculate_years(q10)
                dci_years = calculate_years(q11)
                total_years = hs_years + college_years + dci_years
                
                header = (
                    f"--- METADATA ---\n"
                    f"ResponseID: {response_id}\n"
                    f"Gender (Q5): {q5}\n"
                    f"Primary Instrument (Q3): {q3}\n"
                    f"Activities (Q8): {q8}\n"
                    f"High School Info (Q9): {q9} (Years: {hs_years})\n"
                    f"College Info (Q10): {q10} (Years: {college_years})\n"
                    f"Drum Corps Info (Q11): {q11} (Years: {dci_years})\n"
                    f"Total Membership Years: {total_years}\n"
                    f"----------------\n\n"
                )
                
                transcript_file = f"{response_id}_transcript.txt"
                if os.path.exists(transcript_file):
                    with open(transcript_file, 'r', encoding='utf-8') as tf:
                        content = tf.read()
                    
                    if not content.startswith("--- METADATA ---"):
                        with open(transcript_file, 'w', encoding='utf-8') as tf:
                            tf.write(header + content)
                        print(f"Added header to {transcript_file}")
                    else:
                        print(f"Header already exists in {transcript_file}")
                else:
                    print(f"Transcript not found: {transcript_file}")

if __name__ == '__main__':
    process()
