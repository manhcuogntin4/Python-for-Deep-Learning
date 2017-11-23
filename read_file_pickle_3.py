import pickle

(train_text,train_label),(test_text,test_label)=pickle.load(open( "corpus.pkl", "rb" ))

print train_label