from loader import db

user_id = 5836353276

in_data = db.get_more_indata(user_id, 'Nov')
out_data = db.get_more_outdata(user_id, 'November')

if len(in_data) == 0 and len(out_data) == 0:
    print("List is empty")
else:
    print("List is not empty")
