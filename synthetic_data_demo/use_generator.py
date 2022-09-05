from synthetic_data.generator.generator import SyntheticDataGenerator

n_patients = 10 # TODO get from the stdin
n_days = 100 # TODO get from the stdin

tool = SyntheticDataGenerator(
  # TODO params
  # - configure statics HERE
  # - configure models HERE
)

print("Test one arg")
tool.generate(n_patients)
print()

print("Test two args")
tool.generate(n_patients, n_days)
print()
