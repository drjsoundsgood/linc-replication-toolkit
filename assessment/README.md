# Assessment toolkit

Matched pre- and post-program surveys that let you **quantify change** for each student and across cohorts.

| File | What it is |
|---|---|
| [pre-program-survey.md](pre-program-survey.md) | Given on day one, before training |
| [post-program-survey.md](post-program-survey.md) | Given in the final week |
| [returning-student-module.md](returning-student-module.md) | Extra items for students in their second summer or later |
| [survey-data-template.csv](survey-data-template.csv) | Column layout for exported responses |
| [analyze_surveys.py](analyze_surveys.py) | Matches pre and post responses and tests for change |

See [docs/13-assessment.md](../docs/13-assessment.md) for when and how to use them.

## Design

- **Matched items.** The 19 core items are identical on both surveys, in the same order.
- **One scale.** Every core item uses: 1 = Strongly disagree · 2 = Disagree · 3 = Neutral · 4 = Agree · 5 = Strongly agree.
- **Private codes.** Students create a code from information only they know, so responses can be matched without names.
- **Five domains**, each averaged into a domain score:

| Domain | Items | What it measures |
|---|---|---|
| **Research self-efficacy** | SE1–SE6 | Confidence planning, running and troubleshooting experiments |
| **Belonging and voice** | BE1–BE4 | Feeling included and that one's ideas are valued |
| **Science identity** | ID1–ID3 | Seeing oneself as a scientist |
| **Educational and career intentions** | IN1–IN3 | Plans to study life sciences and do research |
| **Science communication** | CO1–CO3 | Confidence presenting and discussing research |

The post-survey adds mentorship and program-climate items (MT, PC) and open-ended questions. These don't have pre-program equivalents.

## Codebook

| Code | Item |
|---|---|
| SE1 | I feel comfortable working in a research lab. |
| SE2 | I can do the calculations needed to prepare reagents and samples on my own, using my notes. |
| SE3 | I can carry out laboratory experiments on my own, using my notes. |
| SE4 | When an experiment doesn't work, I can come up with ideas for how to improve it. |
| SE5 | I can design an experiment to test a scientific question. |
| SE6 | I could teach a new student how to do an experiment I know. |
| BE1 | I feel like I belong in a research lab. |
| BE2 | I feel comfortable sharing my ideas about experiments with a mentor. |
| BE3 | I believe other students value my opinions about experiments and data. |
| BE4 | I believe scientists (such as graduate students and postdocs) value my opinions about experiments and data. |
| ID1 | I see myself as a scientist. |
| ID2 | I feel comfortable with the idea of becoming a scientist. |
| ID3 | People like me can become scientists. |
| IN1 | I plan to pursue an undergraduate degree in the life sciences or a related field. |
| IN2 | I plan to do research while I am in college. |
| IN3 | I am interested in a career that involves scientific research. |
| CO1 | I feel confident presenting my research to an audience. |
| CO2 | I feel confident answering questions about my research. |
| CO3 | I can explain my research to someone who isn't a scientist. |

### A note on adapting the original survey
These items build on the survey used in the founding program. Two changes make the data more useful:
- The original asked students at the **end** of the summer to rate how comfortable they had felt at the **beginning**. Ratings recalled after the fact are biased by what happened since, so this version asks each question **before and after** instead.
- Items now share one agreement scale, so they can be combined into domain scores and compared across years.

If you have data from an earlier version, keep it, but analyze it separately rather than pooling it with this version.
