from berka_vae.consts import CRED_EMBED_DIM, DEBT_EMBED_DIM
from berka_vae.trainer import Trainer
from common.show_quality import show_quality, show_comp_hists
from single_prtcl_generator_vae_pytorch.models.pdg_deembedder import PDGDeembedder
from single_prtcl_generator_vae_pytorch.models.pdg_embedder import PDGEmbedder

import pandas as pd

trainer = Trainer()
vae, embedder_cred, embedder_debt, deembedder_cred, deembedder_debt = trainer.train(epochs=15, load=False)

trainer.load_trans_data()
vae = trainer.create_vae(load=True)
deemb_cred = PDGDeembedder(pdg_count=20, pdg_embed_dim=CRED_EMBED_DIM, device=trainer.device)
deemb_debt = PDGDeembedder(pdg_count=20, pdg_embed_dim=DEBT_EMBED_DIM, device=trainer.device)

real_df = pd.read_csv('berka_trans_mapped.csv', sep='\t')
gen_data = trainer.gen_autoenc_data(1024*16, vae)
gen_df = trainer.convert_to_dataframe(gen_data, deemb_cred, deemb_debt)

real_col = real_df['trans_amount'][:1024*16]
gen_col = gen_df[2]
show_comp_hists(real_col.to_numpy(), gen_col.to_numpy(), title='Trans amount')

real_col = real_df['acc_balance'][:1024*16]
gen_col = gen_df[3]
show_comp_hists(real_col.to_numpy(), gen_col.to_numpy(), title='Acc balance')

real_col = real_df['trans_type'][:1024*16]
gen_col = gen_df[4]
show_comp_hists(real_col.to_numpy(), gen_col.to_numpy(), title='Trans type')

real_col = real_df['trans_operation'][:1024*16]
gen_col = gen_df[5]
show_comp_hists(real_col.to_numpy(), gen_col.to_numpy(), title='Trans operation')