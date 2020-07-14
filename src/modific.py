import re


class Modific:
    src_snts = []
    de_snts = []

    def __init__(self, bitext_prefix):
        self.load_data(bitext_prefix)

    def load_data(self, path):
        with open(path + '.en') as f:
            self.en_snts = f.readlines()
        with open(path + '.de') as f:
            self.de_snts = f.readlines()

        self.en_snts = [x.strip() for x in self.en_snts]
        self.de_snts = [x.strip() for x in self.de_snts]

    @staticmethod
    def load_dictcc():
        with open('../data/de-en.adv.tsv') as f:
            dict_advs = [line.strip().split('\t') for line in f]
        return dict_advs

    def number_perturbations(self, offset):
        en_snts = []
        de_snts = []

        for en_snt, de_snt in zip(self.en_snts, self.de_snts):
            en_nums = [int(i) for i in re.findall("\d+", en_snt)]
            de_nums = [int(i) for i in re.findall("\d+", de_snt)]
            if en_nums != de_nums:
                continue
            for num in en_nums:
                for k in range(-offset, offset, 1):
                    if num + k > 0 and k != 0:
                        pert_en_snt = re.sub(str(num), str(num + k), en_snt)
                        pert_de_snt = re.sub(str(num), str(num + k), de_snt)
                        de_snts.append(pert_de_snt)
                        en_snts.append(pert_en_snt)
        return {"en": en_snts, "de": de_snts}

    @staticmethod
    def _get_span(s, w):
        span = re.search(f'\\b{w}\\b', s, flags=re.I).span()
        return span

    def _replace(self, sentence, word, rep_word):
        span = self._get_span(sentence, word)
        rep_word = rep_word.capitalize() if sentence[span[0]].isupper() else rep_word
        pert_sent = sentence[:span[0]] + rep_word + sentence[span[1]:]
        return pert_sent

    def pronoun_swap(self):
        en_snts = []
        de_snts = []

        for en_snt, de_snt in zip(self.en_snts, self.de_snts):
            pert_en_sent = ''
            pert_de_sent = ''

            m_pron = {'en': 'he', 'de': 'er'}
            f_pron = {'en': 'she', 'de': 'sie'}

            if f_pron['en'] in en_snt.lower().split() and f_pron['de'] in de_snt.lower().split():
                pert_en_sent = self._replace(en_snt, f_pron['en'], m_pron['en'])
                pert_de_sent = self._replace(de_snt, f_pron['de'], m_pron['de'])
                en_snts.append(pert_en_sent)
                de_snts.append(pert_de_sent)

            if m_pron['en'] in en_snt.lower().split() and m_pron['de'] in de_snt.lower().split():
                pert_en_sent = self._replace(en_snt, m_pron['en'], f_pron['en'])
                pert_de_sent = self._replace(de_snt, m_pron['de'], f_pron['de'])
                en_snts.append(pert_en_sent)
                de_snts.append(pert_de_sent)
        return {"en": en_snts, "de": de_snts}

    def adv_removal(self):
        en_snts = []
        de_snts = []

        dict_advs = self.load_dictcc()

        for de_adv, en_adv, _ in dict_advs:
            for en_snt, de_snt in zip(self.en_snts, self.de_snts):
                if en_adv in en_snt.lower().split()  and de_adv in de_snt.lower().split():
                    en_span = self._get_span(en_snt, en_adv)
                    de_span = self._get_span(de_snt, de_adv)
                    en_snts.append(en_snt[:en_span[0]] + en_snt[en_span[1] + 1:])
                    de_snts.append(de_snt[:de_span[0]] + de_snt[de_span[1] + 1:])
        return {"en": en_snts, "de": de_snts}
