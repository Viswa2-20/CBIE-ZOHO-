import torch
import torch.nn as nn
import torch.optim as optim
import pickle
import os

# Simple LSTM Model for Behavior Sequence
class BehaviorLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(BehaviorLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        # x: (batch, seq_len, input_size)
        out, _ = self.lstm(x)
        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out

def train_behavior_model():
    print("Training Behavior Sequence Model (LSTM)...")
    
    # Dummy parameters
    input_size = 5  # e.g., [time_on_page, scroll_depth, click_count, is_idle, visit_count]
    hidden_size = 16
    num_classes = 3 # e.g., [high_intent, medium_intent, low_intent]
    
    model = BehaviorLSTM(input_size, hidden_size, num_classes)
    
    # Dummy training loop (omitted for brevity, just saving the initialized model)
    # In production, you would load sequence data and train here.
    
    save_path = "ml_engine/artifacts/behavior_model.pth"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    torch.save(model.state_dict(), save_path)
    print(f"Behavior model saved to {save_path}")

if __name__ == "__main__":
    train_behavior_model()
