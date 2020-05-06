# # VAE model = encoder + decoder
# # build encoder model
# inputs = Input(shape=input_shape, name='encoder_input')
# x = Conv2D(32, kernel_size=3, strides=1, padding='same')(inputs)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = MaxPool2D((2, 2), strides=(2, 2))(x)

# x = Conv2D(64, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = MaxPool2D((2, 2), strides=(2, 2))(x)

# x = Conv2D(128, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(64, kernel_size=1, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(128, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = MaxPool2D((2, 2), strides=(2, 2))(x)

# x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(128, kernel_size=1, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(128, kernel_size=1, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)

# # x = Dense(intermediate_dim, activation='relu')(inputs)
# z_mean = Conv2D(filters=latent_dim, kernel_size=(1, 1), padding="same", name='z_mean')(x)
# z_mean = GlobalAveragePooling2D()(z_mean)
# z_log_var = Conv2D(filters=latent_dim, kernel_size=(1, 1), padding="same", name='z_log_var')(x)
# z_log_var = GlobalAveragePooling2D()(z_log_var)

# # use reparameterization trick to push the sampling out as input
# # note that "output_shape" isn't necessary with the TensorFlow backend
# z = Lambda(sampling, output_shape=(latent_dim,), name='z')([z_mean, z_log_var])

# # instantiate encoder model
# encoder = Model(inputs, [z_mean, z_log_var, z], name='encoder')
# encoder.summary()
# #plot_model(encoder, to_file='vae_fonts_encoder.png', show_shapes=True)



# # build decoder model
# latent_inputs = Input(shape=(latent_dim,), name='z_sampling')
# x = Reshape((1, 1, latent_dim))(latent_inputs)
# x = UpSampling2D((image_size//32, image_size//32))(x)

# x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(128, kernel_size=1, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(128, kernel_size=1, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)

# x = UpSampling2D((2, 2))(x)
# x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(128, kernel_size=1, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(256, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)

# x = UpSampling2D((2, 2))(x)
# x = Conv2D(128, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(64, kernel_size=1, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(128, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)

# x = UpSampling2D((2, 2))(x)
# x = Conv2D(64, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)

# x = UpSampling2D((2, 2))(x)
# x = Conv2D(32, kernel_size=3, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)
# x = Conv2D(64, kernel_size=1, strides=1, padding='same')(x)
# x = BatchNormalization()(x)
# x = LeakyReLU()(x)

# # final upsampling 
# x = UpSampling2D((2, 2))(x)

# outputs = Conv2D(filters=num_channels, kernel_size=(1, 1), padding='same', activation='tanh')(x)