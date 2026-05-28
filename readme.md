```markdown
# UCB-PAST: Unit Test Generation with UCB Path Selection

This repository contains the implementation of **UCB-PAST**, a method that applies the Upper Confidence Bound (UCB) algorithm to path selection for LLM-based unit test generation.

## Repository Structure

This repository provides two language versions:

| Folder | Language | Description |
|--------|----------|-------------|
| `ucb-utps-chn/` | Chinese (中文) | **Actual implementation used in experiments** |
| `ucb-utps-eng/` | English | English translation for reference |

> **Note**: The actual experiments were conducted using the **Chinese version** (`ucb-utps-chn/`). The English version (`ucb-utps-eng/`) is a semantically equivalent translation provided for international readers. All results reported in the paper were produced by the Chinese version.

## Project Structure

```
ucb-utps-{lang}/
├── common/
│   ├── __init__.py
│   ├── data_structures.py
│   ├── test_executor.py
│   ├── coverage_analyzer.py
│   └── wilcoxon_analyzer.py
├── methods/
│   ├── __init__.py
│   ├── past_method.py
│   ├── no_healing_method.py
│   ├── hypothesis_method.py
│   ├── smart_random_method.py
│   └── pure_llm_method.py
├── runners/
│   ├── run_past.py
│   ├── run_no_healing.py
│   ├── run_hypothesis.py
│   ├── run_smart_random.py
│   └── run_pure_llm.py
├── analysis/
│   ├── __init__.py
│   ├── aggregate_results.py
│   └── plot_comparison.py
├── results/
│   └── (JSON result files)
└── requirements.txt
```

## Quick Start

### 1. Navigate to the language version

```bash
# For the actual implementation (Chinese)
cd ucb-utps-chn

# Or for the reference version (English)
cd ucb-utps-eng
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pytest coverage hypothesis numpy scipy matplotlib openai
```

### 3. API Key Configuration

The API key is already configured in the code. If you need to change it, update the following line in the method files:

```python
api_key.api_key = "your-api-key-here"
```

## Running Experiments

```bash
# PAST with UCB (proposed method)
python runners/run_past.py target4_dedent.py 5 15 --ucb

# PAST without UCB (greedy baseline)
python runners/run_past.py target4_dedent.py 5 15

# Hypothesis (property-based testing)
python runners/run_hypothesis.py target4_dedent.py 5 15

# No-Healing (random exploration)
python runners/run_no_healing.py target4_dedent.py 5 15

# SmartRandom (parameter-aware random)
python runners/run_smart_random.py target4_dedent.py 5 15

# PureLLM (one-shot LLM generation)
python runners/run_pure_llm.py target4_dedent.py 5 15
```

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `target` | Target Python file | Required |
| `repetitions` | Number of repetitions | 5 |
| `max_iter` | Maximum iterations per run | 15 |
| `--ucb` | Enable UCB strategy | False |
| `--ucb-c` | UCB exploration parameter | 1.414 |
| `--ucb-mode` | UCB mode (`standard` or `tuned`) | standard |

## Analyzing Results

After running experiments, each run produces a JSON result file in the `results/` directory.

To aggregate results and generate statistics:

```bash
python results/analyze_results.py
```

### Output Files

| File | Description |
|------|-------------|
| `results/past_*.json` | PAST experiment results |
| `results/past_ucb_*.json` | PAST-UCB experiment results |
| `analysis_results_*.json` | Aggregated statistics with Wilcoxon tests |
| `coverage_comparison_*.png` | Bar chart of coverage comparison |
| `wilcoxon_heatmap_*.png` | p-value heatmap |
| `effect_size_comparison_*.png` | Effect size comparison chart |
| `ranking_comparison_*.png` | Average ranking chart |

## Experiment Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Repetitions | 5 | Number of independent runs |
| Max iterations | 15 | Iterations per run |
| Test timeout | 30 seconds | Per test execution timeout |
| API timeout | 60 seconds | LLM generation timeout |
| LLM model | Qwen-Turbo | Alibaba Cloud LLM |
| Temperature | 0.3 | LLM sampling temperature |
| UCB exploration c | √2 ≈ 1.414 | Exploration-exploitation balance |
| Significance level | α = 0.05 | Wilcoxon test threshold |

## Notes

- The `past_method.py` supports both original PAST (greedy) and PAST-UCB via the `--ucb` flag
- UCB statistics are saved to `ucb_stats/` directory
- Generated test cases are saved to `generated_tests/` directory
- All result JSON files are saved to `results/` directory

## Citation
If you use this code in your research, please cite:

bibtex
@article{ucb-past-2026,
  title={UCB-based Path Selection for LLM Unit Test Generation: Balancing Exploration and Exploitation},
  author={Yang, Xun},
  journal={Journal of Software: Evolution and Process},
  year={2026}
}

## License
MIT License
