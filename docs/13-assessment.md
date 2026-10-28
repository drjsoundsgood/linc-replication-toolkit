# 13 · Assessment

Measure your program from the first summer. Good data improves the program, makes the case to funders, and lets you report outcomes with confidence.

## What to measure

| Domain | What you're asking | How |
|---|---|---|
| **Research self-efficacy** | Can students confidently plan, run and troubleshoot experiments? | Pre/post survey |
| **Sense of belonging** | Do students feel included and valued in the lab? | Pre/post survey |
| **Science identity** | Do students see themselves as scientists? | Pre/post survey |
| **Career intentions** | Do students intend to pursue a life sciences degree? | Pre/post survey |
| **Skills** | Can students do calculations and experiments independently? | Pre/post survey; mentor observation |
| **Mentorship** | How well did mentors support students? | Post survey |
| **Retention** | Do students return? | Program records |
| **Outputs** | Presentations, publications, awards | Program records |
| **Long-term outcomes** | College admission, major, undergraduate research | Alumni tracking |

## Pre- and post-program surveys

The surveys in [`assessment/`](../assessment/) are built to be **quantifiable**:

- The **same core items appear on both surveys**, so you can compare each student's answers before and after.
- Items use a consistent **1–5 agreement scale**.
- Each student uses a **private code** (not their name) on both surveys, so responses can be matched while staying confidential.
- The post-survey adds questions about mentorship and open-ended feedback.
- A **returning-student module** captures growth across summers.

### When to give them
- **Pre-program survey:** day one, before training begins
- **Post-program survey:** the final week, before final presentations

Returning students take both surveys each summer, which lets you track change across years.

### Setting them up
1. Copy the items into Google Forms, Qualtrics or your institution's survey tool.
2. Keep the wording and order of shared items **identical** on both surveys.
3. Collect the private code as the first question on both.
4. Export responses using the column names in [assessment/survey-data-template.csv](../assessment/survey-data-template.csv).

### Analyzing them
[assessment/analyze_surveys.py](../assessment/analyze_surveys.py) matches pre and post responses by code and reports, for each item and each domain:
- Mean before and after, and the mean change
- A **Wilcoxon signed-rank test**, appropriate for small groups and 1–5 ratings
- The number of students who improved, stayed the same or declined

With small cohorts, results from a single summer have limited statistical power. **Pool across years**, and report effect sizes and individual-level change alongside p-values.

### Ethics
- Ask your institution whether survey research with minors needs review by an institutional review board (IRB), especially if you plan to publish the results. Program evaluation and publishable research are often treated differently.
- Make surveys voluntary and confidential, and say so.
- Store the key linking codes to names separately and securely, or don't keep one at all.

## Long-term tracking

With consent from students (and families, for minors), track each alumnus:

| Field | When |
|---|---|
| Summers completed | Each summer |
| College admitted to and attending | Spring and fall of senior year |
| Intended and declared major | College entry; each year |
| Undergraduate research participation | End of first and second college years |
| Publications, presentations, awards | Ongoing |

## Reporting

Summarize each year in a one-page report for funders, your department and your program office: cohort size, retention, survey results, outputs and alumni outcomes. These reports become the evidence for renewal and expansion.

---
← [12 · Publishing with high school students](12-publishing.md) · Back to [README](../README.md)
