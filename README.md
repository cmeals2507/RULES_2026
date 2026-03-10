# LLM Phenomenology Analysis Scripts

This directory contains the Python scripts utilized to prep, transcribe, and phenomenologically analyze the *Tell Us Your Story* interviews via the OpenAI API.
> Note: All scripts have been cleaned to fully obscure participant internal IDs and directly identifiable text segments in adherence with our IRB and PII protections.
> 
## 1. Data Preparation
- **`data_peek.py` & `data_peek2.py`**: Utility scripts intended to read qualitative data from the initial Qualtrics `.xlsx` export to identify which rows successfully logged linked audio recordings.
- **`transcribe.py`**: Batch processes raw `.m4a` audio files utilizing OpenAI's Whisper-1 model, producing raw `_transcript.txt` text files dynamically. 
- **`add_headers.py`**: Extracts high school, college, and drum corps demographic survey metadata from the `.csv` sheet, calculates total performing years via regex logic on string subsets, and prepends this metadata to the top of each text file to ground the LLM's upcoming read of the transcripts.
  
## 2. Analysis
- **`analyze.py`**: The core API pipeline sequence for Phenomenological analysis modeling human phases.
  - Phase 1 & 2: Holistic Reading & Meaning Unit Extraction (returns JSON)
  - Phase 3 & 4: Interpretive Thematizing & Whole-Part Descriptions (returns JSON)
  - Phase 5: Cross-Narrative Synthesis (Outputs final summary paragraph)
- **`run_gpt52_expansion.py`**: Secondary extraction script targeting individual candidate transcripts. Used strictly GPT-5.2 (High-Reasoning effort) to produce "Candidate Analytic Memos", "Provisional Within-Case Summaries", and "Candidate Thematic Groupings" directly to Markdown arrays representing Post-Phase 2 and Post-Phase 4 API expansions. 
- **`adversarial_probing_parallel.py`**: Code exploring multiple methodological lenses by tasking the system prompting to adopt different personas (Critical Discourse Analyst, Hermeneutic Phenomenologist, Organizational/Identity Theorist). Used on target segments through adversarial processes to minimize output drift and evaluate LLM perspectival shifts.
  
## 3. Fine-Tuning Plan
- **`fine_tuning_plan.md`**: Methodology and workflow document outlining the next phase of the project — fine-tuning Llama 3.3 70B on Microsoft Azure AI Foundry for use in a multi-stage phenomenological analysis pipeline. Describes the methodological instruction tuning approach, training parameters, target training quantities across three sequential stages (holistic memoing and meaning unit identification, provisional themes and whole-part synthesis, cross-case synthesis) and one floating stage (self-evaluation through adversarial prompting), estimated costs, and stage-level deliverables.
- **`sample-finetuning.jsonl`**: A sample file for model fine-tuning.
  
## 4. RULES 2026 Appendix
- **`Online_Appendix.md`**: A supplementary document providing full transparency into the study's hybrid analytical process. It presents direct comparisons between human-coded analysis (holistic memos, meaning units, provisional themes, and whole-part synthesis) and machine-generated expansion outputs via GPT-5.2. Furthermore, it details the exact prompts, system instructions, and formatting directives utilized across all API phases to ensure methodological audibility.
