import jsonDb.database as db

json_db = db.JSONDB('test_db')
json_db.ensureKey('user',['id'])
json_db.perfDotStart()

json_db.insert('user',[{'id':1,'name':'wenxy'},{'id':2,'name':'vincent'}])
r = json_db.find('user',filter={'id':1})
json_db.update('user',filter={'id':1},set={'name':'wenxueyong'})
r = json_db.find('user',filter={'id':1})
json_db.delete('user',filter={'id':1})

json_db.perfDotEnd()
json_db.exportToFile(fileName='test.json')

print(json_db)
