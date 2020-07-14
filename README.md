# variation-generation

This repository includes the codes and scripts for sentence pair variations 
proposed in [our paper](https://www.aclweb.org/anthology/2020.ngt-1.10.pdf).
Given a (German-English) bitext, this code generates sentence pair variations with substituting numbers,
removing adverbs, and swaping pronouns. 

**Note**: Substituting numbers is language independent and can be used for language pairs other than German-English. 

## Usage

```commandline
python main.py --bitext ./data/newstest2012  
               --numvar 10 
               --output ./variations_o/newstest2012.aug
```

## Citation

If you use this code, please cite:
```
@inproceedings{fadaee-monz-2020-unreasonable,
    title = "The Unreasonable Volatility of Neural Machine Translation Models",
    author = "Fadaee, Marzieh  and
      Monz, Christof",
    booktitle = "Proceedings of the Fourth Workshop on Neural Generation and Translation",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.ngt-1.10",
    pages = "88--96",
    abstract = "Recent works have shown that Neural Machine Translation (NMT) models achieve impressive performance, however, questions about understanding the behavior of these models remain unanswered. We investigate the unexpected volatility of NMT models where the input is semantically and syntactically correct. We discover that with trivial modifications of source sentences, we can identify cases where \textit{unexpected changes} happen in the translation and in the worst case lead to mistranslations. This volatile behavior of translating extremely similar sentences in surprisingly different ways highlights the underlying generalization problem of current NMT models. We find that both RNN and Transformer models display volatile behavior in 26{\%} and 19{\%} of sentence variations, respectively.",
}
```
