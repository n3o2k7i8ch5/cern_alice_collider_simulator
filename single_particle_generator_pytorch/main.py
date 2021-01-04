from single_particle_generator_pytorch.trainer import Trainer

### TRAINING
trainer = Trainer()
autoenc, embeder, deembeder = trainer.train(epochs=101)
trainer.show_real_gen_data_comparison(autoenc, embeder, load_model=True, save=True)
