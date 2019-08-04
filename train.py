"""
@file: train
@author: 姬小野
@time: 上午12:17 2019/8/4
@version: v0.1
"""

from preprocess import vgg16, train_loader, train_on_gpu, optimizer, criterion
import torch


def train_epochs(n_epochs):
    vgg16.train()
    for epoch in range(n_epochs):
        train_loss = 0.0
        for batch_i, (image, target) in enumerate(train_loader):
            if train_on_gpu:
                image, target = image.cuda(), target.cuda()
            output = vgg16(image)

            optimizer.zero_grad()
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            train_loss += loss

            torch.save(vgg16, f'my_vgg16_{n_epochs}epochs.pth')
            print(f'\repoch_{epoch} - batch_{batch_i} - loss: {loss:.6f}')
            if batch_i % 10 == 0:
                print()


if __name__ == '__main__':
    n_epochs = 1
    train_epochs(n_epochs)