# WSI / Computational Pathology Quickstart (PathML-oriented)

## Minimal goals
1) Load one slide (or one tile set)
2) Extract a small number of tiles deterministically
3) Produce `figures/tiles_grid.png`
4) Record slide metadata and tile policy in `reports/imaging_overview.md`

## Guardrails
- WSI files are huge; always operate on ROIs/tiles.
- Make tiling deterministic: fixed seed, fixed stride/size, fixed ROI policy.

