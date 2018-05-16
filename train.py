# Import comet_ml in the top of your file
from comet_ml import Experiment

# Create an experiment with your api key
experiment = Experiment(api_key="ZYZWOp8YGYbWZjtv5b0kJJqC1")

# Report hyper params:
hyper_params = {"learning_rate": 0.5, "steps": 100000, "batch_size": 50}
experiment.log_multiple_params(hyper_params)

# Report any information you need by:
hyper_params = {"learning_rate": 0.5, "steps": 100000, "batch_size": 50}
experiment.log_multiple_params(hyper_params)

# Example param
# some_param = "some value"
# experiment.log_parameter("param name", some_param)

# Example value
# train_accuracy = "your_variable"
# experiment.log_metric("acc", train_accuracy)

loss = train_step.run(feed_dict={x: batch[0], y_: batch[1]})
experiment.log_metric("loss", loss)

for i in range(hyper_params["steps"]):
    batch = mnist.train.next_batch(hyper_params["batch_size"])
    experiment.set_step(i)