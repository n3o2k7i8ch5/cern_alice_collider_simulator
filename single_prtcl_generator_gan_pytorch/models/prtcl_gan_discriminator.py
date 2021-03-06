import torch
from torch import nn


class PrtclGANDiscriminator(nn.Module):
    def __init__(self, emb_features, device):
        super(PrtclGANDiscriminator, self).__init__()

        self.emb_features = emb_features

        self.__net = nn.Sequential(
            nn.Linear(emb_features, 2*emb_features),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(2*emb_features, 512),
            #nn.Dropout(.1),
            #nn.Tanh(),

            nn.Linear(512, 512),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(512, 256),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(256, 128),
            nn.Dropout(.1),
            nn.Tanh(),

            nn.Linear(128, 32),
            nn.Tanh(),

            nn.Linear(32, 1),
            nn.Sigmoid()

        ).to(device=device)

    def forward(self, x: torch.Tensor):
        return self.__net(x).squeeze()
