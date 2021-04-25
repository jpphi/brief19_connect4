import random
import tensorflow as tf
import keras
import numpy as np

from tensorflow.keras.models import Sequential, load_model # Model

#from keras.layers import Dense, Dropout, Flatten, Conv2D, Input, MaxPooling2D, Reshape, BatchNormalization
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import Adam

from collections import deque

from tensorflow.python.keras.layers.preprocessing.category_encoding import _NUM_ELEMENTS_NAME

class DQN:
    MOD_CONV= 2 # Modele réseau de neuronne convolutionnel
    MOD_DENSE= 1 # Modele réseau de neuronne dense
    LOAD_MODEL= ""

    def __init__(self, env, num_model= MOD_DENSE, loadmodel= LOAD_MODEL):
        self.env     = env
        self.memory  = deque(maxlen=2000) # initialement à 2000
        
        self.gamma = 0.85
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.005
        self.tau = .125

        self.model        = self.create_model(num_model, loadmodel)
        self.target_model = self.create_model(num_model, loadmodel)
        self.num_model= num_model

    def create_model(self, numero, loadmodel):
        model = Sequential()
        state_shape  = self.env.shape
        """
        state = state.reshape(1, self.env.shape[0] , self.env.shape[1],1)
        """
        if numero== self.MOD_DENSE and loadmodel== "":
            model.add(Dense(20, input_dim=state_shape[0]*state_shape[1], activation='relu'))
            model.add(Dense(100, activation='relu'))
            model.add(Dense(150, activation='relu'))
            model.add(Dense(100, activation='relu'))
            model.add(Dense(50, activation='relu'))
            model.add(Dense(20, activation='relu'))
            model.add(Dense(state_shape[1], activation='linear'))

            model.compile(loss="mean_squared_error", optimizer=Adam(lr=self.learning_rate))


        elif numero== self.MOD_CONV and loadmodel== "":

            model.add(Conv2D(16,3,padding="same", input_shape=(state_shape[0],state_shape[1],1), activation='relu'))
            model.add(MaxPooling2D(pool_size=(4,4),padding="same"))
            model.add(Flatten())
            model.add(Dense(50, activation='relu'))
            model.add(Dense(50, activation='relu'))
            model.add(Dense(50, activation='relu'))
            model.add(Dense(state_shape[1], activation='linear'))

            model.compile(loss="mean_squared_error", optimizer=Adam(lr=self.learning_rate))

        elif loadmodel!= "":
            # https://machinelearningmastery.com/save-load-keras-deep-learning-models/
            model= load_model(loadmodel)


        return model

    """
    def act(self, state):
        self.epsilon *= self.epsilon_decay
        self.epsilon = max(self.epsilon_min, self.epsilon)
        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()
        return np.argmax(self.model.predict(state)[0])
    """

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
            if self.num_model== self.MOD_DENSE:
                state = state.reshape(1, self.env.shape[0] * self.env.shape[1])
            elif self.num_model== self.MOD_CONV:
                state = state.reshape(1, self.env.shape[0] , self.env.shape[1],1)
            else:
                raise ValueError("Model non défini !")

            target = self.target_model.predict(state)

            print(f"Méthode remenber, state shape: {target.shape} \ntarget=\n {target}")
            if done:
                target[0][action] = reward
            else:
                if self.num_model== self.MOD_DENSE:
                    new_state = new_state.reshape(1, self.env.shape[0] * self.env.shape[1])
                elif self.num_model== self.MOD_CONV:
                    new_state = new_state.reshape(1, self.env.shape[0] , self.env.shape[1],1)
                else:
                    raise ValueError("Model non défini !")


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

#---------------------------------------------------------------------------------------------

    def create_model_20_100_100_1(self):
        model = Sequential()
        state_shape  = self.env.shape

        model.add(Dense(20, input_dim=state_shape[0]*state_shape[1], activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(state_shape[1], activation='linear'))

        model.compile(loss="mean_squared_error", optimizer=Adam(lr=self.learning_rate))

        return model


    def create_model_sav(self):
        model = Sequential()
        state_shape  = self.env.shape

        model.add(Dense(20, input_dim=state_shape[0]*state_shape[1], activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(150, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(20, activation='relu'))
        model.add(Dense(state_shape[1], activation='linear'))

        model.compile(loss="mean_squared_error", optimizer=Adam(lr=self.learning_rate))

        return model

    def  create_model_qui_fonctionne(self):
        model = Sequential()
        state_shape  = self.env.shape

        model.add(Dense(24, input_shape= state_shape, activation="relu")) # VOIR EVENTUELLEMENT SANS [0]
        model.add(Dense(state_shape[0] * state_shape[1], input_shape= state_shape, activation="relu"))

        model.add(Dense(7))

        model.compile(loss="mean_squared_error", optimizer=Adam(lr=self.learning_rate))

        return model

