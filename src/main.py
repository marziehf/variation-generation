from src.modific import Modific

mod = Modific()
mod.load_data()

adv_mod = mod.adv_removal()
num_mod = mod.number_perturbations(offset=10)
prn_mod = mod.pronoun_swap()


