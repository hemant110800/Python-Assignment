import pickle
datastore={"office":{"medical":[{"room_number":100,"use":"reception","sq-ft":50,"price":75},
                                {"room_number":101,"use":"waiting","sq-ft":250,"price":75},
                                {"room_number":102,"use":"examination","sq-ft":125,"price":150},
                                {"room_number":103,"use":"examination","sq-ft":125,"price":150},
                                {"room_number":104,"use":"office","sq-ft":150,"price":100}],
                     "parking":{"location":"premium","style":"covered","price":750}}}


#-----------------For datastore file--------------------
def save():
    otfile=open('datastore.dat','wb')
    pickle.dump(datastore,otfile)
    otfile.close()

save()

