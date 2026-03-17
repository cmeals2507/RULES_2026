# **Comparing pathways: Analysis of human-machine qualitative analysis using a pilot hermeneutic phenomenology**

## **Abstract**

We propose a comparative study of three phenomenological analysis workflows (human-only, human-machine, machine-only) using the same transcripts and the same analytic stages. In it, we compare the resulting analysis in two ways. First, we will use embeddings (numerical representations of words, organized for use by LLMs) to measure semantic similarity, interpretive drift, and trajectory alignment across stages. Second, we will conduct a blinded human review using a structured rubric focused on experiential grounding, phenomenological sensitivity, coherence, synthesis, and conceptual restraint. Reviewer scores will be combined into a Phenomenological Fidelity Index (PFI), and qualitative reviewer memos will be used to interpret differences. The aim is to evaluate not only whether the different workflows produce similar findings, but also how they move through the analytic process and how well they preserve phenomenological fidelity. 

## **Overview**

This study will examine how phenomenological analysis converges or diverges when conducted through three related workflows: 

1. Human-only (traditional phenomenology)  
2. Human-machine hybrid  
3. Machine-only

The central goal is not to compare final themes, but to examine the trajectory of interpretation across analytic stages. The study combines two complementary forms of analysis: 

1. Computational comparison using embeddings and semantic distance  
2. Structured human evaluation using phenomenological quality and fidelity

Together, these allow us to explore both how analyses move through interpretive space and how well they preserve the experiential character of the original data.

## **Analytic Design**

### **Common Corpus**

All three workflows analyze the same participant transcripts

### **Common Stages**

Each workflow follows the same analytic sequence: 

1. Holistic memoing  
2. Meaning unit identification  
3. Theme identification  
4. Whole-part reconciliation  
5. Cross-case synthesis/essence statement

### **Controlled output**

To support productive comparison, each workflow should produce outputs with similar constraints at each stage. This includes approximate length, level of detail, and stage definition. 

The study’s object of analysis, therefore, is the full analytic path from transcript to essence.

## **Data Structure**

For each participant, all workflows produce stage-specific outputs. For example: 

| Participant | Workflow ID | Stage ID | Output |
| :---- | :---- | :---- | :---- |
| P1 | Human | Memo | {...} |
| P1 | Human | Meaning Units | {...} |
| P1 | Human | Themes | {...} |
| P1 | Human | Whole-Part | {...} |
| P1 | Human | Essence | {...} |
| P1 | Human-Machine | Memo | {...} |
| P1 | Machine | Memo | {...} |

This will create a comparable dataset across participants, workflows, and stages.

## **Computational Analysis**

### **Embedding-based Semantic Similarity**

Each analytic output is represented as a vector (i.e., a collection of numbers corresponding to words in the output). Similarity is then computed between outputs across workflows and stages. This allows for the comparison of: 

* The same stage across workflows (e.g., human memo vs. human-machine memo vs. machine memo)  
* Movement within workflows across stages (e.g., memo → meaning units → themes → whole-part reconciliation → essence)  
* Clustering of outputs by workflow or participant

These analyses examine whether workflows produce similar or different semantic accounts of the original participants’ transcripts. 

### **Interpretive Drift**

Interpretive drift here is defined as the semantic distance between successive analytic stages. For example: 

* Transcript → memo  
* Memo → meaning units  
* Meaning units → themes  
* Themes → Whole-part  
* Whole-part → Essence

This allows us to quantify how much interpretation changes as the analyses progress. This can take two useful forms: 

* Stage drift \- defining the semantic distance between adjacent stages  
* Total drift \- distance between transcript and final essence

This helps to identify whether a workflow stage stays relatively close to the original account or moves toward abstraction. 

### **Trajectory Alignment Analysis**

Each workflow will be treated as a trajectory through interpretive space. Rather than only comparing outputs, this compares the path of movement across stages. For each workflow, transitions are represented as vectors: 

* Memo minus transcript  
* Meaning units minus memo  
* Themes minus meaning units  
* Whole-part minus themes  
* Essence minus whole-part

These stage-to-stage transitions are compared across workflows within each participant by using [cosine similarity](https://www.ibm.com/think/topics/cosine-similarity), producing a trajectory alignment score. This indicates whether two workflows move through interpretive space in similar ways, and allows us to evaluate similarity within the process rather than just evaluating the endpoints. 

## **Human Evaluation**

The human reading layer evaluates dimensions that embeddings cannot capture well, including: 

* Experiential grounding  
* Phenomenological sensitivity  
* Interpretive coherence  
* Conceptual intrusion  
* Quality of synthesis

To accomplish this, the research team will qualitatively evaluate the outputs from each pathway, seeking to understand the overall quality, themes, and conditional essence of each. To complement this, we also propose the following steps: 

1. ### **Blinded Review**

   1. Outputs will be stripped of workflow data, so researchers see anonymized versions. This helps reduce bias toward a single type of analysis. 

2. ### **Structured Evaluation Rubric**

   1. Researchers will score each analysis extract using a common rubric. Proposed dimensions include:   
      1. Experiential grounding. Q: Is the analysis anchored in the participant’s account?  
      2. Phenomenological sensitivity. Q: Does it attend to lived meaning rather than only abstract themes?   
      3. Interpretive coherence. Q: Is the analytic account internally consistent?   
      4. Structural synthesis. Q: Does the later-stage account integrate earlier insights well?   
      5. Conceptual restraint. Q: Does it avoid imposing constructs that are not clearly grounded in the data?   
   2. A simple 3-point scale (1=weak, 2=moderate, 3=strong) can be used for each dimension.

3. ### **Stage-level and trajectory-level reading**

   1. Review occurs at two levels:   
      1. Stage-level. Comparing the same stage across workflows (inclusive of participant transcript)  
      2. Trajectory-level. Examine how each workflow progresses across stages (e.g., Memo → Themes → Whole-Part)  
   2. This allows researchers to assess whether the workflow remains grounded and coherent over time.

4. ### **Researcher Memos**

   1. In addition to scores, reviewers write brief analytic memos describing features of the evaluated text, including:   
      1. Strengths and weaknesses  
      2. Where interpretations diverged (within a workflow sample)  
      3. Where abstraction becomes excessive  
      4. Which analyses were more faithful to participant experience  
   2. These memos serve as the qualitative dimension of the results

5. ### **Multiple Researchers**

   1. Ideally, this process would include evaluation by 2-3 researchers, allowing for agreement to be inferred using metrics like:   
      1. Intraclass correlation  
      2. Krippendorf’s ⍺

## **Phenomenological Fidelity Index** 

The Phenomenological Fidelity Index (PFI) is a composite score that summarizes how well a given analytic output preserves phenomenological quality across five dimensions: experiential grounding, phenomenological sensitivity, interpretive coherence, structural synthesis, and conceptual restraint. Each dimension is scored on a 3-point scale (1=weak, 2=moderate, 3=strong); the PFI is the mean across all five (range: 1.0–3.0). A high PFI indicates stronger experiential fidelity; a lower score suggests conceptual drift, weak transcript grounding, or poor synthesis. The dimensions draw on van Manen's (1997, 2014\) criteria for phenomenological quality and Lincoln and Guba's (1985) trustworthiness framework, adapted here for stage-level analytic outputs. Dimensions 4 and 5 are additionally motivated by Ashwin et al. (2023, 2025), who identify over-abstraction and conceptual intrusion as systematic tendencies in LLM-generated qualitative analysis. Because the five dimensions operate as an interdependent system — a deficit in one typically propagates into others — the composite captures something isolated scores do not: the overall integrity of the analytic pathway as a phenomenological act. PFI scores are interpreted alongside the computational measures described above.

## **Integration of Analyses**

The study combines semantic structure evaluation with measures of human interpretive judgment that can be interpreted together. For instance: 

* High semantic similarity and high human agreement indicate that the workflow produces genuinely similar interpretations  
* High semantic similarity and low human agreement indicate that outputs are lexically or semantically similar, but differ in phenomenological quality  
* Low semantic similarity and high human agreement indicate that different wording or framing still capture similar lived meaning  
* Low semantic similarity and low human agreement indicate that workflows are divergent in both structure and interpretation.

## **Core Outputs** 

The study will likely report results in four main areas: 

1. Semantic similarity across workflows. Q: How similar are stage outputs across human, human-machine, and machine-only work?   
2. Interpretive drift. Q: How far does each workflow move from transcript to essence, and where are the largest leaps?  
3. Trajectory alignment. Q: Do workflows move through interpretive space in similar or different ways?   
4. Phenomenological fidelity. Q: How do blinded human researchers evaluate the outputs in terms of grounding, coherence, and sensitivity?

## **Contribution**

This study moves beyond the simple question of “did the AI get the same themes as humans?” Instead, it poses the following questions: 

* How does interpretation evolve across workflows?  
* Where does divergence begin?   
* Does the LLM alter the path of analysis, the endpoint (essence), or both?  
* Are semantically similar outputs also phenomenologically strong?   
* Can human-machine collaboration preserve fidelity while changing trajectory? 

