import torch
from torch import nn


class PrtclWGANGenerator(nn.Module):
    def __init__(self, emb_features, latent_size, device):
        super(PrtclWGANGenerator, self).__init__()

        self.emb_features = emb_features
        self.latent_size = latent_size

        self.__net = nn.Sequential(
            nn.Linear(latent_size, 128),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(128, 256),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(256, 512),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(512, 1024),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(1024, 2*emb_features),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(2*emb_features, emb_features),
        ).to(device=device)

    def forward(self, x: torch.Tensor):
        return self.__net(x)