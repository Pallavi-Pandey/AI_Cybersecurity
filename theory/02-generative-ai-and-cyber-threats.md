# 2. Generative AI & Cyber Threats

**Theory time: 45 min** · Hands-on: [lab 02](../labs/02-generative-ai-and-cyber-threats/README.md)

## Attacker use of GenAI
- Convincing phishing and spear-phishing at scale, in any language.
- Deepfake voice/video for impersonation and business email compromise.
- Faster malware variation and reconnaissance; lower barrier to entry for low-skill attackers.

## Risks in GenAI systems themselves
- Prompt injection (direct and indirect) and jailbreaks.
- Data leakage: sensitive data pasted into prompts, training data exposure.
- Insecure output handling and over-privileged agents/tools.
- Reference: OWASP Top 10 for LLM Applications; MITRE ATLAS.

## Defensive use of GenAI
- Alert summarization, log explanation, detection-rule drafting, report writing.
- Guardrails: input/output filtering, least-privilege tool access, human approval for risky actions.

## Discussion
- How would you spot an AI-written phishing email? (Hint: you often can't from style alone, so verify process, not prose.)
