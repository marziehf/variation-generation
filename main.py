import argparse

from src.modific import Modific


def write_to_file(path, nam, dic):
    langs = dic.keys()

    for lang in langs:
        with open(f'{path}.{nam}.{lang}', mode='wt', encoding='utf-8') as output_file:
            output_file.write('\n'.join(dic[lang]))
        output_file.close()


if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-b", "--bitext", default='./data/newstest2012', help="Path to bitext prefix")
    ap.add_argument("-n", "--numvar", default=10, type=int, help="Number variation parameter")
    ap.add_argument("-o", "--output", default='./data/newstest2012', help="Path to output prefix")
    args = vars(ap.parse_args())

    mod = Modific(args['bitext'])

    # substitute numbers
    num_mod = mod.number_perturbations(offset=args['numvar'])
    write_to_file(args['output'], 'num', num_mod)

    # remove adverbs
    adv_mod = mod.adv_removal()
    write_to_file(args['output'], 'adv', adv_mod)

    # swap pronouns
    prn_mod = mod.pronoun_swap()
    write_to_file(args['output'], 'prn', prn_mod)
