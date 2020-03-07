
# WC-MS-Celeb
### A modification of C-MS-Celeb, which replaces the Freebase MIDs with Wikidata Mappings.

This was made using the Freebase/Wikidata Mappings on the Freebase dumps page [here](https://developers.google.com/freebase) and the cleanlist C-MS-Celeb [here](https://github.com/EB-Dodo/C-MS-Celeb).

I replaced the rows in C-MS-Celeb that had mappings the in the table and dropped the rows that didn't. This allows the dataset to be used alongside all the features of Wikidata, rather than having to download the dumps from the now defunct Google Freebase. I do not provide a copy of MS-Celeb-1M, but this includes the Wikidata Identifiers for each image and scripts to generate WC-MS-Celeb from a local copy of MS-Celeb-1M.

## Citations
Chi Jin, Ruochun Jin, Kai Chen, and Yong Dou, “A Community Detection Approach to Cleaning Extremely Large Face Database,” Computational Intelligence and Neuroscience, vol. 2018, Article ID 4512473, 10 pages, 2018. doi:10.1155/2018/4512473

Yandong Guo, Lei Zhang, Yuxiao Hu, Xiaodong He: “MS-Celeb-1M: A Dataset and Benchmark for Large-Scale Face Recognition”, 2016; [http://arxiv.org/abs/1607.08221 arXiv:1607.08221].
