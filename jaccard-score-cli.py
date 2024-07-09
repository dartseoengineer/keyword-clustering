import argparse
from collections import defaultdict
import pandas as pd
from tqdm import tqdm


def cluster_keywords(input_file, output_file, separator, keyword_col, url_col, similarity_threshold):
# Jaccard similarity
    def jaccard_similarity(list1, list2):
        intersection = len(list(set(list1).intersection(list2)))
        union = (len(set(list1)) + len(set(list2))) - intersection
        return float(intersection) / union

    # Load data
    data = pd.read_csv(input_file, sep=separator, engine='python')

    # Similarity Threshold

    similarity_threshold = float(similarity_threshold)

    # Group urls by keyword
    keywords_urls = defaultdict(set)
    for _, row in tqdm(data.iterrows(), total=data.shape[0], desc='Group urls by keyword'):
        keyword, url = row[keyword_col], row[url_col]
        if pd.isna(url) or url == '':
            url = None
        keywords_urls[keyword].add(url)

    # Filter out keywords with no URLs
    unclustered_keywords = [keyword for keyword, urls in keywords_urls.items() if len(urls) == 1 and None in urls]
    keywords_urls = {keyword: urls for keyword, urls in keywords_urls.items() if not (len(urls) == 1 and None in urls)}

    # Find clusters based on url set similarity
    clusters = []
    for keyword, urls in tqdm(keywords_urls.items(), desc='Creating clusters'):
        # Remove None (empty URLs)
        urls = {url for url in urls if url is not None}
        # Find a cluster that this keyword belongs to
        for cluster in clusters:
            if any(jaccard_similarity(urls, keywords_urls[other_keyword]) >= similarity_threshold
                   for other_keyword in cluster):
                cluster.append(keyword)
                break
        else:  # no suitable cluster found
            clusters.append([keyword])

    # Prepare the dataframe for clustered keywords
    clustered_keywords = [(cluster_id, keyword)
                          for cluster_id, cluster in enumerate(clusters)
                          for keyword in cluster]

    # Add unclustered keywords to cluster -1
    clustered_keywords.extend([(-1, keyword) for keyword in unclustered_keywords])

    # Save the result to a csv file
    clustered_keywords_df = pd.DataFrame(clustered_keywords, columns=['Group', 'Keyword'])
    clustered_keywords_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cluster keywords by SERP similarity", epilog="Example: python jaccard-score-cli.py -s ';' -k 'keyword' -u 'url' -t 0.6 for-clustering.csv clustered_keywords.csv")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to save the output clustered keywords")
    parser.add_argument("-s", "--separator", default=',', help="Separator of the input file")
    parser.add_argument("-k", "--keyword_col", default='Keyword', help="Name of the keyword column in input file")
    parser.add_argument("-u", "--url_col", default='URL', help="Name of the URL column in input file")
    parser.add_argument("-t", "--similarity_threshold", default=0.6, help="Threshold of similarity")

    args = parser.parse_args()
    
    cluster_keywords(args.input_file, args.output_file, args.separator, args.keyword_col, args.url_col, args.similarity_threshold)
    print("")
    print("Developed by Dart. Please subscribe:")
    print("Twitter: https://twitter.com/dartseo")
    print("Telegram: https://t.me/advancedseoblog")