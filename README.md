# SEO Keyword Clustering by Jaccard Similarity

This repository provides a Python script to cluster keywords based on the similarity of their associated URLs, calculated using the Jaccard similarity coefficient.

## Description

The script takes a CSV file containing keywords and URLs, groups the keywords by their URLs' similarity, and outputs the grouped keywords into another CSV file. Clusters are formed based on a specified similarity threshold, which is determined through the Jaccard similarity coefficient.

### Jaccard Similarity

The Jaccard similarity coefficient measures similarity between sample sets and is defined as the size of the intersection divided by the size of the union of the sample sets. This script uses this metric to determine the similarity between sets of URLs associated with different keywords.

## Getting Started

### Prerequisites

You need the following Python packages:
- `argparse`
- `pandas`
- `tqdm`

You can install the necessary packages using pip:

```bash
pip install pandas tqdm
```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/keyword-clustering.git
cd keyword-clustering
```

2. Ensure you have the required dependencies installed:

```bash
pip install pandas tqdm
```

## Usage

The script can be run from the command line with the following parameters:

```bash
python cluster_keywords.py input_file output_file [-s SEPARATOR] [-k KEYWORD_COL] [-u URL_COL] [-t SIMILARITY_THRESHOLD]
```

### Required Arguments
- `input_file`: Path to the input CSV file.
- `output_file`: Path to save the output clustered keywords CSV file.

### Optional Arguments
- `-s, --separator`: Separator of the input file (default: `,`).
- `-k, --keyword_col`: Name of the keyword column in the input file (default: `Keyword`).
- `-u, --url_col`: Name of the URL column in the input file (default: `URL`).
- `-t, --similarity_threshold`: Threshold of similarity (default: `0.6`).

### Example

```bash
python cluster_keywords.py for-clustering.csv clustered_keywords.csv -s ';' -k 'keyword' -u 'url' -t 0.6
```

This will cluster the keywords in the `for-clustering.csv` file and save the output to `clustered_keywords.csv` using a semicolon (`;`) as the separator with a similarity threshold of 0.6.

## Output

The output CSV file will contain two columns:
- `Group`: The cluster group number. Keywords with the same group number are clustered together.
- `Keyword`: The keyword belonging to the specified group.

Keywords that could not be clustered will be assigned a group value of `-1`.

## Developed by

Dart. Please subscribe:
- [Twitter](https://twitter.com/dartseo)
- [Telegram](https://t.me/advancedseoblog)
