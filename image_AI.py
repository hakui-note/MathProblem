import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Reshape, Flatten
from keras.optimizers import Adam

# Generatorモデルの定義
def build_generator(latent_dim):
    model = Sequential()
    model.add(Dense(128, input_dim=latent_dim, activation='relu'))
    model.add(Dense(784, activation='sigmoid'))
    model.add(Reshape((28, 28, 1)))
    return model

# Discriminatorモデルの定義
def build_discriminator(img_shape):
    model = Sequential()
    model.add(Flatten(input_shape=img_shape))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    return model

# GeneratorとDiscriminatorの組み合わせるGANモデルの定義
def build_gan(generator, discriminator):
    discriminator.trainable = False
    model = Sequential()
    model.add(generator)
    model.add(discriminator)
    return model

# データの読み込みと前処理
(X_train, _), (_, _) = mnist.load_data()
X_train = X_train / 255.0
X_train = np.expand_dims(X_train, axis=-1)

# モデルの構築とコンパイル
latent_dim = 100
img_shape = (28, 28, 1)
generator = build_generator(latent_dim)
discriminator = build_discriminator(img_shape)
gan = build_gan(generator, discriminator)
discriminator.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
gan.compile(loss='binary_crossentropy', optimizer=Adam())

# G

# GANの訓練
epochs = 100
batch_size = 128
for epoch in range(epochs):
    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    fake_images = generator.predict(noise)
    real_images = X_train[np.random.randint(0, X_train.shape[0], batch_size)]

    X = np.concatenate([real_images, fake_images])
    y_real = np.ones((batch_size, 1))
    y_fake = np.zeros((batch_size, 1))
    y = np.concatenate([y_real, y_fake])

    d_loss_real = discriminator.train_on_batch(real_images, y_real)
    d_loss_fake = discriminator.train_on_batch(fake_images, y_fake)
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

    noise = np.random.normal(0, 1, (batch_size, latent_dim))
    g_loss = gan.train_on_batch(noise, y_real)

    print(f'Epoch: {epoch+1}, D Loss: {d_loss[0]}, Acc.: {100 * d_loss[1]}%, G Loss: {g_loss}')

# 生成された画像の表示
rows, cols = 5, 5
noise = np.random.normal(0, 1, (rows * cols, latent_dim))
gen_imgs = generator.predict(noise)
gen_imgs = 0.5 * gen_imgs + 0.5

fig, axs = plt.subplots(rows, cols)
idx = 0
for i in range(rows):
    for j in range(cols):
        axs[i,j].imshow(gen_imgs[idx, :,:,0], cmap='gray')
        axs[i,j].axis('off')
        idx += 1
plt.show()
