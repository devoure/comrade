from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter

def train_comrade(data_json, config_file, model_dir):
    training_data = load_data(data_json)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'comrade')

def predict_intent(text):
    interpreter = Interpreter.load('./models/nlu/default/comrade')
    print(interpreter.parse(text))

train_comrade('./data/data.json', 'config.json', './models/nlu')
predict_intent("My registration number is 0225")

