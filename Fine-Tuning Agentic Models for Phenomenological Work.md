# **Fine-Tuning Agentic Models for Phenomenological Work**

## **Overview**

To achieve greater accuracy and validity in AI-assisted phenomenological work, we propose fine-tuning a large, agentic large language model (LLM) and integrating it into a multi-agent analysis workflow. Fine-tuning is an additional training process that adjusts a model’s internal weights using structured data, producing outputs more strongly aligned with the target task.  
For phenomenological work, this additional context will consist of chains-of-thought that explicitly detail the process by which target outputs are generated. We term this approach “methodological instruction tuning” rather than supervised fine-tuning. The training data will include validated examples of user prompts, raw transcript text, and system-level outputs for each analysis step (e.g., boundary justifications and interpretive notes for meaning unit identification).  
Two training parameters will constrain the model’s behavior. First, setting the temperature to 0.35 (below the high-creativity threshold of 0.7) increases the likelihood that training data will be interpreted deterministically, allowing the model to use empathetic, interpretive language without parroting training examples. Second, setting the weight decay value to .01 during training reduces the risk of overfitting by preventing excessively large neural weights. Together, these parameters force the LLM to learn generalizable behavior from the training data rather than memorize specific examples.

## **Training**

We plan to fine-tune a copy of Llama 3.3 70B, securely hosted on Microsoft Azure’s AI Foundry. This platform was selected for its zero data retention policy, which further supports the security and anonymity of participant data.

Because the model will be used across all stages of analysis, we will employ multi-task fine-tuning. Training data will include task prefixes specifying the analysis stage, prepended to each entry. Aligned with our pilot methodology, we identify three sequential stages and one floating stage:

* **Stage 1 — Holistic Memoing and Meaning Unit Identification:** After the research team completed human coding of the seed transcripts through Phase 2, the LLM reviewed each remaining transcript and generated candidate analytic memos and meaning units, which were then audited against the source transcripts and retained or discarded before entering the next phase of analysis.

* **Stage 2 — Provisional Themes and Whole-Part Synthesis:** After the research team completed whole-part synthesis of the seed transcripts through Phase 4, the LLM generated provisional within-case summaries and candidate thematic groupings for the remaining transcripts, which were audited, retained, or discarded, and then used alongside human-coded materials to surface candidate experiential categories for cross-case review.

* **Stage 3 — Cross-Case Synthesis:** After we completed cross-case synthesis of the seed transcripts, a portion of the retained LLM output was combined with the human-coded materials to surface candidate experiential categories, which we then evaluated, edited, or rejected against the full corpus before independently developing the conditional essence.

* **Floating Stage — Self-Evaluation Through Adversarial Prompting:** After each LLM-assisted phase, the model is prompted to critique its own outputs against the source transcripts and the research team’s audit trail, flagging candidate hallucinations, unsupported inferences, and drift before human review begins. Applied to Stages 1 and 2, respectively.

Instead of simple input–output pairs, training data will incorporate prompts, context, and multiple iterative responses designed to teach the model the behavioral targets and to force it to synthesize the methodological choices that underpin those outputs. Target quantities for training examples are as follows:

* Stage 1, main process: 500 examples, equally divided between holistic memoing and meaning unit identification.

* Stage 1, self-evaluation: 400 examples, equally divided between passing and failing cases.

* Stage 2, main process: 400 examples, equally divided between provisional thematicizing and whole-part synthesis.

* Stage 2, self-evaluation: 300 examples, equally divided between passing and failing cases.

* Stage 3, main process: 200 examples.

We estimate the training cost at approximately 20 USD, with analysis running up to 50 USD, including multiple model runs due to rejected responses. Fine-tuning is likely to take 1–2 days, and each analysis stage will require 2–3 days at 3–4 hours of model work per day.

Total training and analysis are expected to cost \~75.00 USD. 

## **Example Workflow**

**Model:** Fine-tuned Llama 3.3 70B, hosted on Microsoft Azure AI Foundry

For every stage, the research team will provide 3–5 few-shot examples drawn from human-generated outputs, including annotations for chain-of-thought, disagreements, and process. After each stage, we will examine all viable outputs, with the option to re-run analysis for any responses that fall outside acceptable bounds. Retained outputs will carry forward as inputs for subsequent stages.

### Stage 1: Holistic Memoing and Meaning Unit Identification

The LLM will ingest each transcript to produce a candidate holistic memo and generate a list of candidate meaning units. Each output will include relevant verbatim text snippets that the LLM used to support its candidates. After the first iteration, the model will evaluate its own output through a secondary adversarial prompt template, comparing its results against the original transcript to identify unsupported inferential leaps. Candidates falling below a 90% confidence threshold will automatically trigger re-analysis for the respective step.  
Holistic memoing deliverables include a participant context snapshot, overall experiential orientation, dominant tensions or structures, researcher’s interpretive notes, and questions or ambiguities. Meaning unit identification deliverables, presented in table format, include the meaning unit ID, transcript excerpt, boundary justification, and descriptive paraphrase.

## Stage 2: Provisional Themes and Whole-Part Synthesis

The LLM will ingest each transcript alongside its Stage 1 outputs. After the first iteration, the model will evaluate its own output through the same adversarial process and re-run any analyses that fall outside the fine-tuning data or its extensions.  
Thematicizing deliverables include a theme label, constituent meaning units, interpretive description, supporting quotes, and analyst reasoning. Whole-part synthesis deliverables include a theme consistency check, contradictory passages, theme refinement suggestions, and revised thematic definitions.

## Stage 3: Cross-Case Synthesis

The LLM will ingest all previously generated materials across transcripts, with a focus on Stage 2 outputs. The model will first process a subset of data including human-coded seed responses, then proceed inductively through the remaining transcripts, categorizing and connecting themes identified in Stage 2\. The pre-selected seed responses will be applied to progressively larger, randomly selected segments of available data, with each pass increasing the quantity of records processed until all transcripts have been analyzed. This incremental approach is intended to mitigate the lost-middle problem in large-context LLM interactions, where the model is prone to response smoothing due to gradient descent.

