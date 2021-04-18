import random
import tensorflow as tf
import keras
import numpy as np


from keras.models import Sequential,  Model

from keras.layers import Dense, Dropout, Flatten, Conv2D, Input, MaxPooling2D, Reshape, BatchNormalization
from keras.optimizers import Adam

from collections import deque

class DQN:
    def __init__(self, env):
        self.env     = env
        self.memory  = deque(maxlen=20000) # initialement à 2000
        
        self.gamma = 0.85
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.005
        self.tau = .125

        self.model        = self.create_model()
        self.target_model = self.create_model()

    def create_model222222(self):
        model   = Sequential()
        state_shape  = self.env.shape

        """
        x = Input(shape=(32, 32, 3), batch_size=64)

        
        model.add(Conv2D(42, kernel_size=3, activation='relu', input_shape=(6,7)))
        model.add(Flatten())    
        model.add(Dense(7, activation="softmax"))
        """

        model.add(Dense(state_shape[0] * state_shape[1] * 10, input_shape= state_shape, activation="relu")) # VOIR EVENTUELLEMENT SANS [0]
        model.add(Dense(state_shape[0] * state_shape[1] * 5, activation="relu"))
        model.add(Dense(state_shape[0] * state_shape[1] * 2, activation="relu"))
        model.add(Dense(state_shape[0] * state_shape[1], activation="relu"))
        #model.add(Flatten())
        model.add(Dense(state_shape[1], activation="softmax")) #state_shape[1]


        # Nouvelle approche avec des CNN

        """
        output_nodes = 7  # REMPLACER PAR shape[1]
        n_classes = 1
        batch_size_ = 20 
        epoch = 20 

        input_layer = Input(shape=(6,7,1)) # VOIR AVEC SHAPE MATRICE
        conv1 = Conv2D(16,3,padding="same",activation="relu", input_shape = (6,7,1))(input_layer)
        pool1 = MaxPooling2D(pool_size=(4,4),padding="same")(conv1)  #=> peut renforcer la performance .... à voir ???
        flat = Flatten()(pool1)
        hidden1 = Dense(10, activation='softmax')(flat) #relu

        btNormLayer = BatchNormalization()(hidden1) 
        output_layer = Dense(output_nodes * n_classes, activation="softmax")(btNormLayer) 
        output_layer2 = Dense(output_nodes * n_classes, activation="relu")(output_layer) 
        output_reshape = Reshape((output_nodes, n_classes))(output_layer2)
        model = Model(inputs=input_layer, outputs=output_reshape)  # je pense qu'il manquait le reshape hier ....

        """

        model.compile(loss="mean_squared_error", optimizer=Adam(lr=self.learning_rate))
        #model.compile(loss='mean_squared_error', optimizer='adam', sample_weight_mode='temporal')
        return model
    """
    def act(self, state):
        self.epsilon *= self.epsilon_decay
        self.epsilon = max(self.epsilon_min, self.epsilon)
        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()
        return np.argmax(self.model.predict(state)[0])
    """
    def  create_model(self):
        model = Sequential()
        state_shape  = self.env.shape

        model.add(Dense(24, input_shape= state_shape, activation="relu")) # VOIR EVENTUELLEMENT SANS [0]
        model.add(Dense(state_shape[0] * state_shape[1], input_shape= state_shape, activation="relu"))

        #model.add(Flatten())
        #model.add(Dense(50, activation='relu'))
        #model.add(Dense(50, activation='relu'))
        #model.add(Dense(50, activation='relu'))
        #model.add(Dense(50, activation='relu'))
        #model.add(Dense(50, activation='relu'))
        #model.add(Dense(50, activation='relu'))
        #model.add(Dense(50, activation='relu'))

        model.add(Dense(7))

        model.compile(loss="mean_squared_error", optimizer=Adam(lr=self.learning_rate))

        return model


    def remember(self, state, action, reward, new_state, done):
        #print("Méthode remenber")
        self.memory.append([state, action, reward, new_state, done])

    def replay(self):
        batch_size = 32
        if len(self.memory) < batch_size: 
            #print(f"Méthode replay: self memory= {self.memory} < {batch_size}")
            return

        samples = random.sample(self.memory, batch_size)
        #print(f"Méthode replay: sampleshape= {len(samples)}")
        #print(f"Méthode replay: samples= {samples}")
        for sample in samples:
            state, action, reward, new_state, done = sample
            #state= state.reshape(6,7,1)
            #print(f"Méthode remenber, state shape: {state.shape} \ntarget=\n {state}")
            target = self.target_model.predict(state)

            print(f"Méthode remenber, state shape: {target.shape} \ntarget=\n {target}")
            if done:
                target[0][action] = reward
            else:
                #Q_future = max(self.target_model.predict(new_state)[0])
                #new_state= new_state.reshape(6,7,1)

                Q_future = max(self.target_model.predict(new_state)[0])
                #print(f"Méthode remenber, target future= {Q_future}")
                target[0][action] = reward + Q_future * self.gamma
                print(f"\nMéthode remenber, target[0][action]= {target[0][action]} action= {action}\n")
            self.model.fit(state, target, epochs=1, verbose=1)

    def target_train(self):
        weights = self.model.get_weights()
        target_weights = self.target_model.get_weights()
        for i in range(len(target_weights)):
            target_weights[i] = weights[i] * self.tau + target_weights[i] * (1 - self.tau)
        self.target_model.set_weights(target_weights)
        #print(f"Méthode target train: target_weights\n{target_weights}")

    def save_model(self, fn):
        self.model.save(fn)

    
