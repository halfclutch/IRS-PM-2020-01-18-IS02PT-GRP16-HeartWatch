from experta import *

def return_scheme(useranswers):

    class User(Fact):  # Facts from user input
        cp = Field(int)
        max_heart_beat = Field(int)
        major_vessels = Field(int)
        thal = Field(int)
        restecg = Field(int)
        exang = Field(int)
        pass

    class Prediction (KnowledgeEngine):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.prediction = False
            self.CF_medical = 0
            self.rule = 0

        @Rule(AS.v << User(data__thal=MATCH.data__thal), TEST(lambda data__thal: int(data__thal) == 3 ),
              AS.v << User(data__cp=MATCH.data__cp), TEST(lambda data__cp: int(data__cp) == 2 or int(data__cp) == 3),
              AS.v << User(data__max_heart_beat=MATCH.data__max_heart_beat), TEST(lambda data__max_heart_beat: int(data__max_heart_beat) > 160))
        def rule1(self):
            self.prediction = False
            self.CF_medical = 1
            self.rule = 1

        @Rule(AS.v << User(data__thal=MATCH.data__thal), TEST(lambda data__thal: int(data__thal) == 3 ),
              AS.v << User(data__cp=MATCH.data__cp), TEST(lambda data__cp: int(data__cp) == 2 or int(data__cp) == 3),
              AS.v << User(data__max_heart_beat=MATCH.data__max_heart_beat), TEST(lambda data__max_heart_beat: int(data__max_heart_beat) <= 160))
        def rule2(self):
            self.prediction = False
            self.CF_medical = 0.82
            self.rule = 2

        @Rule(AS.v << User(data__thal=MATCH.data__thal), TEST(lambda data__thal: int(data__thal) == 3 ),
              AS.v << User(data__cp=MATCH.data__cp), TEST(lambda data__cp: int(data__cp) == 1 or int(data__cp) == 4),
              AS.v << User(data__major_vessels=MATCH.data__major_vessels), TEST(lambda data__major_vessels: int(data__major_vessels) == 0))
        def rule3(self):
            self.prediction = False
            self.CF_medical = 0.81
            self.rule = 3

        @Rule(AS.v << User(data__thal=MATCH.data__thal), TEST(lambda data__thal: int(data__thal) == 3 ),
              AS.v << User(data__cp=MATCH.data__cp), TEST(lambda data__cp: int(data__cp) == 1 or int(data__cp) == 4),
              AS.v << User(data__major_vessels=MATCH.data__major_vessels), TEST(lambda data__major_vessels: int(data__major_vessels) != 0))
        def rule4(self):
            self.prediction = True
            self.CF_medical = 0.73
            self.rule = 4

        @Rule(AS.v << User(data__thal=MATCH.data__thal), TEST(lambda data__thal: int(data__thal) == 6 or int(data__thal) == 7),
              AS.v << User(data__exang=MATCH.data__exang), TEST(lambda data__exang: int(data__exang) == 1),
              AS.v << User(data__major_vessels=MATCH.data__major_vessels), TEST(lambda data__major_vessels: int(data__major_vessels) == 0))
        def rule5(self):
            self.prediction = True
            self.CF_medical = 0.79
            self.rule = 5

        @Rule(AS.v << User(data__thal=MATCH.data__thal), TEST(lambda data__thal: int(data__thal) == 6 or int(data__thal) == 7),
              AS.v << User(data__exang=MATCH.data__exang), TEST(lambda data__exang: int(data__exang) == 0),
              AS.v << User(data__major_vessels=MATCH.data__major_vessels), TEST(lambda data__major_vessels: int(data__major_vessels) == 0))
        def rule6(self):
            self.prediction = False
            self.CF_medical = 0.69
            self.rule = 6

        @Rule(AS.v << User(data__thal=MATCH.data__thal),
              TEST(lambda data__thal: int(data__thal) == 6 or int(data__thal) == 7),
              AS.v << User(data__restecg=MATCH.data__restecg), TEST(lambda data__restecg: int(data__restecg) != 0),
              AS.v << User(data__major_vessels=MATCH.data__major_vessels), TEST(lambda data__major_vessels: int(data__major_vessels) != 0))
        def rule7(self):
            self.prediction = True
            self.CF_medical = 1
            self.rule = 7

        @Rule(AS.v << User(data__thal=MATCH.data__thal),
              TEST(lambda data__thal: int(data__thal) == 6 or int(data__thal) == 7),
              AS.v << User(data__restecg=MATCH.data__restecg), TEST(lambda data__restecg: int(data__restecg) == 0),
              AS.v << User(data__major_vessels=MATCH.data__major_vessels), TEST(lambda data__major_vessels: int(data__major_vessels) != 0))
        def rule8(self):
            self.prediction = True
            self.CF_medical = 0.8
            self.rule = 8

    engine = Prediction()
    engine.reset()
    engine.declare(User(data=useranswers))
    engine.run()
    engine.facts

    return engine.prediction, engine.CF_medical, engine.rule
