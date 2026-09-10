# Polaris diagram visibility review

Scope: read-only live browser inspection of the two already-running loopback Polaris pages, at ports 36151 and 7478. No Butlers repository bodies read, no implementation edits. Measurements taken with repository CDP helper at 1440x900 and 390x900. Report contains presentation metadata only.

Verdict: NEEDS REPAIR for diagram discoverability.

[Observed] Both pages have the same measured layout. Two diagram groups exist, both visible outside collapsed disclosures. Desktop: relationship group y7470, height613, width663; core flow y9711, height82, width663. Mobile: relationship group y9965, height858, width343; core flow y13307, height396, width343. These are 8.3 and 11.1 viewport heights from the top before the first diagram.

[Observed] Architecture starts at y6912 desktop /9273 mobile, after purpose, scope and V1 sections. Total page height is26060/38886. Each diagram has six node elements. A desktop screenshot confirms the relationship group resembles three vertically stacked text cards with small connecting arrows and long captions; it does not provide a readily visible architecture overview.

[Observed] The Purpose block and its evidence end at y1217 desktop /1631 mobile. Promises starts at1269/1683. The first purpose paragraph ends at725/928. The complete introductory group continues until approximately2300/2930.

[Inferred] Insert a compact, clearly titled overview figure immediately after Purpose and before Promises. Its top should land near1250/1660, inside two 900px viewport heights while preserving the intact purpose narrative. Moving the whole architecture section after the complete introductory group would still defer the first visual beyond two viewports on mobile.

[Inferred] Three useful placements: (1) a source-backed core-loop overview after Purpose; (2) a connected runtime/component figure at the opening of architecture before its detailed prose; (3) a proactive candidate-to-delivery pipeline beside the relevant component guide. Keep qualifications in text equivalents and link each figure to the deeper component material. Diagrams should answer different questions, rather than repeat card treatments or add a frequency quota.

[Unknown] Whether the user's browser was at either inspected loopback endpoint. Their report is nevertheless explained by the current pages' long distance to the first visual.

Local measurement artifact: /tmp/polaris-diagram-visibility.json. Local screenshot remains private; no captured body content is included in this report.
