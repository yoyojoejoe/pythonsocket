import pickle
a_dict = {"root":"12345679"}
file = open('account.pkl', 'wb')
pickle.dump(a_dict, file)
file.close()
