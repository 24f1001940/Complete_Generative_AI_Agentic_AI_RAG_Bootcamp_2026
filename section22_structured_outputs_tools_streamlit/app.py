import os
import json
from dataclasses import dataclass, asdict
from typing import TypedDict

import streamlit as st

try:
    from pydantic import BaseModel, Field
except Exception:
    BaseModel = None
    Field = None

try:
    from langchain_core.messages import SystemMessage, HumanMessage
except Exception:
    SystemMessage = HumanMessage = None

try:
    from langchain_core.tools import tool
except Exception:
    tool = None

try:
    from langchain_ollama import ChatOllama, OllamaLLM
except Exception:
    ChatOllama = OllamaLLM = None

try:
    from groq import Groq
except Exception:
    Groq = None

st.set_page_config(page_title='Section 22 Structured Outputs & Tools', page_icon='🧩', layout='wide')
st.title('Section 22: Structured Outputs and Tool Use')
st.caption('Switch lectures from the sidebar. One file for lectures 121 to 124.')

LECTURES = {
    'Lecture 121': 'Model Integration, Message Types & Execution Modes',
    'Lecture 122': 'Custom Tools & Tool-Calling Agents',
    'Lecture 123': 'Structured Outputs with Pydantic, TypedDict & Dataclasses',
    'Lecture 124': 'Reliable Schema Design, Fallbacks & Error Handling',
}

lecture_choice = st.sidebar.radio('Choose a lecture', list(LECTURES.keys()), index=0)
model_choice = st.sidebar.selectbox('Local Ollama model', ['llama3.2:3b', 'llama3.1:8b', 'gemma2:2b'])
groq_model = st.sidebar.selectbox('Groq model (optional)', ['llama-3.3-70b-versatile', 'openai/gpt-oss-20b', 'qwen/qwen3.6-27b'])

st.sidebar.markdown('---')
st.sidebar.markdown('### Install')
st.sidebar.code("""pip install streamlit pydantic python-dotenv
pip install langchain-core langchain-ollama langchain-groq groq openai""", language='bash')
st.sidebar.markdown('Install Ollama separately if you want local-model demos. Set GROQ_API_KEY in your environment for hosted demos.')


def lecture_header(num, title, subtitle):
    st.subheader(f'Lecture {num} – {title}')
    st.write(subtitle)


def show_code(title, code, language='python'):
    with st.expander(f'Show code: {title}', expanded=False):
        st.code(code.strip(), language=language)


def groq_client():
    if Groq is None:
        return None
    key = os.environ.get('GROQ_API_KEY')
    if not key:
        return None
    try:
        return Groq(api_key=key)
    except Exception:
        return None


def ollama_llm():
    if OllamaLLM is None:
        return None
    try:
        return OllamaLLM(model=model_choice)
    except Exception:
        return None


def ollama_chat():
    if ChatOllama is None:
        return None
    try:
        return ChatOllama(model=model_choice)
    except Exception:
        return None


# Lecture 121

def lecture_121():
    lecture_header(121, 'Model Integration, Message Types & Execution Modes', 'Understand System, Human, and AI messages, plus invoke, batch, and stream.')
    st.code('System Message + Human Message → Model → AI Message', language='text')

    tab1, tab2, tab3 = st.tabs(['Invoke', 'Batch', 'Stream'])
    with tab1:
        prompt = st.text_input('Single prompt', value='Explain embeddings in simple words.', key='l121_invoke_prompt')
        if st.button('Run invoke()', key='l121_invoke_btn'):
            llm = ollama_chat()
            if llm is None:
                st.warning('Install Ollama and langchain-ollama to run this demo locally.')
            else:
                try:
                    if SystemMessage and HumanMessage:
                        msgs = [SystemMessage(content='You are a helpful AI tutor.'), HumanMessage(content=prompt)]
                        res = llm.invoke(msgs)
                        st.success(res.content if hasattr(res, 'content') else str(res))
                    else:
                        res = llm.invoke(prompt)
                        st.success(res)
                except Exception as e:
                    st.error(f'invoke() failed: {e}')
        show_code('invoke example', '''from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3.2:3b")
messages = [
    SystemMessage(content="You are a helpful AI tutor."),
    HumanMessage(content="What are embeddings?")
]
response = llm.invoke(messages)
print(response.content)''')

    with tab2:
        batch_items = st.text_area('One prompt per line', value='What is AI?\nWhat is machine learning?\nWhat is deep learning?', height=140, key='l121_batch_text')
        if st.button('Run batch()', key='l121_batch_btn'):
            llm = ollama_chat()
            if llm is None:
                st.warning('Install Ollama and langchain-ollama to run this demo locally.')
            else:
                prompts = [x.strip() for x in batch_items.splitlines() if x.strip()]
                try:
                    if SystemMessage and HumanMessage:
                        batch_inputs = [[SystemMessage(content='You are a helpful AI tutor.'), HumanMessage(content=p)] for p in prompts]
                        results = llm.batch(batch_inputs)
                        for i, r in enumerate(results, 1):
                            st.write(f'**Response {i}:** {r.content if hasattr(r, "content") else str(r)}')
                    else:
                        st.write(llm.batch(prompts))
                except Exception as e:
                    st.error(f'batch() failed: {e}')
        show_code('batch example', '''inputs = [
    [SystemMessage(content="You are a helpful AI tutor."), HumanMessage(content="What is AI?")],
    [SystemMessage(content="You are a helpful AI tutor."), HumanMessage(content="What is ML?")],
]
results = llm.batch(inputs)''')

    with tab3:
        stream_prompt = st.text_input('Streaming prompt', value='Explain vectors in machine learning.', key='l121_stream_prompt')
        if st.button('Run stream()', key='l121_stream_btn'):
            llm = ollama_chat()
            if llm is None:
                st.warning('Install Ollama and langchain-ollama to run this demo locally.')
            else:
                try:
                    placeholder = st.empty(); full = ''
                    if SystemMessage and HumanMessage:
                        msgs = [SystemMessage(content='You are a helpful AI tutor.'), HumanMessage(content=stream_prompt)]
                        for chunk in llm.stream(msgs):
                            token = chunk.content if hasattr(chunk, 'content') else str(chunk)
                            full += token
                            placeholder.markdown(full)
                    else:
                        for chunk in llm.stream(stream_prompt):
                            full += str(chunk)
                            placeholder.markdown(full)
                except Exception as e:
                    st.error(f'stream() failed: {e}')
        show_code('stream example', '''for chunk in llm.stream(messages):
    print(chunk.content, end="", flush=True)''')


# Lecture 122

def lecture_122():
    lecture_header(122, 'Custom Tools & Tool-Calling Agents', 'Create small tools that the model can use when it needs an action outside text generation.')
    st.code('User → LLM → Tool → Result → LLM → Final Answer', language='text')

    if tool is not None:
        @tool
        def add_numbers(a: int, b: int) -> int:
            '''Add two numbers and return the result.'''
            return a + b

        @tool
        def word_count(text: str) -> int:
            '''Count words in the text.'''
            return len(text.split())

        @tool
        def clean_text(text: str) -> str:
            '''Remove extra spaces from text.'''
            return ' '.join(text.split())

        c1, c2 = st.columns(2)
        with c1:
            a = st.number_input('First number', value=10, key='l122_a')
            b = st.number_input('Second number', value=15, key='l122_b')
            if st.button('Run calculator tool', key='l122_add'):
                st.success(f'Result: {add_numbers.invoke({"a": int(a), "b": int(b)})}')
        with c2:
            text = st.text_input('Text input', value='  LangChain   makes   tools   easy.  ', key='l122_text')
            mode = st.selectbox('Choose text tool', ['word_count', 'clean_text'], key='l122_mode')
            if st.button('Run text tool', key='l122_text_btn'):
                if mode == 'word_count':
                    st.success(f'Word count: {word_count.invoke({"text": text})}')
                else:
                    st.success(f'Cleaned text: {clean_text.invoke({"text": text})}')
    else:
        st.warning('langchain_core.tools.tool is not available in this environment.')

    show_code('tool example', '''from langchain_core.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

print(add_numbers.invoke({"a": 10, "b": 15}))''')


# Lecture 123

def lecture_123():
    lecture_header(123, 'Structured Outputs with Pydantic, TypedDict & Dataclasses', 'Return clean schema-based outputs instead of free-form paragraphs.')
    st.code('Prompt → Model → Structured Output → Validation → App', language='text')

    if BaseModel is None:
        st.warning('pydantic is not available in this environment.')
        return

    class ArticleSummary(BaseModel):
        title: str = Field(..., description='Short title')
        summary: str = Field(..., description='Short summary')
        confidence: float = Field(..., ge=0.0, le=1.0, description='Confidence between 0 and 1')

    class ArticleDict(TypedDict):
        title: str
        summary: str
        confidence: float

    @dataclass
    class ArticleData:
        title: str
        summary: str
        confidence: float

    t1, t2, t3 = st.tabs(['Pydantic', 'TypedDict', 'Dataclass'])
    with t1:
        raw = st.text_area('Paste JSON-like data', value='{"title":"Embeddings","summary":"Embeddings convert text into vectors.","confidence":0.92}', height=120, key='l123_raw')
        if st.button('Validate with Pydantic', key='l123_validate'):
            try:
                data = json.loads(raw)
                result = ArticleSummary(**data)
                st.success('Valid output!')
                st.json(result.model_dump())
            except Exception as e:
                st.error(f'Validation failed: {e}')
        show_code('Pydantic schema', '''from pydantic import BaseModel, Field

class ArticleSummary(BaseModel):
    title: str = Field(..., description="Short title")
    summary: str = Field(..., description="Short summary")
    confidence: float = Field(..., ge=0.0, le=1.0)''')
    with t2:
        st.code('''from typing import TypedDict

class ArticleDict(TypedDict):
    title: str
    summary: str
    confidence: float''', language='python')
        st.info('TypedDict is useful when you want a typed dictionary shape for development clarity.')
    with t3:
        sample = ArticleData(title='Embeddings', summary='Embeddings convert text into vectors.', confidence=0.92)
        st.json(asdict(sample))
        st.info('Dataclasses give you a clean structured Python object.')


# Lecture 124

def lecture_124():
    lecture_header(124, 'Reliable Schema Design, Fallbacks & Error Handling', 'Design schemas carefully, catch parsing errors, and use fallback logic when output is invalid.')
    st.code('Prompt → Model → Validate → Pass / Repair / Fallback → App', language='text')

    if BaseModel is None:
        st.warning('pydantic is not available in this environment.')
        return

    class QuizAnswer(BaseModel):
        question: str
        answer: str
        explanation: str
        confidence: float = Field(..., ge=0.0, le=1.0)

    demo_mode = st.selectbox('Choose output quality', ['Good output', 'Missing field', 'Wrong type', 'Extra text'], key='l124_mode')
    good = {'question': 'What are embeddings?', 'answer': 'Embeddings are numerical representations of meaning.', 'explanation': 'They help models compare text by meaning.', 'confidence': 0.95}
    missing = {'question': 'What are embeddings?', 'answer': 'Embeddings are numerical representations of meaning.', 'confidence': 0.95}
    wrong_type = {'question': 'What are embeddings?', 'answer': 'Embeddings are numerical representations of meaning.', 'explanation': 'They help models compare text by meaning.', 'confidence': 'high'}
    extra = 'Sure! {"question":"What are embeddings?","answer":"...","explanation":"...","confidence":0.95}'
    payload = good if demo_mode == 'Good output' else missing if demo_mode == 'Missing field' else wrong_type if demo_mode == 'Wrong type' else extra

    st.markdown('### Model output simulation')
    st.json(payload if isinstance(payload, dict) else {'raw_output': payload})

    def validate_payload(data):
        return QuizAnswer(**data)

    def repair_payload(raw_output: str):
        return {'question': 'What are embeddings?', 'answer': 'Embeddings are numerical representations of meaning.', 'explanation': 'They help models compare text by meaning.', 'confidence': 0.75}

    if st.button('Validate output', key='l124_validate'):
        try:
            if isinstance(payload, dict):
                result = validate_payload(payload)
                st.success('Validation succeeded.')
                st.json(result.model_dump())
            else:
                st.error('Validation failed because output is not a valid dictionary.')
                st.info('Using repair strategy...')
                repaired = repair_payload(payload)
                result = validate_payload(repaired)
                st.success('Repaired and validated successfully.')
                st.json(result.model_dump())
        except Exception as e:
            st.error(f'Validation / repair failed: {e}')
            st.info('Using default fallback.')
            fallback = {'question': 'unknown', 'answer': 'unknown', 'explanation': 'The model output could not be validated.', 'confidence': 0.0}
            st.json(fallback)

    st.code('''try:
    result = SchemaModel(**data)
except ValidationError:
    repaired = repair_output(raw_text)
    result = SchemaModel(**repaired)''', language='python')


if lecture_choice == 'Lecture 121':
    lecture_121()
elif lecture_choice == 'Lecture 122':
    lecture_122()
elif lecture_choice == 'Lecture 123':
    lecture_123()
elif lecture_choice == 'Lecture 124':
    lecture_124()
