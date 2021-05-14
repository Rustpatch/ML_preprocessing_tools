from dataset_creator import Dataset_creator
from dataset import Dataset
from imputer import Imputer
from training_set import Training_set
from validation_set import Validation_set
from test_set import Test_set

dataset_creator = Dataset_creator("train.csv", "test.csv", "SalePrice")

# Get rid of string columns :
dataset_creator.clean_dataset_of_string_columns()
dataset_creator.clean_test_set_of_string_columns()

dataset = dataset_creator.create_dataset()

# Cut the dataset between a training set and a validation set :
training_set = Training_set(dataset)
validation_set = Validation_set(dataset)

print(training_set.dataset)
print(validation_set.dataset)


'''
missing_val_number_limiter = 10
deal_with_missing_val_for_X_train = DealWithMissingValues(X_train, "train", missing_val_number_limiter)
deal_with_missing_val_for_X_valid = DealWithMissingValues(X_valid, "valid", missing_val_number_limiter)
deal_with_missing_val_for_X_test = DealWithMissingValues(X_test, "test", missing_val_number_limiter)

reduced_X_train = deal_with_missing_val_for_X_train.drop_columns_with_missing_val()
reduced_X_valid = deal_with_missing_val_for_X_valid.drop_columns_with_missing_val()
model_drop = ModelGenerator(reduced_X_train, reduced_X_valid, y_train, y_valid)
model_drop.generate_random_forest_regressor_model(n_estimators=100, random_state=0)
model_drop.train()
prediction_drop = model_drop.predict(reduced_X_valid)
model_drop_evaluation = ModelEvaluator(y_valid, prediction_drop)
print(model_drop_evaluation.evaluate_and_get_mean_absolute_error())

imputer = Imputer('simple', X_train)
imputed_X_train = deal_with_missing_val_for_X_train.impute_columns_with_missing_val(imputer, X_train)
imputed_X_valid = deal_with_missing_val_for_X_valid.impute_columns_with_missing_val(imputer, X_valid)
model_imputed = ModelGenerator(imputed_X_train, imputed_X_valid, y_train, y_valid)
model_imputed.generate_random_forest_regressor_model(n_estimators=100, random_state=0)
model_imputed.train()
prediction_imputed = model_imputed.predict(imputed_X_valid)
model_imputed_evaluation = ModelEvaluator(y_valid, prediction_imputed)
print(model_imputed_evaluation.evaluate_and_get_mean_absolute_error())

zero_one_X_train = deal_with_missing_val_for_X_train.replace_missing_val_columns_with_zero_one_columns(imputer)
zero_one_X_valid = deal_with_missing_val_for_X_valid.replace_missing_val_columns_with_zero_one_columns(imputer)
model_zero_one = ModelGenerator(zero_one_X_train, zero_one_X_valid, y_train, y_valid)
model_zero_one.generate_random_forest_regressor_model(n_estimators=100, random_state=0)
model_zero_one.train()
prediction_zero_one = model_zero_one.predict(zero_one_X_valid)
model_zero_one_evaluation = ModelEvaluator(y_valid, prediction_zero_one)
print(model_zero_one_evaluation.evaluate_and_get_mean_absolute_error())

zero_one_X_test = deal_with_missing_val_for_X_test.replace_missing_val_columns_with_zero_one_columns(imputer)
prediction_test = model_zero_one.predict(zero_one_X_test)
model_zero_one.generate_sumbmission_file(X_test, prediction_test)
'''