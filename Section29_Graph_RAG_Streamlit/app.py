import streamlit as st

st.set_page_config(page_title='Section 29 - Graph RAG', layout='wide')
st.title('Section 29: Knowledge Graphs & Graph RAG')

lecture=st.sidebar.radio('Lecture',[
'149 - Knowledge Graphs & Neo4j',
'150 - Cypher & LangChain Graph Ingestion',
'151 - Graph RAG'
])

st.sidebar.code('pip install -r requirements.txt\nstreamlit run app.py')

if lecture.startswith('149'):
    st.header('Lecture 149')
    st.code('(Employee)-[:WORKS_IN]->(Department)')
    st.table([
        {'Component':'Node','Purpose':'Entity'},
        {'Component':'Relationship','Purpose':'Connect entities'},
        {'Component':'Property','Purpose':'Metadata'}
    ])
    st.code("""from neo4j import GraphDatabase
driver = GraphDatabase.driver(URI, auth=(USERNAME,PASSWORD))
driver.verify_connectivity()
""", language='python')

elif lecture.startswith('150'):
    st.header('Lecture 150')
    st.code("""CREATE (:Person {name:'Alice'})
MATCH (p:Person) RETURN p
MATCH (p)-[:WORKS_IN]->(d) RETURN p,d
""", language='sql')
    st.code("""from langchain_neo4j import Neo4jGraph
graph = Neo4jGraph(url=URI, username=USERNAME, password=PASSWORD)
""", language='python')
    st.code('Documents -> Entity Extraction -> Relationships -> Neo4j')

else:
    st.header('Lecture 151')
    st.code('Question -> Vector Search + Graph Search -> Merged Context -> LLM -> Answer')
    st.table([
        {'Vector':'Semantic Similarity','Graph':'Relationships'},
        {'Vector':'Embeddings','Graph':'Nodes + Edges'}
    ])
    st.code("""graph_result = graph.query(...)
docs = retriever.invoke(question)
response = llm.invoke(prompt)
""", language='python')
