from neo4j import GraphDatabase
driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","Rambo@1234"))
session=driver.session()

#OUT DEGREE
q1='''
MATCH (N:PERSON)
WITH [(N)-->(P) WHERE P:PERSON|N.NAME] AS NAMES
UNWIND NAMES AS names
return names , count(names)
   '''  
#IN DEGREE   
q2='''
MATCH (N:PERSON{NAME:"RONI"}),(M:PERSON{NAME:"VISWA"})
WITH [(N)-[:friends*1..]->(M)|TRUE] AS NUMBERS
UNWIND NUMBERS AS NO_OF_PATH
RETURN COUNT(NO_OF_PATH) AS NUMBER_OF_AVAILABLE_PATH
   '''    
   
 
result=session.run(q2)

print(list(result))
    
