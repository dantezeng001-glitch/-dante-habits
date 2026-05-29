# Shokz Survey Personas

Source: `2026北美品牌用户调研（测试Agent用） _脱敏进Skill版本.xlsx`, 633 respondents.

These personas use the k=4 clustering result from the product-category model. Persona names are internal shorthand labels, not real respondent names.

## Method Summary

- Variables used: gender, age, household income, race/ethnicity, recoded Shokz product category, purchase reasons, and usage scenarios.
- Product model recode from `Which of the following models did you buy?`:
  - Bone conduction: any selected model containing `OpenRun`, `OpenMove`, or `OpenSwim`.
  - Ear-hook: any selected model containing `OpenFit`.
  - Ear-clip: any selected model containing `OpenDots`.
- Processing:
  - Age and income were treated as numeric/ordinal variables. Income code `8` ("Prefer not to say") was median-imputed and tracked outside the main distance.
  - Gender and race/ethnicity were treated as categorical variables.
  - Product category, purchase reasons, and usage scenarios were treated as multi-select groups and compared with Jaccard distance.
- Model:
  - Weighted Gower-style distance.
  - k-medoids clustering.
  - This reference uses k=4 because the team wants the finer segmentation despite a lower silhouette than k=3.
- Model comparison:
  - k=2 silhouette 0.2400; sizes 366 / 267.
  - k=3 silhouette 0.1841; sizes 243 / 129 / 261.
  - k=4 silhouette 0.1180; sizes 192 / 103 / 138 / 200 before label re-ordering.
  - k=5 silhouette 0.1014; sizes 181 / 123 / 114 / 151 / 64.
  - k=6 silhouette 0.1429; smallest cluster below 10%.

## Persona Weights

Use these exact weights for scoring:

| ID | Persona | Share |
|---|---|---:|
| 1 | 科技老白男 | 0.218009 |
| 2 | 骨传导跑男 | 0.315956 |
| 3 | 日常颜值派 | 0.162717 |
| 4 | 日常开放派 | 0.303318 |

Weighted score formula:

```text
weighted_score = 0.218009 * score_科技老白男
               + 0.315956 * score_骨传导跑男
               + 0.162717 * score_日常颜值派
               + 0.303318 * score_日常开放派
```

The score range is 1-5 per persona and 1-5 overall. The maximum possible weighted score is 5.00.

## 科技老白男

Share: 21.8%. Respondents: 138.

Snapshot:

- High-income, male-dominant, tech/function-oriented multi-category users.
- Average age 40.6.
- Gender skew: 99% male.
- Race/ethnicity skew: Caucasian 66%, Hispanic 13%, African American 13%.
- Highest household income ordinal among the four personas.
- Product categories: ear-hook 76% vs 36% overall; bone conduction 72% vs 78%; ear-clip 19% vs 13%.

Behavior:

- Uses Shokz for cycling, commuting, running, and gym/fitness.
- More multi-category than average, especially ear-hook.
- Less driven by ambient-awareness as a reason to buy.

Motivation:

- Wants new form factors, useful technology, and proof that features solve real problems.
- Over-indexes on smart features, warranty/customer service, battery life, call quality, value for money, product quality, and noise cancellation.
- Can accept a premium/technical concept if it feels concrete and performance-backed.

Concept Reaction Heuristics:

- Score high for concepts about technology, ear-hook innovation, smart features, call quality, battery, reliability, service assurance, and active/commute scenarios.
- Score medium for emotional lifestyle concepts if they still include product proof.
- Score low for concepts that lean only on open-ear philosophy or vague brand feeling without feature credibility.

Likely voice:

> "Show me what is technically better and why this form factor is worth switching to."

## 骨传导跑男

Share: 31.6%. Respondents: 200.

Snapshot:

- Bone-conduction, male, sport-anchored users.
- Average age 38.7.
- Gender skew: 98% male.
- Race/ethnicity skew: Caucasian 66%, Hispanic 15%, African American 11%.
- Product categories: bone conduction 85% vs 78% overall; ear-hook 20% vs 36%; ear-clip 9% vs 13%.

Behavior:

- Uses Shokz for running/jogging and gym/fitness.
- Less likely to use Shokz for home tasks, individual work/study, commuting, or work calls.
- Less ear-hook-oriented than average.

Motivation:

- Wants the classic Shokz open-ear sport promise: hearing surroundings while running, with good sound and low fuss.
- Over-indexes on ambient awareness, sound quality, running, gym, and bone-conduction usage.
- Under-indexes on warranty/service, call quality, noise cancellation, battery life, smart features, and brand reputation.

Concept Reaction Heuristics:

- Score high for bone-conduction sport concepts, running safety, awareness, sweat/fit confidence, and straightforward sound-quality claims.
- Score medium for broader active lifestyle concepts.
- Score low for heavy office/productivity, service-led, or ear-hook-first concepts.

Likely voice:

> "I use Shokz because I can run and still hear the world. Keep it simple and sport-relevant."

## 日常颜值派

Share: 16.3%. Respondents: 103.

Snapshot:

- Lower-income, design/home-task/commute oriented users with mixed gender but female-skew.
- Average age 39.2.
- Gender skew: 74% female, 22% male, 4% non-binary/third gender.
- Race/ethnicity skew: African American 68%, Hispanic 17%, Asian-American 7%.
- Product categories: bone conduction 80% vs 78% overall; ear-hook 29% vs 36%; ear-clip 11% vs 13%.

Behavior:

- Uses Shokz for home tasks and commuting more than average.
- Less connected to cycling, smart features, Bluetooth stability, battery life, and multi-scenario messaging.
- More receptive to marketing/advertising and brand reputation than some other groups.

Motivation:

- Wants Shokz to fit daily movement, commute, chores, and personal style.
- Over-indexes on design/style, ambient awareness, sound quality, brand reputation, and marketing/advertising.
- Needs benefits to feel relevant and accessible, not overly technical.

Concept Reaction Heuristics:

- Score high for design-forward, everyday commuting, lifestyle, awareness, and easy-to-understand concepts.
- Score medium for sports concepts if they are inclusive and not too hardcore.
- Score low for concepts centered on specs, cycling, or performance jargon.

Likely voice:

> "Make it look and feel right for my day. I need to understand why it fits my commute and routine."

## 日常开放派

Share: 30.3%. Respondents: 192.

Snapshot:

- Female, daily-life, open-listening users.
- Average age 39.8.
- Gender skew: 99% female.
- Race/ethnicity skew: Caucasian 80%, Hispanic 12%, Asian-American 4%.
- Product categories: bone conduction 73% vs 78% overall; ear-hook 29% vs 36%; ear-clip 15% vs 13%.

Behavior:

- Uses Shokz more for individual work/study and home tasks.
- Less likely to use Shokz for running/jogging or gym/fitness.
- Less ear-hook, sports, and product-quality oriented than average.

Motivation:

- Wants open listening for everyday focus, chores, errands, and comfort around the home or workday.
- Over-indexes on battery life, design/style, noise cancellation, and slightly on ear-clip.
- Under-indexes on sound quality, product quality, running, gym, and ear-hook.

Concept Reaction Heuristics:

- Score high for everyday convenience, home/work/study, simple open-listening use cases, design, battery, and comfort-adjacent messages.
- Score medium for product performance concepts if they are translated into daily benefits.
- Score low for hardcore sport, spec-heavy, or ear-hook-first concepts.

Likely voice:

> "I want something easy and comfortable for everyday listening, not just another running gadget."

## Stance Labels

Use these labels unless the user requests another scheme:

- 4.2-5.0: 赞成
- 3.5-4.1: 有条件赞成
- 2.8-3.4: 无感/观望
- 2.0-2.7: 有疑虑
- 1.0-1.9: 不赞成

## Recommended Response Template

```markdown
**模拟结论**
综合兴趣得分：x.xx / 5.00（满分 5 分）
折算百分制：xx / 100

| 画像 | 权重 | 画像特征简述 | 态度 | 兴趣度 | 主要理由 | 阻力 | 典型想法 |
|---|---:|---|---|---:|---|---|---|
| 科技老白男 | 21.8% | 平均40.6岁，99%男性，Caucasian 66%，耳挂/多品类高 | ... | x/5 | ... | ... | "..." |
| 骨传导跑男 | 31.6% | 平均38.7岁，98%男性，骨传导85%，跑步/健身高 | ... | x/5 | ... | ... | "..." |
| 日常颜值派 | 16.3% | 平均39.2岁，74%女性，African American 68%，家务/通勤与设计感高 | ... | x/5 | ... | ... | "..." |
| 日常开放派 | 30.3% | 平均39.8岁，99%女性，Caucasian 80%，工作学习/家务高 | ... | x/5 | ... | ... | "..." |

调研支持证据：...
调研风险/不支持点：...
证据缺口：...
优化建议：...
```
