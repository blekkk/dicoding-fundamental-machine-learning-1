# Sentiment Analysis Project for Dicoding

This repository contains the scraping script for data collection to Google Playstore and a training notebook. This project aims to do a simple experiment in proofing the performance improvement on attention based model such as BERT compared to RNN based model with memory gates such as LSTM based on their test accuracies.

Models that are used in this project are:

1. [BERT](https://arxiv.org/abs/1810.04805) (Bidirectional Encoder Representations from Transformers) (Ongoing)
1. [LTSM](https://ieeexplore.ieee.org/abstract/document/6795963) (Long short-term memory) (Todo)

## How to run

Prerequisites:

 - Python 3.10
 - Jupyter lab or alternative
 - Virtual envitronment (Optional)

There is a scraping script included in `scraper.py` for scraping Google Playstore reviews, a dataset is included in the `/dataset` directory which contains user reviews for *video game* *"Fate: Grand Order"* with around 23000+ rows of user review that have been labelled using [BART](https://huggingface.co/facebook/bart-large-mnli) and [vader](https://github.com/cjhutto/vaderSentiment).

---
This code is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)