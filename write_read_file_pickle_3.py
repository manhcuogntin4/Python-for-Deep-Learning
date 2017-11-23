import pickle

train_text=["This is train1","This is train2"]
train_label=[1,0]
test_text=["This is test1", "This is test 2"]
test_label=[1,.0]
corpus=(train_text,train_label),(test_text,test_label)

pickle.dump( corpus, open( "corpus.pkl", "wb" ) )