from synthetic_data.evaluator.evaluator import SyntheticDataEvaluator

dataset = "/a/dataset/path" # TODO get from the stdin

tool = SyntheticDataEvaluator(
  # TODO params
  # - configure statics HERE
)

print("Test one arg")
tool.evaluate(dataset)
print()