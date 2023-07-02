from dvclive import Live
import time, yaml

accuracies = [0.84753, 0.87761, 0.90862, 0.91023, 0.91101, 0.91543, 0.91559, 0.91653, 0.92109, 0.92121]

params = yaml.safe_load(open("params.yaml"))["train"]
num_epochs = params["num_epochs"]

with Live() as live:
    for i in range(num_epochs):
        time.sleep(5)
        live.log_metric("accuracy", accuracies[i])
        live.next_step()

