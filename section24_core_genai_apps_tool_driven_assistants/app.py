import re
from typing import List

import streamlit as st

st.set_page_config(
    page_title='Section 24: Core GenAI Applications & Tool-Driven Assistants',
    page_icon='🧠',
    layout='wide',
)

st.title('Section 24: Core GenAI Applications & Tool-Driven Assistants')
st.caption('Lecture-wise demo app for Lectures 129–132. Use the sidebar to switch lectures without editing code.')

LECTURES = {
    'Lecture 129': 'Conversational Q&A Systems: Architecture, Prompts & Provider Comparisons',
    'Lecture 130': 'Text Summarization Engines: Stuff, Map-Reduce & Refine Chains',
    'Lecture 131': 'Tool Integration, Function Calling & SQL Database Assistants',
    'Lecture 132': 'Specialized Productivity Assistants: Math Solvers, Code Helpers & Study Tools',
}

lecture = st.sidebar.radio('Choose a lecture', list(LECTURES.keys()), index=0)

st.sidebar.markdown('---')
st.sidebar.markdown('### Install')
st.sidebar.code('pip install -r requirements.txt', language='bash')
st.sidebar.markdown('### Run')
st.sidebar.code('streamlit run app.py', language='bash')
st.sidebar.markdown('This app is intentionally self-contained and uses lightweight visual demos so you can record lecture by lecture without changing code.')

st.sidebar.markdown('---')
provider_mode = st.sidebar.selectbox(
    'Provider comparison mode',
    ['Local Ollama', 'Hosted API', 'Fast hosted API'],
    index=0,
)
assistant_mode = st.sidebar.selectbox(
    'Productivity assistant mode',
    ['Math Solver', 'Code Helper', 'Study Tool'],
    index=0,
)


def lecture_header(num: int, title: str, subtitle: str) -> None:
    st.subheader(f'Lecture {num} – {title}')
    st.write(subtitle)


def show_code(title: str, code: str, language: str = 'python') -> None:
    with st.expander(f'Show code: {title}', expanded=False):
        st.code(code.strip(), language=language)


def split_sentences(text: str) -> List[str]:
    text = text.strip().replace('', ' ')
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if p.strip()]


def stuff_summary(text: str) -> str:
    sentences = split_sentences(text)
    if not sentences:
        return 'No content provided.'
    return ' '.join(sentences[:3]) + (' ...' if len(sentences) > 3 else '')


def map_reduce_summary(text: str) -> str:
    sentences = split_sentences(text)
    if not sentences:
        return 'No content provided.'
    chunks = [sentences[i:i+2] for i in range(0, len(sentences), 2)]
    partials = [chunk[0] for chunk in chunks if chunk]
    final = ' '.join(partials[:4])
    return final + (' ...' if len(partials) > 4 else '')


def refine_summary(text: str) -> str:
    sentences = split_sentences(text)
    if not sentences:
        return 'No content provided.'
    summary = sentences[0]
    for s in sentences[1:]:
        if len(summary) < 250:
            summary += ' ' + s
        else:
            summary = summary[:220] + ' ... ' + s[:80]
    return summary


def safe_eval(expr: str):
    import ast
    import operator as op

    allowed_operators = {
        ast.Add: op.add,
        ast.Sub: op.sub,
        ast.Mult: op.mul,
        ast.Div: op.truediv,
        ast.Pow: op.pow,
        ast.USub: op.neg,
        ast.Mod: op.mod,
    }

    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp):
            return allowed_operators[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp):
            return allowed_operators[type(node.op)](_eval(node.operand))
        raise ValueError('Unsupported expression')

    return _eval(ast.parse(expr, mode='eval').body)


# Lecture 129

def render_lecture_129():
    lecture_header(
        129,
        'Conversational Q&A Systems: Architecture, Prompts & Provider Comparisons',
        'Build a question-answering pipeline that can switch between providers and maintain a clean prompt architecture.',
    )

    col1, col2 = st.columns([1.1, 0.9])
    with col1:
        st.markdown('### Q&A architecture')
        st.code('User Question → Prompt Builder → Provider Router → Model → Answer', language='text')
        question = st.text_area('Enter a question', value='Explain embeddings in simple words.', height=110)
        if st.button('Generate Q&A response'):
            prompt = f'''You are a helpful AI tutor.

Answer the user's question clearly and concisely.
Use the selected provider style: {provider_mode}.

Question:
{question}

Answer:
'''
            response = ( 
                        f"[{provider_mode}] The topic is related to the user's question. ",
                        f"In a production app, the prompt above would be sent to the selected model provider."
                    )
            st.success('Response generated')
            st.write(response)
            st.markdown('### Built prompt')
            st.code(prompt.strip(), language='text')

    with col2:
        st.markdown('### Provider comparison')
        comparison = [
            {'Provider': 'Local Ollama', 'Privacy': 'High', 'Latency': 'Depends on hardware', 'Cost': 'Low', 'Best for': 'Private demos'},
            {'Provider': 'Hosted API', 'Privacy': 'Medium', 'Latency': 'Usually good', 'Cost': 'Per request', 'Best for': 'Easy integration'},
            {'Provider': 'Fast hosted API', 'Privacy': 'Medium', 'Latency': 'Very good', 'Cost': 'Per request', 'Best for': 'Interactive apps'},
        ]
        st.dataframe(comparison, use_container_width=True, hide_index=True)
        st.markdown('### Architecture note')
        st.info('The frontend should stay stable while the backend provider can change underneath it.')

    show_code(
            'Lecture 129 prompt architecture',
            """
    def build_prompt(question, provider_name):
        return f'''
    You are a helpful AI tutor.
    Answer clearly and concisely.
    Provider style: {provider_name}

    Question:
    {question}

    Answer:
    '''
    """,
        )

    st.markdown('---')
    st.markdown('### Visual flow')
    st.table(
        [
            {'Stage': 'User Question', 'Relative Size': 100},
            {'Stage': 'Prompt Builder', 'Relative Size': 90},
            {'Stage': 'Provider Router', 'Relative Size': 75},
            {'Stage': 'Model', 'Relative Size': 70},
            {'Stage': 'Answer', 'Relative Size': 65},
        ]
    )


# Lecture 130

def render_lecture_130():
    lecture_header(
        130,
        'Text Summarization Engines: Stuff, Map-Reduce & Refine Chains',
        'Explore three summarization strategies for handling short and long documents.',
    )

    text = st.text_area(
        'Paste a long document',
        value=(
            'Artificial Intelligence is transforming industries. '
            'It automates repetitive tasks. '
            'It improves productivity. '
            'Businesses use AI in healthcare, finance, education, and robotics. '
            'Long documents need strategies that respect context window limits.'
        ),
        height=160,
    )

    strategy = st.selectbox('Choose summarization strategy', ['Stuff', 'Map-Reduce', 'Refine'])

    left, right = st.columns([1, 1])
    with left:
        st.markdown('### Strategy flow')
        if strategy == 'Stuff':
            st.code('Entire document → One prompt → One summary', language='text')
            summary = stuff_summary(text)
        elif strategy == 'Map-Reduce':
            st.code('Split → Summarize chunks → Combine summaries → Final summary', language='text')
            summary = map_reduce_summary(text)
        else:
            st.code('Chunk 1 → Initial summary → Chunk 2 → Refine summary → Final summary', language='text')
            summary = refine_summary(text)

        if st.button('Generate summary'):
            st.success('Summary generated')
            st.write(summary)

    with right:
        st.markdown('### Comparison table')
        data = [
            {'Strategy': 'Stuff', 'Best for': 'Small text', 'Speed': 'Fast', 'Large docs': 'Poor'},
            {'Strategy': 'Map-Reduce', 'Best for': 'Long text', 'Speed': 'Medium', 'Large docs': 'Excellent'},
            {'Strategy': 'Refine', 'Best for': 'Iterative quality', 'Speed': 'Slower', 'Large docs': 'Excellent'},
        ]
        st.dataframe(data, use_container_width=True, hide_index=True)
        st.markdown('### Detected sentences')
        st.write(split_sentences(text))

    show_code(
        'Lecture 130 summarization helpers',
        '''
def stuff_summary(text):
    # one prompt, one summary
    ...

def map_reduce_summary(text):
    # split into chunks, summarize each, then combine
    ...

def refine_summary(text):
    # progressively improve one summary with each chunk
    ...
''',
    )

    st.markdown('---')
    st.markdown('### Visual summary')
    a, b, c = st.columns(3)
    with a:
        st.metric('Stuff', '1 call')
    with b:
        st.metric('Map-Reduce', '2+ calls')
    with c:
        st.metric('Refine', 'progressive')


# Lecture 131

def render_lecture_131():
    lecture_header(
        131,
        'Tool Integration, Function Calling & SQL Database Assistants',
        'Use tools for external actions and databases instead of asking the model to guess.',
    )

    class Employee:
        def __init__(self, name, dept, salary):
            self.name = name
            self.dept = dept
            self.salary = salary

    employees = [
        Employee('Rahul', 'Engineering', 120000),
        Employee('Priya', 'HR', 95000),
        Employee('Aman', 'Finance', 130000),
        Employee('Neha', 'Data', 150000),
    ]

    def calculator(a, b, op_name):
        if op_name == '+':
            return a + b
        if op_name == '-':
            return a - b
        if op_name == '*':
            return a * b
        if op_name == '/':
            return a / b if b != 0 else None
        return None

    def query_employees(min_salary):
        return [e for e in employees if e.salary > min_salary]

    tab1, tab2 = st.tabs(['Calculator Tool', 'SQL Assistant'])

    with tab1:
        st.markdown('### Function calling demo')
        a = st.number_input('Number A', value=245)
        b = st.number_input('Number B', value=786)
        op_sel = st.selectbox('Operation', ['+', '-', '*', '/'])
        if st.button('Run calculator tool'):
            result = calculator(a, b, op_sel)
            st.write(f'Tool result: **{result}**')
            st.code(f'''
User asks: What is {int(a)} {op_sel} {int(b)}?
LLM decides: call calculator tool
Tool returns: {result}
LLM says: The answer is {result}
'''.strip(), language='text')

    with tab2:
        st.markdown('### SQL database assistant demo')
        salary_threshold = st.number_input('Minimum salary', value=100000)
        if st.button('Run SQL assistant'):
            result_rows = query_employees(salary_threshold)
            sql_query = f'SELECT * FROM Employees WHERE Salary > {int(salary_threshold)};'
            st.code(sql_query, language='sql')
            if result_rows:
                st.success('Database result')
                st.table([{'Name': e.name, 'Department': e.dept, 'Salary': e.salary} for e in result_rows])
            else:
                st.warning('No matching employees found.')
            st.info('The model should generate the query, the app should execute it, and then the model should explain the result.')

    show_code(
        'Lecture 131 tool integration pattern',
        '''
# LLM decides whether a tool is needed.
# The application executes the tool.
# The tool result is returned to the model.
# The model writes the final user-friendly response.
''',
    )

    st.markdown('---')
    st.markdown('### Tool flow')
    st.code('Question → LLM → Tool Selection → Execute Tool → Tool Result → LLM → Final Answer', language='text')


# Lecture 132

def render_lecture_132():
    lecture_header(
        132,
        'Specialized Productivity Assistants: Math Solvers, Code Helpers & Study Tools',
        'Build assistant personas that are focused on one productivity task at a time.',
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        task = st.selectbox('Choose assistant type', ['Math Solver', 'Code Helper', 'Study Tool'])
        task_input = st.text_area(
            'Enter the task',
            value=(
                'Solve 2x + 5 = 17'
                if task == 'Math Solver'
                else 'Explain this Python code'
                if task == 'Code Helper'
                else 'Summarize transformer architecture'
            ),
            height=130,
        )

        if st.button('Generate specialized response'):
            if task == 'Math Solver':
                expr = st.text_input('Enter a math expression', value='2 + 3 * 4', key='math_expr')
                try:
                    result = safe_eval(expr)
                    response = f'Step-by-step result: {expr} = {result}'
                except Exception as e:
                    response = f'Could not evaluate expression safely: {e}'
            elif task == 'Code Helper':
                response = (
                    'This assistant should explain the code, identify issues, '
                    'suggest improvements, and keep the answer concise and technical.'
                )
            else:
                response = (
                    'This assistant should create revision-friendly explanations, '
                    'bullet points, key terms, and short summaries.'
                )

            st.success('Specialized response')
            st.write(response)

    with col2:
        st.markdown('### Assistant behavior matrix')
        behavior = [
            {'Assistant': 'Math Solver', 'Style': 'Precise', 'Output': 'Steps + answer', 'Best for': 'Problem solving'},
            {'Assistant': 'Code Helper', 'Style': 'Technical', 'Output': 'Explanation + fix', 'Best for': 'Debugging'},
            {'Assistant': 'Study Tool', 'Style': 'Educational', 'Output': 'Summary + bullets', 'Best for': 'Revision'},
        ]
        st.dataframe(behavior, use_container_width=True, hide_index=True)

        st.markdown('### Prompt template idea')
        st.code(
            f'''
You are a {task}.
Follow the task-specific style.
Task:
{task_input}
'''.strip(),
            language='text',
        )

    st.markdown('---')
    st.markdown('### Visual workflow')
    st.table(
        [
            {'Layer': 'Foundation Model', 'Role': 'Shared base capabilities'},
            {'Layer': 'Math Solver', 'Role': 'Problem solving workflow'},
            {'Layer': 'Code Helper', 'Role': 'Debugging and explanation workflow'},
            {'Layer': 'Study Tool', 'Role': 'Revision and summarization workflow'},
        ]
    )

    show_code(
        'Lecture 132 specialized assistant idea',
        '''
# One base model
# Different prompts / tools / workflows
# Different assistant behaviors
''',
    )


if lecture == 'Lecture 129':
    render_lecture_129()
elif lecture == 'Lecture 130':
    render_lecture_130()
elif lecture == 'Lecture 131':
    render_lecture_131()
elif lecture == 'Lecture 132':
    render_lecture_132()
