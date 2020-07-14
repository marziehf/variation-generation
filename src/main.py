from src.modific import Modific


def write_to_file(path, nam, dic):
    langs = dic.keys()

    for lang in langs:
        with open(f'{path}.{nam}.{lang}', mode='wt', encoding='utf-8') as output_file:
            output_file.write('\n'.join(dic[lang]))
        output_file.close()


if __name__ == '__main__':
    bitext_prefix = '../data/newstest2012'
    mod = Modific(bitext_prefix)

    # substitute numbers
    num_mod = mod.number_perturbations(offset=10)
    write_to_file(bitext_prefix, 'num', num_mod)

    # remove adverbs
    adv_mod = mod.adv_removal()
    write_to_file(bitext_prefix, 'adv', adv_mod)

    # swap pronouns
    prn_mod = mod.pronoun_swap()
    write_to_file(bitext_prefix, 'prn', prn_mod)

