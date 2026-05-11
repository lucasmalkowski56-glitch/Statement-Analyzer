#linear layers 
# Input (3 months of spending) -> Hidden  Layer -> Output (1 predicted month)

import torch 
import torch.nn as nn
import torch.optim as optim

class SpendingPredictor(nn.Module):
    def __init__(self):
            super().__init__()
            # define layers here
            self.l1 = nn.Linear(3, 8) # layer 1: input 3 months, expand to 8 neurons
            self.relu = nn.ReLU() # activation layer
            self.l2 = nn.Linear(8, 1) # layer 2: compress backdown to 1 prediction

    def forward(self, x):
            # define how data flows through layers here 
            x = self.l1(x)
            x = self.relu(x)
            return self.l2(x)
    
def train_model(monthly_totals, window=3, epochs=500):
        # convert to tensor
        data = torch.tensor(monthly_totals, dtype=torch.float32)

        # build sliding window sequences
        X, y =[], []
        for i in range(len(data) - window):
                X.append(data[i:i+window])
                y.append(data[i+window])
        X = torch.stack(X)
        y = torch.stack(y).unsqueeze(1)

        # normalize data so all values are between 0 and 1 
        X_max = X.max()  # returns the max val in the tensor
        X = X / X_max
        y = y / X_max

        # setup model, loss and optimizer 
        model = SpendingPredictor()
        criterion = nn.MSELoss()
        optimizer = optim.Adam(model.parameters(), lr=0.01)

        # training loop 
        for epoch in range(epochs): # epoch = one pass of the trainning dataset
                optimizer.zero_grad() # clear old gradients
                output = model(X)
                loss = criterion(output, y)
                loss.backward() # calculate new gradients
                optimizer.step() # updates weights

        return model, X_max
"""
This funtion will predict the total amount spend for the next upcoming month

model: the mahcine model trainning by train_model
recent_months: the last 3 months from the totals
X_max: the max value in the tensor of all the monthly totals
"""
def predict_next_month(model, recent_months, X_max):
    #convert recen_months to a tensor
    data = torch.tensor(recent_months, dtype=torch.float32)
    
    # normalize it the same way as in train_model
    data = data / X_max

    # pass it through the model
    with torch.no_grad():
           output = model(data.unsqueeze(0))

    # multiply the output back by X_max to get the real dollar amount
    prediction = output.item() * X_max.item()
    
    #return the prediction
    return prediction
